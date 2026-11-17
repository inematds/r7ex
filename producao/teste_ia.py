"""Contratos de troca de motor e do portão visual, sem rede/publicação."""
import copy, datetime as dt, json, os, subprocess, tempfile, unittest
from zoneinfo import ZoneInfo
from pathlib import Path
from unittest.mock import patch
import yaml
import ia_motor as ia
import producao as p

class Teste(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
  self.out=Path(self.tmp.name); self.cfg=copy.deepcopy(ia.carregar())
  self.file=self.out/'ia.yaml'; self.save()
  self.env=patch.dict(os.environ,{ia.CONFIG_ENV:str(self.file),ia.COTA_DB_ENV:str(self.out/'cota.sqlite')}); self.env.start(); self.addCleanup(self.env.stop)
 def save(self): self.file.write_text(yaml.safe_dump(self.cfg))
 def test_modelo_esforco_imagem_e_sem_chaves(self):
  pic=self.out/'quadro.jpg'; pic.write_bytes(b'jpg')
  with patch.dict(os.environ,ANTHROPIC_API_KEY='segredo',OPENAI_API_KEY='segredo'):
   def run(cmd,**kw):
    self.assertIn('-i',cmd); self.assertIn(str(pic),cmd); self.assertIn('gpt-6.1-sol',cmd)
    self.assertIn('model_reasoning_effort="medium"',cmd); self.assertNotIn('OPENAI_API_KEY',kw['env'])
    self.assertNotIn('ANTHROPIC_API_KEY',kw['env']); self.assertIn('read-only',cmd)
    Path(cmd[cmd.index('-o')+1]).write_text('{"ok":true}')
    return subprocess.CompletedProcess(cmd,0,'','')
   with patch.object(ia.subprocess,'run',side_effect=run): self.assertEqual(json.loads(ia.executar('revisao_visual','confira',self.out,imagens=[pic])),{'ok':True})
 def test_api_bloqueada_antes_de_chave_ou_rede(self):
  self.cfg['etapas']['revisao_visual'].update(tipo='api',motor='anthropic',modelo='claude-opus-5-5'); self.save()
  with patch.object(ia,'ler_chave') as key, patch.object(ia.urllib.request,'urlopen') as net:
   with self.assertRaisesRegex(ValueError,'API desativada'): ia.executar('revisao_visual','x',self.out)
   key.assert_not_called(); net.assert_not_called()
 def test_comentarios_preservados(self):
  original=ia.CONFIG.read_text(); new=ia.alterar_com_comentarios(original,'revisao_visual',{'motor':'claude','modelo':'claude-opus-5-5','esforco':'high'})
  self.assertEqual([x for x in original.splitlines() if x.lstrip().startswith('#')],[x for x in new.splitlines() if x.lstrip().startswith('#')])
  self.assertEqual(yaml.safe_load(new)['etapas']['revisao_visual']['esforco'],'high')
 def test_claude_assinatura_modelo_e_esforco(self):
  c=dict(self.cfg['etapas']['revisao_visual'],motor='claude',modelo='claude-opus-5-5',esforco='high')
  cmd=ia.comando(c); self.assertEqual(cmd[cmd.index('--model')+1],c['modelo']); self.assertEqual(cmd[cmd.index('--effort')+1],'high')
 def test_sem_folha_nao_chama_modelo(self):
  with patch.object(p,'executar') as run:
   self.assertEqual(p.revisar(self.out)['veredito'],'erro'); run.assert_not_called()
 def test_resposta_invalida_nao_aprova(self):
  for f in ['build/folha.jpg','contact.jpg','ficha.yaml','roteiro.json']:
   q=self.out/f; q.parent.mkdir(parents=True,exist_ok=True); q.write_text('{}')
  with patch.object(p,'executar',return_value='{"veredito":"talvez"}'):
   self.assertEqual(p.revisar(self.out)['veredito'],'erro')

# Recusa REAL do Claude Code (16/11/2026 14:34, crítico do r7ex; ids de conta removidos).
RECUSA_CLAUDE=json.dumps({"type":"result","subtype":"success","is_error":True,"api_error_status":429,
 "api_error_type":"rate_limit_error","api_error_origin":"first_party","api_error":"usage_limit_reached",
 "result":"You've hit your weekly limit · resets 9pm (America/Sao_Paulo)","num_turns":1,"duration_ms":966,
 "terminal_reason":"api_error","modelUsage":{},"usage":{}})
NOTAS='{"partes":[%s],"bloqueios":[],"resumo":"ok"}'%','.join('{"n":%d,"nota":8,"porque":"x","melhorar":""}'%i for i in range(1,8))

class Trava(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
  self.out=Path(self.tmp.name); self.file=self.out/'ia.yaml'; self.cfg=copy.deepcopy(ia.carregar()); self.file.write_text(yaml.safe_dump(self.cfg))
  self.env=patch.dict(os.environ,{ia.CONFIG_ENV:str(self.file),ia.COTA_DB_ENV:str(self.out/'cota.sqlite'),'CODEX_HOME':str(self.out/'codex')})
  self.env.start(); self.addCleanup(self.env.stop)
  self.chamadas=[]
 def fake(self,claude_stdout=None,claude_rc=0,codex='{"ok":true}'):
  def run(cmd,**kw):
   self.chamadas.append('claude' if cmd[0].endswith('claude') else 'codex')
   if self.chamadas[-1]=='claude': return subprocess.CompletedProcess(cmd,claude_rc,claude_stdout,'')
   Path(cmd[cmd.index('-o')+1]).write_text(codex); return subprocess.CompletedProcess(cmd,0,'','')
  return patch.object(ia.subprocess,'run',side_effect=run)
 def eventos(self): return [json.loads(l) for l in (self.out/'ia-execucoes.jsonl').read_text().splitlines()]
 def test_recusa_real_vira_horario_de_volta(self):
  agora=dt.datetime(2026,11,16,14,34,tzinfo=ZoneInfo('America/Sao_Paulo')).timestamp()
  ate=ia.recusa_cota_claude(RECUSA_CLAUDE,agora)
  self.assertEqual(dt.datetime.fromtimestamp(ate,ZoneInfo('America/Sao_Paulo')).strftime('%d %H:%M'),'16 21:00')
 def test_texto_normal_sobre_limite_nao_bloqueia(self):
  ok=json.dumps({"type":"result","is_error":False,"result":"You've hit your weekly limit · resets 9pm (America/Sao_Paulo)"})
  self.assertIsNone(ia.recusa_cota_claude(ok)); self.assertIsNone(ia.recusa_cota_claude('não é json'))
 def test_horario_com_data_e_absurdo(self):
  agora=dt.datetime(2026,11,15,11,0,tzinfo=ZoneInfo('America/Sao_Paulo')).timestamp()
  ate=ia.horario_volta('resets Nov 16, 9pm (America/Sao_Paulo)',agora)
  self.assertEqual(dt.datetime.fromtimestamp(ate,ZoneInfo('America/Sao_Paulo')).strftime('%d %H'),'16 21')
  self.assertIsNone(ia.horario_volta('resets Dec 30, 9pm (America/Sao_Paulo)',agora))  # > 8 dias: ignora
  self.assertIsNone(ia.horario_volta('resets 9pm (Lugar/Inexistente)',agora))
 def test_trava_grava_e_proxima_nao_abre_programa(self):
  self.cfg['etapas']['critico_plano'].pop('alternativa'); self.file.write_text(yaml.safe_dump(self.cfg))
  with self.fake(RECUSA_CLAUDE,1):
   with self.assertRaises(ia.CotaEsgotada): ia.executar('critico_plano','x',self.out)
   with self.assertRaises(ia.CotaEsgotada): ia.executar('critico_plano','x',self.out)
  self.assertEqual(self.chamadas,['claude'])   # a 2ª falhou na hora, sem abrir o claude
 def test_reserva_quando_principal_sem_cota(self):
  with self.fake(RECUSA_CLAUDE,1,NOTAS):
   self.assertEqual(json.loads(ia.executar('critico_plano','x',self.out))['resumo'],'ok')
   ia.executar('critico_plano','x',self.out)
  self.assertEqual(self.chamadas,['claude','codex','codex'])
  e=self.eventos()[-1]; self.assertEqual((e['motor'],e['modelo'],e['esforco'],e['reserva']),('codex','gpt-6.1-sol','medium',True))
  self.assertEqual(e['sem_cota'],['claude'])
 def test_erro_comum_nao_usa_reserva(self):
  with self.fake(json.dumps({"is_error":True,"result":"outro erro"}),1):
   with self.assertRaisesRegex(RuntimeError,'código 1'): ia.executar('critico_plano','x',self.out)
  self.assertEqual(self.chamadas,['claude'])
 def test_preferir_codex(self):
  with self.fake(codex=NOTAS): ia.executar('critico_plano','x',self.out,preferir='codex')
  self.assertEqual(self.chamadas,['codex'])
 def test_agente_nunca_usa_reserva(self):
  with self.fake(RECUSA_CLAUDE,1):
   with self.assertRaises(ia.CotaEsgotada): ia.executar('critico_plano','x',self.out,agente=True)
  self.assertEqual(self.chamadas,['claude'])
 def test_validacao_da_alternativa(self):
  for ruim in [{'motor':'claude','modelo':'claude-opus-5-5','esforco':'low'},{'motor':'codex','modelo':'gpt-6.1-sol','esforco':'max'},{'motor':'openrouter','modelo':'x','esforco':'low'}]:
   d=copy.deepcopy(self.cfg); d['etapas']['critico_plano']['alternativa']=ruim
   with self.assertRaises(ValueError): ia.validar(d)
  d=copy.deepcopy(self.cfg); d['etapas']['critico_plano']['capacidade']='agente'
  with self.assertRaisesRegex(ValueError,'alternativa só'): ia.validar(d)
 def test_claude_sem_sessao_no_disco(self):
  self.assertIn('--no-session-persistence',ia.comando(dict(self.cfg['etapas']['critico_plano'])))
 def test_revisor_espera_sem_contar_erro(self):
  for f in ['build/folha.jpg','ficha.yaml']:
   q=self.out/f; q.parent.mkdir(parents=True,exist_ok=True); q.write_text('{}')
  with patch.object(p,'executar',side_effect=ia.CotaEsgotada('claude',1e10)):
   self.assertEqual(p.revisar(self.out)['veredito'],'espera')

if __name__=='__main__': unittest.main()
