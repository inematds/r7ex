# Proposta de gancho (v1.2.0) — só registro

A edição publicada não muda. Ela abriu com "Cinco coisas de IA mudaram este mês…", um gancho de **lista**, que a v1.2.0
proíbe (PADRAO §2.1), e junta 5 temas diferentes (Agent Skills, ponytail, Understand Anything, ECC, Tesla Roadster). No
padrão novo, isso vira **um vídeo por tema**. O tema mais forte é o da máxima desta edição ("Quando ela errar, não corrija no
chat. Corrija a pasta."): a pasta de instruções (Agent Skills). Os 3 ganchos abaixo são para esse vídeo; o recomendado vem
primeiro. Os fatos são os de `plano.fatos` desta ficha.

## 1. Recomendado — `contrario`

```yaml
gancho:
  tipo: contrario
  manchete: "PARA DE CORRIGIR IA NO CHAT"     # 6 palavras
  destaque: "CORRIGIR"
  objeto: "uma janela de chat iluminada, cheia de linhas, com um grande risco vermelho #ff2a1f cortando-a na diagonal"
  prova: {parte: 2, de: "291"}               # ECC: ~291 mil estrelas no GitHub (28/10/2026)
  absolvicao: "ninguém te mostrou a pasta"
```

Fala da parte 1: "Eu acho que você não devia mais corrigir a IA no chat. Quem usa ela de verdade corrige outra coisa."

Por que primeiro: a tela manda parar ("PARA DE CORRIGIR"), a voz só opina; o objeto (chat riscado) mostra o dano; e a
máxima da parte 6 fecha o mesmo assunto, sem trocar de tema.

## 2. `terceiro`

```yaml
gancho:
  tipo: terceiro
  manchete: "SETUP DELE: 291 MIL ESTRELAS"     # 5 palavras
  destaque: "291"
  objeto: "uma pasta de arquivos aberta, rachada no meio, com luz amarela vazando pela rachadura"
  prova: {parte: 1, de: "291"}
  absolvicao: "não é falta de estudo"
  fontes: [{url: "https://github.com/affaan-m/ECC", trecho: "~291 mil estrelas (28/10/2026); setup que venceu um hackathon (Anthropic × Forum Ventures)"}]
```

Fala da parte 1: "Um cara venceu um hackathon com o jeito que ele monta o Claude, e hoje duzentas e noventa e uma mil
pessoas marcaram esse projeto com estrela."

## 3. `perda`

```yaml
gancho:
  tipo: perda
  manchete: "E SE SEU CHAT SUMISSE AMANHÃ?"   # 6 palavras
  destaque: "SUMISSE"
  objeto: "uma janela de chat se desfazendo em pedaços, caindo numa lixeira com luz vermelha"
  prova: {parte: 2, de: "291"}
  absolvicao: "não é culpa sua"
```

Fala da parte 1: "Tudo que você ensinou pra IA numa conversa: se ela fechar, você começa do zero amanhã."

## Os outros temas desta edição (um vídeo para cada, se o Nei quiser)

- ponytail (~179 mil estrelas) — `terceiro` ou `contrario` ("O MELHOR CÓDIGO NÃO EXISTE").
- Understand Anything (~88,7 mil estrelas) — `estatistica`.
- Tesla Roadster com propulsores (15/10/2026) — passou da janela de 7 dias do `noticia`; só como `perda`/`contrario`.
