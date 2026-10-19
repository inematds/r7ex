"""ficha.yaml + avatar/tempos.json → cena.js do motor do eventosextremospub (mapa.html).
Mesma lógica do gerar_cena.py da edição modelo eventosextremospub/edicoes/2026-10-18-do-chat-ao-agente."""
import difflib, json, re, unicodedata
from pathlib import Path

BORDA = {"red": "rgba(255,42,31,.7)", "am": "rgba(250,204,21,.75)", "vd": "rgba(34,197,94,.7)"}
NUM = re.compile(r"\d")
MAX_LEG = 21                          # letras por bloco de legenda (23 já encosta na borda; 25 vazou)


def n(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFD", str(s).lower()).encode("ascii", "ignore").decode())


def _roteiro(t, texto):
    """troca as palavras ouvidas pelas da legenda, mantendo os tempos"""
    tok, W = texto.split(), t["palavras"]
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [n(x) for x in tok], [n(p["w"]) for p in W], autojunk=False).get_opcodes():
        if op == "equal":
            out += [{"w": tok[i1 + k], "t": W[j1 + k]["t"], "f": W[j1 + k]["f"]} for k in range(i2 - i1)]
        elif i2 > i1:
            a = W[j1]["t"] if j2 > j1 else (W[j1 - 1]["f"] if j1 else t["ini"])
            b = W[j2 - 1]["f"] if j2 > j1 else (W[j1]["t"] if j1 < len(W) else a + .3)
            d = (b - a) / (i2 - i1)
            out += [{"w": tok[i1 + k], "t": round(a + k * d, 3), "f": round(a + (k + 1) * d, 3)} for k in range(i2 - i1)]
    return out


def acha(palavras, palavra, k=1):
    achou = 0
    for p in palavras:
        if n(palavra) == n(p["w"]) or (len(n(palavra)) > 3 and n(palavra) in n(p["w"])):
            achou += 1
            if achou == k:
                return p["t"]
    return None


def montar(pasta, ficha, falas):
    pasta = Path(pasta)
    T = json.loads((pasta / "avatar/tempos.json").read_text())
    leg = {f["id"]: f["legenda"] for f in falas}
    for t in T:
        t["palavras"] = _roteiro(t, leg[t["id"]])
    F = {t["id"]: t for t in T}
    ids = [t["id"] for t in T]

    def em(fid, palavra, k=1):
        v = acha(F[fid]["palavras"], palavra, k)
        if v is None:
            raise SystemExit(f"{fid}: '{palavra}' não está na fala: " + " ".join(p["w"] for p in F[fid]["palavras"]))
        return v

    DUR = round(F[ids[-1]]["fim"] + 1.4, 2)
    BR = {"lon": -52.0, "lat": -14.0, "zoom": 3.4}       # mapa escondido atrás do fundo preto (o motor exige câmera)
    camera = [{"t": 0, **BR, "pitch": 30, "bearing": 0}, {"t": DUR, **BR, "pitch": 40, "bearing": 20}]

    telas = [{"src": "capa/preto.png", "ini": -1.0, "fim": DUR + 1, "fade": 0, "zoom": 0}]
    partes = ficha["partes"]
    for i, p in enumerate(partes):
        fid = f"f{i + 1}"
        a = -1.0 if i == 0 else F[fid]["ini"] - .1
        b = F[f"f{i + 2}"]["ini"] - .1 if i + 1 < len(partes) else DUR + 1
        if i == 0:
            src, selo, zoom = "capa/abertura-desce.png", None, .03
        elif p.get("print"):
            src, selo, zoom = f"prints/p{i + 1}-c.png", p["print"].get("selo") or "print da página", .04
        elif p.get("diagrama"):                          # diagrama animado (19/10/2026): fundo limpo, o motor desenha por cima
            src, selo, zoom = "capa/preto.png", None, 0
        else:
            src, selo, zoom = f"capa/p{i + 1}.png", "ilustração", .07
        d = {"src": src, "ini": a, "fim": b, "fade": .3, "zoom": zoom}
        # escurece a foto por baixo da legenda/painel/avatar (a vinheta do motor fica ABAIXO das telas; 19/10/2026)
        if i == 0:
            d["escurece"] = "base"                        # abertura: só a faixa de baixo (o título do topo fica intacto)
        elif selo == "ilustração":
            d["escurece"] = "foto"                        # ilustração: faixa de baixo + brilho/saturação menores
        if selo:
            d["selo"] = selo
        telas.append(d)

    paineis = []
    for i, p in enumerate(partes):
        pn = p.get("painel")
        if not pn:
            continue
        fid = f"f{i + 1}"
        a = em(fid, pn["de"]) - .1 if pn.get("de") else F[fid]["ini"]
        b = (F[f"f{i + 2}"]["ini"] if i + 1 < len(partes) else DUR) - .05
        d = {"ini": a, "fim": b, "k": pn["k"], "borda": BORDA[pn.get("borda", "am")]}
        if pn.get("itens"):
            d["itens"] = [{"t": em(fid, x[0], x[2] if len(x) > 2 else 1), "txt": x[1]} for x in pn["itens"]]
        if pn.get("contador"):
            c = pn["contador"]
            d["contador"] = {"de": c.get("de", 0), "ate": c["ate"], "dec": c.get("dec", 0), "ini": em(fid, c["em"]) - 1.0,
                             "dur": c.get("dur", 1.2), "cor": c.get("cor", "#FACC15"), "unid": c.get("unid", "")}
        if pn.get("l"):
            d["l"] = pn["l"]
        paineis.append(d)

    # diagramas (19/10/2026, pedido do Nei: "não só imagem, animações e diagramas"): fluxo | hub | terminal,
    # cada nó/linha acende na palavra falada (de)
    diagramas = []
    for i, p in enumerate(partes):
        dg = p.get("diagrama")
        if not dg:
            continue
        fid = f"f{i + 1}"
        a = F[fid]["ini"] - .1
        b = (F[f"f{i + 2}"]["ini"] if i + 1 < len(partes) else DUR) - .1
        d = {"ini": a, "fim": b, "forma": dg.get("forma", "fluxo"), "titulo": dg.get("titulo", "")}
        itens = dg.get("nos") or dg.get("linhas") or []
        d["nos"] = [{**{k: v for k, v in x.items() if k not in ("de", "k")}, "t": em(fid, x["de"], x.get("k", 1)) - .05 if x.get("de") else a + .2}
                    for x in itens]
        if dg.get("centro"):
            c = dg["centro"]
            d["centro"] = {**{k: v for k, v in c.items() if k != "de"}, "t": em(fid, c["de"]) - .05 if c.get("de") else a + .1}
        diagramas.append(d)

    ult = f"f{len(partes)}"
    cta = {"ini": em(ult, "pede"), "fim": DUR, "a": ficha["cta"]["a"], "b": ficha["cta"]["b"]}
    club = {"ini": em(ult, "inema.club"), "fim": DUR, "a": "inema.club", "b": ficha["club"]}
    fontes = [{"ini": .3, "fim": DUR, "html": ficha["fonte"]}]

    cores = {n(k): v for k, v in (ficha.get("cores") or {}).items()}
    for k in ("inemaclub", "comentarios", "link"):
        cores.setdefault(k, "#FACC15")
    legenda = []
    for t in T:
        bloco = []; ant = None
        for i, p in enumerate(t["palavras"]):
            w = p["w"]; k = n(w)
            # bloco cabe na largura: até 3 palavras e até MAX_LEG letras ("BILLION CONTEXT ENXUGANDO" vazou, 19/10)
            if bloco and len(" ".join(b["w"] for b in bloco) + " " + w) > MAX_LEG:
                legenda.append({"ini": bloco[0]["t"] - .05, "fim": ant["f"] + .12, "palavras": bloco})
                bloco = []
            ant = p
            cor = cores.get(k) or ("#FACC15" if NUM.search(k) else None)
            bloco.append({"w": w, "t": p["t"], **({"cor": cor} if cor else {})})
            if len(bloco) == 3 or w[-1:] in ".?!,:" or i == len(t["palavras"]) - 1:
                legenda.append({"ini": bloco[0]["t"] - .05, "fim": p["f"] + .12, "palavras": bloco})
                bloco = []
    for a, b in zip(legenda, legenda[1:]):
        a["fim"] = min(max(a["fim"], b["ini"]), b["ini"])

    C = {"layout": "canto", "padding_baixo": 640, "duracao": DUR, "padding_topo": 0, "marca": ficha["marca"], "selo": ficha["selo"],
         "camera": camera, "telas": telas, "hero": [], "paineis": paineis, "diagramas": diagramas, "cta": cta, "club": club, "fontes": fontes, "legenda": legenda}
    (pasta / "cena.js").write_text("window.CENA=" + json.dumps(C, ensure_ascii=False) + ";")
    return DUR, len(telas), len(paineis), len(legenda)
