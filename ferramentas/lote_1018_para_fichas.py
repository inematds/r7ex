#!/usr/bin/env python3
"""Converte os 7 reels de 18/10/2026 (roteiros do reel7etapas + lote do eventosextremospub) em fichas do r7ex,
para refazer pelo r7ex com imagens novas e o MESMO avatar (pedido do Nei: "faça novamente ... não será a mesma cópia,
mas vai usar o avatar que já está pronto ... manda para o lives3").
uso: python3 ferramentas/lote_1018_para_fichas.py   → edicoes/2026-10-18-<slug>-v2/ficha.yaml (+ avatar/AVATAR_DE.txt)"""
import importlib.util, json, re
from pathlib import Path

import yaml

R = Path(__file__).resolve().parent.parent
R7 = Path.home() / "projetos/reel7etapas/edicoes"
spec = importlib.util.spec_from_file_location("lote", R7 / "ev-lote-1018.py")
src = (R7 / "ev-lote-1018.py").read_text()
src = src[:src.index("PRINTS = {")]          # só os dados (R, COMUM); sem executar o lote
ns = {"__file__": str(R7 / "ev-lote-1018.py")}
exec(compile(src.replace("RAW = Path(sys.argv[1])", "RAW = None").replace("import ev_util  # noqa: E402", ""), "lote", "exec"), ns)
LOTE, COMUM = ns["R"], ns["COMUM"]

URL = {"prof2027-c.png": "https://inematds.github.io/profissional2027x/", "prof2030-c.png": "https://inematds.github.io/prof2030/",
       "chat72-c.png": "https://inematds.github.io/do-chat-ao-agente-v72/", "emp27-c.png": "https://inematds.github.io/empresas-2027-v62/landing.html",
       "diga-c.png": "https://inematds.github.io/diga-o-que-importa/guia/", "const-c.png": "https://inematds.github.io/constituicao-agentes-v62/landing.html",
       "club-c.png": "https://inema.club"}
PLANO = {
    "ferramentas": ("quem vive testando ferramenta nova de IA e sente que está ficando para trás", "parar de correr atrás de app e aprender a pedir", "provocação: quem caça app é superficial; tudo está no GitHub", 8),
    "2027": ("profissional que acha que precisa virar programador para ganhar com IA", "faturar em 2027 ajudando empresas", "provocação: quem fatura em 2027 não é quem cria software", 8),
    "saas": ("quem paga assinatura de software ou aposta em criar um SaaS", "não apostar no formato que está morrendo", "medo: o SaaS está morrendo e tem gente apostando tudo nele", 8),
    "chat": ("quem usa ChatGPT copiando e colando", "sair na frente do colega fazendo o agente produzir", "provocação: você ainda copia e cola?", 8),
    "demissao": ("gerente ou executivo que ainda não lida com agentes de IA", "não estar na fila da demissão", "medo: demissão em massa de gerentes e executivos", 9),
    "gestor": ("gestor de empresa pequena ou média", "chefiar uma equipe com agentes sem medo", "novidade: seu novo funcionário não é gente", 8),
}
DESTINO = {"ferramentas": "https://inema.club", "2027": URL["prof2027-c.png"], "saas": URL["prof2030-c.png"], "chat": URL["chat72-c.png"],
           "demissao": URL["emp27-c.png"], "gestor": URL["diga-c.png"]}


def frases(t):
    return [s for s in re.split(r"(?<=[.?!])\s+", t.strip()) if s]


for slug, c in LOTE.items():
    rot = yaml.safe_load((R7 / f"2026-10-18-{c['r7']}/roteiro.yaml").read_text())
    fs = frases(rot["fala"]); k = 0; partes = []
    imgs = dict(c["imgs"])
    for i, g in enumerate(c["grupos"]):
        fala = " ".join(fs[k:k + g]); k += g
        tela = c["telas"][i][0]
        p = {"etapa": ["gancho", "medo", "desejo", "facilidade", "descoberta", "beneficio", "comentario"][i], "fala": fala}
        if i > 0:
            nome = tela.split("/")[-1]
            if tela.startswith("prints/"):
                p["print"] = {"url": URL[nome], "selo": c["telas"][i][2] if len(c["telas"][i]) > 2 else "print da página"}
            else:
                p["imagem"] = imgs[nome]
        pn = next((x for x in c["paineis"] if (x["de"] if isinstance(x["de"], str) else x["de"][0]) == f"f{i + 1}"), None)
        if pn:
            d = {"k": pn["k"]}
            if not isinstance(pn["de"], str):
                d["de"] = pn["de"][1]
            if pn.get("borda"):
                d["borda"] = pn["borda"]
            if pn.get("itens"):
                d["itens"] = [[x[1], x[2]] + ([x[3]] if len(x) > 3 else []) for x in pn["itens"]]
            if pn.get("contador"):
                cc = dict(pn["contador"]); cc["em"] = cc["em"][1]; d["contador"] = cc
            if pn.get("l"):
                d["l"] = pn["l"]
            p["painel"] = d
        partes.append(p)
    a, b, cor, cena = c["abre"]
    pessoa, quer, gancho, nota = PLANO[slug]
    tit = rot["titulo_post"]; tit = tit if "#shorts" in tit else tit + " #shorts"
    ctx = rot.get("contexto_youtube") or f"Short vertical do INEMA.CLUB (Nei Maldaner): {rot['tema']}. Material no inema.club. CTA: peça o link nos comentários."
    ficha = {"slug": f"{slug}-v2", "tema": rot["tema"],
             "plano": {"pessoa": pessoa, "quer": quer, "gancho": gancho, "nota": nota, "destino": DESTINO[slug]},
             "marca": c["marca"], "selo": c["selo"], "fonte": c["fonte"],
             "abertura": {"branco": a, "destaque": b, "cor": "vermelho" if "vermelho" in cor else "amarelo",
                          "cena": cena + " (nova composição, ângulo diferente de qualquer versão anterior)"},
             "trocas": c["troca"], "partes": partes,
             "cta": {"a": c["cta"][0], "b": c["cta"][1]}, "club": c["club"], "cores": c["cores"],
             "publicar": {"fila": "lives3", "titulo": tit, "contexto": ctx}}
    E = R / "edicoes" / f"2026-10-18-{slug}-v2"; (E / "avatar").mkdir(parents=True, exist_ok=True)
    (E / "ficha.yaml").write_text(yaml.safe_dump(ficha, allow_unicode=True, sort_keys=False, width=140))
    (E / "avatar/AVATAR_DE.txt").write_text(str(R7 / f"2026-10-18-{c['r7']}/avatar/avatar.mp4") + "\n")
    print(slug, "→", E.name)

# o hacker: a ficha do modelo, com imagens novas e destino lives3
f = yaml.safe_load((R / "modelo/ficha.yaml").read_text())
f["slug"] = "hacker-v2"; f["publicar"]["fila"] = "lives3"
f["abertura"]["cena"] += " (nova composição, ângulo diferente de qualquer versão anterior)"
E = R / "edicoes/2026-10-18-hacker-v2"; (E / "avatar").mkdir(parents=True, exist_ok=True)
(E / "ficha.yaml").write_text(yaml.safe_dump(f, allow_unicode=True, sort_keys=False, width=140))
(E / "avatar/AVATAR_DE.txt").write_text(str(R7 / "2026-10-18-opencode-v3/avatar/avatar.mp4") + "\n")
print("hacker →", E.name)
