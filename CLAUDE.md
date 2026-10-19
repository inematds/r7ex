# r7ex

Reel viral do INEMA: roteiro de 7 etapas (r7e) + acabamento de telejornal (motor copiado do eventosextremospub).
Padrão em `PADRAO.md`; explicação completa em `README.md`; skill em `skill/SKILL.md` (ligada em `~/.claude/skills/r7ex`).

- Autor dos commits: `inematds <inematds@gmail.com>`. Repo `inematds/r7ex`.
- **Independente**: motor (`motor/`), estúdio HeyGen (`heygen/`), Whisper (`r7ex/whisper.py`), trilha, envio ao bot
  e fila são cópias daqui. Não importar nada do eventosextremospub/reel7etapas/cardshorts/explicavideos.
- Mídia fica fora do git (`.gitignore`): entram `ficha.yaml`, `falas.json`, `capa/pedido.txt` e o código.
- Avatar só pelo estúdio do HeyGen (assinatura) com `avatar/APROVADO_HEYGEN` daquela produção; status/download pela leitura
  da API (exceção do Nei). Tudo que abre navegador roda com `DISPLAY=:99`; só a janela de LOGIN vai na tela do Nei (`:10`).
- Imagens: Codex `image_gen` pela assinatura (`codex exec`). Ler `capa/abertura.png` e conferir a grafia antes do render.
- Antes de enviar: ler `build/folha.jpg` (12 quadros). Publicar só pela fila (`r7ex.py fila`), nunca upload direto.
- Falhou? Linha em `FALHAS.md` (data | o que quebrou | menor correção | prompt/infra).
