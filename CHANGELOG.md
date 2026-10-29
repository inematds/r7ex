# Changelog do r7ex

Semver `X.YY.ZZ`: o minor sobe e carrega o patch; só o major zera o resto.

## 1.2.1 — 28/10/2026 · manchete larga não sai mais da tela nos cortes da capa

- Os cortes de aproximação da capa (1,05× em 1 s e 1,10× em 2 s, mais os 3% do motor) cortavam o "P" e o "T" de uma
  manchete de 986 px ("PARA DE CORRIGIR IA NO CHAT"). `pecas.batidas` agora mede a manchete na arte e, quando ela não cabe,
  aproxima só a arte e cola por cima a faixa inteira da manchete original (degradê de 18 px). O corte é preso no meio
  da manchete medida, não mais em y=480 fixo.

## 1.2.0 — 28/10/2026 · gancho: quadro 0 + 3 primeiros segundos

Pedido do Nei: os reels usavam as técnicas de chamada que analisamos só na forma; a edição do dia abriu com "5 novidades de
IA…", um gancho de lista. "Sim, aplica no r7ex também." Regras em `PADRAO.md` §2.1.

- Bloco `gancho:` na ficha: `tipo` (`contrario` | `perda` | `estatistica` | `terceiro` | `noticia`), `manchete` (quadro 0,
  ≤ 6 palavras, CAIXA ALTA, mais forte que a fala), `destaque` (a palavra em amarelo), `objeto` (com dano/ameaça), `prova`
  (número com fonte até ~20 s), `absolvicao` (parte 2 ou 3), `fontes` (estatística/terceiro/notícia), `data` (notícia, até 7 dias).
- `r7ex.py checar` reprova gancho de lista ("N coisas/novidades…"), "você sabia…", "eu fiz…", manchete com mais de 6 palavras,
  fora da caixa alta ou igual a um pedaço da fala, e os campos faltando. Edição com avatar já gravado só recebe aviso.
- O pedido ao Codex desenha a `manchete` (uma palavra em amarelo) e o `objeto` na capa, na metade de cima, com margens.
- A capa troca de quadro a cada ~1 s até os 3 s: cortes de aproximação 1,05× (1 s) e 1,10× (2 s) na mesma arte
  (`pecas.batidas`, só em ficha com `gancho:`). A folha de revisão mostra 0 s, ~1,2 s e ~2,2 s.
- Um tema por vídeo: vários temas → um vídeo por tema (no bot, o mais forte; os outros vão propostos no resumo).
- Crítico do plano, revisor da folha, `prompts/bot-ficha.md`, `modelo/ficha.yaml` (gancho `terceiro`), README, COMO-PEDIR,
  HELP, skill e guia atualizados.

## 1.1.0 — 28/10/2026 · ritmo da fala e cartão segurado

- Fala esticada até ~182 palavras/min (máx. 12%), ~0,75 s de silêncio antes da máxima, roteiro de 450–620 caracteres.
- Cartão do comentário 9 s na tela depois da última palavra, com o gesto de comentar.
