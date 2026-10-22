# r7ex — o reel viral do INEMA

[![r7ex — o reel viral do INEMA](guia/assets/banner.jpg)](https://inematds.github.io/r7ex/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

O r7ex é a linha de produção de reels verticais (9:16) do INEMA. Você entrega uma ideia forte, a tese, e ele monta um vídeo de 30 a 40 segundos com o avatar do Nei falando, imagens geradas pelo Codex e um acabamento de telejornal: título na abertura, painéis que entram na palavra certa, contador e legenda que acende junto com a fala. O roteiro segue 7 etapas de gatilho, do gancho com número até o pedido de comentário, sempre levando a pessoa ao inema.club. Para usar é preciso Python, Node, o Codex e a assinatura do HeyGen, rodando na máquina do INEMA.

## 🎬 Vídeos sobre o r7ex

Feitos com o próprio r7ex (19/10/2026):

- [Reel 1 — "Meus reels tiveram zero visualização, 4 lotes até acertar"](https://inematds.github.io/r7ex/guia/assets/videos/r7ex-divulga.mp4)
- [Reel 2 — "O reel de 7 etapas ficou velho, agora tem o r7ex"](https://inematds.github.io/r7ex/guia/assets/videos/r7e-para-r7ex.mp4)

Também tocam no guia, seção Exemplos.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/r7ex/guia/**

---

**r7ex = r7e + x.** O **r7e** (reel7etapas) dá o **roteiro**: 7 etapas de gatilho, do gancho ao comentário.
O **x** vem do **eventosextremospub**: o **acabamento de telejornal** que viraliza mais.
Objetivo de todo reel: **trazer gente para o inema.club.**

Este repo funciona **sozinho**: tem cópia própria do motor de render, dos scripts do estúdio do HeyGen, da transcrição,
da trilha, do envio ao bot e da fila de publicação. Mudar algo aqui **não afeta** o eventosextremospub, o reel7etapas,
o explicavideos nem o cardshorts.

- Padrão fixo (a regra curta): [`PADRAO.md`](PADRAO.md)
- Ficha de exemplo (o reel do hacker): [`modelo/ficha.yaml`](modelo/ficha.yaml)

---

## O processo, do início ao fim (12 passos)

🧠 = sessão com o Nei (gasta tokens) · ⚙️ = script/timer (zero token) · 🤖 = `claude -p` curto (sessão nova)

**Parte 1: com o Nei, na sessão**

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| 1 | Pedido | o Nei diz o tema, o canal e o que citar | Nei |
| 2 | Pesquisa | conferir fatos e fontes (vão para `plano.fatos` com a origem) | 🧠 |
| 3 | Ficha | `python3 r7ex.py novo <slug>` + escrever as 7 partes, a abertura, os painéis e `publicar` | 🧠 |
| 4 | Portão da ficha | `python3 r7ex.py checar <pasta>`: 7 partes, 550–700 caracteres, palavras dos painéis na fala | ⚙️ |
| 5 | Portão viral | `python3 r7ex.py plano <pasta>`: crítico dá nota por parte; sem bloqueio, gancho ≥ 8, média ≥ 7,5 | 🤖 |
| 6 | Entregar à produção | `avatar/APROVADO_HEYGEN` + `python3 producao/producao.py --add <pasta>` | 🧠 |
| 7 | Enviar o avatar | o timer `r7ex-producao` manda a fala ao estúdio HeyGen (tela :99, um por vez) | ⚙️ |

**Parte 2: sem sessão aberta**

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| 8 | Esperar o avatar | `r7ex.py avatar-conferir` (HeyGen, só leitura) até "pronto" e baixa. **Minutos a horas** | ⚙️ |
| 9 | Montar | `r7ex.py fazer`: Codex desenha abertura e imagens, prints, tempos das palavras, legenda, render e `build/folha.jpg` | ⚙️ |
| 10 | Revisar | revisor `claude -p` + `producao/revisor.md` lê a folha: aprova, aprova com 🟥 SUGESTÃO ou para com o motivo | 🤖 |
| 11 | Entregar | `r7ex.py enviar` (v3) + `r7ex.py fila` (fila do canal); aviso "Terminei" no v3 | ⚙️ |
| 12 | Publicar | o timer da fila sobe 1 a cada 2 h (9 h–21 h) pelo yt-pubx e avisa no v3 | ⚙️ |

**Pelo bot, sem sessão nenhuma (22/10/2026): `/r7ex <tema>` ou `/rtex <tema>` no inemaccbot.**

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| B1 | Pedido | o Nei manda `/r7ex <tema, canal, "agora">` no inemaccbot; o comando já é o OK do avatar | Nei |
| B2 | Ficha + portões | fase `ficha` (`prompts/bot-ficha.md`): passos 2–6 acima, canal em `publicar.fila`, "agora" → `FRENTE`, `APROVADO_HEYGEN`, `producao.py --add`; mostra o `BOT-RESUMO.md` no chat | 🤖 |
| B3 | Produção | passos 7–11 pelo timer `r7ex-producao`, como sempre | ⚙️ |
| B4 | Fim no bot | fase `producao`: `producao/esperar.py <pasta>` espera `na_fila` e mostra o `BOT-FIM.md`; `parado` → falha com o motivo | ⚙️ |

Definição: `flow.json` (prefixo `RX`), ajuda do bot em `HELP.md`. O bot não faz upload direto nem tópico no Telegram:
isso continua pela sessão + vigia `continua` (abaixo). O `/r7ex` no terminal segue igual.

**Quando o Nei pede algo fora do caminho padrão** ("publica agora sem fila", "posta no INEMA.DEV", links no inemaytbot),
os passos 8–12 vão pelo vigia **`continua`** do wifi (`~/projetos/wifi/continua`): a sessão escreve
`<pasta>/CONTINUAR.md` com o que falta, as ordens e as travas, tira a edição da produção e registra
`continua.py --add <pasta> --cwd ~/projetos/r7ex --confere "python3 r7ex.py avatar-conferir <pasta>"`. Quando o avatar
fica pronto, o vigia abre uma **sessão nova** (`claude -p`) que lê só o bilhete e segue até o fim. O `--add` avisa no v3
("⏳ Fase 1 concluída", msg N) e a sessão termina dizendo "pode fechar o terminal, acompanhe pela msg N"; o Terminei/Falhou
da fase 2 chega como resposta a essa mensagem. Detalhes: `~/projetos/wifi/continua/README.md`.
Primeiro uso: `edicoes/2026-10-22-hackers-atacam` (22/10/2026).

---

## 1. Como chegamos aqui (18/10/2026) — 4 lotes, o que mudou em cada um

| Lote | Conteúdo (o que se fala) | Forma (o que se vê) | Resultado |
|---|---|---|---|
| **1. r7e antigo** (deepseek, faxina, opencode, contexto, diga) | Assunto do dia (divulgar guia/repo), público de nicho, gancho = **promessa** ("SEU AGENTE OBEDECE E GASTA MENOS"), 7 etapas em ordem fixa, medo fraco e às vezes desarmado na hora | Motor do r7e: foto de banco de imagens desfocada atrás do rosto em meia tela, letra Anton com âmbar apagado | Sem visualização no TikTok/Instagram |
| **2. r7e "-gatilho"** (os mesmos 5, mesmo avatar) | Fala igual (a voz às vezes contrariava a tela) | Só o gancho mudou: medo/novidade/provocação com número, imagem nítida dramática, amarelo #FACC15 com contorno | Melhor, mas "ainda padrão" |
| **3. r7e D10** (5 teses do Nei + hacker refeito; 2 de gestão) | **Plano antes da fala** (pessoa, o que quer, gancho com número, nota, destino no inema.club), **fala nova** com o gatilho primeiro e o alívio no meio, CTA fixo, prints reais das páginas | Motor do r7e com tarja e diagramas em Pillow | "Ficou padrão" |
| **4. r7ex** (os mesmos 7, **mesmo avatar e fala do lote 3**) | Nenhum conteúdo novo: a fala dividida em 7 blocos, cada um com imagem e painel tirados da própria fala | **Motor do eventosextremospub**: título dentro da arte, preto e dourado, faixa de telejornal, painéis no tempo da fala, contador, karaokê, CTA em pergunta | Formato padrão a partir de agora |

Lição: o **conteúdo** acertou no lote 3 (teses fortes, gatilho, plano) e a **forma** acertou no lote 4 (motor do eventos).

### Links no YouTube

| O quê | Link |
|---|---|
| O de referência que funcionou (evento extremo, r7e antigo com flagrante + número) | https://www.youtube.com/shorts/DfdtX9HbkWg (lives10) |
| Lote 1 — Faxina no setup (promessa, sem visualização) | https://www.youtube.com/shorts/E5Y94BLfuJU (lives4) |
| Lote 1 — Camada de contexto (promessa, sem visualização) | https://www.youtube.com/shorts/XflFkvIl4mw (lives4) |
| Lote 3 — Demissão em massa de gerentes (motor r7e) | https://www.youtube.com/shorts/xpDV5qQe5oE (lives3) |
| Lote 3 — Funcionário que não é gente (motor r7e) | https://www.youtube.com/shorts/cMhIavjhdh0 (lives3) |
| **Lote 4 / r7ex — Hackers roubaram as chaves** | https://youtube.com/shorts/DG30IdeqWcg (lives7) |
| Lote 4 / r7ex — os outros 6 | na fila do lives7 (1 a cada 2 h); `python3 fila/fila.py --status` |

## 2. Como o conteúdo é formado (o plano)

Antes de escrever uma palavra da fala:

1. **Pessoa:** público geral (IA traduzida para o dia a dia), não o nicho.
2. **O que ela quer:** ganhar algo, resolver uma dor ou chegar a um desejo.
3. **Gancho:** medo, novidade ou provocação, **com número ou fato** e fonte.
4. **Nota de potencial (0–10):** "um desconhecido rolando o feed para aqui?" Abaixo de 7, troque o ângulo ou o tema.
5. **Destino:** a página do inema.club que resolve (vira o print de prova).

Base real: leio a página do curso/guia antes (nome, quantas aulas, se é grátis). Nunca invento número;
"grátis" só quando a página diz ou o Nei afirma.

## 3. As 7 etapas — exemplo real (o reel do hacker)

| Etapa | Fala | Tela |
|---|---|---|
| 1. Gancho (medo) | "Hackers invadiram o OpenCode… US$ 1.700 numa noite" | abertura com o título desenhado + contador 0 → 1.700 |
| 2. Medo | "A chave é a senha que a IA usa… a sua pode ser a próxima" | encapuzado puxando a chave + painel vermelho |
| 3. Desejo | "Imagina dormir sabendo que… o prejuízo tem teto" | homem dormindo + "prejuízo com teto" |
| 4. Facilidade | "Você não precisa ser especialista, nem programador" | painel de limite + "sem ser especialista" |
| 5. Descoberta | "São três ajustes: limite, uma chave por uso, alarme…" | cadeado, chaves e sino + os 3 ajustes entrando |
| 6. Benefício | "O susto vira um aviso no celular…" | fatura rasgada + "sem limite × com limite" |
| 7. Comentário | "Tá tudo no inema.club. Ou me pede o link…" | print do inema.club + CTA vermelho em pergunta |

A ordem 2–6 se adapta ao tema (ex.: no "Quem fatura em 2027" a etapa 3 virou **prova**: "já aconteceu 3 vezes"),
mas são sempre 7 partes de ~30–40 s.

## 4. O que o motor faz

O motor **não cria conteúdo nem imagem**: ele **sincroniza e anima**. É uma página web (`motor/mapa.html`) que vira vídeo.

- **Recebe:**
  - o avatar (HeyGen) e o tempo de cada palavra dele (`r7ex/retempo.py`, Whisper local);
  - as imagens (Codex) e os prints;
  - a `cena.js`, gerada da ficha por `r7ex/cena.py`: qual imagem em qual frase, painéis, contadores, CTA, cores.
- **Desenha em camadas, quadro a quadro:**
  1. fundo preto (o mapa 3D dos vídeos de clima fica tapado);
  2. a imagem da vez, com entrada suave e zoom leve;
  3. a faixa do topo (marca + selo vermelho) e a linha de fonte;
  4. o painel, com os itens entrando no segundo da palavra e o contador subindo;
  5. a legenda karaokê;
  6. o CTA em pergunta e a pílula do inema.club.
- **Filma** a página a 30 quadros por segundo (`motor/render.mjs`, Chrome escondido na tela `:99`).
- **Junta** (`motor/compor_avatar.sh`):
  - o rosto na caixinha do canto;
  - a voz a −14 LUFS;
  - a trilha baixinha, que abaixa quando você fala.

Em uma frase: **o Claude escreve, o Codex desenha, o HeyGen fala e o motor sincroniza tudo com a voz.**

## 5. O que veio de cada lugar

| Do **r7e** (reel7etapas) | Do **eventosextremospub** |
|---|---|
| As 7 etapas de gatilho e a ordem | O motor de render (`mapa.html`, `render.mjs`, `compor_avatar.sh`) |
| O gancho = gatilho com número (D9) | O visual de telejornal: faixa, selo, linha de fonte |
| O plano antes da fala e o CTA fixo do inema.club (D10) | A abertura com o título desenhado pelo Codex (`abertura-desce`) |
| O avatar do Nei pelo estúdio do HeyGen | A paleta preto + amarelo, vermelho só no perigo |
| Os prints reais das páginas como prova | Os painéis com itens no tempo da fala e os contadores |
| A fila e o envio ao bot v3 | A legenda karaokê colorida e o CTA vermelho em pergunta |
| | O `retempo` (dividir o avatar nas falas) |
| Também: a transcrição Whisper (cópia do cardshorts) | |

Tudo isso foi **copiado** para cá (não é link): `motor/`, `heygen/`, `r7ex/whisper.py`, `r7ex/retempo.py`,
`assets/trilha.mp3`, `bin/enviar_bot_v3.mjs`, `fila/`.

## 6. Como usar

```bash
cd ~/projetos/r7ex
python3 r7ex.py novo <slug>                 # cria edicoes/<data>-<slug>/ficha.yaml a partir do modelo
#   → escreva o plano, a abertura, as 7 partes (fala + imagem/print + painel), o CTA e "publicar"
python3 r7ex.py checar edicoes/<pasta>      # portão da ficha
python3 r7ex.py plano edicoes/<pasta>       # crítico de viralidade (D15): sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6
#   produto citado → `logos:` (logo real, D13); lista no alto (`lista:`), embaixo uma coisa só (`painel.titulo|contador|logo`, D14)
echo 'Nei, <data>: "<frase do OK>"' > edicoes/<pasta>/avatar/APROVADO_HEYGEN   # só com o OK do Nei para esta produção
python3 r7ex.py fazer edicoes/<pasta>       # imagens + avatar → cena → render → folha de revisão
#   (ou --de <avatar.mp4> para reaproveitar um avatar pronto)
# LER edicoes/<pasta>/capa/abertura.png (grafia) e edicoes/<pasta>/build/folha.jpg
python3 r7ex.py enviar edicoes/<pasta>      # bot v3
python3 r7ex.py fila edicoes/<pasta>        # fim da fila do canal (padrão lives7)
```

Passo a passo separado: `avatar`, `imagens`, `cena`, `render`, `revisar` (ver `python3 r7ex.py`).

## 7. Como mudar

### Mudar o layout (o que se vê)
| Quero mudar | Onde |
|---|---|
| Cores, fonte, tamanho e posição da faixa, painel, legenda, CTA | `motor/mapa.html` (CSS e desenho das camadas) |
| Posição e tamanho do rosto, moldura, nome | `motor/compor_avatar.sh` (`LAYOUT=canto`: 400x453 em x 640, y 1290) + `motor/meia_filtro.py` (meia tela 1080x960 em y 960 nos trechos de `avatar/meia.txt`) |
| Quando o rosto fica em meia tela | `r7ex/cena.py` (parte 1 sempre; `avatar: meia` na parte) e `body.mt` em `motor/mapa.html` (o que sobe/some) — D16 |
| Onde a abertura desce, o cartão do print, o brilho do print | `r7ex/pecas.py` (`abertura`, `print_card`) |
| Estilo das imagens (paleta, robô, sem texto) | `ESTILO` em `r7ex.py` |
| Cores das palavras na legenda | `cores:` na ficha (por reel) |
| Trilha | `assets/trilha.mp3` |

### Mudar a estrutura (quantas partes, o que cada uma tem)
- As partes são a lista `partes:` da ficha. O motor aceita qualquer quantidade. O portão `checar` exige 7
  (padrão); mude lá se o padrão mudar.
- Cada parte pode ter `imagem` (o Codex desenha) **ou** `print` (página real), e um `painel`
  (`itens`, `contador`, `borda`).
- O painel entra na palavra `de:` e cada item na sua palavra. Escolha palavras que existem na fala daquela parte.

### Mudar o planejamento (o que se fala)
- `plano:` na ficha (pessoa, quer, gancho, nota, destino) e as regras do §2.
- As regras fixas estão em `PADRAO.md` e no kit `inema-design` (D9, D10, D11). Mudança de padrão:
  primeiro o kit (`DECISOES.md` + `HISTORICO.md`), depois aqui.

## 8. HeyGen e publicação

- **Avatar:** estúdio do HeyGen pela assinatura (`heygen/heygen-studio.mjs`), sempre na tela escondida `:99`.
  Status e download pela leitura da API (exceção autorizada). Gerar só com `avatar/APROVADO_HEYGEN` daquela produção.
- **Sessão do HeyGen caiu** ("não está logada"): abrir **só a janela de login** na tela do Nei (`:10`); ele entra
  com Google. A sessão dura ~30 dias; o aviso vermelho chega no v3 um dia antes (`~/projetos/wifi/heygen-aviso`).
- **Publicação:** sempre pela fila (`fila/fila.py`, timer systemd `fila-lives7`, 9 h às 21 h, 1 a cada 2 h),
  nunca upload direto. Cada publicação avisa no v3.

## Licença
MIT.
