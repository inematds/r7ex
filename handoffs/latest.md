# Handoffs — trabalhos abertos

Cada linha é um assunto em andamento: leia o snapshot do assunto que for continuar. Gravado por handoff-grava.py.

<!-- handoff-indice:inicio -->
- `r7ex` · handoffs/history/2026-10-19T012804Z-r7ex.md · 18/10 22:28
<!-- handoff-indice:fim -->

---

Cópia integral do snapshot mais recente (handoffs/history/2026-10-19T012804Z-r7ex.md):

# Handoff — 2026-10-18 — r7ex criado (7 etapas + telejornal), 7 reels no v3 e nas filas lives7/lives3

## Projeto e escopo
Raiz ~/projetos/r7ex (repo inematds/r7ex, criado nesta sessão; a sessão foi aberta em ~/projetos/reel7etapas). O Nei reprovou o r7e duas vezes ("não tem gancho", "ficou padrão") e mandou seguir o eventosextremospub; virou o padrão r7ex: roteiro de 7 etapas do r7e + acabamento de telejornal do eventosextremospub, num repo independente (cópia própria do motor, estúdio HeyGen, Whisper, trilha, envio ao v3 e fila). Repos tocados: ~/projetos/reel7etapas, ~/projetos/eventosextremospub, ~/projetos/inema-design, ~/projetos/wifi.

## Objetivo atual
Reels do Nei no padrão r7ex, publicados pelas filas e mandados ao v3. Pronto: os 7 v2 publicados no lives3 pela fila (e os 6 r7e-ev no lives7), sem erro.

## Estado aceito
- [confirmed] Repo r7ex com PADRAO.md, README (4 lotes, conteúdo × forma, links YT, motor, origens, como mudar), r7ex.py (novo/checar/avatar/imagens/cena/render/revisar/enviar/fila/fazer), skill — evidência: commit c797389, 0f89f74
- [confirmed] Teste ponta a ponta do exemplo hacker no r7ex — teste: `python3 r7ex.py fazer edicoes/2026-10-18-hacker --de …` → vídeo 36,5 s, -13,8 LUFS, fala 97%
- [confirmed] 7 reels v2 (imagens novas, mesmo avatar) feitos, revisados (folhas lidas), enviados ao v3 e na fila do lives3 — arquivo: `fila/fila.json` (local, fora do git)
- [confirmed] Hacker r7e-ev publicado no lives7 pela fila: https://youtube.com/shorts/DG30IdeqWcg — arquivo: `fila/fila.json`
- [confirmed] Kit inema-design D9 (gancho gatilho), D10 (propósito e plano), D11 (acabamento eventos) — evidência: commits 7e825bb, 55829ef, ef73aa6 em ~/projetos/inema-design
- [confirmed] 2 reels de gestão (motor antigo) publicados no lives3: xpDV5qQe5oE, cMhIavjhdh0 — arquivo: ~/projetos/reel7etapas/edicoes/2026-10-18-demissao-gestores/roteiro.yaml
- [confirmed] Aviso vermelho do HeyGen no v3 1 dia antes de vencer (cookie heygen_session, vence 17/11/2026 17:44) — arquivo: ~/projetos/wifi/heygen-aviso/aviso.py; timer heygen-aviso (9h/19h)
- [confirmed] Guia "como pedir um r7ex" enviado ao v3 — arquivo: `COMO-PEDIR.md`

## Proposto / tentado, não confirmado
- [?] Fila tem 2 itens para lives1 colocados por OUTRA sessão (r7ex edicoes/2026-10-18-hacker e 2026-10-18-deepseek-flash) — o hacker de teste já está no lives7 e vai ao lives3; perguntar ao Nei se mantém
- [unverified] Se o HeyGen renova a sessão sozinho com o uso — ~/projetos/wifi/heygen-aviso/historico.log vai mostrar

## Decisões
- Nome r7ex (r8ex daria a entender 8 etapas) — Nei 18/10
- r7ex independente: cópias em motor/, heygen/, r7ex/whisper.py, assets/trilha.mp3, bin/, fila/ — pedido do Nei ("se quiser ajustar não afeta os outros")
- Publicação só pela fila (fila/fila.py, timer fila-lives7, 9–21 h, 1 a cada 2 h); a fila mudou de ~/projetos/wifi/fila-lives7 para r7ex/fila
- Rejeitado: motor Pillow do r7e (tarja, diagramas.py) e "capa = ganho" para reel novo

## Não fazer (restrições e travas)
- Nunca abrir o estúdio HeyGen na tela do Nei: tudo com DISPLAY=:99; só a janela de LOGIN vai no :10 — fonte: ~/.claude/projects/-home-nmaldaner-projetos-reel7etapas/memory/heygen-login-na-tela.md
- Avatar só pelo estúdio, com avatar/APROVADO_HEYGEN daquela produção; nunca trocar de plano no HeyGen — fonte: `CLAUDE.md`
- Publicar só pela fila, nunca upload direto — fonte: `CLAUDE.md`
- "Grátis" só quando a página diz ou o Nei afirma (Empresas de 2027 e Constituição são INEMA.CLUB PRO) — fonte: `PADRAO.md`
- Não mexer nos itens lives1 da fila nem na edição deepseek-flash (outra sessão) sem o Nei — dito em 18/10, só nesta conversa
- Mudança de padrão vai primeiro ao kit inema-design (DECISOES/HISTORICO/correcoes) — fonte: ~/.claude/CLAUDE.md

## Arquivos alterados
- `PADRAO.md`, `README.md`, `CLAUDE.md`, `COMO-PEDIR.md`, `r7ex.py`, `r7ex/*.py`, `motor/*`, `heygen/*`, `fila/fila.py`, `skill/SKILL.md`, `modelo/ficha.yaml`, `ferramentas/lote_1018_para_fichas.py`, `edicoes/2026-10-18-*-v2/ficha.yaml` — o r7ex inteiro
- Fora do projeto: ~/projetos/reel7etapas (letra tarja, passos, diagramas.py, ev_cena.py, ev_util.py, README, SKILL, FALHAS, roteiros do dia); ~/projetos/eventosextremospub/edicoes/2026-10-18-r7e-* (7 edições); ~/projetos/inema-design (D9–D11); ~/projetos/wifi (heygen-aviso, LIMITES, fila-lives7/MUDOU.md); ~/.config/systemd/user/{heygen-aviso,fila-lives7}.{service,timer}

## Memória e regras duráveis tocadas
- ~/.claude/projects/-home-nmaldaner-projetos-reel7etapas/memory/heygen-login-na-tela.md — login HeyGen na tela :10, estúdio no :99
- ~/.claude/projects/-home-nmaldaner-projetos-reel7etapas/memory/r7e-motor-eventos.md — reel novo = r7ex
- ~/projetos/reel7etapas/FALHAS.md e ~/projetos/wifi/LIMITES.md — falhas e o login caído

## Verificação
- Rodado: `python3 r7ex.py checar` nas 7 fichas v2 → OK (chat com aviso de 466 caracteres, avatar já existe)
- Rodado: `python3 r7ex.py fazer` nas 7 → rc=0; folhas lidas
- Rodado: `python3 fila/fila.py --status` → 1 feito, 15 pendentes
- Não rodado: medição de visualizações (Metricool é API sem autorização)

## Estado em execução
- Processos em segundo plano: nenhum desta sessão
- Timers: fila-lives7 (r7ex/fila/fila.py, 9–21 h), heygen-aviso (9h/19h), systemctl --user list-timers
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: manter os 2 itens lives1 da outra sessão na fila?
- Aberta: as 2 de gestão vão aparecer duas vezes no lives3 (versão antiga já publicada + v2 na fila) — Nei pode querer tirar
- Adiado: guia (página) do r7ex em 3 idiomas — oferecido, sem resposta
- Adiado: autorização do Metricool para medir TikTok/Instagram

## Pela metade
- nada

## Próxima ação exata
Acompanhar os avisos da fila no v3 (amanhã 9 h em diante). Se o Nei pedir reel novo: skill r7ex (`python3 r7ex.py novo <slug>` → ficha → `fazer` → ler folha → `enviar` + `fila`); avatar novo só com o OK dele.

## Mapa de retomada
- `PADRAO.md` — o padrão fixo
- `README.md` — história, motor, como mudar
- `modelo/ficha.yaml` — ficha de exemplo
- `r7ex.py` — comandos
- `fila/fila.py` — fila de publicação

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → reels no padrão r7ex publicados pelas filas e no v3 — fonte: `PADRAO.md`
2. Qual foi a última decisão e por quê? → refazer os 7 pelo r7ex com imagens novas e mesmo avatar, para o lives3 — fonte: commit 0f89f74
3. O que não pode mudar? → estúdio só no :99, publicar só pela fila, avatar só com OK — fonte: `CLAUDE.md`
4. O que está pela metade? → nada — fonte: `fila/fila.py --status`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → acompanhar a fila; reel novo precisa do OK do avatar — fonte: `skill/SKILL.md`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim (credenciais citadas só pelo papel/caminho)


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 0f89f7461481fff7fffb4d258e081db5f38f1b14 · branch: main
- arquivos sujos fora de handoffs/: 12
- `edicoes/2026-10-18-2027-v2/capa/codex.log` · sha256:6b2c975c3ee5 · sujo
- `edicoes/2026-10-18-chat-v2/capa/codex.log` · sha256:009e2a3cd79f · sujo
- `edicoes/2026-10-18-deepseek-flash/capa/codex.log` · sha256:07be4413cce3 · sujo
- `edicoes/2026-10-18-deepseek-flash/capa/pedido.txt` · sha256:5fe24d4b58de · sujo
- `edicoes/2026-10-18-deepseek-flash/falas.json` · sha256:ad0049a39dee · sujo
- `edicoes/2026-10-18-deepseek-flash/ficha.yaml` · sha256:dfe0f0c58f00 · sujo
- `edicoes/2026-10-18-demissao-v2/capa/codex.log` · sha256:d83c41469409 · sujo
- `edicoes/2026-10-18-ferramentas-v2/capa/codex.log` · sha256:01a14480263f · sujo
- `edicoes/2026-10-18-ferramentas-v2/capa/prompts-imagegen.txt` · sha256:906f10b2f244 · sujo
- `edicoes/2026-10-18-gestor-v2/capa/codex.log` · sha256:15e744cf997e · sujo
- `edicoes/2026-10-18-hacker-v2/capa/codex.log` · sha256:50b6573dbb32 · sujo
- `edicoes/2026-10-18-saas-v2/capa/codex.log` · sha256:9dae914e5b67 · sujo
- `fila/fila.json` · sha256:98fec530a201 · citado
- `COMO-PEDIR.md` · sha256:5f1f653abbca · citado
- `CLAUDE.md` · sha256:4a4e3af78fde · citado
- `PADRAO.md` · sha256:11db80b2e497 · citado
- `README.md` · sha256:e1bf63329d88 · citado
- `r7ex.py` · sha256:68824f52bccb · citado
- `fila/fila.py` · sha256:46b1e28b487f · citado
- `skill/SKILL.md` · sha256:971e1b6b6ba2 · citado
- `modelo/ficha.yaml` · sha256:e6da61061795 · citado
- `ferramentas/lote_1018_para_fichas.py` · sha256:77769dcee954 · citado

### Repo do trabalho: /home/nmaldaner/projetos/reel7etapas
- commit: a95205c42ef606c808b562bab9f1cf592d724486 · branch: main
- arquivos sujos: 431 (lista cortada)
- impressão de todos os sujos: 948cedb31c117b86
- `edicoes/.wes-imagens-ok` · sha256:e3b0c44298fc · sujo
- `edicoes/2026-10-11-google-carbon/capa.jpg` · sha256:520cdd52a5e6 · sujo
- `edicoes/2026-10-11-google-carbon/fazer.log` · sha256:54e31940ecca · sujo
- `edicoes/2026-10-11-google-carbon/mapa.jpg` · sha256:09f7b6b87d41 · sujo
- `edicoes/2026-10-11-rea-clona-qualquer-software/fazer.log` · sha256:8c11ecc3c9cb · sujo
- `edicoes/2026-10-11-rea-clona-qualquer-software/fazer2.log` · sha256:00d0a5506da7 · sujo
- `edicoes/2026-10-11-repos-claude/capa.jpg` · sha256:f2706a9d7cfb · sujo
- `edicoes/2026-10-11-repos-claude/fazer.log` · sha256:0c2361c4055c · sujo
- `edicoes/2026-10-11-repos-claude/mapa.jpg` · sha256:2e9455695f24 · sujo
- `edicoes/2026-10-11-videos-com-ia/fazer.log` · sha256:eb1495b7e11a · sujo
- `edicoes/2026-10-11-videos-com-ia/fazer2.log` · sha256:142b4127db11 · sujo
- `edicoes/2026-10-12-agent-skills-addy/fazer.out` · sha256:505c670211d0 · sujo
- `edicoes/2026-10-12-agent-skills-addy/fazer.sh` · sha256:2f91cb0466c1 · sujo
- `edicoes/2026-10-12-agent-skills-addy/imagens.out` · sha256:9a3903a21345 · sujo
- `edicoes/2026-10-12-clima-furacoes/avatar.log` · sha256:12bb41d98ac4 · sujo
- `edicoes/2026-10-12-clima-furacoes/avatar/APROVADO_HEYGEN` · sha256:378289105935 · sujo
- `edicoes/2026-10-12-clima-furacoes/avatar/fala.txt` · sha256:25adefee6d59 · sujo
- `edicoes/2026-10-12-clima-furacoes/avatar/video_id.txt` · sha256:ad7b9e02861d · sujo
- `edicoes/2026-10-12-clima-furacoes/capa.jpg` · sha256:743dcd73fabe · sujo
- `edicoes/2026-10-12-clima-furacoes/imagens.log` · sha256:d4df962d16c6 · sujo
- `edicoes/2026-10-12-clima-furacoes/mapa.jpg` · sha256:ea30cbddac56 · sujo
- `edicoes/2026-10-12-clima-furacoes/montar.log` · sha256:ecacc9a0122b · sujo
- `edicoes/2026-10-12-clima-furacoes/montar2.log` · sha256:669bf799ab8e · sujo
- `edicoes/2026-10-12-clima-japao/avatar.log` · sha256:d84deb9b3353 · sujo
- `edicoes/2026-10-12-clima-japao/avatar/APROVADO_HEYGEN` · sha256:378289105935 · sujo
- `edicoes/2026-10-12-clima-japao/avatar/baixar.log` · sha256:3f9984de7a2c · sujo
- `edicoes/2026-10-12-clima-japao/avatar/fala.txt` · sha256:93bc029d7332 · sujo
- `edicoes/2026-10-12-clima-japao/avatar/video_id.txt` · sha256:d0e26993cad2 · sujo
- `edicoes/2026-10-12-clima-japao/capa.jpg` · sha256:ec15ad33783d · sujo
- `edicoes/2026-10-12-clima-japao/imagens.log` · sha256:ffb045b658b2 · sujo
- `edicoes/2026-10-12-clima-japao/mapa.jpg` · sha256:1737664bdd99 · sujo
- `edicoes/2026-10-12-clima-japao/montar.log` · sha256:363170c68331 · sujo
- `edicoes/2026-10-12-clima-planeta/avatar.log` · sha256:769fc629a1c6 · sujo
- `edicoes/2026-10-12-clima-planeta/avatar/APROVADO_HEYGEN` · sha256:378289105935 · sujo
- `edicoes/2026-10-12-clima-planeta/avatar/fala.txt` · sha256:546514a7d4ef · sujo
- `edicoes/2026-10-12-clima-planeta/avatar/video_id.txt` · sha256:50c0a60f678c · sujo
- `edicoes/2026-10-12-clima-planeta/capa.jpg` · sha256:0b88124ef149 · sujo
- `edicoes/2026-10-12-clima-planeta/imagens.log` · sha256:a0f15f351526 · sujo
- `edicoes/2026-10-12-clima-planeta/mapa.jpg` · sha256:f1768e9d7617 · sujo
- `edicoes/2026-10-12-clima-planeta/montar.log` · sha256:099adb58d7d9 · sujo
- `edicoes/2026-10-12-clima-tailandia/avatar.log` · sha256:6e8bb015d006 · sujo
- `edicoes/2026-10-12-clima-tailandia/avatar/APROVADO_HEYGEN` · sha256:378289105935 · sujo
- `edicoes/2026-10-12-clima-tailandia/avatar/baixar.log` · sha256:957827c2983b · sujo
- `edicoes/2026-10-12-clima-tailandia/avatar/fala.txt` · sha256:27188e23e020 · sujo
- `edicoes/2026-10-12-clima-tailandia/avatar/video_id.txt` · sha256:6b202607ceef · sujo
- `edicoes/2026-10-12-clima-tailandia/capa.jpg` · sha256:d6f99b19dfbc · sujo
- `edicoes/2026-10-12-clima-tailandia/imagens.log` · sha256:0fa6c79df108 · sujo
- `edicoes/2026-10-12-clima-tailandia/mapa.jpg` · sha256:3fb9a40cbfaf · sujo
- `edicoes/2026-10-12-clima-tailandia/montar.log` · sha256:da2d6df4ef6c · sujo
- `edicoes/2026-10-12-consultoria-2027/avatar/APROVADO_HEYGEN` · sha256:8e79e036f941 · sujo
- `edicoes/2026-10-12-consultoria-2027/avatar/fala.txt` · sha256:ece72afaaebd · sujo
- `edicoes/2026-10-12-consultoria-2027/avatar/video_id.txt` · sha256:f2d4666b9664 · sujo
- `edicoes/2026-10-12-consultoria-2027/roteiro.yaml` · sha256:f1dd8bd587ed · sujo
- `edicoes/2026-10-12-oscoach/avatar/APROVADO_HEYGEN` · sha256:903f04fc04a3 · sujo
- `edicoes/2026-10-12-oscoach/avatar/fala.txt` · sha256:481a5de0583b · sujo
- `edicoes/2026-10-12-oscoach/avatar/video_id.txt` · sha256:5d27ecb79632 · sujo
- `edicoes/2026-10-12-oscoach/capa.jpg` · sha256:3eaabbdf9713 · sujo
- `edicoes/2026-10-12-oscoach/espera-heygen.sh` · sha256:6ccf377ee7dd · sujo
- `edicoes/2026-10-12-oscoach/fazer.log` · sha256:81d19967b035 · sujo
- `edicoes/2026-10-12-oscoach/imagens.log` · sha256:a0f15f351526 · sujo
- `edicoes/2026-10-12-oscoach/mapa.jpg` · sha256:076fca2c0bf8 · sujo
- `edicoes/2026-10-12-oscoach/roteiro.yaml` · sha256:6a7306b61fc3 · sujo
- `edicoes/2026-10-12-oswork-antes-jarvis/fazer.log` · sha256:012b56f771e7 · sujo
- `edicoes/2026-10-12-oswork-jarvis-3d/fazer.log` · sha256:5f292a169afb · sujo
- `edicoes/2026-10-12-oswork-jarvis-3d/montar.log` · sha256:ab8e0f925977 · sujo
- `edicoes/2026-10-12-oswork-jarvis-exec/fazer.log` · sha256:81f438330c38 · sujo
- `edicoes/2026-10-12-oswork-jarvis-flat/fazer.log` · sha256:1d794106040f · sujo
- `edicoes/2026-10-12-oswork-jarvis-flat/montar.log` · sha256:8b4de70d7343 · sujo
- `edicoes/2026-10-12-oswork-jarvis-hq/fazer.log` · sha256:4cdbd53a9ac6 · sujo
- `edicoes/2026-10-12-oswork-jarvis-hq/montar.log` · sha256:0c890ca3ac84 · sujo
- `edicoes/2026-10-12-r7e-como-funciona/fazer.log` · sha256:e29e2e08528b · sujo
- `edicoes/2026-10-12-rea-area/avatar.log` · sha256:8b68c329cd9e · sujo
- `edicoes/2026-10-12-rea-area/fazer.log` · sha256:d2a7908a810e · sujo
- `edicoes/2026-10-12-rea-area/fazer2.log` · sha256:7ca1816b48ce · sujo
- `edicoes/2026-10-12-rea-area/imagens.log` · sha256:a0f15f351526 · sujo
- `edicoes/2026-10-12-rea-area/publicar.log` · sha256:e7df36774483 · sujo
- `edicoes/2026-10-12-rea-clone-tudo/avatar.log` · sha256:8c3e43f3e3e8 · sujo
- `edicoes/2026-10-12-rea-clone-tudo/fazer.log` · sha256:eefc1be44728 · sujo
- `edicoes/2026-10-12-rea-clone-tudo/fazer2.log` · sha256:e78aacb705bd · sujo
- `edicoes/2026-10-12-rea-clone-tudo/imagens.log` · sha256:a0f15f351526 · sujo
- `edicoes/2026-10-12-rea-clone-tudo/publicar.log` · sha256:992c24996d50 · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/avatar/studio.draft1.log` · sha256:5a3681db2310 · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/avatar/video_id.draft1.txt` · sha256:a95a5e9dcb37 · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/avatar2.log` · sha256:cce8ad7392df · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/fazer.log` · sha256:6d96fec8bd74 · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/fazer3.log` · sha256:5df196cb14a6 · sujo
- `edicoes/2026-10-12-rea-mundo-bilionario/video-v1.mp4` · sha256:af6445f3e292 · sujo
- `edicoes/2026-10-12-rea-nem-precisa/fazer.log` · sha256:b7c5c5f718dd · sujo
- `edicoes/2026-10-12-rea-nem-precisa/imagens.log` · sha256:9a3903a21345 · sujo
- `edicoes/2026-10-12-rea-nem-precisa/montar2.log` · sha256:9f1cd0c5c5e2 · sujo
- `edicoes/2026-10-12-rea-nem-precisa/publicar.log` · sha256:5c62aef4095d · sujo
- `edicoes/2026-10-12-rea-nem-precisa/validar2.log` · sha256:3cedebec0514 · sujo
- `edicoes/2026-10-12-rea-quatro-passos/fazer.log` · sha256:ff9fafc7ffea · sujo
- `edicoes/2026-10-12-rea-quatro-passos/montar2.log` · sha256:133243e3a411 · sujo
- `edicoes/2026-10-12-rea-sem-travas/fazer.log` · sha256:e8c2e93bc9f6 · sujo
- `edicoes/2026-10-12-rea-sem-travas/imagens.log` · sha256:9a3903a21345 · sujo
- `edicoes/2026-10-12-rea-sem-travas/montar2.log` · sha256:fecf117401a4 · sujo
- `edicoes/2026-10-12-rea-sem-travas/publicar.log` · sha256:7071eafbe3e2 · sujo
- `edicoes/2026-10-12-rea-sem-travas/validar2.log` · sha256:8d14ff01944f · sujo
- `edicoes/2026-10-12-rea-servidor/fazer.log` · sha256:b93182b1770a · sujo
- `edicoes/2026-10-13-clima-semana-mundo/avatar/fala.txt` · sha256:10a5a22ae769 · sujo
- `edicoes/2026-10-13-clima-semana-mundo/avatar/video_id.txt` · sha256:b323d84e25dd · sujo
- `edicoes/2026-10-13-clima-semana-mundo/capa.jpg` · sha256:e053b9ed1f1f · sujo
- `edicoes/2026-10-13-clima-semana-mundo/fazer.log` · sha256:7fd9ffaa777b · sujo
- `edicoes/2026-10-13-clima-semana-mundo/mapa.jpg` · sha256:39b804e6a237 · sujo
- `edicoes/2026-10-13-constituicao-agentes/fazer.log` · sha256:0725916eb0fc · sujo
- `edicoes/2026-10-13-rato-gene/avatar/APROVADO_HEYGEN` · sha256:87e6d568c298 · sujo
- `edicoes/2026-10-13-rato-gene/avatar/fala.txt` · sha256:596b46c69a2e · sujo
- `edicoes/2026-10-13-rato-gene/avatar/video_id.txt` · sha256:a76a83d4e0ba · sujo
- `edicoes/2026-10-13-rato-gene/capa.jpg` · sha256:338e5946bff1 · sujo
- `edicoes/2026-10-13-rato-gene/fazer.log` · sha256:e41b59306187 · sujo
- `edicoes/2026-10-13-rato-gene/mapa.jpg` · sha256:a8578aa0d52e · sujo
- `edicoes/2026-10-13-rato-gene/roteiro.yaml` · sha256:1b95f8976e05 · sujo
- `edicoes/2026-10-13-rea-area-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-area-es/avatar/fala.txt` · sha256:7bb5aa8e5dd5 · sujo
- `edicoes/2026-10-13-rea-area-es/avatar/video_id.txt` · sha256:e577fe348ffc · sujo
- `edicoes/2026-10-13-rea-area-es/capa.jpg` · sha256:19176318cb59 · sujo
- `edicoes/2026-10-13-rea-area-es/mapa.jpg` · sha256:6f38d6f43cdc · sujo
- `edicoes/2026-10-13-rea-area-es/roteiro.yaml` · sha256:5c2bb77d8aad · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/avatar/fala.txt` · sha256:20954f80d321 · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/avatar/video_id.txt` · sha256:a921f3ad9e79 · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/capa.jpg` · sha256:cf255a39f260 · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/mapa.jpg` · sha256:41fafdac1b60 · sujo
- `edicoes/2026-10-13-rea-clona-qualquer-software-es/roteiro.yaml` · sha256:089252867321 · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/avatar/fala.txt` · sha256:0c6ede81f2be · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/avatar/video_id.txt` · sha256:b277c3aae543 · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/capa.jpg` · sha256:b49e1f5006db · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/mapa.jpg` · sha256:04960f94d12c · sujo
- `edicoes/2026-10-13-rea-clone-tudo-es/roteiro.yaml` · sha256:9473a3cfb8c1 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/avatar/fala.txt` · sha256:ef54ffaac012 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/avatar/video_id.txt` · sha256:39b644aba124 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/capa.jpg` · sha256:4f1bc524d1f7 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/mapa.jpg` · sha256:e4410b041dd5 · sujo
- `edicoes/2026-10-13-rea-mundo-bilionario-es/roteiro.yaml` · sha256:3ad49ef2bf3a · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/avatar/fala.txt` · sha256:f52bd08e42e5 · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/avatar/video_id.txt` · sha256:cdca7264f180 · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/capa.jpg` · sha256:e3f75198afab · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/mapa.jpg` · sha256:f5df55c3caed · sujo
- `edicoes/2026-10-13-rea-nem-precisa-es/roteiro.yaml` · sha256:7b6b58fde1dd · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/antes-portugues/avatar.mp4` · sha256:563dac3d1bcc · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/antes-portugues/fala.txt` · sha256:b0794d32d5a6 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/antes-portugues/studio.log` · sha256:315dc089f57d · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/antes-portugues/video_id.txt` · sha256:ccff041d37f6 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/fala.txt` · sha256:a99bac8603bf · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/avatar/video_id.txt` · sha256:c1c1dc18e118 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/capa.jpg` · sha256:c90ddf151065 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/mapa.jpg` · sha256:55fca32fd6d2 · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/roteiro.yaml` · sha256:27cf7b9c9cfd · sujo
- `edicoes/2026-10-13-rea-quatro-passos-es/roteiro.yaml.antes-portugues` · sha256:a29a415c6bb4 · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/avatar/fala.txt` · sha256:eeea23a815fd · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/avatar/video_id.txt` · sha256:94ec92a2cf86 · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/capa.jpg` · sha256:5397ba42cbe4 · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/mapa.jpg` · sha256:9005b92380df · sujo
- `edicoes/2026-10-13-rea-sem-travas-es/roteiro.yaml` · sha256:32f79b25002e · sujo
- `edicoes/2026-10-13-rea-servidor-es/avatar/APROVADO_HEYGEN` · sha256:4d3dc6ac4046 · sujo
- `edicoes/2026-10-13-rea-servidor-es/avatar/fala.txt` · sha256:125d9eae7973 · sujo
- `edicoes/2026-10-13-rea-servidor-es/avatar/video_id.txt` · sha256:e2a83e603ce0 · sujo
- `edicoes/2026-10-13-rea-servidor-es/capa.jpg` · sha256:5f211cb1aa52 · sujo
- `edicoes/2026-10-13-rea-servidor-es/mapa.jpg` · sha256:b333b0404f3b · sujo
- `edicoes/2026-10-13-rea-servidor-es/roteiro.yaml` · sha256:af0584fec2e9 · sujo
- `edicoes/2026-10-14-constituicao-limites/avatar/baixar.log` · sha256:8b8e17881a67 · sujo
- `edicoes/2026-10-14-constituicao-limites/imagens.log` · sha256:2a4a24f43ab6 · sujo
- `edicoes/2026-10-14-meta-muse-wonder/avatar/APROVADO_HEYGEN` · sha256:da81e4703eca · sujo
- `edicoes/2026-10-14-meta-muse-wonder/avatar/fala.txt` · sha256:f5819d0bee63 · sujo
- `edicoes/2026-10-14-meta-muse-wonder/avatar/video_id.txt` · sha256:a188189cb06d · sujo
- `edicoes/2026-10-14-meta-muse-wonder/capa.jpg` · sha256:64458c957909 · sujo
- `edicoes/2026-10-14-meta-muse-wonder/fazer.log` · sha256:7a531abab9ba · sujo
- `edicoes/2026-10-14-meta-muse-wonder/imagens.log` · sha256:a0f15f351526 · sujo
- `edicoes/2026-10-14-meta-muse-wonder/mapa.jpg` · sha256:f8e1a6318194 · sujo
- `edicoes/2026-10-14-meta-muse-wonder/roteiro.yaml` · sha256:215e697af856 · sujo
- `edicoes/2026-10-14-rea-clones-queda/avatar/APROVADO_HEYGEN` · sha256:49245e195ef3 · sujo
- `edicoes/2026-10-14-rea-clones-queda/avatar/fala.txt` · sha256:1cdc0fd0685a · sujo
- `edicoes/2026-10-14-rea-clones-queda/avatar/video_id.txt` · sha256:7bb9df6e9661 · sujo
- `edicoes/2026-10-14-rea-clones-queda/montar.log` · sha256:e96f3bf9a5dc · sujo
- `edicoes/2026-10-14-rea-clones-queda/roteiro.yaml` · sha256:94ed921818e9 · sujo
- `edicoes/2026-10-14-robo-sem-robo/avatar/APROVADO_HEYGEN` · sha256:e96d3b53c1af · sujo
- `edicoes/2026-10-14-robo-sem-robo/avatar/fala.txt` · sha256:419dbfe20b34 · sujo
- `edicoes/2026-10-14-robo-sem-robo/avatar/video_id.txt` · sha256:85409b530779 · sujo
- `edicoes/2026-10-14-robo-sem-robo/capa.jpg` · sha256:3bdfacf72d59 · sujo
- `edicoes/2026-10-14-robo-sem-robo/fazer.log` · sha256:15db932873a2 · sujo
- `edicoes/2026-10-14-robo-sem-robo/mapa.jpg` · sha256:18d50504b371 · sujo
- `edicoes/2026-10-14-robo-sem-robo/roteiro.yaml` · sha256:f945c1d1b50a · sujo
- `edicoes/2026-10-14-robo-uma-foto/avatar/APROVADO_HEYGEN` · sha256:c85836a71683 · sujo
- `edicoes/2026-10-14-robo-uma-foto/avatar/fala.txt` · sha256:761560fae3d7 · sujo
- `edicoes/2026-10-14-robo-uma-foto/avatar/video_id.txt` · sha256:31b48ac6c146 · sujo
- `edicoes/2026-10-14-robo-uma-foto/capa.jpg` · sha256:9b9749b9b7bc · sujo
- `edicoes/2026-10-14-robo-uma-foto/fazer.log` · sha256:26656f74cf36 · sujo
- `edicoes/2026-10-14-robo-uma-foto/imagens.log` · sha256:95962fb90b6b · sujo
- `edicoes/2026-10-14-robo-uma-foto/mapa.jpg` · sha256:93b01736f2f2 · sujo
- `edicoes/2026-10-14-robo-uma-foto/publicar.log` · sha256:9a4afda982db · sujo
- `edicoes/2026-10-14-robo-uma-foto/publicar2.log` · sha256:dd43d27871ba · sujo
- `edicoes/2026-10-14-robo-uma-foto/roteiro.yaml` · sha256:ef774f475358 · sujo
- `edicoes/2026-10-14-software-ensina-robos/avatar/APROVADO_HEYGEN` · sha256:e96d3b53c1af · sujo
- `edicoes/2026-10-14-software-ensina-robos/avatar/fala.txt` · sha256:9a3ea3dfc86a · sujo

### Repo do trabalho: /home/nmaldaner/projetos/eventosextremospub
- commit: a604345ce41f06260a71dec30867b655a7f72fe3 · branch: main
- arquivos sujos: 807 (lista cortada)
- impressão de todos os sujos: c6dd7c21c086e425
- `CLAUDE.md` · sha256:71ffe0603e53 · sujo
- `FALHAS.md` · sha256:5a4fb7af95a0 · sujo
- `auto/previsao-usados.txt` · sha256:58365ecb131a · sujo
- `edicoes/2026-10-09-alerta-norte-nordeste/video-avatar.mp4.envio-v3.json` · sha256:d3fec43b751f · sujo
- `edicoes/2026-10-09-alerta-norte-nordeste/video.mp4.envio-v3.json` · sha256:356bde79342d · sujo
- `edicoes/2026-10-09-el-nino/avatar/foto.jpg` · sha256:4a387696d84d · sujo
- `edicoes/2026-10-09-el-nino/fonte/painel-el-nino-4.pdf` · sha256:8058947c242b · sujo
- `edicoes/2026-10-09-el-nino/previa-16x9.mp4.envio-v3.json` · sha256:152d7f71b582 · sujo
- `edicoes/2026-10-09-el-nino/previa.mp4.envio-v3.json` · sha256:c99530b92148 · sujo
- `edicoes/2026-10-09-el-nino/sat/web/anomalia.png` · sha256:87c7e4f6737b · sujo
- `edicoes/2026-10-09-el-nino/video-avatar.mp4.envio-v3.json` · sha256:74c69c4a617b · sujo
- `edicoes/2026-10-10-el-nino-explicado/avatar/video_id.txt` · sha256:7bd8bef1f42e · sujo
- `edicoes/2026-10-10-el-nino-explicado/sat/web/anomalia.png` · sha256:3cf05867665b · sujo
- `edicoes/2026-10-10-el-nino-explicado/video-avatar-bot.mp4.envio-v3.json` · sha256:c222bf494599 · sujo
- `edicoes/2026-10-10-ultimas-24h/sat/web/ir_tempos.json` · sha256:0093b9fbcc3b · sujo
- `edicoes/2026-10-10-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:93d5275dc291 · sujo
- `edicoes/2026-10-10-ultimas-24h/video.mp4.envio-v3.json` · sha256:3b73ea0d4b44 · sujo
- `edicoes/2026-10-11-semana/om/prev15_capitais.json` · sha256:de2d6ea61b90 · sujo
- `edicoes/2026-10-11-semana/om/prev15_grade.json` · sha256:a12abf1c36ec · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:024651b3971b · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:70740ae45e49 · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:8139abb88947 · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:ed0d7c1f0a1f · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:06611266fcbb · sujo
- `edicoes/2026-10-11-semana/sat/web/ir_tempos.json` · sha256:e5c7c26860b8 · sujo
- `edicoes/2026-10-11-semana/video-avatar.mp4.envio-v3.json` · sha256:2735f7759277 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:b14ba84c80c4 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:7a36901321eb · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:b33519abe086 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:d4d660256cf4 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:d5c28f4d9663 · sujo
- `edicoes/2026-10-11-ultimas-24h/sat/web/ir_tempos.json` · sha256:9898057fe396 · sujo
- `edicoes/2026-10-11-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:ebbd75b5e6b0 · sujo
- `edicoes/2026-10-12-amazonia-mundo/AVATAR-STATUS.txt` · sha256:58973896896b · sujo
- `edicoes/2026-10-12-amazonia-mundo/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-amazonia-mundo/avatar/video_id.txt` · sha256:8d2b0205a515 · sujo
- `edicoes/2026-10-12-amazonia-mundo/video-avatar-bot.mp4.envio-v3.json` · sha256:3c7806a71744 · sujo
- `edicoes/2026-10-12-amazonia-mundo/video-bot.mp4.envio-v3.json` · sha256:005b1a70c6df · sujo
- `edicoes/2026-10-12-amazonia-reel/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-amazonia-reel/avatar/video_id.txt` · sha256:fb51897b4973 · sujo
- `edicoes/2026-10-12-amazonia-reel/video-avatar.mp4.envio-v3.json` · sha256:06e8b61ab915 · sujo
- `edicoes/2026-10-12-amazonia-reel/video.mp4.envio-v3.json` · sha256:a9e6d3e9b0fa · sujo
- `edicoes/2026-10-12-mundo-clima/AVATAR-STATUS.txt` · sha256:f73b37dbbcd3 · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/fala.txt` · sha256:f8371ab6656c · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/tempos.json` · sha256:45957a78d8ba · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/video_id.txt` · sha256:2e18a64b6eee · sujo
- `edicoes/2026-10-12-mundo-clima/sat/web/anomalia.png` · sha256:93a6cd64b51a · sujo
- `edicoes/2026-10-12-mundo-clima/video-avatar-bot.mp4.envio-v3.json` · sha256:605d104a4328 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:cc4897ad649e · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:28bd35263839 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:7b901359f016 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:0748fabcb069 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:a9d4ee964f96 · sujo
- `edicoes/2026-10-12-ultimas-24h/sat/web/ir_tempos.json` · sha256:848644d2d9b0 · sujo
- `edicoes/2026-10-12-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:7600d935ee46 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/fala.txt` · sha256:35f7d5d5085f · sujo
- `edicoes/2026-10-13-24h-foto/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-24h-foto/avatar/tempos.json` · sha256:e756e0286f71 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/video_id.txt` · sha256:8846c538f621 · sujo
- `edicoes/2026-10-13-24h-foto/falas.json` · sha256:bd7cacaca636 · sujo
- `edicoes/2026-10-13-24h-foto/gerar_cena.py` · sha256:a628ff9fa682 · sujo
- `edicoes/2026-10-13-24h-foto/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:8d45b4a93ef9 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:802a051b6c1e · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:47173b7139ce · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:36bf59ffe2e2 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/previsao7d.json` · sha256:a6412fc8a1cb · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/resumo.json` · sha256:474fd69f9176 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/dados.md` · sha256:508e8bad69eb · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/noticias.md` · sha256:b71c6c80d7af · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/proposta.md` · sha256:0bccc7e17577 · sujo
- `edicoes/2026-10-13-24h-foto/previa/avatar/avatar.mp4` · sha256:52eaf247a0ef · sujo
- `edicoes/2026-10-13-24h-foto/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-24h-foto/previa/avatar/tempos.json` · sha256:716d08429e04 · sujo
- `edicoes/2026-10-13-24h-foto/previa/build/mapa-avatar.mp4` · sha256:f3d77e899cfe · sujo
- `edicoes/2026-10-13-24h-foto/previa/cena.js` · sha256:d230ba23e43c · sujo
- `edicoes/2026-10-13-24h-foto/previa/gerar_cena.py` · sha256:a628ff9fa682 · sujo
- `edicoes/2026-10-13-24h-foto/sat/web/ir_tempos.json` · sha256:a3a07cc5dacf · sujo
- `edicoes/2026-10-13-24h-foto/tempos.json` · sha256:716d08429e04 · sujo
- `edicoes/2026-10-13-24h-foto/video-avatar.mp4.envio-v3.json` · sha256:02f8c7e17e1d · sujo
- `edicoes/2026-10-13-24h-foto/video-previa.mp4.envio-v3.json` · sha256:b21b24b100e3 · sujo
- `edicoes/2026-10-13-24h-foto/yt.txt` · sha256:91f6e04c661d · sujo
- `edicoes/2026-10-13-clima-do-dia/REFAZER-VISUAL.md` · sha256:76732fdd5557 · sujo
- `edicoes/2026-10-13-clima-do-dia/VISUAL-OK.txt` · sha256:8ae3d17ddc35 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/fala.txt` · sha256:aeb87eaedf74 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/tempos.json` · sha256:81a3924aa399 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/video_id.txt` · sha256:745189a6ee43 · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/LIMITES.md` · sha256:bdbf1caf92e5 · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/abertura.png` · sha256:21c07d0154ae · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/granizo.png` · sha256:95549d1f976a · sujo
- `edicoes/2026-10-13-clima-do-dia/coleta_colunas.py` · sha256:eea4295ead46 · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/audio.wav` · sha256:35cfaf1576bc · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/checkpoint.json` · sha256:abde5e7b34ef · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/whisper_gpu_result.json` · sha256:734e3ec2f652 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.json` · sha256:b08e4adba833 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.srt` · sha256:dfe4f8b8db34 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.txt` · sha256:57bb75176895 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript_summary.json` · sha256:a1a31002e897 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/video.mp4` · sha256:616cb78ab572 · sujo
- `edicoes/2026-10-13-clima-do-dia/gerar_cena.v1.py` · sha256:f22d34263f8c · sujo
- `edicoes/2026-10-13-clima-do-dia/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/boletim.md` · sha256:b8fcc50116d7 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:ea604d7b7891 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/colunas_sul_16d.json` · sha256:805795a5bba5 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:ed0f6b0eb2e1 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:d84b7bd78035 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:7a886f5f4547 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/previsao7d.json` · sha256:a6412fc8a1cb · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/resumo.json` · sha256:4c3e311968cd · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/proposta.md` · sha256:14b81c105bc4 · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/avatar/avatar.mp4` · sha256:837f18deb29e · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/avatar/tempos.json` · sha256:f333b9b530fc · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/build/mapa-avatar.mp4` · sha256:a07815b5694f · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/cena.js` · sha256:f477d8b8a95e · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/gerar_cena.py` · sha256:f22d34263f8c · sujo
- `edicoes/2026-10-13-clima-do-dia/refazer-visual.sh` · sha256:4a952f0a007d · sujo
- `edicoes/2026-10-13-clima-do-dia/sat/web/anomalia.png` · sha256:37a492aa6cab · sujo
- `edicoes/2026-10-13-clima-do-dia/sat/web/ir_tempos.json` · sha256:fa8e52f6c9bd · sujo
- `edicoes/2026-10-13-clima-do-dia/tempos.json` · sha256:f333b9b530fc · sujo
- `edicoes/2026-10-13-clima-do-dia/video-avatar.mp4.envio-v3.json` · sha256:3a758fdd1171 · sujo
- `edicoes/2026-10-13-clima-do-dia/video-previa.mp4.envio-v3.json` · sha256:5f9a8b87ce66 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/tempos-original.json` · sha256:49e2c64aef94 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/video_id.txt` · sha256:5156f7e0f4d9 · sujo
- `edicoes/2026-10-13-mundo-7d/falas-original.json` · sha256:57e3ddd50803 · sujo
- `edicoes/2026-10-13-mundo-7d/gerar_cena-original.py` · sha256:88d67f202d93 · sujo
- `edicoes/2026-10-13-mundo-7d/narrar.py` · sha256:589de45d4fd8 · sujo
- `edicoes/2026-10-13-mundo-7d/pesquisa/noticias.md` · sha256:76e7fc608c15 · sujo
- `edicoes/2026-10-13-mundo-7d/pesquisa/proposta.md` · sha256:dd12796b350c · sujo
- `edicoes/2026-10-13-mundo-7d/previa/.mapa.html` · sha256:f607bc88a497 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/avatar/avatar.mp4` · sha256:5edac8708228 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/avatar/foto.png` · sha256:f00259b33535 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/avatar/tempos.json` · sha256:12aa32b862a5 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/cena.js` · sha256:a103de9e5009 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/gerar_cena.py` · sha256:88d67f202d93 · sujo
- `edicoes/2026-10-13-mundo-7d/video-avatar-v2.mp4.envio-v3.json` · sha256:48dd2feba514 · sujo
- `edicoes/2026-10-13-mundo-7d/video-avatar.mp4.envio-v3.json` · sha256:2a68d6d22606 · sujo
- `edicoes/2026-10-13-mundo-7d/yt-original.txt` · sha256:eac4426d9051 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/fala.txt` · sha256:a666780ddf77 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-semana-foto/avatar/tempos.json` · sha256:6904d4f879a1 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/video_id.txt` · sha256:2ed9030782ec · sujo
- `edicoes/2026-10-13-semana-foto/falas.json` · sha256:cf0502b393d3 · sujo
- `edicoes/2026-10-13-semana-foto/gerar_cena.py` · sha256:fbf2a1f36e93 · sujo
- `edicoes/2026-10-13-semana-foto/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_capitais.json` · sha256:f355ea5f94e2 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_grade.json` · sha256:17c90fd9fc30 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_resumo.json` · sha256:8374f57d120d · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:62b683e1db2f · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:ed0f6b0eb2e1 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:03f32480e20e · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:402694e4b665 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/previsao7d.json` · sha256:16a240552e84 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/resumo.json` · sha256:1e1211248eaf · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/dados.md` · sha256:fadeeb411aa5 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/noticias.md` · sha256:41b9d3ba0d16 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/proposta.md` · sha256:441edcfcec14 · sujo
- `edicoes/2026-10-13-semana-foto/previa/avatar/avatar.mp4` · sha256:90020a3ccf78 · sujo
- `edicoes/2026-10-13-semana-foto/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-semana-foto/previa/avatar/tempos.json` · sha256:1fbb83e0642a · sujo
- `edicoes/2026-10-13-semana-foto/previa/build/mapa-avatar.mp4` · sha256:4e91d223cbfc · sujo
- `edicoes/2026-10-13-semana-foto/previa/cena.js` · sha256:a0e952c5feea · sujo
- `edicoes/2026-10-13-semana-foto/previa/gerar_cena.py` · sha256:fbf2a1f36e93 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/inema-design
- commit: ef73aa602c0649827ad92ee5e68960963a45cdd3 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14

### Repo do trabalho: /home/nmaldaner/projetos/wifi
- commit: e17b723028866a337e8d86965262e12512832d7e · branch: main
- arquivos sujos: 20
- impressão de todos os sujos: 89e12dcee8b3f025
- `FALHAS.md` · sha256:bfcd85de2d88 · sujo
- `LESSONS.md` · sha256:7b249b5e51b9 · sujo
- `LIMITES.md` · sha256:b6c0bc8ee0a8 · sujo
- `fila-lives7/.lock` · sha256:e3b0c44298fc · sujo
- `fila-lives7/fila.json.antigo` · sha256:8869bb8b0f30 · sujo
- `heygen-aviso/envios/aviso-teste-202610181749.jpg` · sha256:88a0ddb5462f · sujo
- `heygen-aviso/envios/aviso-teste-202610181749.jpg.envio-v3.json` · sha256:c74ed6557bc4 · sujo
- `longrun/2026-10-13-rea-es/canal.md` · sha256:51148d4a733b · sujo
- `longrun/2026-10-13-rea-es/folhas/r7e-rea-clone-tudo-es.jpg` · sha256:2b560479ca5f · sujo
- `longrun/2026-10-13-rea-es/folhas/r7e-rea-quatro-passos-es.jpg` · sha256:00c16adc1e44 · sujo
- `longrun/2026-10-13-rea-es/folhas/rea-pratico-es.jpg` · sha256:3318ea92e4c6 · sujo
- `longrun/2026-10-13-rea-es/folhas/rea-sem-travas-es.jpg` · sha256:df0a54a7cc71 · sujo
- `longrun/2026-10-13-rea-es/folhas/rea-servidor-es.jpg` · sha256:a3ed963d43e5 · sujo
- `longrun/2026-10-13-rea-es/folhas/rea-tecnico-es.jpg` · sha256:9c3cde689961 · sujo
- `longrun/2026-10-13-rea-es/logs/release-assets.json` · sha256:8ef41a7a51aa · sujo
- `move-pasta-hd8t.sh` · sha256:d4ddbaa216bd · sujo
- `move-videos-avisa.sh` · sha256:6a14eb369a1b · sujo
- `move-videos-hd8t.sh` · sha256:bc20b33646e5 · sujo
- `move-videos-lista.txt` · sha256:6c2752e3600f · sujo
- `pendencias.md` · sha256:4f79df8e7cf2 · sujo
<!-- handoff-estado:fim -->
