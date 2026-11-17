## 1.10.7 — 17/11/2026

Fluência (D26, Nei 17/11/2026, sobre o enxame v2: "parece não tem fluência, não parece natural eu falando"; "começou bem, mas a explicação não, e o final mal entra sobre pergunta e CTA misturando"; "teto pode ficar em 900, mantendo objetivo do 620… explicação tem que ser impactante. imagem também"). `r7ex/ritmo.py` v2: k = 1 (velocidade natural do HeyGen; era esticar até 12%), sem pausa inserida (`ritmo.pausa_congelada: true` religa); `motor/compor_avatar.sh`: o rosto sai 0,5 s depois da última palavra (era 9 s congelado). `cena.py`: painel.titulo sem `de` entra na 1ª palavra dele dita; caixa da pergunta entra depois da última palavra; meia tela não passa da fala. `motor/mapa.html`: diagrama com até 4 nós em tamanho grande, nós só aparecem quando ditos, comentário ~2 s depois da pergunta com fundo escurecido. `checar`: fala 450–900 (objetivo 620, aviso acima), print sem repetir, painel.titulo amarrado a uma palavra. `revisar` chama `conferir_montagem` (reprova avatar esticado, rosto parado ≥ 1,2 s até a última palavra e pergunta por cima da fala; aviso acima de 60 s). Crítico: fluência, explicação com comparação concreta, imagem com teste do leigo, print sem repetir. Revisor: tela vazia e print que contradiz. Testado: a v2 remontada com o avatar já gravado (44,1 s, k = 1, sem congelar, fecho em fila) passa na `conferir_montagem`; freezedetect acha o rosto parado do vídeo antigo a partir de 38,8 s; a ficha v2 reprova no `checar` (print repetido); fichas da fila continuam OK. Medida de frase telegráfica testada e descartada (não separa a v2 das aprovadas): fica com o crítico.

## 1.9.7 — 17/11/2026

Nunca calmo (D25, Nei 17/11/2026: "nenhum vídeo tem que sair calmo; r7ex ou rtex não são vídeos calmos, são provocativos, são virais e têm que ter gancho, fonte de imagem e de narração"). Caso: `2026-11-17-enxame-quebra-empresa-lives4` abriu com "Você pensou em montar um enxame de agentes? A Anthropic mediu…", capa-metáfora em meia tela, e passou com 8 no crítico. Modelo: `plano.posicao` (opinião do Nei em 1ª pessoa), `pessoa` com o nível de IA, PADRAO §2.5, bot-ficha, modelo e skill. Verificação: `checar` reprova abertura morna e, com `posicao`, gancho fora de contrario/provocacao/acusacao, tese em pergunta ou sem 1ª pessoa nas partes 1–2 (avatar gravado: só aviso); crítico com nota de pressão e teste do leigo; revisor com "nunca calmo". Tela: `abertura.layout: cheia` (arte em tela cheia, rosto no canto desde o quadro 0; capa pedida em tela cheia) e teste do leigo no pedido da capa. Regressão: a ficha do reel calmo reprova no `checar` (abertura morna) e no crítico (gancho 5, média 6,9); a ficha v2 (`2026-11-17-esqueca-os-enxames-lives4`) passa nos dois (gancho 9, média 8,4); 16 conferências da produção ok.

## 1.8.7 — 17/11/2026

Capa: manchete entre 6% e 24% da altura e a cena chocante logo abaixo, entre 24% e 41%; dos 42% para baixo só fundo. No 1º teste (lives3 da imersão) a avalanche ficou atrás da legenda e do rosto em meia tela.

## 1.8.6 — 17/11/2026

Capa chocante (D24, Nei 17/11/2026: "a imagem inicial chocante não está feita com o codex"). O pedido da `abertura.png` ganha o padrão CHOQUE (momento da perda/quebra ou o "depois", nunca solução pronta nem anúncio calmo; luz vermelha no perigo). `imagens` grava `capa/abertura.codex.json` só se a capa for cópia byte a byte de um arquivo do `generated_images` do Codex; `render` recusa ficha com gancho sem essa prova (edição antiga: `R7X_CAPA_ANTIGA=1`). Testado: capa do Codex aceita, capa da imersão posta por fora recusada.

## 1.7.6 — 17/11/2026

`ia_motor.py cota ver|liberar` para ver e tirar a trava antes do horário; testes antigos isolados do banco real de cota; IA.md corrigido (inverter principal = editar os dois no YAML; reserva vale também para 429 estruturado).

## 1.7.5 — 17/11/2026

Crítico do plano pelo `producao/ia.yaml` (etapa `critico_plano`, Claude opus-5-5/low com reserva Codex gpt-6.1-sol/medium), sem `claude -p` fixo; `R7X_CRITICO=codex` preservado. Trava de cota compartilhada no `ia_motor.py` (tabela `pools` do EngineBridge): recusa estruturada do Claude grava o horário de volta e as chamadas seguintes falham na hora; reserva só entre assinaturas, texto/visão, com cota confirmada. Revisor sem cota espera sem contar erro; `--no-session-persistence` nas chamadas automáticas. 17 contratos e 16 conferências passaram; crítico real nos dois motores.

## 1.6.5 — 15/11/2026

Isolar a variável de configuração por projeto e remover chaves herdadas dos CLIs; a seleção por etapa continua explícita. Versões dos manifestos alinhadas.

## 1.6.4 — 15/11/2026

Revisor visual configurável por etapa (tipo/motor/modelo/esforço), imagens anexadas, sem fallback pago. APIs desativadas. Teste real Codex aprovado; 6 contratos de IA e testes existentes da produção passaram. Nenhuma publicação pelo teste.

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
