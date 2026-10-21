#!/usr/bin/env python3
"""r7ex — reel viral do INEMA: roteiro de 7 etapas (r7e) + acabamento de telejornal (motor copiado do eventosextremospub).
Padrão em PADRAO.md · explicação completa em README.md · ficha de exemplo em modelo/ficha.yaml.

  python3 r7ex.py novo <slug>             cria edicoes/<data>-<slug>/ficha.yaml (copia o modelo para editar)
  python3 r7ex.py checar <pasta>          portão da ficha: 7 partes, 550–700 caracteres, palavras dos painéis na fala, `prende` por parte
  python3 r7ex.py plano <pasta>           crítico de viralidade (claude -p): sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6 antes do avatar (D15)
  python3 r7ex.py avatar <pasta> [--de <mp4>]   avatar no estúdio do HeyGen (precisa de avatar/APROVADO_HEYGEN), ou reaproveita um mp4
  python3 r7ex.py imagens <pasta>         Codex desenha a abertura (com o título) e as imagens; prints reais das páginas
  python3 r7ex.py cena <pasta>            falas.json + tempo de cada palavra do avatar + cena.js
  python3 r7ex.py render <pasta>          monta o vídeo (tela :99) → <pasta>/video.mp4
  python3 r7ex.py revisar <pasta>         folha de 12 quadros → <pasta>/build/folha.jpg (LER antes de enviar)
  python3 r7ex.py enviar <pasta>          manda ao bot v3
  python3 r7ex.py fila <pasta>            entra no fim da fila do canal (fila/fila.py; padrão lives7)
  python3 r7ex.py fazer <pasta> [--de <mp4>]   (ou avatar/AVATAR_DE.txt na pasta) checar → imagens + avatar → cena → render → revisar (enviar/fila depois de ler a folha)
  python3 r7ex.py avatar-enviar <pasta>   só manda a fala ao estúdio (grava avatar/video_id.txt), sem esperar
  python3 r7ex.py avatar-conferir <pasta> uma conferência no HeyGen (leitura): imprime pronto | processando
  Produção sozinha (sem sessão aberta): python3 producao/producao.py --add <pasta>  (ver producao/README.md)
"""
import concurrent.futures as cf
import datetime as dt
import json, os, re, shutil, subprocess, sys
from pathlib import Path

import yaml

R = Path(__file__).resolve().parent
sys.path.insert(0, str(R))
from r7ex import cena as CENA, pecas, retempo as RT  # noqa: E402

PERFIL = Path.home() / ".cache/inemaccbot/perfil-heygen"     # perfil do estúdio (compartilhado: tem fila própria)
TEMPLATE_HEYGEN = "TEMPLATE-AVATAR16"
TELA = ":99"                                                  # nunca a tela do Nei (memória heygen-login-na-tela)
TROCAS_PADRAO = {"inema ponto club": "inema.club", "dois mil e vinte e sete": "2027", "dois mil e trinta": "2030",
                 "dois mil e vinte e seis": "2026"}
# Imagem LIMPA (Nei, 19/10/2026: "saturadas, muita informação, não é como o eventosextremos"): um assunto só, fundo liso,
# luz neutra; o amarelo é do texto/painel (regra "imagens sem amarelado" de 12/10). A metade de baixo fica sob legenda+painel+avatar.
# 2ª calibragem (Nei, 19/10/2026: o limpo "ficou limpo demais, não tem impacto"): continua UM assunto e fundo liso,
# mas com luz dramática de cinema no assunto — o impacto vem da luz e da ação, não da quantidade de coisas.
ESTILO = ("Estilo foto cinematográfica realista de impacto, como pôster de filme: UM único objeto ou assunto principal, grande, "
          "na metade de CIMA do quadro, numa AÇÃO ou estado dramático (quebrando, acendendo, se abrindo, sendo puxado); "
          "luz dramática: foco de luz forte de cima ou contraluz com recorte brilhante na borda, sombras profundas, contraste alto. "
          "A luz do assunto pode ser amarela (#FACC15) ou, só se houver perigo, vermelha (#ff2a1f); o resto da cena é fundo "
          "liso e escuro (preto #0c0c10), sem outros objetos — a metade de baixo escura e vazia. Sem objetos espalhados, sem "
          "pilhas, sem chuva de partículas ou papéis, sem hologramas. "
          "Sem logotipo de empresa (o logo real do produto é colado depois, nunca desenhado — D13), sem marca d'água, sem pessoas reconhecíveis (rostos de lado, na sombra ou de costas). "
          "Robô, quando houver: humanoide industrial estilo Tesla Optimus, com visor preto na frente, nunca fofo ou cartoon. "
          "Nenhum texto nas imagens, EXCETO na abertura.png.")
COR = {"vermelho": "vermelho #ff2a1f", "amarelo": "amarelo #FACC15"}


def log(*a):
    print("[r7ex]", *a, flush=True)


def falha(msg):
    sys.exit(f"[r7ex] REPROVOU: {msg}")


def ficha(pasta):
    p = Path(pasta).resolve()
    f = yaml.safe_load((p / "ficha.yaml").read_text())
    return p, f


def fala_total(f):
    return " ".join(x["fala"].strip() for x in f["partes"])


def falas(p, f):
    out = []
    for i, x in enumerate(f["partes"]):
        leg = x.get("legenda") or x["fala"].strip()
        if not x.get("legenda"):
            for a, b in {**TROCAS_PADRAO, **(f.get("trocas") or {})}.items():
                leg = leg.replace(a, b)
        out.append({"id": f"f{i + 1}", "fala": x["fala"].strip(), "legenda": leg})
    (p / "falas.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    return out


# ------------------------------------------------------------------ comandos
def cmd_novo(slug):
    p = R / "edicoes" / f"{dt.date.today().isoformat()}-{slug}"
    if (p / "ficha.yaml").exists():
        sys.exit(f"já existe: {p / 'ficha.yaml'}")
    (p / "avatar").mkdir(parents=True, exist_ok=True)
    txt = (R / "modelo/ficha.yaml").read_text().replace("slug: hacker", f"slug: {slug}", 1)
    (p / "ficha.yaml").write_text(txt)
    log("criado", p / "ficha.yaml", "— reescreva plano, abertura, as 7 partes, CTA e publicar (modelo: o reel do hacker)")


def cmd_checar(pasta):
    p, f = ficha(pasta)
    erros = []
    if len(f.get("partes") or []) != 7:
        erros.append(f"são {len(f.get('partes') or [])} partes; o padrão é 7")
    tot = fala_total(f)
    teto = min(int(f.get("fala_max") or 720), 900)   # reel de lista de notícias (vários produtos): até 900 (~50 s), com motivo (21/10/2026)
    if f.get("fala_max") and not f.get("fala_max_motivo"):
        erros.append("fala_max sem fala_max_motivo (por que este reel precisa de mais fala)")
    if not 550 <= len(tot) <= teto:
        if (p / "avatar/AVATAR_DE.txt").exists() or (p / "avatar/avatar.mp4").exists():   # avatar já gravado: a fala não muda
            log(f"aviso: fala com {len(tot)} caracteres (padrão 550–700), aceita porque o avatar já existe")
        else:
            erros.append(f"fala com {len(tot)} caracteres (padrão 550–700; teto desta ficha {teto})")
    if "inema ponto club" not in f["partes"][-1]["fala"] or "pede" not in f["partes"][-1]["fala"]:
        erros.append("a parte 7 precisa de 'inema ponto club' e 'me pede o link' (CTA fixo)")
    if (f.get("plano") or {}).get("nota", 0) < 8:
        erros.append("nota de potencial < 8: troque o ângulo ou o tema (PADRAO.md §1, D15)")
    for k in ("branco", "destaque", "cena"):
        if not (f.get("abertura") or {}).get(k):
            erros.append(f"abertura sem '{k}'")
    for i, x in enumerate(f["partes"]):
        texto = CENA.n(x.get("legenda") or x["fala"])
        if i > 0 and not (x.get("imagem") or x.get("print") or x.get("diagrama") or x.get("logos")):
            erros.append(f"parte {i + 1} sem imagem, logos, print nem diagrama")
        dg = x.get("diagrama") or {}
        if dg and dg.get("forma", "fluxo") not in ("fluxo", "hub", "terminal"):
            erros.append(f"parte {i + 1}: diagrama.forma deve ser fluxo, hub ou terminal")
        if dg and not 2 <= len(dg.get("nos") or dg.get("linhas") or []) <= 6:
            erros.append(f"parte {i + 1}: diagrama com 2 a 6 nós/linhas")
        if not str(x.get("prende") or "").strip():   # D15: por que um desconhecido continua aqui
            erros.append(f"parte {i + 1} sem 'prende:' (por que um desconhecido para e continua nesta parte)")
        for lg in sum(([y] if "id" in y else y.get("junto", []) for y in x.get("logos") or []), []):
            try:
                pecas.logo_png(lg["id"])
            except SystemExit as e:
                erros.append(f"parte {i + 1}: {e}")
        lgs = x.get("logos") or []
        if len(lgs) > 2 and not all(lg.get("de") for lg in lgs):
            erros.append(f"parte {i + 1}: mais de 2 logos só com 'de' em cada um (uma tela por produto, troca na palavra)")
        if len(lgs) > 4:
            erros.append(f"parte {i + 1}: no máximo 4 produtos numa parte")
        pb = x.get("painel") or {}
        if bool(pb.get("contador")) + bool(pb.get("titulo") or pb.get("logo")) > 1:   # logo + valor = uma coisa (marca e número)
            erros.append(f"parte {i + 1}: embaixo só UMA coisa — titulo, contador OU logo (logo + titulo juntos valem como um) (D14)")
        if pb.get("logo"):
            try:
                pecas.logo_png(pb["logo"])
            except SystemExit as e:
                erros.append(f"parte {i + 1}: {e}")
        if len((x.get("lista") or {}).get("itens") or []) > 4:
            erros.append(f"parte {i + 1}: lista com mais de 4 itens")
        if re.search(r"\d", x["fala"]):
            erros.append(f"parte {i + 1}: número em algarismo na fala (o avatar lê errado): escreva por extenso e use 'trocas'")
        pn = x.get("painel") or {}
        em = str((pn.get("contador") or {}).get("em") or "")
        if pn.get("contador") and not em.strip():   # sem 'em' a montagem cai com KeyError (ia-novembro, 20/10)
            erros.append(f"parte {i + 1}: contador sem 'em' (a palavra da fala em que o número entra)")
        if " " in em.strip():   # a montagem casa o contador com UMA palavra da legenda (fim-capitalismo, 19/10)
            erros.append(f"parte {i + 1}: contador.em '{em}' tem mais de uma palavra; use só o número (ex.: '48')")
        palavras = [pn.get("de")] + [it[0] for it in pn.get("itens", [])] + [(pn.get("contador") or {}).get("em")]
        palavras += [it[0] for it in (x.get("lista") or {}).get("itens", [])]
        palavras += [lg.get("de") for lg in x.get("logos") or []]
        palavras += [it.get("de") for it in (dg.get("nos") or dg.get("linhas") or [])] + [(dg.get("centro") or {}).get("de")]
        for w in palavras:   # todo marcador de tempo casa com UMA palavra (6 reels das formações pararam na montagem, 20/10)
            if w and " " in str(w).strip() and str(w) != em:
                erros.append(f"parte {i + 1}: marcador '{w}' (de/itens) tem mais de uma palavra; use uma só (ex.: o número)")
        leg = x.get("legenda") or x["fala"]
        for a, b in {**TROCAS_PADRAO, **(f.get("trocas") or {})}.items():
            leg = leg.replace(a, b)
        for w in filter(None, palavras):
            if CENA.n(w) not in CENA.n(leg):
                erros.append(f"parte {i + 1}: '{w}' do painel/diagrama não está na fala/legenda")
    if not any(x.get("print") for x in f["partes"]):
        erros.append("nenhum print real (PADRAO.md: pelo menos 1)")
    if erros:
        falha("\n  - " + "\n  - ".join(erros))
    log(f"ficha OK: 7 partes, {len(tot)} caracteres, plano nota {f['plano']['nota']}")


def plano_aprovado(c):
    """D15 calibrado (21/10/2026): sem bloqueios objetivos E gancho ≥ 8 E média ≥ 7,5 E nenhuma parte < 6.
    (o 1º desenho, gancho ≥ 9 e todas ≥ 8, não convergiu: o crítico oscila ±1 e sempre acha algo — ia-novembro-v2, 8 rodadas)"""
    n = c["notas"]
    return not c.get("bloqueios") and n[0] >= 8 and sum(n) / len(n) >= 7.5 and min(n) >= 6


def cmd_plano(pasta):
    """D15 (Nei, 20/10/2026): "isso prende alguém, isso engaja alguém? validar as 7 etapas, o objetivo é ser viral".
    Crítico (claude -p, assinatura) dá nota por parte e lista bloqueios objetivos; regra em plano_aprovado().
    Resultado em plano-critica.json com o hash da ficha (mudou a ficha, critica de novo; o veredito é recalculado na leitura)."""
    import hashlib
    p, f = ficha(pasta)
    h = hashlib.sha1((p / "ficha.yaml").read_bytes()).hexdigest()
    arq = p / "plano-critica.json"
    c = json.loads(arq.read_text()) if arq.exists() else {}
    if c.get("hash") != h:
        r = subprocess.run(["claude", "-p", "--output-format", "json", "--allowedTools", "Read", "--",
                            (R / "producao/critico-plano.md").read_text()], cwd=p, capture_output=True, text=True, timeout=900,
                           stdin=subprocess.DEVNULL)
        try:
            res = json.loads(r.stdout)["result"].strip()
            c = json.loads(res[res.index("{"): res.rindex("}") + 1])
            c["notas"] = [int(x["nota"]) for x in sorted(c["partes"], key=lambda x: x["n"])]
            assert len(c["notas"]) == 7
        except Exception as e:
            falha(f"crítico do plano não respondeu direito: {str(e)[:200]} {r.stderr[-200:]}")
        c["hash"] = h
        arq.write_text(json.dumps(c, ensure_ascii=False, indent=1))
    n = c["notas"]
    log("plano: notas " + " · ".join(f"{i + 1}:{x}" for i, x in enumerate(n)) + f" (média {sum(n) / 7:.1f})"
        + (f" · bloqueios: {len(c['bloqueios'])}" if c.get("bloqueios") else "") + f" — {c.get('resumo', '')}")
    if not plano_aprovado(c):
        itens = [f"BLOQUEIO: {b}" for b in c.get("bloqueios") or []]
        itens += [f"parte {x['n']} ({x['nota']}): {x.get('melhorar') or x.get('porque')}" for x in c["partes"] if x.get("melhorar")]
        falha("plano não passou (D15: sem bloqueios, gancho ≥ 8, média ≥ 7,5, nenhuma < 6) — reescreva:\n  - " + "\n  - ".join(itens))
    log("plano aprovado")
    return c


def avatar_enviar(pasta):
    """manda a fala ao estúdio do HeyGen (fila/trava do estúdio) e grava avatar/video_id.txt; não espera o render"""
    p, f = ficha(pasta); av = p / "avatar"; av.mkdir(exist_ok=True)
    if (av / "avatar.mp4").exists() or (av / "video_id.txt").exists():
        return
    if not (av / "APROVADO_HEYGEN").exists():
        falha("falta avatar/APROVADO_HEYGEN (o HeyGen só roda com o OK do Nei para esta produção)")
    cmd_checar(pasta); cmd_plano(pasta)                 # D15: só grava avatar de roteiro que prende
    falas(p, f)
    (av / "fala.txt").write_text(fala_total(f) + "\n")
    with open(av / "studio.log", "w") as lg:
        subprocess.run(["node", "heygen-studio.mjs", "--titulo", f"R7X-{p.name}" + (f"-{(av / 'ESTUDIO_SUFIXO.txt').read_text().strip()}" if (av / 'ESTUDIO_SUFIXO.txt').exists() else ""), "--fala-arquivo", av / "fala.txt",
                        "--perfil", PERFIL, "--template", TEMPLATE_HEYGEN], cwd=R / "heygen", env=dict(os.environ, DISPLAY=TELA),
                       stdout=lg, stderr=subprocess.STDOUT, timeout=12000)
    s = (av / "studio.log").read_text()
    if "ERRO:" in s:
        falha("estúdio: " + s[s.index("ERRO:"):][:200] + "  (sessão caiu? abra o login na tela do Nei — README §HeyGen)")
    m = re.search(r"create-v4/([0-9a-f]{32})", s)
    if not m:
        falha("estúdio não devolveu o id (avatar/studio.log)")
    (av / "video_id.txt").write_text(m.group(1))
    log("avatar enviado ao estúdio:", m.group(1))


def avatar_conferir(pasta, minutos=0.02):
    """confere o avatar no HeyGen (leitura) e baixa se pronto → 'pronto' | 'processando'; erro do HeyGen = falha.
    minutos=0.02 = uma conferência só (para a produção); o fazer manual espera até 290 min."""
    av = Path(pasta) / "avatar"
    if (av / "avatar.mp4").exists():
        return "pronto"
    r = subprocess.run(["node", "heygen-estudio-baixar.mjs", "--id", (av / "video_id.txt").read_text().strip(),
                        "--saida", av / "avatar.mp4", "--minutos", str(minutos), "--intervalo", "1" if minutos < 1 else "60"],
                       cwd=R / "heygen", capture_output=True, text=True, timeout=int(minutos * 60) + 1200)
    if r.returncode == 0:
        return "pronto"
    if r.returncode == 4:
        return "processando"
    falha("avatar no HeyGen: " + (r.stdout + r.stderr)[-300:])


def cmd_avatar(pasta, de=None):
    p, f = ficha(pasta); av = p / "avatar"; av.mkdir(exist_ok=True)
    falas(p, f)
    if de:
        shutil.copy(de, av / "avatar.mp4")
        (av / "APROVADO_HEYGEN").write_text(f"Reaproveita o avatar {de} (nenhuma geração nova no HeyGen).\n")
        log("avatar reaproveitado de", de)
    elif not (av / "avatar.mp4").exists():
        if not (av / "APROVADO_HEYGEN").exists():
            falha("falta avatar/APROVADO_HEYGEN (o HeyGen só roda com o OK do Nei para esta produção)")
        avatar_enviar(pasta)
        if avatar_conferir(pasta, minutos=290) != "pronto":
            falha("download do avatar: tempo esgotado esperando o HeyGen")
    d, sem = RT.retempo(p)
    log(f"avatar {d:.1f} s · fala × roteiro {sem:.0%}")
    if sem < 0.90:
        falha(f"o avatar não fala o roteiro ({sem:.0%} < 90%)")


def cmd_imagens(pasta):
    p, f = ficha(pasta)
    capa, prints = p / "capa", p / "prints"; capa.mkdir(exist_ok=True); prints.mkdir(exist_ok=True)
    pecas.preto(capa / "preto.png")
    a = f["abertura"]
    linhas = [f"1. abertura.png — capa de impacto: {a['cena']}. Texto ESCRITO DENTRO da arte, grande, em português, fonte bold sem "
              f"serifa: no topo, branco, \"{a['branco']}\"; logo abaixo, maior, em {COR.get(a.get('cor', 'amarelo'), a.get('cor'))}, "
              f"\"{a['destaque']}\". Todo o texto na METADE DE CIMA da imagem; a metade de baixo sem texto. Confira a grafia exata, com acentos."]
    nome = {}                                            # D13: parte com logos → o Codex faz só o fundo, o logo real é colado
    for i, x in enumerate(f["partes"][1:], 2):
        if x.get("imagem"):
            nome[i] = f"p{i}-fundo.png" if x.get("logos") else f"p{i}.png"
            extra = (" Deixe o CENTRO da metade de cima vazio e escuro (um logo será colocado ali depois): nenhum logo, nenhum texto,"
                     " nenhum objeto no centro; o impacto vem da luz e do cenário em volta.") if x.get("logos") else ""
            linhas.append(f"{len(linhas) + 1}. {nome[i]} — {x['imagem']}.{extra}")
    pedido = (f"Gere {len(linhas)} imagens com a ferramenta de geração de imagem (image_gen) e salve nesta pasta, em PNG, formato RETRATO 9:16 "
              f"(o maior tamanho vertical disponível). {ESTILO}\n\n" + "\n".join(linhas) + "\n\nAo final, liste os arquivos salvos.\n")
    (capa / "pedido.txt").write_text(pedido)
    falta = [n for n in ["abertura.png"] + list(nome.values()) if not (capa / n).exists()]
    if falta:
        log(f"Codex: {len(falta)} imagem(ns)…")
        with open(capa / "codex.log", "w") as lg:
            subprocess.run(["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox"], input=pedido, text=True,
                           cwd=capa, stdout=lg, stderr=subprocess.STDOUT, timeout=2700)
    for n in ["abertura.png"] + list(nome.values()):
        if not (capa / n).exists():
            falha(f"o Codex não gerou capa/{n} (capa/codex.log)")
        pecas.vertical(capa / n)
    pecas.abertura(capa / "abertura.png")
    for i, x in enumerate(f["partes"], 1):
        if x.get("logos"):
            fundo = capa / f"p{i}-fundo.png" if x.get("imagem") else None
            if len(x["logos"]) > 1 and all(lg.get("de") for lg in x["logos"]):   # uma tela por produto
                for k, lg in enumerate(x["logos"], 1):   # {"de", "junto": [2 logos]} = dois logos na mesma tela
                    pecas.logo_card(lg.get("junto") or [lg], capa / f"p{i}-{k}.png", fundo)
            else:
                pecas.logo_card(x["logos"], capa / f"p{i}.png", fundo)
        if (x.get("painel") or {}).get("logo"):
            pecas.logo_solto(x["painel"]["logo"], capa / f"logo-{x['painel']['logo']}.png")
    for i, x in enumerate(f["partes"], 1):
        if x.get("print"):
            raw = prints / f"raw-p{i}.png"
            if not raw.exists():
                pecas.screenshot(x["print"]["url"], raw)
            from PIL import Image, ImageStat
            if ImageStat.Stat(Image.open(raw).convert("L")).stddev[0] < 8:   # print todo preto (skills15, 19/10)
                raw.rename(raw.with_name(raw.stem + "-vazio.png"))
                falha(f"print da parte {i} saiu vazio (página sem conteúdo no headless? tire âncora #…): {x['print']['url']}")
            pecas.print_card(raw, prints / f"p{i}-c.png")
    log("imagens OK — LEIA capa/abertura.png e confira a grafia do título antes do render")


def cmd_cena(pasta):
    p, f = ficha(pasta)
    fl = falas(p, f)
    t = p / "avatar/tempos.json"
    if not t.exists() or t.stat().st_mtime < (p / "avatar/avatar.mp4").stat().st_mtime:
        d, sem = RT.retempo(p); log(f"retempo {d:.1f} s · {sem:.0%}")
    dur, nt, npn, nl = CENA.montar(p, f, fl)
    log(f"cena.js ok: {dur} s · {nt} telas · {npn} painéis · {nl} blocos de legenda")


def cmd_render(pasta):
    p, f = ficha(pasta)
    env = dict(os.environ, DISPLAY=TELA, GEO="geo-br.js", LAYOUT="canto", MUSICA=str(R / "assets/trilha.mp3"))
    with open(p / "build-render.log", "w") as lg:
        r = subprocess.run(["bash", R / "motor/compor_avatar.sh", p, p / "video.mp4"], cwd=R, env=env, stdout=lg, stderr=subprocess.STDOUT,
                           timeout=3600)
    if r.returncode:
        txt = (p / "build-render.log").read_text()       # a linha do erro, não o fim do traceback (20/10/2026)
        chave = [l.strip() for l in txt.splitlines() if re.search(r"Error|Timeout|exceeded|NO_MEMORY|failed", l)]
        falha("render: " + (" | ".join(chave[:2]) if chave else txt[-400:]))
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p / "video.mp4"]))
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-nostats", "-i", p / "video.mp4", "-af", "ebur128", "-f", "null", "-"],
                                                            capture_output=True, text=True).stderr)
    log(f"vídeo {p / 'video.mp4'} · {d:.1f} s · {lufs[-1] if lufs else '?'} LUFS")
    if d >= 60:
        falha(f"{d:.0f} s: short passa de 1 min")


def cmd_revisar(pasta):
    p, _ = ficha(pasta); v = p / "video.mp4"; b = p / "build"; b.mkdir(exist_ok=True)
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v]))
    ts = [0.2, 1.5, 3.5] + [round(5 + (d - 6) * i / 8, 2) for i in range(9)]
    qs = []
    for k, t in enumerate(ts):
        q = b / f"q{k:02d}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", v, "-frames:v", "1", "-vf",
                        f"scale=300:-1,drawtext=text='{t}':x=6:y=6:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6", q], check=True)
        qs.append(q)
    lay = "|".join(f"{(i % 6) * 300}_{(i // 6) * 533}" for i in range(12))
    subprocess.run(["ffmpeg", "-v", "error", "-y", *sum((["-i", q] for q in qs), []), "-filter_complex", f"xstack=inputs=12:layout={lay}",
                    b / "folha.jpg"], check=True)
    log("folha", b / "folha.jpg", "— leia antes de enviar: título certo, nada cobrindo nada, prints legíveis")


def cmd_enviar(pasta):
    p, f = ficha(pasta)
    leg = f"r7ex · {f['tema']}" + (f" · {f['publicar']['titulo']}" if f.get("publicar") else "")
    subprocess.run(["node", R / "bin/enviar_bot_v3.mjs", p / "video.mp4", leg], check=True, timeout=600)


def cmd_fila(pasta):
    p, f = ficha(pasta); pub = f["publicar"]
    subprocess.run(["python3", R / "fila/fila.py", "--add", p / "video.mp4", "--nome", f["tema"], "--titulo", pub["titulo"],
                    "--contexto", pub["contexto"], "--canal", pub.get("fila", "lives7")], check=True)


def cmd_fazer(pasta, de=None):
    cmd_checar(pasta)
    arq = Path(pasta) / "avatar/AVATAR_DE.txt"          # avatar a reaproveitar, anotado na pasta (refazer com o mesmo avatar)
    if not de and arq.exists() and not (Path(pasta) / "avatar/avatar.mp4").exists():
        de = arq.read_text().strip()
    with cf.ThreadPoolExecutor(2) as ex:
        a = ex.submit(cmd_imagens, pasta); b = ex.submit(cmd_avatar, pasta, de)
        a.result(); b.result()
    cmd_cena(pasta); cmd_render(pasta); cmd_revisar(pasta)
    log("Terminei: reel pronto — leia build/folha.jpg; depois `enviar` e `fila`")


def main(a):
    if len(a) < 2:
        sys.exit(__doc__)
    de = a[a.index("--de") + 1] if "--de" in a else None
    c = {"novo": cmd_novo, "checar": cmd_checar, "plano": cmd_plano, "imagens": cmd_imagens, "cena": cmd_cena, "render": cmd_render,
         "revisar": cmd_revisar, "enviar": cmd_enviar, "fila": cmd_fila}
    if a[0] == "avatar":
        cmd_avatar(a[1], de)
    elif a[0] == "fazer":
        cmd_fazer(a[1], de)
    elif a[0] == "avatar-enviar":
        avatar_enviar(a[1])
    elif a[0] == "avatar-conferir":
        print(avatar_conferir(a[1]))
    elif a[0] in c:
        c[a[0]](a[1])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
