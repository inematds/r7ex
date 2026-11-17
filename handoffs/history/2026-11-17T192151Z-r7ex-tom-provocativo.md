# Handoff — 2026-11-17 — r7ex/rtex: nunca calmo (modelo + verificação) e v2 do reel do enxame

## Projeto e escopo
Raiz ~/projetos/r7ex (também ~/projetos/rtex e ~/projetos/inema-design). Nei reprovou o reel do enxame (calmo, sem a voz dele, abertura em meia tela pouco legível para gestor) e pediu: "nenhum vídeo tem que sair calmo; r7ex e rtex são provocativos, virais, com gancho de imagem e de narração; ajusta a falha no modelo e na verificação".

## Objetivo atual
Ajustar modelo (PADRAO, prompts/bot-ficha.md, skill, regra comum chamada.md) e verificação (checar_gancho em r7ex.py, producao/critico-plano.md, producao/revisor.md) do r7ex e o equivalente no rtex; depois produzir a v2 do reel com a fala aprovada. Pronto = a ficha do reel publicado reprova ou tem nota ≤ 7 no gancho, a ficha v2 passa, os testes existentes passam.

## Estado aceito
- [confirmed] Reel v1 publicado no lives4 — evidência: arquivo: fila/fila.json (video_id AR2vGZMOe9k, 2026-11-17T09:01). Nei: não tirar do ar.
- [confirmed] Linha da falha no topo de `FALHAS.md` (não commitada).
- [confirmed] Kit enxame-com-conta v1.0.1 + guia PT/EN/ES + portal publicados — evidência: commits portal deef65b, inemabuscas 3567df0, inemapro-mono 7e49538.

## Proposto / tentado, não confirmado
- [unverified] Plano das mudanças (do advisor): campo `plano.posicao` (opinião do Nei em 1ª pessoa) obriga gancho contrario/provocacao/acusacao e 1ª frase afirmativa; `abertura.layout: cheia` opt-in (parte 1 em PiP, prompt de capa em tela cheia, ligado à mesma flag); crítico com pressão + leigo entende o quadro 0 em 1 s; revisor aceita PiP na parte 1 quando a ficha pede.

## Decisões
- Fala v2 aprovada pelo Nei em 17/11: "Esqueça os enxames de agentes. Faz um ano que eu falo disso: a ideia é boa, mas o custo é proibitivo..." (7 partes, na conversa); imagem: sala de reunião com robôs falando e taxímetro em R$; texto ESQUEÇA OS ENXAMES; destino guia enxame-com-conta.
- Layout tela cheia: opt-in pela ficha (default D16 fica), pergunta ao Nei no relatório final.

## Não fazer (restrições e travas)
- Não tirar AR2vGZMOe9k do ar — dito pelo Nei em 17/11, só nesta conversa.
- Commitar só por caminho explícito: árvore do r7ex tem arquivos de outros (edicoes/*/ficha.yaml, r7ex/retempo.py, .descartes/, .layout-meia-ok).
- Claude/Codex só pela assinatura; autor inematds; não usar AskUserQuestion — ~/.claude/CLAUDE.md.
- Versão: minor carrega o patch (r7ex 1.8.7 → 1.9.7; rtex 1.7.2 → 1.8.2) — ~/.claude/CLAUDE.md.

## Arquivos alterados
- `FALHAS.md` — linha da falha do reel calmo.
- Fora do projeto: ~/projetos/enxame-com-conta (guia, commits já empurrados).

## Memória e regras duráveis tocadas
- `FALHAS.md` (r7ex) — linha de 17/11 sobre o reel calmo.

## Verificação
- Não rodado: checar/crítico nas fichas — mudanças ainda não feitas.

## Estado em execução
- Processos em segundo plano: nenhum. Servidores: nenhum. Worktrees: nenhum.

## Perguntas abertas e adiados
- Aberta: tela cheia + PiP para todos os reels ou só quando a ficha pedir?
- Aberta: portão "mostrar quadro 0 + fala ao Nei antes do HeyGen" vale também para o bot?

## Pela metade
- Ajuste do modelo/verificação — parou em: leitura de PADRAO.md, critico-plano.md, revisor.md, checar_gancho (r7ex.py:188) e cena.py:219 — falta: editar tudo, rtex, inema-design, testes, v2.

## Próxima ação exata
Editar inema-design/regras/chamada.md e r7ex (PADRAO §1/§2.1/§3/§4, bot-ficha.md, r7ex.py checar_gancho, cena.py meia, prompt da capa, critico-plano.md, revisor.md), testar na ficha publicada e na v2; depois rtex. Publicar o reel v2 segue a fila (sem nova aprovação: Nei aprovou o modelo).

## Mapa de retomada
- `PADRAO.md` — regras do gancho e do avatar (§2.1, §3).
- `producao/critico-plano.md` — crítico do plano.
- `producao/revisor.md` — revisor final.
- `r7ex.py` — checar_gancho (linha ~188).
- `edicoes/2026-11-17-enxame-quebra-empresa-lives4/ficha.yaml` — ficha do reel calmo (teste de regressão).

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → ajustar modelo e verificação do r7ex/rtex para nunca sair calmo; ficha calma reprova, v2 passa — fonte: FALHAS.md — chave: `calmo`
2. Qual foi a última decisão e por quê? → tela cheia + PiP opt-in pela ficha, para não mexer nos 12 da fila — fonte: só nesta conversa — chave: `opt-in`
3. O que não pode mudar? → o reel AR2vGZMOe9k fica no ar — fonte: fila/fila.json + dito pelo Nei — chave: `AR2vGZMOe9k`
4. O que está pela metade? → edição de PADRAO, checar, crítico, revisor — fonte: FALHAS.md — chave: `critico`
5. Qual é a próxima ação e precisa de aprovação? → editar chamada.md e r7ex; não precisa (Nei aprovou) — fonte: só nesta conversa — chave: `chamada.md`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim.


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: dea4da67cb6025f1f1f3807f746b5d72c1de9638 · branch: main
- arquivos sujos fora de handoffs/: 1124 (lista cortada)
- `.descartes/plano-90-dias-p2-relogio.png` · sha256:e23fceaadaf4 · sujo
- `.layout-meia-ok` · sha256:e3b0c44298fc · sujo
- `FALHAS.md` · sha256:98f7cf17dc79 · sujo
- `edicoes/2026-10-18-claude-15-comandos/capa/pedido.txt` · sha256:6de4037d1b0b · sujo
- `edicoes/2026-10-18-claude-15-comandos/capa/prompts-imagegen.txt` · sha256:d780f1ef782d · sujo
- `edicoes/2026-10-18-claude-15-comandos/falas.json` · sha256:9619927b2de5 · sujo
- `edicoes/2026-10-18-claude-15-comandos/ficha.yaml` · sha256:5a8af88c495d · sujo
- `edicoes/2026-10-18-deepseek-flash/capa/pedido.txt` · sha256:5fe24d4b58de · sujo
- `edicoes/2026-10-18-deepseek-flash/falas.json` · sha256:ad0049a39dee · sujo
- `edicoes/2026-10-18-deepseek-flash/ficha.yaml` · sha256:dfe0f0c58f00 · sujo
- `edicoes/2026-10-18-ferramentas-v2/capa/prompts-imagegen.txt` · sha256:906f10b2f244 · sujo
- `edicoes/2026-10-19-atende-academia-promo/capa/pedido.txt` · sha256:b054a014ed9e · sujo
- `edicoes/2026-10-19-atende-academia-promo/falas.json` · sha256:ffab4497006f · sujo
- `edicoes/2026-10-19-atende-academia-promo/ficha.yaml` · sha256:ba589c69814a · sujo
- `edicoes/2026-10-19-atende-fisioterapia-promo/capa/pedido.txt` · sha256:6325277d30f7 · sujo
- `edicoes/2026-10-19-atende-fisioterapia-promo/capa/prompts-imagegen.txt` · sha256:21fe7fbfbd0f · sujo
- `edicoes/2026-10-19-atende-fisioterapia-promo/falas.json` · sha256:6f6683e11f56 · sujo
- `edicoes/2026-10-19-atende-fisioterapia-promo/ficha.yaml` · sha256:007e891e645e · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/capa/anteriores-20261020/p2.png` · sha256:e3e6a2a4af23 · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/capa/anteriores-20261020/p3.png` · sha256:e8c01900d7c9 · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/capa/pedido.txt` · sha256:5a84eb337449 · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/capa/prompts-imagegen.txt` · sha256:57ba30921852 · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/falas.json` · sha256:067636f0cc5a · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/ficha.yaml` · sha256:b8fcb83b78bc · sujo
- `edicoes/2026-10-19-atende-nutricao-promo/video.mp4.envio-v3.acento-errado.json` · sha256:002fe0535906 · sujo
- `edicoes/2026-10-19-bigtech-ipo/FRENTE` · sha256:40d35d30de83 · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/_antigo/abertura-desce.png` · sha256:3e1bcb57004e · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/_antigo/abertura-fundo.png` · sha256:47dd4d6c6da3 · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/_antigo/abertura.png` · sha256:57a6e6978f65 · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/flux.log` · sha256:37704bc75908 · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/pedido.txt` · sha256:9b323c972518 · sujo
- `edicoes/2026-10-19-bigtech-ipo/capa/prompts-flux.json` · sha256:19ab61d40e88 · sujo
- `edicoes/2026-10-19-bigtech-ipo/falas.json` · sha256:1107136c0aaf · sujo
- `edicoes/2026-10-19-bigtech-te-paga/FRENTE` · sha256:40d35d30de83 · sujo
- `edicoes/2026-10-19-bigtech-te-paga/capa/flux.log` · sha256:37704bc75908 · sujo
- `edicoes/2026-10-19-bigtech-te-paga/capa/pedido.txt` · sha256:2cd52c6b4d79 · sujo
- `edicoes/2026-10-19-bigtech-te-paga/capa/prompts-flux.json` · sha256:6d0ed11027ba · sujo
- `edicoes/2026-10-19-bigtech-te-paga/capa/velhas/p3-celular.png` · sha256:637bc471f8e0 · sujo
- `edicoes/2026-10-19-bigtech-te-paga/falas.json` · sha256:cdac916867af · sujo
- `edicoes/2026-10-19-bigtech-te-paga/ficha.yaml` · sha256:c13f41ceb98f · sujo
- `edicoes/2026-10-19-bigtech-troco/FRENTE` · sha256:40d35d30de83 · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/_antigo/abertura-desce.png` · sha256:7e7115447e6d · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/_antigo/abertura-fundo.png` · sha256:beac2fe258b2 · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/_antigo/abertura.png` · sha256:1a115c95fb2f · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/flux.log` · sha256:6d4d72e735df · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/pedido.txt` · sha256:356a33f9cef5 · sujo
- `edicoes/2026-10-19-bigtech-troco/capa/prompts-flux.json` · sha256:37e79706a117 · sujo
- `edicoes/2026-10-19-bigtech-troco/falas.json` · sha256:5c78980a9ede · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/ESTADO.md` · sha256:012248cdbf03 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/capa/codex-atual.log` · sha256:99e3cac75d2a · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/capa/codex-retry.log` · sha256:e8e507a70638 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/capa/pedido.txt` · sha256:7b1d6f92aef7 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/capa/prompts-imagegen.txt` · sha256:972aa72b53d2 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/descricao.txt` · sha256:a92471050c46 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/falas.json` · sha256:b4f3469021f5 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/ficha.yaml` · sha256:784af525f353 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/montar-quando-pronto.sh` · sha256:26ea6d0cd245 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/.lock` · sha256:e3b0c44298fc · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/APROVADO_API_YOUTUBE` · sha256:a2fbfb82c5ba · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/dry-run.log` · sha256:976c23bf41eb · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/envio-inemaytbot.json` · sha256:3651ec253862 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/fila.json` · sha256:5d6f49e7542e · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/fila.log` · sha256:1a1b69758508 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/publicacao/fila.py` · sha256:a904404b2f66 · sujo
- `edicoes/2026-10-19-curso-chat-agente-v72/verificacao.json` · sha256:31f7c8fd2a39 · sujo
- `edicoes/2026-10-19-dev-2027/capa/pedido.txt` · sha256:882004011140 · sujo
- `edicoes/2026-10-19-dev-2027/falas.json` · sha256:0a852d135e1d · sujo
- `edicoes/2026-10-19-dev-2027/ficha.yaml` · sha256:fd811c897402 · sujo
- `edicoes/2026-10-19-dev-futuro/capa/pedido.txt` · sha256:21d95d1aec03 · sujo
- `edicoes/2026-10-19-dev-futuro/falas.json` · sha256:e4969c1274fe · sujo
- `edicoes/2026-10-19-dev-futuro/ficha.yaml` · sha256:4d77916e37e3 · sujo
- `edicoes/2026-10-19-dev-prepare/capa/pedido.txt` · sha256:df2e8ac1f1ce · sujo
- `edicoes/2026-10-19-dev-prepare/falas.json` · sha256:a13aba550c56 · sujo
- `edicoes/2026-10-19-dev-prepare/ficha.yaml` · sha256:19a364f21b6f · sujo
- `edicoes/2026-10-19-dev-telegram/POSTADO` · sha256:0499a583d571 · sujo
- `edicoes/2026-10-19-dev-telegram/folha-imagens.jpg` · sha256:968b6cc231f7 · sujo
- `edicoes/2026-10-19-dev-telegram/folha-refeitas.jpg` · sha256:68a7119c3802 · sujo
- `edicoes/2026-10-19-dev-telegram/gerar_dev_flux.py` · sha256:71a02f24e5bf · sujo
- `edicoes/2026-10-19-dev-telegram/post.md` · sha256:496bdc83a6fe · sujo
- `edicoes/2026-10-19-dev-telegram/vigia.sh` · sha256:10ded91110cc · sujo
- `edicoes/2026-10-19-fim-capitalismo/capa/pedido.txt` · sha256:9c85d4257fc5 · sujo
- `edicoes/2026-10-19-fim-capitalismo/falas.json` · sha256:7659ba4e773e · sujo
- `edicoes/2026-10-19-fim-capitalismo/ficha.yaml` · sha256:4e8a4eb755c4 · sujo
- `edicoes/2026-10-19-gestao-formacao/capa/pedido.txt` · sha256:8948f62bba6a · sujo
- `edicoes/2026-10-19-gestao-formacao/falas.json` · sha256:00231bda4db7 · sujo
- `edicoes/2026-10-19-gestao-formacao/ficha.yaml` · sha256:266432729dec · sujo
- `edicoes/2026-10-19-gestao-repo/capa/pedido.txt` · sha256:4fdfbfd82a24 · sujo
- `edicoes/2026-10-19-gestao-repo/falas.json` · sha256:f71d90be34e3 · sujo
- `edicoes/2026-10-19-gestao-repo/ficha.yaml` · sha256:c19f97e0284f · sujo
- `edicoes/2026-10-19-gestao-tecnico/capa/pedido.txt` · sha256:1c4e8c8761da · sujo
- `edicoes/2026-10-19-gestao-tecnico/falas.json` · sha256:af87566fb342 · sujo
- `edicoes/2026-10-19-gestao-tecnico/ficha.yaml` · sha256:b4ce24095294 · sujo
- `edicoes/2026-10-19-ia-de-elite/capa/pedido.txt` · sha256:f79cf5fbff8a · sujo
- `edicoes/2026-10-19-ia-de-elite/falas.json` · sha256:dc914ca5083d · sujo
- `edicoes/2026-10-19-ia-de-elite/ficha.yaml` · sha256:164f2cbec10d · sujo
- `edicoes/2026-10-19-ia-decide-renda/capa/pedido.txt` · sha256:fb7654254a8f · sujo
- `edicoes/2026-10-19-ia-decide-renda/falas.json` · sha256:1882209d7a0e · sujo
- `edicoes/2026-10-19-ia-decide-renda/ficha.yaml` · sha256:6a78f7fe2b7f · sujo
- `edicoes/2026-10-19-ia-offline/capa/pedido.txt` · sha256:6aebb78a4523 · sujo
- `edicoes/2026-10-19-ia-offline/falas.json` · sha256:d9d9eca72138 · sujo
- `edicoes/2026-10-19-ia-offline/ficha.yaml` · sha256:c6dfc1290845 · sujo
- `edicoes/2026-10-19-identidade-ia/capa/pedido.txt` · sha256:aea28415869e · sujo
- `edicoes/2026-10-19-identidade-ia/falas.json` · sha256:c947ebe20440 · sujo
- `edicoes/2026-10-19-identidade-ia/ficha.yaml` · sha256:bdbdd26de687 · sujo
- `edicoes/2026-10-19-kit-14-dias/capa/pedido.txt` · sha256:7280bd9bc10d · sujo
- `edicoes/2026-10-19-kit-14-dias/falas.json` · sha256:aad7a216ae8d · sujo
- `edicoes/2026-10-19-kit-14-dias/ficha.yaml` · sha256:5e93b048f9d6 · sujo
- `edicoes/2026-10-19-loopr-formacao/capa/pedido.txt` · sha256:744e1d16fe55 · sujo
- `edicoes/2026-10-19-loopr-formacao/capa/prompts-imagegen.json` · sha256:736b695151b4 · sujo
- `edicoes/2026-10-19-loopr-formacao/falas.json` · sha256:44e73da6b0aa · sujo
- `edicoes/2026-10-19-loopr-formacao/ficha.yaml` · sha256:fb58b6889f66 · sujo
- `edicoes/2026-10-19-loopr-repo/capa/pedido.txt` · sha256:574d142d9e67 · sujo
- `edicoes/2026-10-19-loopr-repo/falas.json` · sha256:2b90f53fc7bf · sujo
- `edicoes/2026-10-19-loopr-repo/ficha.yaml` · sha256:b8ecb55e5dbb · sujo
- `edicoes/2026-10-19-loopr-tecnico/capa/pedido.txt` · sha256:c0537bad2552 · sujo
- `edicoes/2026-10-19-loopr-tecnico/capa/prompts-imagegen.json` · sha256:4e0ca2fc970b · sujo
- `edicoes/2026-10-19-loopr-tecnico/falas.json` · sha256:9fa56f11cda4 · sujo
- `edicoes/2026-10-19-loopr-tecnico/ficha.yaml` · sha256:fa3cb8dea913 · sujo
- `edicoes/2026-10-19-plano-90-dias/capa/codex-p2.log` · sha256:ac1c72bde383 · sujo
- `edicoes/2026-10-19-plano-90-dias/capa/pedido-p2.txt` · sha256:dc31a4bbe664 · sujo
- `edicoes/2026-10-19-plano-90-dias/capa/pedido.txt` · sha256:0b30ba3b89b5 · sujo
- `edicoes/2026-10-19-plano-90-dias/falas.json` · sha256:9770c1e4a61d · sujo
- `edicoes/2026-10-19-plano-90-dias/plano-critica.json` · sha256:3a38fd3da18d · sujo
- `edicoes/2026-10-19-prof2030-formacao/capa/pedido.txt` · sha256:d7a2518be829 · sujo
- `edicoes/2026-10-19-prof2030-formacao/capa/prompts-imagegen.txt` · sha256:b0834d094927 · sujo
- `edicoes/2026-10-19-prof2030-formacao/falas.json` · sha256:38eeda759009 · sujo
- `edicoes/2026-10-19-prof2030-formacao/ficha.yaml` · sha256:6bb863ed2a76 · sujo
- `edicoes/2026-10-19-prof2030-repo/capa/pedido.txt` · sha256:039829e4ad37 · sujo
- `edicoes/2026-10-19-prof2030-repo/capa/prompts-imagegen.json` · sha256:5d124ce97f20 · sujo
- `edicoes/2026-10-19-prof2030-repo/falas.json` · sha256:5751424ebc1e · sujo
- `edicoes/2026-10-19-prof2030-repo/ficha.yaml` · sha256:a991dd44ee6b · sujo
- `edicoes/2026-10-19-prof2030-tecnico/capa/pedido.txt` · sha256:15ab87a73a47 · sujo
- `edicoes/2026-10-19-prof2030-tecnico/falas.json` · sha256:bcae553cd712 · sujo
- `edicoes/2026-10-19-prof2030-tecnico/ficha.yaml` · sha256:5477a69f5606 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/capa/pedido.txt` · sha256:cd31f2f46baf · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/capa/prompts-imagegen.txt` · sha256:688494cb2298 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/falas.json` · sha256:3211568604b1 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/ficha.yaml` · sha256:8a73c21a12be · sujo
- `edicoes/2026-10-19-r7ex-divulga/capa/pedido.txt` · sha256:8b4c38fa4d2b · sujo
- `edicoes/2026-10-19-r7ex-divulga/falas.json` · sha256:02d2f6f53c72 · sujo
- `edicoes/2026-10-19-r7ex-divulga/ficha.yaml` · sha256:1140ab34f2dc · sujo
- `edicoes/2026-10-19-reserva-hotel-promo/capa/pedido.txt` · sha256:4fe08f12886f · sujo
- `edicoes/2026-10-19-reserva-hotel-promo/falas.json` · sha256:3db63ed4780d · sujo
- `edicoes/2026-10-19-reserva-restaurante-promo/capa/pedido.txt` · sha256:883e7c4d3437 · sujo
- `edicoes/2026-10-19-reserva-restaurante-promo/falas.json` · sha256:ff87a18c395e · sujo
- `edicoes/2026-10-19-reserva-restaurante-promo/ficha.yaml` · sha256:84993da4e2a9 · sujo
- `edicoes/2026-10-19-reserva-restaurante-promo/ficha.yaml.antes-marcadores` · sha256:89137fc2e1b0 · sujo
- `edicoes/2026-10-19-sair-do-sms/capa/pedido.txt` · sha256:95d441cd6e6b · sujo
- `edicoes/2026-10-19-sair-do-sms/falas.json` · sha256:206ec8fbdf71 · sujo
- `edicoes/2026-10-19-sair-do-sms/ficha.yaml` · sha256:6fde4fc1972b · sujo
- `edicoes/2026-10-19-seo-formacao/capa/pedido.txt` · sha256:62e9f8b3d252 · sujo
- `edicoes/2026-10-19-seo-formacao/falas.json` · sha256:6bebaaef8ade · sujo
- `edicoes/2026-10-19-seo-formacao/ficha.yaml` · sha256:afe017c36762 · sujo
- `edicoes/2026-10-19-seo-repo/capa/pedido.txt` · sha256:349a4dc71d9b · sujo
- `edicoes/2026-10-19-seo-repo/falas.json` · sha256:19bf029bd91e · sujo
- `edicoes/2026-10-19-seo-repo/ficha.yaml` · sha256:0bc7665780e4 · sujo
- `edicoes/2026-10-19-seo-tecnico/capa/pedido.txt` · sha256:894125ccf604 · sujo
- `edicoes/2026-10-19-seo-tecnico/falas.json` · sha256:9bc715a1e836 · sujo
- `edicoes/2026-10-19-seo-tecnico/ficha.yaml` · sha256:b8d37fad1d6a · sujo
- `edicoes/2026-10-19-singularidade-chegou/capa/prompts-imagegen.txt` · sha256:ff95d0070863 · sujo
- `edicoes/2026-10-19-skills15-impacto/capa/prompts-imagegen.json` · sha256:7d167602e053 · sujo
- `edicoes/2026-10-19-skills15-limpo/capa/prompts-imagegen.txt` · sha256:13e4501a6bb4 · sujo
- `edicoes/2026-10-19-skills15/capa/pedido.txt` · sha256:603071f534e5 · sujo
- `edicoes/2026-10-19-skills15/falas.json` · sha256:13418e87911b · sujo
- `edicoes/2026-10-19-skills15/ficha.yaml` · sha256:32abf160828f · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/capa/pedido.txt` · sha256:d21df8d457d2 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/capa/prompts-imagegen.json` · sha256:41db9e0ed5b6 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/falas.json` · sha256:fce59fb13305 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/ficha.yaml` · sha256:03a0acd1206b · sujo
- `edicoes/2026-10-19-tecnofeudalismo/capa/pedido.txt` · sha256:034643fe1003 · sujo
- `edicoes/2026-10-19-tecnofeudalismo/falas.json` · sha256:dc491469ffed · sujo
- `edicoes/2026-10-19-tecnofeudalismo/ficha.yaml` · sha256:fb5cb2bee7e0 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/20261019-003301/p2.png` · sha256:fda6c2537807 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/20261019-003301/p3.png` · sha256:a1b82fe795b7 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/20261019-003301/p4.png` · sha256:2cfae89f9bd2 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/20261019-003301/p5.png` · sha256:b16197b6d617 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/20261019-003301/p6.png` · sha256:46f1c1526697 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/abertura-desce.png` · sha256:49d0e95bd5bf · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/antiga/abertura.png` · sha256:5dd9eee8a576 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/pedido.txt` · sha256:44a2556176a5 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/prompts-imagegen-20261019.txt` · sha256:aa2657ace687 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/capa/prompts-imagegen.txt` · sha256:1b9677baff35 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/falas.json` · sha256:7da038084337 · sujo
- `edicoes/2026-10-19-tres-estagios-ia/ficha.yaml` · sha256:32c1b11a9224 · sujo
- `edicoes/2026-10-19-vendas-formacao/capa/pedido.txt` · sha256:12a96eda8573 · sujo
- `edicoes/2026-10-19-vendas-formacao/capa/prompts-imagegen.txt` · sha256:f25ce6b96ead · sujo
- `edicoes/2026-10-19-vendas-formacao/falas.json` · sha256:ff7c15cd3791 · sujo
- `edicoes/2026-10-19-vendas-formacao/ficha.yaml` · sha256:1759d1b23b20 · sujo
- `edicoes/2026-10-19-vendas-repo/capa/pedido.txt` · sha256:7a4b16f13890 · sujo
- `edicoes/2026-10-19-vendas-repo/falas.json` · sha256:a7f8cb6bdb1e · sujo
- `edicoes/2026-10-19-vendas-repo/ficha.yaml` · sha256:d47b95717e21 · sujo
- `edicoes/2026-10-19-vendas-tecnico/capa/pedido.txt` · sha256:eeb846fb0916 · sujo
- `edicoes/2026-10-19-vendas-tecnico/falas.json` · sha256:ace974dd9949 · sujo
- `edicoes/2026-10-19-vendas-tecnico/ficha.yaml` · sha256:be529cfc0e2b · sujo
- `edicoes/2026-10-20-bigtech-aurora/falas.json` · sha256:914d6b8d818a · sujo
- `edicoes/2026-10-20-bigtech-aurora/plano-critica.json` · sha256:4bcb14adca63 · sujo
- `edicoes/2026-10-20-bigtech-fable/capa/pedido.txt` · sha256:3dad60496dcf · sujo
- `edicoes/2026-10-20-bigtech-fable/falas.json` · sha256:172ef67e6573 · sujo
- `edicoes/2026-10-20-bigtech-fable/ficha.yaml` · sha256:e26eab97f777 · sujo
- `edicoes/2026-10-20-bigtech-ipo-b/capa/_antigo/abertura-desce.png` · sha256:9edeffd23d36 · sujo
- `PADRAO.md` · sha256:01c3755b311a · citado
- `producao/critico-plano.md` · sha256:a781cde1cae1 · citado
- `producao/revisor.md` · sha256:662bfd7d80e0 · citado
- `r7ex.py` · sha256:c122f1074ed0 · citado
- `edicoes/2026-11-17-enxame-quebra-empresa-lives4/ficha.yaml` · sha256:99692cc3f5c8 · citado

### Repo do trabalho: /home/nmaldaner/projetos/rtex
- commit: f8a3e5117925f7741107fc816a21af7fbd354688 · branch: main
- arquivos sujos: 39
- impressão de todos os sujos: 60902c64b2ec879a
- `FALHAS.md` · sha256:e562840e0ae2 · sujo
- `edicoes/2026-11-01-comece-por-tres/critica.json` · sha256:81ef333fffa7 · sujo
- `edicoes/2026-11-01-comece-por-tres/metritds-texto.txt` · sha256:64e16a262d1e · sujo
- `edicoes/2026-11-01-comece-por-tres/roteiro.json` · sha256:17ea212cfa20 · sujo
- `edicoes/2026-11-01-prospeccao-por-sinal/critica.json` · sha256:ca1188615ec0 · sujo
- `edicoes/2026-11-01-prospeccao-por-sinal/metritds-texto.txt` · sha256:d8313a98f0b0 · sujo
- `edicoes/2026-11-01-prospeccao-por-sinal/roteiro.json` · sha256:b67548588910 · sujo
- `edicoes/2026-11-04-claude-code-2/critica.json` · sha256:1b99d5eb2e4d · sujo
- `edicoes/2026-11-04-claude-code-2/metritds.txt` · sha256:7ecc5205224a · sujo
- `edicoes/2026-11-04-claude-code-2/roteiro.json` · sha256:4ddd11470cf0 · sujo
- `edicoes/2026-11-04-claude-escritorio/critica.json` · sha256:2302efb0570c · sujo
- `edicoes/2026-11-04-claude-escritorio/metritds-texto.txt` · sha256:e93b08e89444 · sujo
- `edicoes/2026-11-04-claude-escritorio/roteiro.json` · sha256:0bc9be93a62f · sujo
- `edicoes/2026-11-04-jarvis-local/CONTINUAR.md` · sha256:10ab3725a500 · sujo
- `edicoes/2026-11-04-jarvis-local/CONTINUAR.resultado` · sha256:806563799da1 · sujo
- `edicoes/2026-11-04-jarvis-local/critica.json` · sha256:2549dfac49ba · sujo
- `edicoes/2026-11-04-jarvis-local/metritds-texto.txt` · sha256:baaf2f11d003 · sujo
- `edicoes/2026-11-04-jarvis-local/metritds.txt` · sha256:87909a6c9b65 · sujo
- `edicoes/2026-11-04-jarvis-local/roteiro.json` · sha256:1e04c6436795 · sujo
- `edicoes/2026-11-04-openduet/CONTINUAR.md` · sha256:bf1f1a92f76a · sujo
- `edicoes/2026-11-04-openduet/CONTINUAR.resultado` · sha256:90663999d4be · sujo
- `edicoes/2026-11-04-openduet/capa-azul.jpg` · sha256:695b1ba53193 · sujo
- `edicoes/2026-11-04-openduet/critica.json` · sha256:53e5db8a588d · sujo
- `edicoes/2026-11-04-openduet/metritds-texto.txt` · sha256:0f31b85af343 · sujo
- `edicoes/2026-11-04-openduet/metritds.txt` · sha256:ab869f2c7a59 · sujo
- `edicoes/2026-11-04-openduet/roteiro.json` · sha256:e41046409375 · sujo
- `edicoes/2026-11-04-openduet/video.jpg` · sha256:6551e87627b5 · sujo
- `edicoes/2026-11-07-curiosidade-viral/critica.json` · sha256:219c0b3f67fb · sujo
- `edicoes/2026-11-07-curiosidade-viral/roteiro.json` · sha256:1fa8977bc08b · sujo
- `edicoes/2026-11-08-kit-design-ia/DECISAO-EDITORIAL.md` · sha256:79c6450c64c3 · sujo
- `edicoes/2026-11-08-kit-design-ia/PUBLICACAO-PENDENTE.md` · sha256:92930e0c1b35 · sujo
- `edicoes/2026-11-08-kit-design-ia/critica.json` · sha256:d776b8b32c32 · sujo
- `edicoes/2026-11-08-kit-design-ia/roteiro.json` · sha256:15044f83cab2 · sujo
- `edicoes/2026-11-11-esforco-ou-produto/critica.json` · sha256:f07968b39306 · sujo
- `edicoes/2026-11-11-esforco-ou-produto/roteiro.json` · sha256:4ca6cc992388 · sujo
- `edicoes/2026-11-12-ia-acelerando/critica.json` · sha256:dac6e4e1b1f3 · sujo
- `edicoes/2026-11-12-ia-acelerando/roteiro.json` · sha256:ea8ec6344370 · sujo
- `edicoes/2026-11-12-nivel-escada/critica.json` · sha256:48047422d3e8 · sujo
- `edicoes/2026-11-12-nivel-escada/roteiro.json` · sha256:5091ba5b8460 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/inema-design
- commit: 7c04856160ccbe540fd08538e2613dd018fd850f · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14
<!-- handoff-estado:fim -->
