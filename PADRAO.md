# Padrão r7ex — o reel viral do INEMA

**r7ex = roteiro de 7 etapas (r7e) + acabamento de telejornal do eventosextremospub (x).**
Fechado em 18/10/2026 com o Nei, depois de dois lotes reprovados ("não tem gancho", "ficou padrão").
Decisões no kit `inema-design`: D9 (gancho = gatilho), D10 (propósito e plano), D11 (acabamento).

Objetivo de todo reel: **trazer gente para o inema.club.** Se não viralizar, não atingiu o objetivo.

---

## 1. Plano (antes da fala)

| Campo | Regra |
|---|---|
| pessoa | público geral (IA traduzida para o dia a dia), não o nicho |
| quer | ganhar algo, resolver uma dor ou chegar a um desejo — uma frase |
| gancho | medo, novidade ou provocação, **com número ou fato** (e fonte) |
| nota | 0–10: "um desconhecido rolando o feed para aqui?" Abaixo de **8**, troque o ângulo ou o tema |
| destino | o curso/guia/formação do inema.club que resolve (URL para o print) |

Grátis só quando a página diz ou o Nei afirma. Nunca inventar número.

**Portão de viralidade (D15, Nei 20/10/2026: "isso prende alguém, isso engaja alguém? validar as 7 etapas, o objetivo é
ser viral").** Cada parte tem `prende:` (por que um desconhecido continua ali). Antes do avatar, `r7ex.py plano <pasta>`
(crítico `claude -p` + `producao/critico-plano.md`) dá nota por parte e lista **bloqueios** objetivos (fato sem origem em
`plano.fatos`, produto sem logo, fecho incompleto, pedido do Nei não cumprido). Passa com **zero bloqueios, gancho ≥ 8,
média ≥ 7,5 e nenhuma parte < 6** (calibrado em 21/10: "todas ≥ 8" não convergia). Fatos da fonte vão em `plano.fatos`
(com o trecho); o que o Nei exigiu vai em `pedido:`; reel de lista pode ter `fala_max` (≤ 900) com `fala_max_motivo`.
A produção só manda ao estúdio roteiro aprovado. **Ético e competitivo:** o fato verdadeiro mais forte, dito com força
("vazou", "apareceu no código", "num teste custou 1 centavo"); a incerteza vai na linha de fonte, não amolece a fala.
Nada inventado — exagero falso zera a parte.

**Emoção primeiro, a verdade confirma (Nei, 21/10/2026): "temos nossa ética, que entende o povo e não a máquina; não podemos
faltar com a verdade, mas ela vem depois para confirmar e não impor; a emoção vem primeiro".** A fala conversa com a pessoa
(pergunta em "você", palavra simples, sentimento); o número e a fonte vão para a tela (contador, gráfico, linha de fonte).
A fala pode simplificar no mesmo sentido da fonte, nunca contradizê-la. CTA pede compromisso positivo ("eu consigo / eu faço /
eu vou tentar"), nunca confissão de fracasso. O crítico (`producao/critico-plano.md`) segue esta regra.

## 2. Roteiro — 7 partes, ~30–40 s, fala de 550–700 caracteres

| Parte | Função | Regra |
|---|---|---|
| 1 | **Gancho** | o gatilho + o número; nunca desarmar na mesma frase |
| 2 | **Medo / prova** | por que isso é com você (ou "já aconteceu 3 vezes") |
| 3 | **Desejo** | como fica se der certo |
| 4 | **Facilidade** | derruba "não sou técnico / não tenho tempo" |
| 5 | **Descoberta** | o método ou o nome da solução, com 3 itens |
| 6 | **Benefício / urgência** | o depois, ou "aproveita antes de…" |
| 7 | **Comentário** | "Tá tudo no inema ponto club. Ou me pede o link aqui nos comentários." |

A ordem 2–6 pode se adaptar ao tema (as etapas são checklist de gatilhos), mas são sempre 7 partes.
Fala: número e ano **por extenso** (o avatar lê); a legenda troca por algarismo (`trocas` na ficha).
Fala nunca termina parte em número solto.

## 3. Tela — motor do eventosextremospub

**Mudança de 20/10/2026 (D13, D14):**
- **Produto citado = logo real.** Parte que fala de um produto/empresa usa `logos: [{id, nome}]` (1 ou 2 por tela): cartão
  com o logo real (pacote MIT lobe-icons em `~/.cache/r7ex/lobe-icons`, `ferramentas/logos.sh`), luz âmbar e o nome
  grande. Com `imagem:` junto, o Codex faz só o fundo (centro vazio) e o logo é colado. Fora do produto, imagem sem logo.
  Um produto por parte; vários produtos = tela para cada um ou dois lado a lado, nunca três nomes num painel.
- **Lista no alto, embaixo uma coisa só.** `lista: {k, itens: [[palavra, texto]], borda}` aparece sobre a imagem
  (y ~860–1150), item a item na palavra. O `painel` embaixo (à esquerda do avatar) leva UMA coisa: `titulo` (texto
  grande, `cor` opcional), `contador` ou `logo` (id do pacote). Ficha antiga com `painel.itens` sobe sozinha para a lista.

- **Abertura:** o título do gancho **desenhado pelo Codex dentro da arte** (branco + amarelo ou vermelho), metade de cima.
- **Imagens:** uma por parte, **UM assunto só em ação dramática** (quebrando, acendendo, se abrindo, sendo puxado), grande,
  na metade de cima; luz de cinema (foco forte ou contraluz com recorte), amarela no assunto ou vermelha #ff2a1f no perigo;
  fundo preto liso e metade de baixo vazia. Na ficha, descreva um objeto + a ação + a sensação; nunca "cinco objetos",
  pilhas, chuva de partículas/papéis ou hologramas. O motor escurece a faixa de baixo (legenda/painel/avatar).
  Calibrado em 19/10/2026: o lote com muita coisa ficou "saturado, muita informação"; o só-neutro ficou "limpo demais,
  sem impacto"; o meio-termo `edicoes/2026-10-19-skills15-impacto` foi APROVADO pelo Nei em 19/10/2026 — é a referência.
  Sem logos (exceto o produto citado, D13), sem rostos reconhecíveis; robô = humanoide estilo Optimus de visor preto.
- **Faixa do topo:** marca do tema ("INEMA · …") + **selo vermelho**; **linha de fonte** embaixo.
- **Avatar:** caixinha no canto desde o quadro 0 (nunca tela cheia — D8).
- **Painel por parte:** 2–4 itens com emoji entrando **na palavra certa** (só o que já foi dito, no máximo 3 na tela); **contador** sempre que houver número;
  borda vermelha no medo, amarela no ganho, verde na solução.
- **Prova real:** pelo menos 1 print da página do inema.club / curso.
- **Diagrama animado** (D12, 19/10/2026): uma parte pode trocar a imagem por `diagrama:` — `forma: fluxo | hub | terminal`,
  `titulo`, `nos: [{de: <palavra da fala>, ic: emoji, txt, sub?, cor?: vd}]` (2–6; no terminal `tipo: cmd | out | ok | cm`;
  no hub `centro: {de, ic, txt}`). Fundo preto com grade leve; cada nó acende na palavra. Use em produto/técnico
  (como funciona, o que tem no repo, o comando que roda); deixe a abertura com a arte do Codex.
- **Legenda karaokê:** a palavra falada acende; vermelho = perigo, amarelo = ganho e números.
- **Fecho:** caixa vermelha com **pergunta** (gera comentário) + pílula "inema.club".

## 4. Portões

- ficha: 7 partes, fala 550–700 caracteres, toda palavra de painel/lista/contador existe na fala da parte, `prende` em cada parte;
- plano: `r7ex.py plano` aprovado (sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6) antes de gravar o avatar;
- avatar × fala ≥ 90% (retempo); duração < 60 s;
- grafia do título da abertura conferida na imagem (ler a imagem antes do render);
- revisão da folha de 12 quadros (`r7ex.py revisar`): nada cobrindo nada, prints legíveis, **produto com logo, impacto ≥ 7**.

**Tolerância (Nei, 21/10/2026: "temos que ser mais tolerantes na reprovação; quando for sugestão vai em uma tarja vermelha
dizendo SUGESTÃO e manda para frente, aí se for eu refaço").** Só DEFEITO para o vídeo: título errado, quadro preto, print
ilegível, número errado, texto ilegível por sobreposição, marcação crua (`**`), avatar ausente/cheio, fecho incompleto,
marca d'água/rosto. Estilo (logo faltando, impacto < 7, encostar de leve, lista embaixo) é **SUGESTÃO**: o vídeo segue para
a fila e o aviso "Terminei" no v3 leva a tarja 🟥 SUGESTÃO com os itens. No plano, logo faltando também vira `melhorar`,
não bloqueio.

## 5. Publicação

- v3 sempre (`r7ex.py enviar`).
- Canal só pela fila (`r7ex.py fila` → `~/projetos/wifi/fila-lives7`), nunca upload direto.
