---
name: r7ex
description: >-
  Tema ou tese do Nei → reel 9:16 VIRAL no padrão r7ex: roteiro de 7 etapas de gatilho (gancho de 5 tipos com manchete no quadro 0 → medo →
  desejo → facilidade → descoberta → benefício → comentário "tá tudo no inema.club") com acabamento de telejornal
  (título desenhado na abertura pelo Codex, preto + amarelo, painéis no tempo da fala, contador, legenda karaokê,
  avatar do Nei em meia tela embaixo no gancho e depois no canto), v3 e fila do lives7. Gatilho: "/r7ex", "faz um r7ex", "reel viral", "reel no padrão novo",
  "reel com gatilhos", ou uma tese/opinião do Nei pedindo vídeo curto.
---

# r7ex — reel viral do INEMA

Repo `~/projetos/r7ex` (inematds/r7ex). **Leia `PADRAO.md` antes de escrever.** Explicação completa: `README.md`.
Comando único: `python3 r7ex.py` (sem argumentos mostra a ajuda).

## Passos
1. **Plano** (PADRAO §1): pessoa = público geral; o que ela quer; gancho com número e fonte; nota ≥ 8; destino no
   inema.club (leia a página: nome, aulas, se é grátis). **Um tema por vídeo**: vários temas → proponha um vídeo por tema.
   **Nunca calmo (D25, PADRAO §2.5):** `pessoa` com o nível de IA; opinião do Nei → `plano.posicao` em 1ª pessoa e gancho
   `contrario`/`provocacao`/`acusacao` com a posição na boca dele; 1ª frase afirma com pressão (nunca "Você pensou em…?");
   capa que um leigo entende em 1 s; `abertura.layout: cheia` quando a imagem é o gancho.
   **Gancho (PADRAO §2.1, v1.2.0):** bloco `gancho:` com `tipo` (`contrario` | `perda` | `estatistica` | `terceiro` |
   `noticia` | `provocacao` (v1.3.1: afirma e cutuca, com nome ou número na 1ª frase); lista, "você sabia" e "eu fiz" reprovam; `entrega` = o que a pessoa leva do vídeo, PADRAO §2.2), `manchete` (quadro 0, ≤ 6 palavras, CAIXA ALTA, mais forte que a
   fala), `destaque` (a palavra em amarelo), `objeto` (com dano/ameaça), `prova` (até ~20 s), `absolvicao` (parte 2 ou 3),
   `fontes` (estatística/terceiro/notícia) e `data` (notícia).
2. `python3 r7ex.py novo <slug>` e preencha `ficha.yaml` (modelo: o reel do hacker, gancho `terceiro`): gancho, abertura
   (a cena; o título é a `gancho.manchete`), 7 partes (fala por extenso, objetivo 620 caracteres, teto 900 — fala natural vale mais que caber, nunca telegráfica (D26); explicação com comparação concreta e imagem que a mostra; imagem OU print; painel com itens nas palavras
   da fala; contador onde houver número), `trocas` para a legenda, CTA em pergunta, `publicar`.
3. `python3 r7ex.py checar <pasta>` até passar.
4. Avatar: OK do Nei → `avatar/APROVADO_HEYGEN` com a frase dele; ou `--de <mp4>` para reaproveitar.
5. **Padrão (sem sessão aberta):** `python3 producao/producao.py --add <pasta>`. O timer `r7ex-producao` (5 em 5 min)
   manda ao estúdio todas as pendentes na mesma rodada (sem esperar a anterior ficar pronta), espera o HeyGen, roda o `fazer`, o revisor (claude -p + `producao/revisor.md`) lê a
   folha e, aprovado, manda ao v3 e põe na fila do canal; avisa no v3 "Terminei/Falhou". Reprovou → `parado` com o
   motivo; corrigiu → `producao.py --retomar <pasta>`. Ver: `producao.py --status`. Detalhes: `producao/README.md`.
6. **Manual** (só se o Nei pedir para acompanhar): `python3 r7ex.py fazer <pasta>`, **ler** `capa/abertura.png` e
   `build/folha.jpg` (nada cobrindo nada, prints legíveis, legenda dentro da tela), depois
   `python3 r7ex.py enviar <pasta>` e `python3 r7ex.py fila <pasta>`. Dizer ao Nei "Terminei: …".

## Ritmo e fecho (28/10/2026)
- D26 (17/11/2026): a montagem (`r7ex/ritmo.py` v2) NÃO estica a fala nem congela o quadro: o avatar fala na velocidade
  natural do HeyGen; o rosto sai 0,5 s depois da última palavra e o cartão do comentário fica 9 s (`cta.comentario`).
  Fecho em fila: inema.club na palavra → pergunta depois da última palavra → comentário ~2 s depois. O `revisar` reprova
  (`conferir_montagem`) avatar esticado, rosto parado ou pergunta por cima da fala.
- Remontar edição antiga sem novo avatar: `python3 r7ex.py cena <pasta>` + `render` + `revisar` (aplica o ritmo sozinho).

## Regras
- Tudo que abre navegador roda na tela `:99`; só o LOGIN do HeyGen vai na tela do Nei (`:10`).
- Nunca número em algarismo na fala (o avatar lê errado); a legenda troca por algarismo.
- "Grátis" só quando a página diz ou o Nei afirma. Nunca inventar número.
- Publicar só pela fila; nunca upload direto. Exceção (Nei, 05/11/2026): quando a entrega precisa do link do YouTube (portal, link no tópico do Telegram), publicar direto com o yt-pubx no canal pedido (mesmo título e contexto do item) e marcar o item da fila como `feito` com `video_id` e nota `direto`, para não sair duas vezes; aviso no v3 em texto normal (faixa azul só no Metricool). Nos outros casos o portal pode entrar antes e ganhar o link do vídeo depois. Avatar pelo estúdio HeyGen é free: não pedir OK, gravar `avatar/APROVADO_HEYGEN` citando a regra de 07/11/2026 e seguir.
- Mudança de padrão (layout, estrutura, plano): README §7; padrão novo → kit inema-design primeiro (D9–D11).
