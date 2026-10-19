#!/usr/bin/env python3
"""Fila de publicação do r7ex (padrão: lives7 · INEMA LOOPY): publica UM short por execução e avisa no bot v3.
Mudou de ~/projetos/wifi/fila-lives7 para dentro do r7ex em 18/10/2026 (o r7ex funciona sozinho).

Pedido do Nei (18/10/2026): "pode distribuir no lives7, mas na fila" — não subir tudo de uma vez.
Modelo: ~/projetos/wifi/fila-espanhol/fila_es.py (sem o 'liberar' e sem a trava de 15 min, que é do canal ES).
Roda pelo timer systemd `fila-lives7.timer` (9 h às 21 h, 1 a cada 2 h = 7 por dia).
Uso: fila_lives7.py            (publica o próximo)
     fila_lives7.py --status   (mostra a fila)
     fila.py --add <mp4> --nome "..." --contexto "..." [--titulo "..."] [--canal lives7]   (entra no FIM da fila)
"""
import fcntl, json, os, re, subprocess, sys, time
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FILA = AQUI / "fila.json"
LOG = AQUI / "fila.log"
YTPUBX = Path.home() / "projetos/yt-pubx"
AVISA = Path.home() / "projetos/wifi/scripts/avisa-v3.sh"
CANAL = "lives7"
HORAS = [9, 11, 13, 15, 17, 19, 21]
MAX_TENTATIVAS = 2


def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}\n")
    print(msg, flush=True)


def avisa(msg):
    h = datetime.now()
    if h.hour == 23 and 20 <= h.minute <= 55:           # janela proibida do Telegram
        time.sleep((56 - h.minute) * 60)
    subprocess.run(["bash", str(AVISA), msg], capture_output=True, timeout=60)


def proxima_hora():
    h = datetime.now().hour
    return f"{next((x for x in HORAS if x > h), HORAS[0]):02d}h"


def ler():
    return json.loads(FILA.read_text()) if FILA.exists() else []


def adicionar(argv):
    op = {"--nome": "nome", "--contexto": "contexto", "--titulo": "titulo", "--canal": "canal"}
    arq = os.path.abspath(argv[argv.index("--add") + 1])
    item = {"arquivo": arq, "estado": "pendente"}
    for k, v in op.items():
        if k in argv:
            item[v] = argv[argv.index(k) + 1]
    if not item.get("nome") or not item.get("contexto"):
        sys.exit("--nome e --contexto são obrigatórios")
    if not os.path.exists(arq):
        sys.exit(f"arquivo não existe: {arq}")
    item["id"] = re.sub(r"[^a-z0-9-]", "", Path(arq).parent.name.lower() + "-" + Path(arq).stem.lower())
    fila = ler()
    if any(x.get("arquivo") == arq for x in fila):
        sys.exit(f"já está na fila: {arq}")
    fila.append(item)
    FILA.write_text(json.dumps(fila, ensure_ascii=False, indent=1))
    pend = sum(x["estado"] == "pendente" for x in fila)
    print(f"na fila do {item.get("canal", CANAL)}: {item['id']} (posição {pend}; ~{(pend + len(HORAS) - 1) // len(HORAS)} dia(s))")


def main():
    if "--add" in sys.argv:
        return adicionar(sys.argv)
    # Só publica quando chamado SEM argumentos (o timer). Qualquer outro (--help, erro de digitação) só mostra a ajuda.
    if len(sys.argv) > 1 and "--status" not in sys.argv:
        print(__doc__ or "uso: fila.py [--status | --add <mp4> --nome ... --contexto ...]"); return
    fila = ler()
    pend = [x for x in fila if x["estado"] == "pendente"]
    if "--status" in sys.argv:
        print(f"{sum(x['estado'] == 'feito' for x in fila)} feitos, {len(pend)} pendentes, {sum(x['estado'] == 'erro' for x in fila)} com erro")
        for x in pend[:8]:
            print("  próximo:", x["id"], "-", x["nome"][:70])
        return
    if not pend:
        log("fila vazia"); return
    x = pend[0]; restantes = len(pend) - 1
    log(f"início {x['id']}")
    cmd = ["./yt-pubx", "publicar", x["arquivo"], "--canal", x.get("canal", CANAL), "--contexto", x["contexto"]]
    if x.get("titulo"):
        cmd += ["--title", x["titulo"]]
    r = subprocess.run(cmd, cwd=YTPUBX, capture_output=True, text=True, timeout=5400)
    saida = (r.stdout + r.stderr)[-1500:]
    m = re.search(r"URL: https://www.youtube.com/watch\?v=([\w-]{11})", r.stdout)
    if m:
        x["video_id"] = m.group(1); url = f"https://youtube.com/shorts/{x['video_id']}"
        t = re.search(r"T[ÍI]TULO: (.+)", r.stdout)
        if t:
            x["titulo_yt"] = t.group(1).strip()
        x["estado"], x["quando"] = "feito", datetime.now().isoformat(timespec="minutes")
        FILA.write_text(json.dumps(fila, ensure_ascii=False, indent=1))
        log(f"feito {x['id']} {url}")
        avisa(f"Fila r7ex ({x.get('canal', CANAL)}): publiquei {x.get('titulo_yt') or x['nome']}\n{url}\n" +
              (f"Faltam {restantes}. Próximo às {proxima_hora()}." if restantes else "Terminei: a fila do r7ex acabou."))
        return
    x["tentativas"] = x.get("tentativas", 0) + 1
    cota = re.search(r"uploadLimitExceeded|quotaExceeded|exceeded the number of videos", saida)
    if not cota and x["tentativas"] >= MAX_TENTATIVAS:
        x["estado"] = "erro"
    x["erro"] = saida[-400:]
    FILA.write_text(json.dumps(fila, ensure_ascii=False, indent=1))
    log(f"FALHOU {x['id']}: {saida[-300:]}")
    motivo = "limite de envio do YouTube; tento de novo no próximo horário" if cota else \
        (f"vou pular este item (tentativa {x['tentativas']})" if x["estado"] == "erro" else "tento de novo no próximo horário")
    avisa(f"Falhou: fila lives7 — {x['nome'][:80]} — {motivo}.\n{saida.strip().splitlines()[-1][:200] if saida.strip() else ''}")


if __name__ == "__main__":
    with open(AQUI / ".lock", "w") as lk:
        try:
            fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("outra execução em andamento"); sys.exit(0)
        main()
