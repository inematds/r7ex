# CONTINUAR — r7ex "Protegendo seus repos" (05/11/2026)

## Ordem do Nei (citada pelo agente principal)
Página-projeto "protegendo seus repos" (backup de repositórios git contra bloqueio de conta ou invasão) + portal + Telegram
INEMA.DEV + explicavideo no lives3 + **"um r7ex"**. Este arquivo cuida SÓ do r7ex. Tese: "Se a sua conta do GitHub sumir
amanhã, você perde tudo? Outra conta no GitHub não salva. Backup em camadas … Tá tudo no inema.club." Sem citar fonte,
nada sensível (nenhum e-mail, token, IP, conta secundária).

## Fase 1 (feita, sessão wifi 05/11)
- Ficha `edicoes/2026-11-05-protegendo-seus-repos/ficha.yaml`: `checar` OK (620 caracteres), `plano` aprovado (média 7,7, gancho 8, sem bloqueios).
- `avatar/APROVADO_HEYGEN` gravado. Unidade `r7ex-espera-protegendo` esperou o avatar do explicavideo entrar no estúdio
  (flag `~/projetos/wifi/longrun/2026-11-05-protegendo-seus-repos/heygen-explicavideo-submetido.flag`, teto 90 min) e fez
  `producao.py --add`. A produção (timer `r7ex-producao`) envia ao estúdio, espera, roda `fazer`, o revisor independente
  (claude -p + `producao/revisor.md`), manda ao v3 e põe na fila do lives3 → estado `na_fila`. Este vigia dispara aí.

## FASE 2 — o que falta (cwd ~/projetos/r7ex)
1. Conferir: `python3 producao/producao.py --status | grep protegendo` = `na_fila`; ler `edicoes/2026-11-05-protegendo-seus-repos/build/folha.jpg`
   (nada cobrindo nada, print do guia legível — se o print saiu vazio/404, anotar como SUGESTÃO, não parar).
   Achar a msg do v3 do envio em `edicoes/2026-11-05-protegendo-seus-repos/producao.log`.
2. **Publicar DIRETO no lives3** (a entrega precisa do link para o tópico do Telegram — regra do Nei de 05/11 no SKILL do r7ex):
   pegar o item em `fila/fila.json` cujo `arquivo` termina em `2026-11-05-protegendo-seus-repos/video.mp4` (estado `pendente`);
   se ele já tiver `video_id` (a fila publicou antes), pular para o passo 3 usando esse id. Senão:
   `cd ~/projetos/yt-pubx && ./yt-pubx publicar <arquivo> --canal lives3 --contexto "<contexto do item>" --title "<titulo do item>"`
   (timeout longo; NÃO rodar `--help` de yt-pubx/fila). Pegar o id de `URL: https://www.youtube.com/watch?v=<id>`.
   Editar o item em `fila/fila.json`: `estado: feito`, `video_id: <id>`, `quando: <agora>`, `nota: direto` (para não sair duas vezes).
   Link = `https://youtube.com/shorts/<id>`. Aviso no v3 em texto normal (`~/projetos/wifi/scripts/avisa-v3.sh "Terminei: r7ex Protegendo seus repos publicado no lives3 <link>"`), sem faixa azul.
3. **metritds** (lives3 → metritds direto, Nei 05/11): escrever `edicoes/2026-11-05-protegendo-seus-repos/metritds-texto.txt`
   (1ª linha = gancho "O GitHub bloqueou sua conta. Você perdeu tudo?"; linhas curtas: outra conta no GitHub não salva, é a
   mesma empresa; 3 camadas: GitLab numa conta sem vínculo com token que não apaga, fotos datadas no disco, teste de restaurar;
   "Backup que você nunca testou não é backup."; "Guia completo em inema.club"; pergunta "Você vai proteger os seus hoje?";
   hashtags #github #git #backup #seguranca #programacao #inemaclub). Nada sensível, sem fonte.
   `cd ~/projetos/metricool-inematds && EXTRA="YouTube: <link>" ./publicar.sh ~/projetos/r7ex/edicoes/2026-11-05-protegendo-seus-repos/video.mp4 ~/projetos/r7ex/edicoes/2026-11-05-protegendo-seus-repos/metritds-texto.txt inematds/r7ex`
   (vídeo < 60 s → IG + TikTok). Anotar em `metritds.txt`.
4. **Telegram INEMA.DEV**: o link do tópico está em `~/projetos/wifi/longrun/2026-11-05-protegendo-seus-repos/canal.md`
   (procure "t.me" / "tópico"; o id é o último número do link). Responder DENTRO dele, sem criar tópico e sem MENU:
   `cd ~/projetos/telegramtopicosindex && venv/bin/python postar_topico.py --grupo INEMA.DEV --topico <id> ...` com o texto
   "🎬 Reel: <link>" (ver `~/.claude/skills/postar-telegram/SKILL.md` §tópico que já existe; ensaio primeiro, depois `--enviar`;
   conferir `lsof` da `telegram_session.session` antes; **nunca entre 23:20 e 23:55**). Sem link no canal.md → não postar,
   anotar "Telegram aguarda link do tópico" no resultado e no canal.md.
5. `~/projetos/wifi/PRODUCOES-VIDEO.md`, linha "Protegendo seus repos": acrescentar no Estado só a parte do r7ex
   ("r7ex lives3 <link>, v3 msg N, metritds <quando>, INEMA.DEV reel ok"). Não mexer no resto da linha.
6. Acrescentar uma linha em `~/projetos/wifi/longrun/2026-11-05-protegendo-seus-repos/canal.md` (só acrescentar):
   `- 2026-11-05 HH:MM · fato · r7ex publicado lives3 <link>; metritds <quando>; Telegram INEMA.DEV <ok|pendente>`.
7. Gravar `CONTINUAR.resultado` com "FEITO: r7ex lives3 <link> …" (ou "FALHOU: <passo> — <motivo>") e dizer "Terminei: …".

## Travas
- Não gerar outro avatar (um por reel); nunca API do HeyGen para gerar; nunca trocar de plano no estúdio.
- Canal só lives3 (+ metritds). Nunca lives1/lives7. Não mexer no portal. Não criar tópico no Telegram, não apagar nada.
- Revisor reprovou / edição `parado` → NÃO publicar; avisar "Falhou: r7ex Protegendo seus repos — <motivo>" e gravar FALHOU.
- Commits no r7ex (se houver): autor inematds. Falha real corrigida → linha em `~/projetos/r7ex/FALHAS.md`.
