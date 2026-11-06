#!/bin/bash
# Espera o agente do explicavideo submeter o avatar dele primeiro (flag), até 90 min; depois põe este r7ex na produção.
FLAG=/home/nmaldaner/projetos/wifi/longrun/2026-11-05-protegendo-seus-repos/heygen-explicavideo-submetido.flag
ED=/home/nmaldaner/projetos/r7ex/edicoes/2026-11-05-protegendo-seus-repos
LOG=$ED/espera-explicavideo.log
for i in $(seq 1 90); do
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') flag encontrada" >> "$LOG"; break; }
  sleep 60
done
[ -f "$FLAG" ] || echo "$(date '+%F %T') 90 min sem flag; sigo (a trava do estúdio serializa)" >> "$LOG"
sleep 120   # folga para o envio do explicavideo terminar de entrar no estúdio
cd /home/nmaldaner/projetos/r7ex && python3 producao/producao.py --add "$ED" >> "$LOG" 2>&1
echo "$(date '+%F %T') producao --add rc=$?" >> "$LOG"
