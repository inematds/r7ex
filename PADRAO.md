# Padrão r7ex — o reel viral do INEMA

**r7ex = roteiro de 7 etapas (r7e) + acabamento de telejornal do eventosextremospub (x).**
Fechado em 18/10/2026 com o Nei, depois de dois lotes reprovados ("não tem gancho", "ficou padrão").
Decisões no kit `inema-design`: D9 (gancho = gatilho), D10 (propósito e plano), D11 (acabamento).

Objetivo de todo reel: **trazer gente para o inema.club.** Se não viralizar, não atingiu o objetivo.

---

## 1. Plano (antes da fala)

| Campo | Regra |
|---|---|
| pessoa | público geral (IA traduzida para o dia a dia), não o nicho; diga **quanto ela sabe de IA** ("gestor que nunca rodou um agente", D25) |
| posicao | quando a tese é **opinião do Nei**: as palavras dele em 1ª pessoa ("faz um ano que eu falo disso: a ideia é boa, mas o custo é proibitivo"); abre a fala (§2.5) |
| quer | ganhar algo, resolver uma dor ou chegar a um desejo — uma frase |
| gancho | um dos tipos do §2.1–2.3 (contrário, perda, estatística, terceiro, notícia, provocação, promessa, acusação), **com número, fato ou a dor/desejo em "você"**; nunca lista |
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

## 2. Roteiro — 7 partes, fala com objetivo de 620 caracteres (teto 900)

**Fluência primeiro (D26, Nei 17/11/2026: "parece não tem fluência, não parece natural eu falando"; "teto pode ficar em
900, mantendo objetivo do 620… temos que ser flexíveis com algo que não vai ser o fundamental").** Substitui o ritmo de 28/10:
- fala com **objetivo de 620 caracteres**; passa até **900** com aviso. Fala natural vale mais que caber: nunca encurtar
  até virar frase telegráfica ("Cada agente lê tudo, fala, refaz." reprovou). Frase ligada, do jeito que o Nei fala;
- a montagem (`r7ex/ritmo.py` v2) **não estica** a fala: o avatar fala na velocidade natural do HeyGen (~195 palavras/min).
  Antes (28/10) esticava até 12% para ~182, e boca e gesto ficavam em câmera lenta;
- **nenhum quadro congelado com o Nei na tela**: sem pausa inserida antes da máxima (o vão natural fica; `ritmo.pausa_congelada:
  true` religa só se pedido) e o rosto sai 0,5 s depois da última palavra (o cartão de 9 s segue sem ele);
- a máxima numa frase só, curta, que a pessoa repete;
- **explicação impactante** (partes que explicam o caminho, em geral 3 e 4): uma comparação do dia a dia que um gestor
  vê ("dez pessoas na mesma reunião lendo o mesmo relatório e cobrando por hora") e uma tela que a mostra — imagem
  concreta da comparação ou diagrama com poucas peças grandes, que entram na palavra. Abstração ("quem coordena, como se
  ligam, onde aplicar") sem exemplo não explica;
- **imagem também** (teste do leigo em TODA `imagem`, não só a abertura); o mesmo print não se repete em duas partes, e
  o texto do print não pode contradizer o gancho.

| Parte | Função | Regra |
|---|---|---|
| 1 | **Gancho** | um dos tipos do §2.1–2.3 + o número ou a dor/desejo em "você"; manchete do quadro 0 clara e completa (a informação inteira, entendida sozinha); nunca desarmar na mesma frase |
| 2 | **Medo / prova** | a prova com fonte (até ~20 s) e o problema do espectador **com absolvição** ("não é falta de estudo, ninguém te deu o mapa") |
| 3 | **Desejo** | como fica se der certo |
| 4 | **Facilidade** | derruba "não sou técnico / não tenho tempo" |
| 5 | **Descoberta** | o método ou o nome da solução, com 3 itens |
| 6 | **Benefício / urgência** | o depois, ou "aproveita antes de…" |
| 7 | **Comentário** | frase de comunidade com o inema ponto club (§2.4: "toda semana tem kit novo, grátis, no inema ponto club") + pergunta de verdade sobre a vida/opinião da pessoa (grátis só se for verdade); nunca "me pede o link" nem "comenta PALAVRA" (§2.3) |

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
2. **Manchete do quadro 0** (`gancho.manchete`): até **9 palavras** (acima de 6 o `checar` avisa para conferir a capa), CAIXA ALTA,
   **uma** palavra em amarelo (`gancho.destaque`), CLARA E COMPLETA (Nei, 12/11/2026: "manchete tem que ser objetiva mas clara… uma informação clara e entendida, e aí vamos atrás de detalhes"): quem lê só ela entende o que acontece (quem + o quê; "SUA IA DIZ 'PRONTO' SEM TER FEITO"), nunca enigmática ("IA COM PROVA") nem slogan sem sujeito; a fala traz os detalhes (v1.4.4; antes: "≤ 6 palavras, mais forte que a fala").
   Manchete igual a um pedaço da fala só gera aviso. Ela é a capa: pronta e legível no quadro 0.
3. **Objeto-metáfora com dano ou ameaça** (`gancho.objeto`: lixeira, olhos em X, risco vermelho, chave partida) no centro da
   abertura; o pedido ao Codex leva o objeto e a manchete. **Troca de quadro a cada ~1 s nos 3 primeiros segundos:** a montagem
   corta a capa em 0 s → aproximação 1,05× em 1 s → 1,10× em 2 s (`pecas.batidas`, presa no meio da manchete). É corte de
   enquadramento, não pulso de brilho (que não conta como troca no `video/style.md`).
4. **Prova com fonte até ~20 s** (`gancho.prova: {parte: 1|2, de: <palavra do número>}`, até a 60ª palavra) e, logo depois,
   o **problema do espectador com absolvição** (`gancho.absolvicao`, igual na fala da parte 2 ou 3: "não é falta de estudo,
   ninguém te deu o mapa").
5. **Um tema por vídeo.** O r7ex não junta temas diferentes numa lista. Pedido com vários temas → a ficha propõe N vídeos,
   um por tema (no bot: faz o mais forte e lista os outros no resumo, um `/r7ex` para cada).
6. A parte 7 ("tá tudo no inema ponto club…"), o cartão de 9 s e a fala na velocidade natural (D26) ficam como estão. Nunca
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

### 2.3 Chamada: clareza + atenção, e o CTA sem palavra nem link (v1.4.4, 12/11/2026, D20)

Nei: "não adianta ele estar claro e correto se não chama atenção, não mexe na dor ou desejo". E: "no CTA não deve pedir
para a pessoa colocar palavra ou link; deve sempre criar engajamento natural e [dizer] que o kit está disponível free no
inema.club, direto na internet". Regra única para todos os motores: `~/projetos/inema-design/regras/chamada.md`.

1. **Dois tipos de gancho a mais (soma):** `promessa` (o ganho com a garantia verdadeira, em "você": "Seu agente nunca
   mais diz 'pronto' sem prova.") e `acusacao` (revela o que está acontecendo com a pessoa: "Seu agente mente pra você.").
   O `checar` reprova os dois sem "você/seu/sua" na 1ª frase.
2. **Método com nome:** quando o vídeo entrega um método ou kit, a parte 5 (Descoberta) diz o NOME dele, e o nome volta
   na parte 7. Inventário ("8 frases", "9 soluções") nunca vai na manchete.
3. **Parte 7 nova:** uma pergunta de verdade, ligada à dor/desejo, que a pessoa responde com a opinião ou a experiência
   dela, + "tá tudo no inema ponto club" ("o kit está grátis no inema ponto club, direto na internet", quando for verdade).
   Proibido: "me pede o link", "comenta PALAVRA", "link na bio", "te mando". Sem "pede" na fala, `cta.de` = a palavra
   onde a caixa da pergunta entra (1ª palavra da pergunta). Edição com avatar já gravado só recebe aviso.

### 2.2 Provocação e entrega (v1.3.1, 29/10/2026) — soma ao §2.1, não substitui

O Nei comparou os r7ex do robô com os 5 reels de referência e o gitbombando, que bombaram ("os do robô ficaram bons, as
novas sugestões também, não quero substituir o anterior; o bombando deu certo porque entregou conteúdo que as pessoas querem").
Os 5 tipos e o "E se…" continuam. Entram duas coisas:

1. **6º tipo, `provocacao`:** a 1ª frase **afirma** (não pergunta) algo que cutuca quem assiste, com **nome ou número**, e
   deixa uma pergunta no ar (por quê? e eu?). Precisa de `gancho.fontes`. O `checar` reprova pergunta e frase sem nome nem número.
2. **`gancho.entrega`** (todo tipo): em uma linha, o que a pessoa **leva** do vídeo e quer ver — o Top 10 do dia, quem está
   trocando gente por robô, o que fazer antes. Sem ela o `checar` avisa (não reprova). Provocação sem entrega é só barulho.

Aberturas que bombaram (use como régua, não como molde):

| Vídeo | 1ª fala |
|---|---|
| referência 1 | "Eu acho que você não devia mais montar agente de IA." |
| referência 2 | "Você sabia que metade do código que o Claude escreve é lixo?" |
| referência 3 | "IA, você viu que ontem saiu o carro voador?" |
| referência 4 | "Se o Claude Code sumisse amanhã, você saberia mexer no sistema que ele montou pra você?" |
| referência 5 | "O cara que ganhou o hackathon montou o produto inteiro em oito horas, sem digitar uma linha de código." |
| gitbombando | "Hoje o GitHub escolheu um professor. E ele não é gente." (tela: +2.371 ESTRELAS PRA UM PROFESSOR ROBÔ) |

Em comum: falam de algo que a pessoa faz ou usa, com nome; o fato estranho vem na 1ª frase; abrem uma pergunta que só o
vídeo responde; e entregam o que prometem.

Provocação no tema robô/emprego (exemplos de 29/10):

| Tela | 1ª fala |
|---|---|
| NENHUM PEDE AUMENTO | "A Hyundai contratou vinte e cinco mil funcionários. Nenhum pede aumento." |
| NÃO É O ROBÔ | "Para de ter medo do robô. Quem vai tirar teu emprego é o colega que já manda nele." (tipo `contrario`) |
| 5 ANOS × 1 FOTO | "Você levou cinco anos pra aprender teu trabalho. Esse robô aprendeu vendo uma foto." |
| O ROBÔ TÁ GANHANDO | "Tem gente chutando robô na rua. E o robô tá ganhando." |

```yaml
gancho:
  tipo: provocacao
  manchete: "NENHUM PEDE AUMENTO"
  destaque: "AUMENTO"
  entrega: "quais empresas já trocam gente por robô e o que fazer antes de chegar na sua"
  fontes: [{nome: "Hyundai, plano de humanoides", trecho: "25 mil robôs humanoides nas fábricas"}]
```

### 2.4 Retenção: pesquisa de ganchos e CTA de pertencimento (v1.5.4, 13/11/2026)

Caso: os vídeos do /swarm (13/11/2026) foram publicados e reprovados pelo Nei ("muito fraca, nem eu consigo ficar
assistindo"). A seção Retenção do explicavideos (`~/projetos/explicavideos/engine/v2/PADRAO-VIRAL.md`, 2.26.11) vale
para o r7ex em duas coisas (Nei, 13/11/2026: "aplica"):

1. **Pesquisa de ganchos antes da ficha** (`gancho.referencias`): 3–5 vídeos de quem fala do tema no YouTube, cada um
   `{canal, titulo, abertura, gatilho}`. Levante títulos com `yt-dlp --flat-playlist "ytsearch15:<termo>"` e a 1ª fala
   (0–35 s) pela legenda automática; anote o gatilho (número antes/depois, perda concreta, imagem fácil, "você também
   pode", promessa do fim; "INSANE" sem conteúdo e abrir pedindo like são fracos). Modelo:
   `~/projetos/output/explica-gemini-swarm/ganchos/LISTA.md`. O crítico do plano compara: o nosso gancho tem de ser
   pelo menos tão forte quanto o melhor delas. **Número de terceiro não entra no roteiro**: é só régua. Sem
   referências ou com menos de 3, o `checar` avisa (não reprova).
2. **CTA de pertencimento:** na parte 7, antes da pergunta final, uma frase curta de comunidade que já carrega o
   "inema ponto club" ("Toda semana tem kit novo, grátis, no inema ponto club."), no lugar do "tá tudo no inema ponto
   club" depois da pergunta (a fala continua em 450–620 caracteres). Depois, a pergunta de verdade (§2.3). Continua
   proibido "comenta PALAVRA", "me pede o link" e "te mando". Sem frase de comunidade antes da pergunta, o `checar` avisa.

```yaml
gancho:
  referencias:
    - {canal: "<canal>", titulo: "<título>", abertura: "<1ª fala, 0–35 s>", gatilho: "perda concreta"}
partes:
  # … parte 7:
  - fala: "Toda semana tem kit novo, grátis, no inema ponto club. E você, já deixou de proteger a sua conta por preguiça?"
```

### 2.5 Nunca calmo: gancho de imagem e de narração (v1.9.7, 17/11/2026, D25)

Nei, 17/11/2026: "nenhum vídeo tem que sair calmo; r7ex ou rtex não são vídeos calmos, são vídeos provocativos, são virais
e têm que ter gancho, fonte de imagem e de narração". Caso: `edicoes/2026-11-17-enxame-quebra-empresa-lives4` (lives4). A tese
era dele ("a ideia é genial, a conta não"), mas a fala virou notícia neutra ("Você pensou em montar um enxame de agentes? A
Anthropic mediu…"), a capa era metáfora (prédio devorado por robôs) em meia tela e o público era de nicho. O crítico deu 8. O
que ele queria: ESQUEÇA OS ENXAMES enorme, imagem em tela cheia que um gestor entende, ele no canto, e "faz um ano que eu falo
de enxames: a ideia é boa, mas o custo é proibitivo, e não sei por que ainda continuam falando disso". Regra comum:
`~/projetos/inema-design/regras/chamada.md` §2b.

1. **Narração:** a 1ª frase afirma com pressão (ordem, acusação, contradição, número que dói). "Você pensou em…?", "Já
   imaginou…?", "Você já ouviu falar…?", "Neste vídeo…" reprovam no `checar`.
2. **Posição do Nei:** com `plano.posicao`, o gancho é `contrario`, `provocacao` ou `acusacao`, a 1ª frase não é pergunta e
   as partes 1–2 têm a opinião em 1ª pessoa ("eu falo disso há um ano"); o número da fonte vira prova logo depois. O
   `checar` reprova. ("Eu fiz/criei" continua proibido: é opinião, não vitrine.)
3. **Imagem:** o quadro 0 passa no teste do leigo: um gestor entende a cena em 1 s (taxímetro girando em R$, fatura, sala de
   reunião), não metáfora que pede para pensar. Vai no pedido da capa ao Codex.
4. **Tela cheia (opcional):** `abertura.layout: cheia` põe a arte em tela cheia e o rosto na caixinha do canto desde o
   quadro 0 (a capa é pedida para tela cheia, com o canto de baixo à direita livre). Sem o campo, vale o D16 (meia tela).
5. **Verificação:** o crítico do plano dá nota de pressão ao gancho (calmo, neutro ou em tom de notícia = ≤ 6, não passa o
   portão de 8) e confere o teste do leigo na cena da capa; o revisor final julga o quadro 0 pelo leigo.

## 3. Tela — motor do eventosextremospub

**Mudança de 20/10/2026 (D13, D14):**
- **Produto citado = logo real.** Parte que fala de um produto/empresa usa `logos: [{id, nome}]` (1 ou 2 por tela): cartão
  com o logo real (pacote MIT lobe-icons em `~/.cache/r7ex/lobe-icons`, `ferramentas/logos.sh`), luz âmbar e o nome
  grande. Com `imagem:` junto, o Codex faz só o fundo (centro vazio) e o logo é colado. Fora do produto, imagem sem logo.
  Um produto por parte; vários produtos = tela para cada um ou dois lado a lado, nunca três nomes num painel.
- **Lista no alto, embaixo uma coisa só.** `lista: {k, itens: [[palavra, texto]], borda}` aparece sobre a imagem
  (y ~860–1150), item a item na palavra. O `painel` embaixo (à esquerda do avatar) leva UMA coisa: `titulo` (texto
  grande, `cor` opcional), `contador` ou `logo` (id do pacote). Ficha antiga com `painel.itens` sobe sozinha para a lista.

- **Capa chocante (D24, v1.8.6):** a `abertura.png` sai SEMPRE do `r7ex.py imagens` (Codex image_gen) e mostra o momento da perda/quebra ou o "depois" chocante, nunca a solução pronta nem anúncio calmo (mão apertando botão, documento com check). O `imagens` grava a prova `capa/abertura.codex.json` (sha256 igual a um arquivo do `generated_images`) e o `render` recusa sem ela. Arte posta à mão na pasta não vale.
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
  Nunca o AVATAR em tela cheia (D8). **Exceção D25 (17/11/2026):** `abertura.layout: cheia` → a ARTE da abertura em tela cheia e o
  rosto na caixinha do canto desde o quadro 0 (§2.5).
- **Painel por parte:** 2–4 itens com emoji entrando **na palavra certa** (só o que já foi dito, no máximo 3 na tela); **contador** sempre que houver número;
  borda vermelha no medo, amarela no ganho, verde na solução.
- **Prova real:** pelo menos 1 print da página do inema.club / curso.
- **Diagrama animado** (D12, 19/10/2026): uma parte pode trocar a imagem por `diagrama:` — `forma: fluxo | hub | terminal`,
  `titulo`, `nos: [{de: <palavra da fala>, ic: emoji, txt, sub?, cor?: vd}]` (2–6; no terminal `tipo: cmd | out | ok | cm`;
  no hub `centro: {de, ic, txt}`). Fundo preto com grade leve; cada nó acende na palavra. Use em produto/técnico
  (como funciona, o que tem no repo, o comando que roda); deixe a abertura com a arte do Codex.
- **Legenda karaokê:** a palavra falada acende; vermelho = perigo, amarelo = ganho e números.
- **Fecho em fila (D26, 17/11/2026):** a pílula "inema.club" entra quando o Nei diz "inema ponto club"; a caixa vermelha da
  **pergunta** entra SOZINHA depois da última palavra da pergunta (nunca por cima da fala); ~2 s depois, o gesto de comentar,
  com o fundo escurecido (nunca por cima do print). Antes os três entravam juntos.
- **Cartão segurado (Nei, 28/10/2026):** o vídeo NÃO corta na última palavra. O cartão do comentário fica **9 s** depois
  dela, com o gesto encenado no meio da tela: campo "Adicione um comentário…" → o texto sendo digitado (`cta.comentario`,
  ou a palavra em CAIXA ALTA do `cta.b`) → "Publicar" apertado → o comentário publicado. Sem o rosto (D26: sai 0,5 s depois da última palavra), trilha
  continuando até o fade final, sem legenda. Antes: 0,8–1,6 s de cartão.

## 4. Portões

- ficha: 7 partes, fala 450–900 caracteres (objetivo 620, aviso acima; D26), print sem repetir entre partes, painel.titulo amarrado a uma palavra (`de` ou palavra do título na fala), toda palavra de painel/lista/contador existe na fala da parte, `prende` em cada parte;
- gancho (v1.2.0, §2.1): `gancho.tipo` válido, manchete ≤ 6 palavras em CAIXA ALTA e diferente da fala, `destaque` = uma palavra dela, `objeto`, `prova` até a 60ª palavra, `absolvicao` na parte 2 ou 3, fontes (estatística/terceiro/notícia) e data (notícia); lista, "você sabia" e "eu fiz" reprovam. Edição com avatar já gravado só recebe aviso;
- nunca calmo (v1.9.7, §2.5): abertura morna reprova; `plano.posicao` exige gancho contrario/provocacao/acusacao, 1ª frase afirmativa e 1ª pessoa nas partes 1–2; aviso sem `plano.posicao`;
- retenção (v1.5.4, §2.4): aviso sem `gancho.referencias` (3–5) e sem frase de comunidade antes da pergunta da parte 7;
- plano: `r7ex.py plano` aprovado (sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6) antes de gravar o avatar;
- avatar × fala ≥ 90% (retempo); 9 s de cartão (`avatar/ritmo.json`); aviso acima de 60 s;
- montagem (D26, `conferir_montagem` no `revisar`, reprova): avatar sem esticar (k = 1) e sem pausa congelada, rosto sem quadro parado ≥ 1,2 s até a última palavra, caixa da pergunta só depois do fim da pergunta;
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
