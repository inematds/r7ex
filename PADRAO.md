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
| nota | 0–10: "um desconhecido rolando o feed para aqui?" Abaixo de 7, troque o ângulo ou o tema |
| destino | o curso/guia/formação do inema.club que resolve (URL para o print) |

Grátis só quando a página diz ou o Nei afirma. Nunca inventar número.

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

- **Abertura:** o título do gancho **desenhado pelo Codex dentro da arte** (branco + amarelo ou vermelho), metade de cima.
- **Imagens:** uma por parte, foto **limpa**: UM assunto só, na metade de cima, fundo preto/grafite liso com muito vazio,
  luz neutra; amarelo só num detalhe pequeno (o amarelo é do texto), vermelho #ff2a1f só no perigo. Na ficha, descreva
  um objeto, nunca "cinco objetos", feixes, partículas ou pilhas. O motor escurece a faixa de baixo e tira brilho/saturação
  das ilustrações (19/10/2026: "saturadas, muita informação" — comparado ao eventosextremospub, que tem fundo de mapa calmo).
  Sem logos, sem rostos reconhecíveis; robô = humanoide estilo Optimus de visor preto.
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

- ficha: 7 partes, fala 550–700 caracteres, toda palavra de painel/contador existe na fala da parte;
- avatar × fala ≥ 90% (retempo); duração < 60 s;
- grafia do título da abertura conferida na imagem (ler a imagem antes do render);
- revisão da folha de 12 quadros (`r7ex.py revisar`): nada cobrindo nada, prints legíveis.

## 5. Publicação

- v3 sempre (`r7ex.py enviar`).
- Canal só pela fila (`r7ex.py fila` → `~/projetos/wifi/fila-lives7`), nunca upload direto.
