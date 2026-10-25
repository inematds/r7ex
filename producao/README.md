# Produção do r7ex (sem sessão aberta)

Leva cada edição do avatar no HeyGen até a fila do canal sozinha. Pedido do Nei em 19/10/2026: uma fila que espera
o retorno do HeyGen e continua o processo.

```
--add ─► enviar_avatar ─► esperando_avatar ─► montar ─► revisao ─► publicar ─► na_fila
            (estúdio,        (conferência       (r7ex.py   (claude -p    (v3 + fila
             1 por rodada)    no HeyGen, leitura) fazer)    lê a folha)   do canal)
                    qualquer erro / revisão reprovada ─► parado (+ aviso "Falhou" no v3)
```

- **Quem espera é um script**, no timer `r7ex-producao` (a cada 5 min). Esperar o HeyGen pode levar horas e não pede
  inteligência.
- **O agente só revisa.** O revisor (`claude -p`, assinatura, só leitura) recebe `revisor.md`, lê a `ficha.yaml` e a
  `build/folha.jpg` e responde `aprovado` ou `reprovado` com o motivo. Na dúvida, reprova. Ele não corrige nada:
  reprovou, a edição para e o aviso chega no v3.
- **Todas as idas ao estúdio na mesma rodada** (25/10/2026: nenhuma espera a anterior ficar pronta; a trava do estúdio só põe uma atrás da outra) **e uma montagem por rodada.** Conferências e revisões não têm limite. A rodada pula se a anterior
  ainda está trabalhando.

## Comandos

```
python3 producao/producao.py --add edicoes/<pasta>       # entra (precisa de avatar/APROVADO_HEYGEN ou AVATAR_DE.txt)
python3 producao/producao.py --status                    # estado de cada edição
python3 producao/producao.py --retomar edicoes/<pasta>   # depois de corrigir uma edição parada
python3 producao/producao.py                             # uma rodada à mão (o timer faz isso)
python3 producao/teste_producao.py                       # teste com edições falsas (sem HeyGen, sem Telegram)
```

Instalar o timer (uma vez):
`cp producao/systemd/r7ex-producao.* ~/.config/systemd/user/ && systemctl --user daemon-reload && systemctl --user enable --now r7ex-producao.timer`

## Travas

- Só entra edição adicionada com `--add`. A produção nunca varre `edicoes/`.
- O avatar só é gerado com `avatar/APROVADO_HEYGEN` (OK do Nei para aquela produção). A produção nunca cria esse arquivo.
- O estúdio passa pela trava da ferramenta (`heygen/heygen-perfil.mjs` → `~/.cache/inemaccbot/heygen-estudio.trava`).
- Publicação só pela fila do canal (`r7ex.py fila`). Edição que já está na fila não entra de novo.
- Estado em `producao/estado.json` (local, fora do git); log geral em `producao/producao.log`; log de cada edição em
  `edicoes/<pasta>/producao.log`.

## Quando o revisor erra

- Deixou passar um defeito: escreva o caso em `revisor.md` (lista "Reprove se") e, se der, crie uma proteção
  automática no `r7ex.py`, como a do print vazio (`imagens`) e a da largura da legenda (`cena.py`, `MAX_LEG`).
- Reprovou algo certo: escreva o caso em "NÃO reprove por".
