| 2026-10-19 | Capa divulga sem faixa no último celular; p3 com timeline em vez de mensagem | Edição pontual via image_gen corrigiu telas | prompt |
| 2026-10-19 | Imagens em systemd usaram Codex 0.116 do /usr/bin | PATH explícito com ~/.npm-global/bin (0.163) | infra |
| 2026-10-19 | image_gen acrescentou marca no notebook e robôs nas cenas p3/p4 | Edição pontual removeu elementos extras, preservando cenas e texto | prompt |
# FALHAS — r7ex

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-19 | Print do guia (skills15) saiu todo preto com âncora #numeros e a folha mostrou moldura vazia; contador sem "MILHÃO" | print sem âncora + unid com MILHÃO; falta portão: print quase uniforme (desvio baixo) reprovar no `imagens` | infra + prompt |
| 2026-10-19 | Dois envios ao estúdio HeyGen no mesmo segundo: o 2º caiu com "Opening in existing browser session" (r7e-para-r7ex) | trava atômica (mkdir) no heygen-perfil.mjs, da ferramenta: ~/.cache/inemaccbot/heygen-estudio.trava (commit 592659c) | infra |
| 2026-10-19 | `fila.py --help` publicou o próximo short do lives7 fora do horário (argumento desconhecido = publicar) | argumento que não seja --add/--status só mostra a ajuda | infra |
