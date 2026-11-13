# Changelog do r7ex

Semver `X.YY.ZZ`: o minor sobe e carrega o patch; só o major zera o resto.

## 1.5.4 — 13/11/2026 · retenção: pesquisa de ganchos + CTA de pertencimento

- Nei (13/11/2026, "aplica"), depois dos /swarm reprovados ("nem eu consigo ficar assistindo"); seção Retenção do
  explicavideos 2.26.11. PADRAO §2.4.
- `gancho.referencias` (opcional): 3–5 `{canal, titulo, abertura, gatilho}` de quem fala do tema no YouTube (yt-dlp
  `ytsearch15` + legenda automática 0–35 s). O `checar` avisa se faltar ou tiver menos de 3. Número de terceiro não entra.
- Crítico do plano compara o nosso gancho com a melhor referência (mais fraco → parte 1 ≤ 7, sem bloqueio).
- Parte 7: frase de comunidade com o inema ponto club ANTES da pergunta ("Toda semana tem kit novo, grátis, no inema
  ponto club."). Sem ela o `checar` avisa e o crítico tira nota. Modelo atualizado (617 caracteres, passa no `checar`).
- Bot (`prompts/bot-ficha.md`) faz a pesquisa de ganchos e escreve o fecho novo.

## 1.4.4 — 12/11/2026 · chamada: clareza + atenção, CTA sem palavra nem link (D20)

- Nei: "não adianta estar claro e correto se não chama atenção, não mexe na dor ou desejo". Regra única de todos os
  motores em `~/projetos/inema-design/regras/chamada.md`; PADRAO §2.3.
- Ganchos `promessa` e `acusacao` (soma): o `checar` reprova os dois sem "você/seu/sua" na 1ª frase.
- Parte 7: sai o CTA fixo "Ou me pede o link aqui nos comentários". O `checar` reprova "pede o link", "comenta PALAVRA",
  "link na bio", "te mando" e fecho sem pergunta; sem "pede" na fala pede `cta.de`. Edição com avatar gravado só avisa.
- Crítico do plano com a pergunta dos 15 s (dor/desejo, por que importa, nome do método) e o CTA novo.

## 1.3.1 — 29/10/2026 · gancho de provocação + entrega (soma, não substitui)

- 6º tipo de gancho `provocacao`: a 1ª frase afirma algo que cutuca, com nome ou número, e pede `gancho.fontes`.
  O `checar` reprova provocação em pergunta ou sem nome/número. Os 5 tipos e o "E se…" seguem valendo.
- `gancho.entrega` (o que a pessoa leva do vídeo): sem ela o `checar` só avisa.
- PADRAO §2.2 com as aberturas que bombaram (5 referências + gitbombando) e 4 provocações para o tema robô/emprego.

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
