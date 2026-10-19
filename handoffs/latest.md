# Handoffs — trabalhos abertos

Cada linha é um assunto em andamento: leia o snapshot do assunto que for continuar. Gravado por handoff-grava.py.

<!-- handoff-indice:inicio -->
- `r7ex` · handoffs/history/2026-10-19T170623Z-r7ex.md · 19/10 14:06
<!-- handoff-indice:fim -->

---

Cópia integral do snapshot mais recente (handoffs/history/2026-10-19T170623Z-r7ex.md):

# Handoff — 2026-10-19 — r7ex: produção ligada; os 10 reprovados da fila são de outras sessões (não mexer sem OK)

## Projeto e escopo
Raiz ~/projetos/r7ex (repo inematds/r7ex). Sessão aberta em ~/projetos/reel7etapas. Continuação do handoff handoffs/history/2026-10-19T155457Z-r7ex.md (trava do estúdio, produção sem sessão, varredura do revisor). Depois dele só houve conferência de estado; nenhum código mudou nesta parte.

## Objetivo atual
Reels r7ex saindo sozinhos do avatar no HeyGen até a fila do canal, impecáveis. Produção ligada (feito). Os 10 reprovados da fila: decisão do Nei, que lembrou que são conteúdo de outras sessões.

## Estado aceito
- [confirmed] Produção sem sessão ligada: timer r7ex-producao a cada 5 min; estado só com r7e-para-r7ex (na_fila) — arquivo: producao/producao.py; teste: `python3 producao/producao.py --status` → 1 linha na_fila
- [confirmed] Motor corrigido (cartão do print até y 1090, MAX_LEG 21) — commit 53f6ecb
- [confirmed] Fila do canal: 5 feitos (os 5 r7e do eventosextremospub, com video_id), 17 pendentes, 0 erro; nenhum dos 10 reprovados do r7ex foi ao YouTube — arquivo: fila/fila.json
- [confirmed] Outra sessão commitou no r7ex depois de mim: e885aab (D12 diagrama animado), 3ccacbb + revert af2601b, 9bc2e9a (imagem limpa) — commit 9bc2e9a
- [confirmed] Outra sessão roda 5 `r7ex.py fazer` à mão, fora da produção, esperando avatar no HeyGen: seo-repo, seo-tecnico, seo-formacao, gestao-formacao, gestao-repo — arquivo: edicoes/2026-10-19-seo-formacao/fazer3.log

## Proposto / tentado, não confirmado
- [unverified] Os 10 reprovados já foram ao v3 com o defeito — o Nei disse que foram; não conferi
- [?] Os 5 fazer manuais não passam pelo revisor automático — quem os lança deveria ler a folha ou usar `producao.py --add`

## Decisões
- Não mexer nos 10 reprovados (hacker, deepseek-flash, hacker-v2, ferramentas-v2, 2027-v2, saas-v2, chat-v2, demissao-v2, gestor-v2, tres-estagios-ia) sem OK explícito do Nei — são de outras sessões (Nei, 19/10)
- Intervalo da fila (1 a cada 2 h) segue até o Nei decidir — pendência em ~/projetos/wifi/pendencias.md

## Não fazer (restrições e travas)
- Não refazer nem tirar da fila os 10 reprovados sem OK do Nei — dito pelo usuário em 19/10, só nesta conversa
- Não interferir nos 5 fazer manuais de outra sessão nem no FALHAS.md sujo (linha seo-formacao, de outra sessão) — dito em 19/10, só nesta conversa
- Avatar só pelo estúdio com avatar/APROVADO_HEYGEN daquela produção; API HeyGen só status/download — fonte: CLAUDE.md
- Estúdio HeyGen sempre em DISPLAY=:99; login só no :10 — fonte: ~/.claude/projects/-home-nmaldaner-projetos-reel7etapas/memory/heygen-login-na-tela.md
- Publicar só pela fila; nunca upload direto — fonte: skill/SKILL.md
- Nunca trocar plano do HeyGen; nunca AskUserQuestion; commits como inematds; avisos Terminei/Falhou; telegrama fora de 23:20–23:55 — fonte: ~/.claude/CLAUDE.md

## Arquivos alterados
- nenhum nesta parte (as mudanças estão no handoff anterior)
- Fora do projeto: nenhum

## Memória e regras duráveis tocadas
- nenhuma

## Verificação
- Rodado: `python3 producao/producao.py --status` → na_fila r7e-para-r7ex
- Rodado: `systemctl --user list-timers r7ex-producao.timer fila-lives7.timer` → ambos ativos
- Rodado: `python3 fila/fila.py --status` → 5 feitos, 17 pendentes, 0 com erro
- Não rodado: conferência do que foi ao v3 — não pedido

## Estado em execução
- Processos em segundo plano: timer systemd r7ex-producao (systemctl --user stop r7ex-producao.timer para parar); os `r7ex.py fazer` são de outra sessão
- Servidores / portas: nenhum
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: refazer os 10 reprovados (Nei autoriza) ou deixar com quem fez — primeiro publica às 19 h de 19/10 (hacker, lives1)
- Aberta: intervalo da fila (1 a cada 2 h, 17 pendentes)
- Adiado: primeiro teste real do envio ao estúdio pela produção — no próximo `--add` com APROVADO_HEYGEN

## Pela metade
- nada desta sessão

## Próxima ação exata
Esperar a resposta do Nei sobre os 10 reprovados. Com OK: `python3 r7ex.py cena` + `render` em cada um, no lugar, e conferir a folha. Sem OK: não tocar.

## Mapa de retomada
- `producao/README.md` — como a produção funciona
- `producao/producao.py` — estados e travas
- `FALHAS.md` — linhas de 19/10 (revisor, MAX_LEG, print preto)
- `fila/fila.json` — o que já publicou

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → reels saindo sozinhos do HeyGen até a fila; produção ligada — fonte: producao/README.md
2. Qual foi a última decisão e por quê? → não mexer nos 10 reprovados sem OK, porque são de outras sessões — fonte: só nesta conversa
3. O que não pode mudar? → avatar só com APROVADO_HEYGEN; publicar só pela fila — fonte: skill/SKILL.md
4. O que está pela metade? → nada; os 10 reprovados esperam decisão — fonte: FALHAS.md
5. Qual é a próxima ação, por quê, e precisa de aprovação? → refazer os 10 só com OK do Nei — fonte: FALHAS.md

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 9bc2e9a2deee2b5a171a58432aa555df7335544c · branch: main
- arquivos sujos fora de handoffs/: 95
- `FALHAS.md` · sha256:205d1e2a6a11 · sujo
- `edicoes/2026-10-18-claude-15-comandos/capa/pedido.txt` · sha256:6de4037d1b0b · sujo
- `edicoes/2026-10-18-claude-15-comandos/capa/prompts-imagegen.txt` · sha256:d780f1ef782d · sujo
- `edicoes/2026-10-18-claude-15-comandos/falas.json` · sha256:9619927b2de5 · sujo
- `edicoes/2026-10-18-claude-15-comandos/ficha.yaml` · sha256:5a8af88c495d · sujo
- `edicoes/2026-10-18-deepseek-flash/capa/pedido.txt` · sha256:5fe24d4b58de · sujo
- `edicoes/2026-10-18-deepseek-flash/falas.json` · sha256:ad0049a39dee · sujo
- `edicoes/2026-10-18-deepseek-flash/ficha.yaml` · sha256:dfe0f0c58f00 · sujo
- `edicoes/2026-10-18-ferramentas-v2/capa/prompts-imagegen.txt` · sha256:906f10b2f244 · sujo
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
- `edicoes/2026-10-19-gestao-formacao/capa/pedido.txt` · sha256:84520fd8a368 · sujo
- `edicoes/2026-10-19-gestao-formacao/falas.json` · sha256:00231bda4db7 · sujo
- `edicoes/2026-10-19-gestao-formacao/ficha.yaml` · sha256:460d408eec83 · sujo
- `edicoes/2026-10-19-gestao-repo/capa/pedido.txt` · sha256:3ced72d21a23 · sujo
- `edicoes/2026-10-19-gestao-repo/falas.json` · sha256:f71d90be34e3 · sujo
- `edicoes/2026-10-19-gestao-repo/ficha.yaml` · sha256:c19f97e0284f · sujo
- `edicoes/2026-10-19-gestao-tecnico/capa/pedido.txt` · sha256:1c4e8c8761da · sujo
- `edicoes/2026-10-19-gestao-tecnico/falas.json` · sha256:af87566fb342 · sujo
- `edicoes/2026-10-19-gestao-tecnico/ficha.yaml` · sha256:b4ce24095294 · sujo
- `edicoes/2026-10-19-loopr-formacao/capa/pedido.txt` · sha256:744e1d16fe55 · sujo
- `edicoes/2026-10-19-loopr-formacao/capa/prompts-imagegen.json` · sha256:736b695151b4 · sujo
- `edicoes/2026-10-19-loopr-formacao/falas.json` · sha256:44e73da6b0aa · sujo
- `edicoes/2026-10-19-loopr-formacao/ficha.yaml` · sha256:1551c6c003a1 · sujo
- `edicoes/2026-10-19-loopr-repo/capa/pedido.txt` · sha256:b886161fc076 · sujo
- `edicoes/2026-10-19-loopr-repo/falas.json` · sha256:2b90f53fc7bf · sujo
- `edicoes/2026-10-19-loopr-repo/ficha.yaml` · sha256:d79b3aaa7027 · sujo
- `edicoes/2026-10-19-loopr-tecnico/capa/pedido.txt` · sha256:140d063c7e83 · sujo
- `edicoes/2026-10-19-loopr-tecnico/capa/prompts-imagegen.json` · sha256:4e0ca2fc970b · sujo
- `edicoes/2026-10-19-loopr-tecnico/falas.json` · sha256:9fa56f11cda4 · sujo
- `edicoes/2026-10-19-loopr-tecnico/ficha.yaml` · sha256:65d83072da41 · sujo
- `edicoes/2026-10-19-prof2030-formacao/ficha.yaml` · sha256:128d364ffa85 · sujo
- `edicoes/2026-10-19-prof2030-repo/ficha.yaml` · sha256:15ea7f251d46 · sujo
- `edicoes/2026-10-19-prof2030-tecnico/ficha.yaml` · sha256:403769a30d27 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/capa/pedido.txt` · sha256:cd31f2f46baf · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/capa/prompts-imagegen.txt` · sha256:688494cb2298 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/falas.json` · sha256:3211568604b1 · sujo
- `edicoes/2026-10-19-r7e-para-r7ex/ficha.yaml` · sha256:8a73c21a12be · sujo
- `edicoes/2026-10-19-r7ex-divulga/capa/pedido.txt` · sha256:8b4c38fa4d2b · sujo
- `edicoes/2026-10-19-r7ex-divulga/falas.json` · sha256:02d2f6f53c72 · sujo
- `edicoes/2026-10-19-r7ex-divulga/ficha.yaml` · sha256:1140ab34f2dc · sujo
- `edicoes/2026-10-19-seo-formacao/capa/pedido.txt` · sha256:a6e4940013e2 · sujo
- `edicoes/2026-10-19-seo-formacao/falas.json` · sha256:6bebaaef8ade · sujo
- `edicoes/2026-10-19-seo-formacao/ficha.yaml` · sha256:afe017c36762 · sujo
- `edicoes/2026-10-19-seo-repo/capa/pedido.txt` · sha256:c04dd2e6ef85 · sujo
- `edicoes/2026-10-19-seo-repo/falas.json` · sha256:19bf029bd91e · sujo
- `edicoes/2026-10-19-seo-repo/ficha.yaml` · sha256:0bc7665780e4 · sujo
- `edicoes/2026-10-19-seo-tecnico/capa/pedido.txt` · sha256:b9765ae40a58 · sujo
- `edicoes/2026-10-19-seo-tecnico/falas.json` · sha256:9bc715a1e836 · sujo
- `edicoes/2026-10-19-seo-tecnico/ficha.yaml` · sha256:b8d37fad1d6a · sujo
- `edicoes/2026-10-19-singularidade-chegou/capa/prompts-imagegen.txt` · sha256:ff95d0070863 · sujo
- `edicoes/2026-10-19-skills15-limpo/capa/prompts-imagegen.txt` · sha256:13e4501a6bb4 · sujo
- `edicoes/2026-10-19-skills15/capa/pedido.txt` · sha256:603071f534e5 · sujo
- `edicoes/2026-10-19-skills15/falas.json` · sha256:13418e87911b · sujo
- `edicoes/2026-10-19-skills15/ficha.yaml` · sha256:32abf160828f · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/capa/pedido.txt` · sha256:d21df8d457d2 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/capa/prompts-imagegen.json` · sha256:41db9e0ed5b6 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/falas.json` · sha256:fce59fb13305 · sujo
- `edicoes/2026-10-19-sobreviver-2-anos/ficha.yaml` · sha256:03a0acd1206b · sujo
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
- `edicoes/2026-10-19-vendas-formacao/capa/pedido.txt` · sha256:39dbd98f3ef8 · sujo
- `edicoes/2026-10-19-vendas-formacao/capa/prompts-imagegen.txt` · sha256:f25ce6b96ead · sujo
- `edicoes/2026-10-19-vendas-formacao/falas.json` · sha256:ff7c15cd3791 · sujo
- `edicoes/2026-10-19-vendas-formacao/ficha.yaml` · sha256:c5391948febb · sujo
- `edicoes/2026-10-19-vendas-repo/capa/pedido.txt` · sha256:a15933624779 · sujo
- `edicoes/2026-10-19-vendas-repo/falas.json` · sha256:a7f8cb6bdb1e · sujo
- `edicoes/2026-10-19-vendas-repo/ficha.yaml` · sha256:da02767a5199 · sujo
- `edicoes/2026-10-19-vendas-tecnico/ficha.yaml` · sha256:be529cfc0e2b · sujo
- `fila/fila.json.bak-20261019` · sha256:cb2d0d4e82c6 · sujo
- `producao/README.md` · sha256:baa24068e491 · citado
- `producao/producao.py` · sha256:5149dfddd5a6 · citado
- `fila/fila.json` · sha256:3baeb818e884 · citado
<!-- handoff-estado:fim -->
