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
| gancho | um dos 5 tipos do §2.1 (contrário, perda, estatística, terceiro, notícia), **com número ou fato** (e fonte); nunca lista |
| nota | 0–10: "um desconhecido rolando o feed para aqui?" Abaixo de **8**, troque o ângulo ou o tema |
| destino | o curso/guia/formação do inema.club que resolve (URL para o print) |

Grátis só quando a página diz ou o Nei afirma. Nunca inventar número.

**Portão de viralidade (D15, Nei 20/10/2026: "isso prende alguém, isso engaja alguém? validar as 7 etapas, o objetivo é
ser viral").** Cada parte tem `prende:` (por que um desconhecido continua ali). Antes do avatar, `r7ex.py plano <pasta>`
(crítico `claude -p` + `producao/critico-plano.md`) dá nota por parte e lista **bloqueios** objetivos (fato sem origem em
`plano.fatos`, produto sem logo, fecho incompleto, pedido do Nei não cumprido). Passa com **zero bloqueios, gancho ≥ 8,
média ≥ 7,5 e nenhuma parte < 6** (calibrado em 21/10: "todas ≥ 8" não convergia). Fatos da fonte vão em `plano.fatos`
(com o trecho); o que o Nei exigiu vai em `pedido:`; um tema com muitos itens (ex.: os comandos de UMA ferramenta) pode ter `fala_max` (≤ 800) com `fala_max_motivo` — nunca temas diferentes juntos (§2.1).
A produção só manda ao estúdio roteiro aprovado. **Ético e competitivo:** o fato verdadeiro mais forte, dito com força
("vazou", "apareceu no código", "num teste custou 1 centavo"); a incerteza vai na linha de fonte, não amolece a fala.
Nada inventado — exagero falso zera a parte.

**Emoção primeiro, a verdade confirma (Nei, 21/10/2026): "temos nossa ética, que entende o povo e não a máquina; não podemos
faltar com a verdade, mas ela vem depois para confirmar e não impor; a emoção vem primeiro".** A fala conversa com a pessoa
(pergunta em "você", palavra simples, sentimento); o número e a fonte vão para a tela (contador, gráfico, linha de fonte).
A fala pode simplificar no mesmo sentido da fonte, nunca contradizê-la. CTA pede compromisso positivo ("eu consigo / eu faço /
eu vou tentar"), nunca confissão de fracasso. O crítico (`producao/critico-plano.md`) segue esta regra.

## 2. Roteiro — 7 partes, fala de 450–620 caracteres (~30–37 s de fala + 9 s de cartão)

**Ritmo (Nei, 28/10/2026).** Medimos 202–222 palavras/min e nenhum silêncio: rápido demais para o público 40+. Agora:
- fala dimensionada para **160–190 palavras/min**: **450–620 caracteres** (≈ 85–110 palavras). Um tema com muitos itens pode ir a
  `fala_max` ≤ 800 com `fala_max_motivo` (passa de 1 min acima disso);
- o HeyGen fala no ritmo dele (~210), então a montagem (`r7ex/ritmo.py`) estica a fala até ~182 palavras/min (no máximo
  12%, tom preservado, boca casada) — nunca acelera;
- **silêncio de ~0,75 s antes da máxima** (a frase de efeito final; padrão = início da parte 6, ou `ritmo.pausa_antes:
  {parte: 6, de: <palavra>}`): a voz e a trilha somem, o quadro segura;
- frases curtas; a máxima numa frase só, curta, que a pessoa repete.

| Parte | Função | Regra |
|---|---|---|
| 1 | **Gancho** | um dos 5 tipos do §2.1 + o número; manchete do quadro 0 mais forte que a fala; nunca desarmar na mesma frase |
| 2 | **Medo / prova** | a prova com fonte (até ~20 s) e o problema do espectador **com absolvição** ("não é falta de estudo, ninguém te deu o mapa") |
| 3 | **Desejo** | como fica se der certo |
| 4 | **Facilidade** | derruba "não sou técnico / não tenho tempo" |
| 5 | **Descoberta** | o método ou o nome da solução, com 3 itens |
| 6 | **Benefício / urgência** | o depois, ou "aproveita antes de…" |
| 7 | **Comentário** | "Tá tudo no inema ponto club. Ou me pede o link aqui nos comentários." |

A ordem 2–6 pode se adaptar ao tema (as etapas são checklist de gatilhos), mas são sempre 7 partes.
Fala: número e ano **por extenso** (o avatar lê); a legenda troca por algarismo (`trocas` na ficha).
Fala nunca termina parte em número solto.

### 2.1 Gancho: o quadro 0 e os 3 primeiros segundos (v1.2.0, 28/10/2026)

O Nei perguntou se os reels usavam as técnicas de chamada que analisamos; usavam só a forma. A edição de 28/10 abriu com
"5 novidades de IA…", um gancho de **lista**, que nenhum reel de referência usa. Regras novas (Nei: "sim, aplica no r7ex também"):

1. **`gancho.tipo` obrigatório**, um destes:

   | tipo | o que é | exemplo de manchete |
   |---|---|---|
   | `contrario` | manda parar ou inverte o senso comum | PARA DE MONTAR AGENTE DE IA |
   | `perda` | perda hipotética | E SE O CLAUDE SUMISSE AMANHÃ? |
   | `estatistica` | número que dá medo, com fonte em `gancho.fontes` | METADE DO CÓDIGO É LIXO |
   | `terceiro` | história de outra pessoa, com número | ACORDOU DEVENDO US$ 1.700 |
   | `noticia` | fato de ontem/desta semana, com `data` e fonte | SAIU O CARRO VOADOR? |

   **Proibido:** lista ("5 novidades…", "N coisas…"), "você sabia que…", "eu fiz…". O `checar` reprova.
2. **Manchete do quadro 0** (`gancho.manchete`): no máximo **6 palavras**, CAIXA ALTA, **uma** palavra em amarelo
   (`gancho.destaque`), **mais forte que a fala** (tela "PARA DE MONTAR", voz "eu acho que você não devia montar"). O `checar`
   reprova manchete igual a um pedaço da fala. Ela é a capa: pronta e legível no quadro 0.
3. **Objeto-metáfora com dano ou ameaça** (`gancho.objeto`: lixeira, olhos em X, risco vermelho, chave partida) no centro da
   abertura; o pedido ao Codex leva o objeto e a manchete. **Troca de quadro a cada ~1 s nos 3 primeiros segundos:** a montagem
   corta a capa em 0 s → aproximação 1,05× em 1 s → 1,10× em 2 s (`pecas.batidas`, presa no meio da manchete). É corte de
   enquadramento, não pulso de brilho (que não conta como troca no `video/style.md`).
4. **Prova com fonte até ~20 s** (`gancho.prova: {parte: 1|2, de: <palavra do número>}`, até a 60ª palavra) e, logo depois,
   o **problema do espectador com absolvição** (`gancho.absolvicao`, igual na fala da parte 2 ou 3: "não é falta de estudo,
   ninguém te deu o mapa").
5. **Um tema por vídeo.** O r7ex não junta temas diferentes numa lista. Pedido com vários temas → a ficha propõe N vídeos,
   um por tema (no bot: faz o mais forte e lista os outros no resumo, um `/r7ex` para cada).
6. A parte 7 ("tá tudo no inema ponto club…"), o cartão de 9 s e o ritmo de 160–190 palavras/min ficam como estão. Nunca
   prometer "eu te mando".

```yaml
gancho:
  tipo: terceiro
  manchete: "ACORDOU DEVENDO US$ 1.700"
  destaque: "1.700"
  objeto: "uma chave dourada partida ao meio, com um risco vermelho, presa a um cartão de crédito rachado"
  prova: {parte: 1, de: "1.700"}
  absolvicao: "não é descuido seu"
  fontes: [{nome: "relatos de usuários afetados, out/2026", trecho: "US$ 1.700 de conta numa noite"}]
  # noticia: data: 2026-10-27  (até 7 dias antes da edição)
```

## 3. Tela — motor do eventosextremospub

**Mudança de 20/10/2026 (D13, D14):**
- **Produto citado = logo real.** Parte que fala de um produto/empresa usa `logos: [{id, nome}]` (1 ou 2 por tela): cartão
  com o logo real (pacote MIT lobe-icons em `~/.cache/r7ex/lobe-icons`, `ferramentas/logos.sh`), luz âmbar e o nome
  grande. Com `imagem:` junto, o Codex faz só o fundo (centro vazio) e o logo é colado. Fora do produto, imagem sem logo.
  Um produto por parte; vários produtos = tela para cada um ou dois lado a lado, nunca três nomes num painel.
- **Lista no alto, embaixo uma coisa só.** `lista: {k, itens: [[palavra, texto]], borda}` aparece sobre a imagem
  (y ~860–1150), item a item na palavra. O `painel` embaixo (à esquerda do avatar) leva UMA coisa: `titulo` (texto
  grande, `cor` opcional), `contador` ou `logo` (id do pacote). Ficha antiga com `painel.itens` sobe sozinha para a lista.

- **Abertura:** a manchete do gancho (`gancho.manchete`, ≤ 6 palavras, uma em amarelo) **desenhada pelo Codex dentro da arte**, metade de
  cima, com o objeto com dano no centro; nos 3 primeiros segundos a capa troca de quadro a cada ~1 s (§2.1). Ficha antiga sem
  `gancho:` continua com `abertura.branco` + `destaque`.
- **Imagens:** uma por parte, **UM assunto só em ação dramática** (quebrando, acendendo, se abrindo, sendo puxado), grande,
  na metade de cima; luz de cinema (foco forte ou contraluz com recorte), amarela no assunto ou vermelha #ff2a1f no perigo;
  fundo preto liso e metade de baixo vazia. Na ficha, descreva um objeto + a ação + a sensação; nunca "cinco objetos",
  pilhas, chuva de partículas/papéis ou hologramas. O motor escurece a faixa de baixo (legenda/painel/avatar).
  Calibrado em 19/10/2026: o lote com muita coisa ficou "saturado, muita informação"; o só-neutro ficou "limpo demais,
  sem impacto"; o meio-termo `edicoes/2026-10-19-skills15-impacto` foi APROVADO pelo Nei em 19/10/2026 — é a referência.
  Sem logos (exceto o produto citado, D13), sem rostos reconhecíveis; robô = humanoide estilo Optimus de visor preto.
- **Faixa do topo:** marca do tema ("INEMA · …") + **selo vermelho**; **linha de fonte** embaixo.
- **Avatar (D16, 21/10/2026):** abre em **meia tela na metade de baixo** (1080x960) durante a parte 1 (gancho) e depois vai
  para a caixinha do canto (PiP); `avatar: meia` numa parte faz o rosto voltar à meia tela nela (o plano decide). Na meia tela
  título/legenda/lista ficam na metade de cima e o painel de baixo some. A abertura do Codex põe título e assunto na metade de cima.
  Nunca tela cheia (D8).
- **Painel por parte:** 2–4 itens com emoji entrando **na palavra certa** (só o que já foi dito, no máximo 3 na tela); **contador** sempre que houver número;
  borda vermelha no medo, amarela no ganho, verde na solução.
- **Prova real:** pelo menos 1 print da página do inema.club / curso.
- **Diagrama animado** (D12, 19/10/2026): uma parte pode trocar a imagem por `diagrama:` — `forma: fluxo | hub | terminal`,
  `titulo`, `nos: [{de: <palavra da fala>, ic: emoji, txt, sub?, cor?: vd}]` (2–6; no terminal `tipo: cmd | out | ok | cm`;
  no hub `centro: {de, ic, txt}`). Fundo preto com grade leve; cada nó acende na palavra. Use em produto/técnico
  (como funciona, o que tem no repo, o comando que roda); deixe a abertura com a arte do Codex.
- **Legenda karaokê:** a palavra falada acende; vermelho = perigo, amarelo = ganho e números.
- **Fecho:** caixa vermelha com **pergunta** (gera comentário) + pílula "inema.club".
- **Cartão segurado (Nei, 28/10/2026):** o vídeo NÃO corta na última palavra. O cartão do comentário fica **9 s** depois
  dela, com o gesto encenado no meio da tela: campo "Adicione um comentário…" → o texto sendo digitado (`cta.comentario`,
  ou a palavra em CAIXA ALTA do `cta.b`) → "Publicar" apertado → o comentário publicado. Avatar congelado no PiP, trilha
  continuando até o fade final, sem legenda. Antes: 0,8–1,6 s de cartão.

## 4. Portões

- ficha: 7 partes, fala 450–620 caracteres (um tema com muitos itens: até 800 com motivo), toda palavra de painel/lista/contador existe na fala da parte, `prende` em cada parte;
- gancho (v1.2.0, §2.1): `gancho.tipo` válido, manchete ≤ 6 palavras em CAIXA ALTA e diferente da fala, `destaque` = uma palavra dela, `objeto`, `prova` até a 60ª palavra, `absolvicao` na parte 2 ou 3, fontes (estatística/terceiro/notícia) e data (notícia); lista, "você sabia" e "eu fiz" reprovam. Edição com avatar já gravado só recebe aviso;
- plano: `r7ex.py plano` aprovado (sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6) antes de gravar o avatar;
- avatar × fala ≥ 90% (retempo); ritmo 160–190 palavras/min, pausa antes da máxima e 9 s de cartão (`avatar/ritmo.json`); duração < 60 s;
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
