---
name: r7ex
description: >-
  Tema ou tese do Nei → reel 9:16 VIRAL no padrão r7ex: roteiro de 7 etapas de gatilho (gancho com número → medo →
  desejo → facilidade → descoberta → benefício → comentário "tá tudo no inema.club") com acabamento de telejornal
  (título desenhado na abertura pelo Codex, preto + amarelo, painéis no tempo da fala, contador, legenda karaokê,
  avatar do Nei em meia tela embaixo no gancho e depois no canto), v3 e fila do lives7. Gatilho: "/r7ex", "faz um r7ex", "reel viral", "reel no padrão novo",
  "reel com gatilhos", ou uma tese/opinião do Nei pedindo vídeo curto.
---

# r7ex — reel viral do INEMA

Repo `~/projetos/r7ex` (inematds/r7ex). **Leia `PADRAO.md` antes de escrever.** Explicação completa: `README.md`.
Comando único: `python3 r7ex.py` (sem argumentos mostra a ajuda).

## Passos
1. **Plano** (PADRAO §1): pessoa = público geral; o que ela quer; gancho = medo/novidade/provocação com número e fonte;
   nota ≥ 7; destino no inema.club (leia a página: nome, aulas, se é grátis).
2. `python3 r7ex.py novo <slug>` e preencha `ficha.yaml` (modelo: o reel do hacker): abertura (título branco +
   destaque), 7 partes (fala por extenso, 550–700 caracteres no total; imagem OU print; painel com itens nas palavras
   da fala; contador onde houver número), `trocas` para a legenda, CTA em pergunta, `publicar`.
3. `python3 r7ex.py checar <pasta>` até passar.
4. Avatar: OK do Nei → `avatar/APROVADO_HEYGEN` com a frase dele; ou `--de <mp4>` para reaproveitar.
5. **Padrão (sem sessão aberta):** `python3 producao/producao.py --add <pasta>`. O timer `r7ex-producao` (5 em 5 min)
   manda ao estúdio todas as pendentes na mesma rodada (sem esperar a anterior ficar pronta), espera o HeyGen, roda o `fazer`, o revisor (claude -p + `producao/revisor.md`) lê a
   folha e, aprovado, manda ao v3 e põe na fila do canal; avisa no v3 "Terminei/Falhou". Reprovou → `parado` com o
   motivo; corrigiu → `producao.py --retomar <pasta>`. Ver: `producao.py --status`. Detalhes: `producao/README.md`.
6. **Manual** (só se o Nei pedir para acompanhar): `python3 r7ex.py fazer <pasta>`, **ler** `capa/abertura.png` e
   `build/folha.jpg` (nada cobrindo nada, prints legíveis, legenda dentro da tela), depois
   `python3 r7ex.py enviar <pasta>` e `python3 r7ex.py fila <pasta>`. Dizer ao Nei "Terminei: …".

## Regras
- Tudo que abre navegador roda na tela `:99`; só o LOGIN do HeyGen vai na tela do Nei (`:10`).
- Nunca número em algarismo na fala (o avatar lê errado); a legenda troca por algarismo.
- "Grátis" só quando a página diz ou o Nei afirma. Nunca inventar número.
- Publicar só pela fila; nunca upload direto. Avatar gerado só com OK daquela produção.
- Mudança de padrão (layout, estrutura, plano): README §7; padrão novo → kit inema-design primeiro (D9–D11).
