| 2026-10-25 | VPS da Tiza sem GPU: render a ~10 s por quadro (3 h por reel) — o mapa deck.gl (WebGL) era pintado em software a cada quadro, mesmo coberto pelas telas | `R7X_SEM_MAPA=1` esconde `#mapa` (0,01% da tela) → 0,25 s/quadro | infra |
| 2026-10-25 | transcrição em CPU (faster-whisper) caía com `open() got an unexpected keyword argument metadata_errors` (PyAV novo) | decodificar o áudio pelo ffmpeg e passar o array ao modelo | infra |
| 2026-10-23 | r7ex hackers-atacam parado 1 dia: avatar pronto no HeyGen mas `avatar-conferir` com pasta relativa dava ENOENT (node roda em heygen/) e o vigia lia como falha | `avatar_conferir` usa `Path(pasta).resolve()` | infra |
| 2026-10-21 | refazer só 1 imagem (volante do musk): o Codex refez TODAS e trocou a abertura aprovada por uma com título menor | `cmd_imagens` só pede as que faltam + "não mexa em outros arquivos" | prompt |
| 2026-10-21 | Robô e volante gerados invadiram metade inferior | edição image_gen reduzindo assunto e ancorando no topo | prompt |
| 2026-10-21 | Capa gerada avançou com o robô sobre a metade inferior | Reduzir o robô via image_gen mantendo o título | prompt |
| 2026-10-21 | remontar rust-fim-python com o MESMO avatar falhou: "fala f6 não achada" (Whisper retranscreveu diferente) | retempo reaproveita tempos.json se for mais novo que o avatar.mp4 e as falas forem iguais | infra |
| 2026-10-21 | 8 de 35 reels parados na produção; metade por estilo (logo faltando, impacto, encostar de leve) e 3 por `**` cru no painel (bigtech-ipo/troco/ipo-b); rust-fim-python parou por falta do logo do Copilot no gancho | revisor em 2 níveis (defeito para; sugestão segue com tarja 🟥 SUGESTÃO no v3); crítico do plano não bloqueia por logo; `cena.sem_markdown` tira `**` | prompt + infra |
| 2026-10-21 | reel thwaites: a caixa da pergunta do fecho só entrava em "pede" e a fala termina em "me pede o link." → apareceu <1 s e o revisor reprovou | `cta.de` na ficha escolhe a deixa da caixa (padrão "pede"); thwaites usa "cidade" | prompt |
| 2026-10-21 | refazer reel com fala nova: o estúdio achou o vídeo ANTIGO já gerado com o mesmo título (R7X-<pasta>), tratou como rascunho e travou (waitForURL 60 s) | `avatar/ESTUDIO_SUFIXO.txt` (ex.: v2) muda o título no estúdio sem mexer na ficha | infra |
| 2026-10-21 | reel plano-90-dias (ficha de 19/10, antes do D15) parou na produção: sem `prende` e nota 7; o crítico também barrou Stanford "sem logo", e Stanford é a fonte, não um produto | ficha reescrita (ângulo "teste de 3 segundos"); critico-plano.md: instituição-fonte não precisa de logo (PADRAO §1). Crítico oscila ±1 entre rodadas (7,3 → 7,1 → 7,4) | prompt |
| 2026-10-20 | `enviar` ao bot v3 falhou uma vez (exit 1 do enviar_bot_v3.mjs) no reel feudo-servo-l3, num lote de 3 envios seguidos | reenviar isolado funcionou; proteção: 1 retry automático no cmd_enviar | infra |
| 2026-10-20 | montagem do reel ia-novembro caiu com KeyError: 'em' (contador sem a palavra de entrada) e o aviso veio cortado ("a") | `checar` agora reprova contador sem `em` | prompt |
| 2026-10-20 | Capa gerou Transformer em vez de humanoide industrial | Especificar visor preto oval, painéis brancos e excluir Optimus Prime no image_gen | prompt |
| 2026-10-20 | 3 reels pararam de madrugada (fisioterapia, plano-90-dias) por memória cheia (NVRM NO_MEMORY 03:04–03:13; vários renders + flux + inemaimg 30 GB juntos) e o aviso veio cortado ("og:") | montagem com falha passageira (memória/tempo) tenta mais 2 vezes, 10 e 20 min depois, antes de avisar; erro do render mostra a linha do erro | infra |
| 2026-10-20 | image_gen incluiu pessoa não solicitada em p5 | Edição removeu pessoa e explicitou notebook sozinho, sem humanos | prompt |
| 2026-10-20 | render do reel atende-fisioterapia travou 53 min ("Failed to create WebGL context" quando um whisper_gpu_worker segurava a GPU) e parou toda a fila | `timeout 1200` no render.mjs do compor_avatar.sh; matar o render e `--retomar` | infra |
| 2026-10-20 | Capa atende-nutricao veio com livros/caneta extras e celular abaixo da metade | Edição via image_gen removendo extras e subindo composição | prompt |
| 2026-10-20 | 5 reels do sobreviver-ia parados na montagem: Codex "out of credits" e o `r7ex.py imagens` só usa Codex | reserva: cenas no flux2-klein (inemaimg :8000) + título da abertura no Pillow, salvas em `capa/` antes do `--retomar` (o r7ex pula o Codex se as imagens existem) | infra |
| 2026-10-19 | reel dev-futuro parou na montagem: `whisper.py` chamava `log()` inexistente quando o whisper residente caía | trocar por `print` no fallback | infra |
| 2026-10-20 | 4 reels (3 bigtech + ia-de-elite) parados: `claude -p` do revisor falhou de passagem ("substring not found") e o item parou de vez | revisor com erro tenta de novo no próximo ciclo (até 3 vezes) antes de parar | infra |
| 2026-10-19 | reel fim-capitalismo parou na montagem: contador `em: "48 bilhões"` (2 palavras) não casa com a legenda, e o `checar` deixou passar | `checar` recusa `contador.em` com espaço | prompt |
| 2026-10-19 | Capa divulga sem faixa no último celular; p3 com timeline em vez de mensagem | Edição pontual via image_gen corrigiu telas | prompt |
| 2026-10-19 | Imagens em systemd usaram Codex 0.116 do /usr/bin | PATH explícito com ~/.npm-global/bin (0.163) | infra |
| 2026-10-19 | image_gen acrescentou marca no notebook e robôs nas cenas p3/p4 | Edição pontual removeu elementos extras, preservando cenas e texto | prompt |
# FALHAS — r7ex

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-19 | Imagem p2 de seo-formacao gerou símbolo parecido com logotipo apesar da restrição | Edição localizada via image_gen para remover símbolo e caracteres do celular | prompt |
| 2026-10-19 | Revisor reprovou 10 de 12 reels r7ex da fila: legenda em cima do texto do print (cartão alto demais) e legenda vazando (saas, tres-estagios) | cartão do print até y 1090 (pecas.print_card) + MAX_LEG; refazer cena+render dos 10 com o OK do Nei | infra |
| 2026-10-19 | Legenda "BILLION CONTEXT ENXUGANDO" vazou da tela (skills15); passou na minha leitura da folha, o revisor claude -p pegou | bloco de legenda quebra também por largura (MAX_LEG 21) + revisor automático na produção | infra |
| 2026-10-19 | Print do guia (skills15) saiu todo preto com âncora #numeros e a folha mostrou moldura vazia; contador sem "MILHÃO" | print sem âncora + unid com MILHÃO; falta portão: print quase uniforme (desvio baixo) reprovar no `imagens` | infra + prompt |
| 2026-10-19 | Dois envios ao estúdio HeyGen no mesmo segundo: o 2º caiu com "Opening in existing browser session" (r7e-para-r7ex) | trava atômica (mkdir) no heygen-perfil.mjs, da ferramenta: ~/.cache/inemaccbot/heygen-estudio.trava (commit 592659c) | infra |
| 2026-10-19 | `fila.py --help` publicou o próximo short do lives7 fora do horário (argumento desconhecido = publicar) | argumento que não seja --add/--status só mostra a ajuda | infra |

| 2026-10-20 | Capa feudo com mão humana ultrapassando metade superior | editar via image_gen com mão entrando pela lateral e coordenadas de composição | prompt |
