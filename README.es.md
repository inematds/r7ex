# r7ex — el reel viral de INEMA

[![r7ex — el reel viral de INEMA](guia/assets/banner-es.jpg)](https://inematds.github.io/r7ex/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

r7ex es la línea de producción de reels verticales (9:16) de INEMA. Tú entregas una idea fuerte, la tesis, y él arma un video de 40 a 50 segundos (30–37 s de habla a ritmo calmo + 9 s de tarjeta de comentario) con el avatar de Nei hablando, imágenes generadas por Codex y un acabado de noticiero: título en la apertura, paneles que entran en la palabra correcta, contador y subtítulo que se ilumina junto con el habla. El guion sigue 7 etapas de gatillo, desde el gancho con número hasta el pedido de comentario, siempre llevando a la persona a inema.club. Para usarlo se necesitan Python, Node, Codex y la suscripción de HeyGen, corriendo en la máquina de INEMA.

## 🎬 Videos sobre el r7ex

Hechos con el propio r7ex (19/10/2026, en portugués):

- [Reel 1 — "Mis reels tuvieron cero vistas, 4 lotes hasta acertar"](https://inematds.github.io/r7ex/guia/assets/videos/r7ex-divulga.mp4)
- [Reel 2 — "El reel de 7 etapas quedó viejo, ahora existe el r7ex"](https://inematds.github.io/r7ex/guia/assets/videos/r7e-para-r7ex.mp4)

También se reproducen en la guía, sección Ejemplos.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/r7ex/guia/es/**

---

**r7ex = r7e + x.** **r7e** (reel7etapas) aporta el **guion**: 7 etapas de gatillo, del gancho al comentario.
La **x** viene de **eventosextremospub**: el **acabado de noticiero** que más se viraliza.
Objetivo de todo reel: **traer gente a inema.club.**

Este repo funciona **solo**: tiene copia propia del motor de render, de los scripts del estudio de HeyGen, de la transcripción,
de la pista musical, del envío al bot y de la cola de publicación. Cambiar algo aquí **no afecta** a eventosextremospub, reel7etapas,
explicavideos ni cardshorts.

- Estándar fijo (la regla corta): [`PADRAO.md`](PADRAO.md) (en portugués)
- Ficha de ejemplo (el reel del hacker): [`modelo/ficha.yaml`](modelo/ficha.yaml) (en portugués)

---

## 1. Cómo llegamos aquí (18/10/2026) — 4 lotes, qué cambió en cada uno

| Lote | Contenido (lo que se dice) | Forma (lo que se ve) | Resultado |
|---|---|---|---|
| **1. r7e antiguo** (deepseek, faxina, opencode, contexto, diga) | Tema del día (divulgar guía/repo), público de nicho, gancho = **promesa** ("TU AGENTE OBEDECE Y GASTA MENOS"), 7 etapas en orden fijo, miedo débil y a veces desarmado en el acto | Motor de r7e: foto de banco de imágenes desenfocada detrás del rostro a media pantalla, letra Anton con ámbar apagado | Sin visualizaciones en TikTok/Instagram |
| **2. r7e "-gatilho"** (los mismos 5, mismo avatar) | Habla igual (la voz a veces contradecía la pantalla) | Solo cambió el gancho: miedo/novedad/provocación con número, imagen nítida dramática, amarillo #FACC15 con contorno | Mejor, pero "todavía genérico" |
| **3. r7e D10** (5 tesis de Nei + hacker rehecho; 2 de gestión) | **Plan antes del habla** (persona, lo que quiere, gancho con número, nota, destino en inema.club), **habla nueva** con el gatillo primero y el alivio en el medio, CTA fijo, capturas reales de las páginas | Motor de r7e con franja y diagramas en Pillow | "Quedó genérico" |
| **4. r7ex** (los mismos 7, **mismo avatar y habla del lote 3**) | Ningún contenido nuevo: el habla dividida en 7 bloques, cada uno con imagen y panel sacados de la propia habla | **Motor de eventosextremospub**: título dentro del arte, negro y dorado, franja de noticiero, paneles al ritmo del habla, contador, karaoke, CTA en pregunta | Formato estándar a partir de ahora |

Lección: el **contenido** acertó en el lote 3 (tesis fuertes, gatillo, plan) y la **forma** acertó en el lote 4 (motor de eventos).

### Links en YouTube

| Qué | Link |
|---|---|
| El de referencia que funcionó (evento extremo, r7e antiguo con flagrante + número) | https://www.youtube.com/shorts/DfdtX9HbkWg (lives10) |
| Lote 1 — Limpieza del setup (promesa, sin visualizaciones) | https://www.youtube.com/shorts/E5Y94BLfuJU (lives4) |
| Lote 1 — Capa de contexto (promesa, sin visualizaciones) | https://www.youtube.com/shorts/XflFkvIl4mw (lives4) |
| Lote 3 — Despido masivo de gerentes (motor r7e) | https://www.youtube.com/shorts/xpDV5qQe5oE (lives3) |
| Lote 3 — Empleado que no es persona (motor r7e) | https://www.youtube.com/shorts/cMhIavjhdh0 (lives3) |
| **Lote 4 / r7ex — Hackers robaron las claves** | https://youtube.com/shorts/DG30IdeqWcg (lives7) |
| Lote 4 / r7ex — los otros 6 | en la cola de lives7 (1 cada 2 h); `python3 fila/fila.py --status` |

## 2. Cómo se forma el contenido (el plan)

Antes de escribir una palabra del habla:

1. **Persona:** público general (IA traducida al día a día), no el nicho.
2. **Lo que quiere:** ganar algo, resolver un dolor o alcanzar un deseo.
3. **Gancho:** miedo, novedad o provocación, **con número o dato** y fuente.
4. **Nota de potencial (0–10):** "¿un desconocido que desliza el feed se detiene aquí?" Por debajo de 7, cambia el ángulo o el tema.
5. **Destino:** la página de inema.club que lo resuelve (se convierte en la captura de prueba).

Base real: leo antes la página del curso/guía (nombre, cuántas clases, si es gratis). Nunca invento números;
"gratis" solo cuando la página lo dice o Nei lo afirma.

## 3. Las 7 etapas — ejemplo real (el reel del hacker)

| Etapa | Habla | Pantalla |
|---|---|---|
| 1. Gancho (miedo) | "Hackers invadieron OpenCode… US$ 1.700 en una noche" | apertura con el título dibujado + contador 0 → 1.700 |
| 2. Miedo | "La clave es la contraseña que usa la IA… la tuya puede ser la próxima" | encapuchado sacando la clave + panel rojo |
| 3. Deseo | "Imagina dormir sabiendo que… la pérdida tiene tope" | hombre durmiendo + "pérdida con tope" |
| 4. Facilidad | "No necesitas ser especialista, ni programador" | panel de límite + "sin ser especialista" |
| 5. Descubrimiento | "Son tres ajustes: límite, una clave por uso, alarma…" | candado, claves y campana + los 3 ajustes entrando |
| 6. Beneficio | "El susto se convierte en un aviso en el celular…" | factura rota + "sin límite × con límite" |
| 7. Comentario | "Está todo en inema.club. O pídeme el link…" | captura de inema.club + CTA rojo en pregunta |

El orden 2–6 se adapta al tema (ej.: en "Quién factura en 2027" la etapa 3 se volvió **prueba**: "ya pasó 3 veces"),
pero siempre son 7 partes (~30–37 s de habla + 9 s de tarjeta final desde el 28/10/2026).

## 4. Qué hace el motor

El motor **no crea contenido ni imágenes**: **sincroniza y anima**. Es una página web (`motor/mapa.html`) que se convierte en video.

- **Recibe:**
  - el avatar (HeyGen) y el tiempo de cada una de sus palabras (`r7ex/retempo.py`, Whisper local);
  - las imágenes (Codex) y las capturas;
  - la `cena.js`, generada desde la ficha por `r7ex/cena.py`: qué imagen en qué frase, paneles, contadores, CTA, colores.
- **Dibuja en capas, cuadro a cuadro:**
  1. fondo negro (el mapa 3D de los videos de clima queda tapado);
  2. la imagen del momento, con entrada suave y zoom leve;
  3. la franja superior (marca + sello rojo) y la línea de fuente;
  4. el panel, con los ítems entrando en el segundo de la palabra y el contador subiendo;
  5. el subtítulo karaoke;
  6. el CTA en pregunta y la píldora de inema.club.
- **Filma** la página a 30 cuadros por segundo (`motor/render.mjs`, Chrome oculto en la pantalla `:99`).
- **Une** (`motor/compor_avatar.sh`):
  - el rostro en la cajita de la esquina;
  - la voz a −14 LUFS;
  - la pista bajita, que se atenúa cuando hablas.

En una frase: **Claude escribe, Codex dibuja, HeyGen habla y el motor sincroniza todo con la voz.**

## 5. Qué vino de cada lugar

| De **r7e** (reel7etapas) | De **eventosextremospub** |
|---|---|
| Las 7 etapas de gatillo y el orden | El motor de render (`mapa.html`, `render.mjs`, `compor_avatar.sh`) |
| El gancho = gatillo con número (D9) | El visual de noticiero: franja, sello, línea de fuente |
| El plan antes del habla y el CTA fijo de inema.club (D10) | La apertura con el título dibujado por Codex (`abertura-desce`) |
| El avatar de Nei por el estudio de HeyGen | La paleta negro + amarillo, rojo solo en el peligro |
| Las capturas reales de las páginas como prueba | Los paneles con ítems al ritmo del habla y los contadores |
| La cola y el envío al bot v3 | El subtítulo karaoke a color y el CTA rojo en pregunta |
| | El `retempo` (dividir el avatar en las frases) |
| También: la transcripción Whisper (copia de cardshorts) | |

Todo esto fue **copiado** aquí (no es un link): `motor/`, `heygen/`, `r7ex/whisper.py`, `r7ex/retempo.py`,
`assets/trilha.mp3`, `bin/enviar_bot_v3.mjs`, `fila/`.

## 6. Cómo usarlo

```bash
cd ~/projetos/r7ex
python3 r7ex.py novo <slug>                 # crea edicoes/<data>-<slug>/ficha.yaml a partir del modelo
#   → escribe el plan, la apertura, las 7 partes (habla + imagen/captura + panel), el CTA y "publicar"
python3 r7ex.py checar edicoes/<pasta>      # filtro de la ficha
echo 'Nei, <data>: "<frase do OK>"' > edicoes/<pasta>/avatar/APROVADO_HEYGEN   # solo con el OK de Nei para esta producción
python3 r7ex.py fazer edicoes/<pasta>       # imágenes + avatar → escena → render → hoja de revisión
#   (o --de <avatar.mp4> para reutilizar un avatar ya hecho)
# LEER edicoes/<pasta>/capa/abertura.png (ortografía) y edicoes/<pasta>/build/folha.jpg
python3 r7ex.py enviar edicoes/<pasta>      # bot v3
python3 r7ex.py fila edicoes/<pasta>        # final de la cola del canal (por defecto lives7)
```

Paso a paso por separado: `avatar`, `imagens`, `cena`, `render`, `revisar` (ver `python3 r7ex.py`).

## 7. Cómo cambiarlo

### Cambiar el layout (lo que se ve)
| Quiero cambiar | Dónde |
|---|---|
| Colores, fuente, tamaño y posición de la franja, panel, subtítulo, CTA | `motor/mapa.html` (CSS y dibujo de las capas) |
| Posición y tamaño del rostro, marco, nombre | `motor/compor_avatar.sh` (`LAYOUT=canto`: 400x453 en x 640, y 1290) |
| Dónde baja la apertura, la tarjeta de la captura, el brillo de la captura | `r7ex/pecas.py` (`abertura`, `print_card`) |
| Estilo de las imágenes (paleta, robot, sin texto) | `ESTILO` en `r7ex.py` |
| Colores de las palabras en el subtítulo | `cores:` en la ficha (por reel) |
| Pista musical | `assets/trilha.mp3` |

### Cambiar la estructura (cuántas partes, qué tiene cada una)
- Las partes son la lista `partes:` de la ficha. El motor acepta cualquier cantidad. El filtro `checar` exige 7
  (estándar); cámbialo ahí si el estándar cambia.
- Cada parte puede tener `imagem` (Codex la dibuja) **o** `print` (página real), y un `painel`
  (`itens`, `contador`, `borda`).
- El panel entra en la palabra `de:` y cada ítem en su palabra. Elige palabras que existan en el habla de esa parte.

### Cambiar la planificación (lo que se dice)
- `plano:` en la ficha (pessoa, quer, gancho, nota, destino) y las reglas del §2.
- Las reglas fijas están en `PADRAO.md` y en el kit `inema-design` (D9, D10, D11). Cambio de estándar:
  primero el kit (`DECISOES.md` + `HISTORICO.md`), después aquí.

## 8. HeyGen y publicación

- **Avatar:** estudio de HeyGen con la suscripción (`heygen/heygen-studio.mjs`), siempre en la pantalla oculta `:99`.
  Estado y descarga por lectura de la API (excepción autorizada). Generar solo con `avatar/APROVADO_HEYGEN` de esa producción.
- **Se cayó la sesión de HeyGen** ("no tiene sesión iniciada"): abrir **solo la ventana de login** en la pantalla de Nei (`:10`); él entra
  con Google. La sesión dura ~30 días; el aviso rojo llega al v3 un día antes (`~/projetos/wifi/heygen-aviso`).
- **Publicación:** siempre por la cola (`fila/fila.py`, timer systemd `fila-lives7`, de 9 h a 21 h, 1 cada 2 h),
  nunca subida directa. Cada publicación avisa en el v3.

## Licencia
MIT.
