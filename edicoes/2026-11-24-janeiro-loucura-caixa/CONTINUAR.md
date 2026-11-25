# CONTINUAR — r7ex "Janeiro vai ser uma loucura pro contador" (lives1 + lives8)

Pasta: ~/projetos/r7ex/edicoes/2026-11-24-janeiro-loucura-caixa (repo inematds/r7ex).

## Ordens do Nei (24/11/2026, citadas)
- "faz um reels no lives1 e lives8, chamada vai ser uma loucura para os contadores e empresários deixar o sistema funcionando em janeiro. uma imagem dele apavorado e no outro uma fila de supermercado gigante e as pessoas do caixa apavorados e os outros furiosos com a fila"
- "manda eles para o v3 também"

## Onde parou (fase 1, sessão com o Nei)
- A ficha passou no `checar`, e o crítico aprovou o plano (média 8,3, gancho 8). A edição entrou na produção (`producao/producao.py`), que manda o avatar ao estúdio, espera, faz o vídeo, revisa e manda ao v3.
- `publicar.so_v3: true`: a produção NÃO põe na fila nem no YouTube. Por isso esta fase 2 existe.

## O que falta (fase 2)
1. Conferir `python3 producao/producao.py --status | grep janeiro-loucura-caixa`.
   - `parado` → FALHOU com o motivo do `producao.log` (não refazer avatar; não reenviar ao estúdio).
   - `na_fila` → o vídeo foi revisado e enviado ao v3 (`video.mp4.envio-v3.json`). Seguir.
2. Ler `build/folha.jpg`. Se algum quadro tiver defeito que impeça entender (título errado, quadro preto, número errado), FALHOU e parar.
3. Publicar `video.mp4` DIRETO pelo yt-pubx (regra do Nei de 05/11 e a ficha empresa-chatgpt de 22/11), como Short:
   - lives1 agora: `cd ~/projetos/yt-pubx && ./yt-pubx publicar <video.mp4> --canal lives1 --contexto "<publicar.contexto da ficha>" --dry-run`. Olhar o plano e publicar com `--plano <pasta>/plano.json`. Título-base: `publicar.titulo`. Short não leva thumb.
   - lives8 pelo menos 1 h depois (regra das publicações com 1 h de intervalo): o mesmo vídeo, `--canal lives8`, mesmo contexto.
   - O Metricool e o INEMA.FREE seguem o que o yt-pubx/timers já fazem sozinhos. Não postar à mão.
4. Mandar ao v3, em resposta à msg do continua, os 2 links (lives1 e lives8). O inemaytbot recebe os links como de costume.
5. Gravar `CONTINUAR.resultado` com "FEITO: lives1 <url> · lives8 <url>" ou "FALHOU: <passo> — <motivo>".

## Travas
- Nunca chamar 8,8% ou 11,3% de alíquota de 2027. Nada de logo da Receita na arte. Nada de dados pessoais da nota (CPF, CNPJ da loja, chave, QR).
- Não reenviar o avatar ao HeyGen. Não trocar de plano no HeyGen. Não pôr na fila do lives7.
- Em lives1 só PT. Não publicar duas vezes no mesmo canal: antes, conferir se já há vídeo com o mesmo título no canal (`~/.local/share/yt-pubx/` histórico).
