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
