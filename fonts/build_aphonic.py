#!/usr/bin/env python3
"""
Aphonic v5 — escritura alien angular abstracta.
Sin ojos. Sin parentesco deliberado con letterforms latinas/españolas.
Uso: python3 fonts/build_aphonic.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

OUT_DIR = Path(__file__).resolve().parent
EM = 1000
ASCENDER = 850
DESCENDER = -150
CX, CY = 500, 430
ST = 86


def add_poly(path: pathops.Path, pts):
    if len(pts) < 3:
        return
    path.moveTo(*pts[0])
    for p in pts[1:]:
        path.lineTo(*p)
    path.close()


def add_bar(path: pathops.Path, x0, y0, x1, y1, t=ST):
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1
    px, py = -dy / length * t / 2, dx / length * t / 2
    add_poly(
        path,
        [
            (x0 + px, y0 + py),
            (x1 + px, y1 + py),
            (x1 - px, y1 - py),
            (x0 - px, y0 - py),
        ],
    )
    # terminales en diamante (más alien que círculos/cuadrados “tipo hueso”)
    s = t * 0.45
    for x, y in ((x0, y0), (x1, y1)):
        add_poly(path, [(x, y + s), (x + s, y), (x, y - s), (x - s, y)])


def chain(path, pts, t=ST):
    for i in range(len(pts) - 1):
        add_bar(path, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], t)


def wedge(path, cx, cy, r, a0, a1, t=ST):
    """Sector angular macizo (triángulo/trapecio radial), no arco suave."""
    p0 = (cx + r * math.cos(a0), cy + r * math.sin(a0))
    p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
    # trapecio corto desde radio interno
    ri = r * 0.25
    q0 = (cx + ri * math.cos(a0), cy + ri * math.sin(a0))
    q1 = (cx + ri * math.cos(a1), cy + ri * math.sin(a1))
    add_poly(path, [q0, p0, p1, q1])
    add_bar(path, p0[0], p0[1], p1[0], p1[1], t * 0.7)


def shard(path, cx, cy, w, h, rot_deg):
    """Romboide/rotación arbitraria."""
    a = math.radians(rot_deg)
    ca, sa = math.cos(a), math.sin(a)
    pts = [(-w, -h), (w, -h * 0.2), (w * 0.6, h), (-w * 0.8, h * 0.5)]
    out = [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts]
    add_poly(path, out)


def union_body(fn) -> pathops.Path:
    raw = pathops.Path()
    fn(raw)
    raw.simplify(fix_winding=True)
    return raw


def path_to_contours(path: pathops.Path):
    contours, current = [], []
    for verb, pts in path:
        if verb == pathops.PathVerb.MOVE:
            if current:
                contours.append(current)
            current = [pts[0]]
        elif verb == pathops.PathVerb.LINE:
            current.append(pts[0])
        elif verb == pathops.PathVerb.QUAD:
            current.append(pts[1])
        elif verb == pathops.PathVerb.CUBIC:
            current.append(pts[2])
        elif verb == pathops.PathVerb.CLOSE:
            if current:
                contours.append(current)
                current = []
    if current:
        contours.append(current)
    return contours


def build_glyph_from_path(path: pathops.Path):
    contours = path_to_contours(path)
    pen = TTGlyphPen(None)
    for pts in contours:
        if len(pts) < 3:
            continue
        pen.moveTo(pts[0])
        for p in pts[1:]:
            pen.lineTo(p)
        pen.closePath()
    return pen.glyph(), contours


def make_empty():
    return TTGlyphPen(None).glyph()


def glyph(fn):
    return union_body(fn)


def glyph_set():
    """
    Kit abstracto: cuñas, shards, cadenas quebradas, stacks descentrados.
    Evita siluetas tipo A E H M N S T V X Y Z latinas.
    """
    G = {}

    def A(p):
        # tres cuñas a 75° (reloj asimétrico)
        wedge(p, CX - 40, CY, 260, math.radians(20), math.radians(70))
        wedge(p, CX - 40, CY, 220, math.radians(140), math.radians(195))
        wedge(p, CX - 40, CY, 240, math.radians(250), math.radians(300))

    G["A"] = glyph(A)

    def B(p):
        # shard + cadena quebrada lateral
        shard(p, CX - 60, CY + 40, 120, 160, 25)
        chain(p, [(CX + 40, CY + 220), (CX + 220, CY + 40), (CX + 80, CY - 200), (CX + 240, CY - 280)])

    G["B"] = glyph(B)

    def C(p):
        # marco incompleto descentrado (no C)
        chain(p, [(CX + 200, CY + 240), (CX - 180, CY + 180), (CX - 220, CY - 60), (CX - 40, CY - 260)])
        add_bar(p, CX + 40, CY - 40, CX + 220, CY - 180)

    G["C"] = glyph(C)

    def D(p):
        # dos shards apilados en diagonal
        shard(p, CX - 80, CY + 120, 140, 110, -20)
        shard(p, CX + 100, CY - 140, 120, 130, 40)
        add_bar(p, CX - 20, CY + 40, CX + 60, CY - 60)

    G["D"] = glyph(D)

    def E(p):
        # nodo + 3 shards orbitando (nada de peines horizontales)
        shard(p, CX, CY, 70, 60, 0)
        shard(p, CX + 160, CY + 140, 90, 70, 40)
        shard(p, CX - 180, CY + 80, 85, 75, -30)
        shard(p, CX + 40, CY - 200, 100, 80, 70)

    G["E"] = glyph(E)

    def F(p):
        # trapecio irregular + púa
        add_poly(p, [(CX - 200, CY + 200), (CX + 160, CY + 280), (CX + 80, CY - 40), (CX - 240, CY - 100)])
        add_bar(p, CX + 40, CY - 20, CX + 220, CY - 260)

    G["F"] = glyph(F)

    def Gfn(p):
        # dos cuñas + shard flotante
        wedge(p, CX + 40, CY - 20, 260, math.radians(40), math.radians(110))
        wedge(p, CX + 40, CY - 20, 240, math.radians(200), math.radians(270))
        shard(p, CX - 160, CY + 180, 80, 70, 25)

    G["G"] = glyph(Gfn)

    def H(p):
        # dos cuñas opuestas sin barra H
        wedge(p, CX, CY + 40, 250, math.radians(-30), math.radians(40))
        wedge(p, CX, CY + 40, 250, math.radians(150), math.radians(220))
        shard(p, CX, CY - 180, 90, 70, 10)

    G["H"] = glyph(H)

    def I(p):
        # stack escalonado (no poste I)
        for i, (dx, dy) in enumerate([(-80, 200), (40, 40), (-30, -140), (90, -260)]):
            shard(p, CX + dx, CY + dy, 70 + i * 8, 55, 15 * i)

    G["I"] = glyph(I)

    def J(p):
        # gancho quebrado + cuña
        chain(p, [(CX + 200, CY + 260), (CX + 40, CY + 80), (CX + 120, CY - 100), (CX - 180, CY - 240)])
        wedge(p, CX - 40, CY + 40, 180, math.radians(200), math.radians(260))

    G["J"] = glyph(J)

    def K(p):
        # racimo de 3 shards convergentes
        shard(p, CX + 40, CY + 160, 100, 90, -35)
        shard(p, CX + 120, CY - 40, 110, 80, 10)
        shard(p, CX - 100, CY - 160, 120, 100, 55)
        add_bar(p, CX - 40, CY + 40, CX + 40, CY - 20, 60)

    G["K"] = glyph(K)

    def L(p):
        # boomerang triple
        chain(p, [(CX - 240, CY + 160), (CX - 40, CY + 280), (CX + 200, CY + 40), (CX + 40, CY - 260)])

    G["L"] = glyph(L)

    def M(p):
        # racimo de 4 shards (nada de M/W)
        shard(p, CX - 140, CY + 120, 100, 90, -20)
        shard(p, CX + 130, CY + 160, 90, 80, 35)
        shard(p, CX - 40, CY - 60, 110, 70, 10)
        shard(p, CX + 80, CY - 200, 95, 85, -50)

    G["M"] = glyph(M)

    def N(p):
        # marco romboidal roto
        chain(p, [(CX, CY + 280), (CX + 240, CY + 40), (CX + 40, CY - 260)])
        chain(p, [(CX, CY + 120), (CX - 240, CY - 40), (CX - 80, CY - 240)])

    G["N"] = glyph(N)

    def O(p):
        # pentágono irregular sólido (no O circular)
        pts = []
        for i, r in enumerate([210, 250, 190, 240, 200]):
            a = math.radians(-90 + 15 + i * 72)
            pts.append((CX + r * math.cos(a), CY + r * math.sin(a)))
        add_poly(p, pts)

    G["O"] = glyph(O)

    def P(p):
        # tres cuñas desde puntos distintos
        wedge(p, CX - 100, CY + 120, 220, math.radians(-40), math.radians(20))
        wedge(p, CX + 80, CY - 40, 200, math.radians(100), math.radians(160))
        shard(p, CX + 40, CY + 200, 70, 60, -15)

    G["P"] = glyph(P)

    def Q(p):
        # no hexágono+cola: dos shards cruzados + cuña
        shard(p, CX - 60, CY + 80, 140, 120, 25)
        shard(p, CX + 80, CY - 100, 130, 110, -40)
        wedge(p, CX, CY, 180, math.radians(250), math.radians(310))

    G["Q"] = glyph(Q)

    def R(p):
        # asta + dos cuñas laterales
        add_bar(p, CX - 80, CY + 260, CX - 160, CY - 260)
        wedge(p, CX - 40, CY + 80, 230, math.radians(-10), math.radians(50))
        wedge(p, CX - 40, CY - 40, 210, math.radians(300), math.radians(350))

    G["R"] = glyph(R)

    def S(p):
        # tres shards en diagonal (rompe S)
        shard(p, CX - 120, CY + 180, 110, 90, 50)
        shard(p, CX + 40, CY, 100, 85, -20)
        shard(p, CX + 100, CY - 200, 120, 95, 35)

    G["S"] = glyph(S)

    def T(p):
        # bloque irregular + púa lateral
        add_poly(p, [(CX - 180, CY + 160), (CX + 140, CY + 240), (CX + 200, CY - 40), (CX - 100, CY - 120)])
        add_bar(p, CX + 60, CY - 80, CX - 40, CY - 280)

    G["T"] = glyph(T)

    def U(p):
        # no U: cuña grande + shard
        wedge(p, CX, CY, 270, math.radians(30), math.radians(120))
        shard(p, CX - 140, CY - 160, 100, 90, 20)
        add_bar(p, CX + 100, CY + 40, CX + 240, CY - 200)

    G["U"] = glyph(U)

    def V(p):
        # no V/A: anillo poligonal abierto + shard interno
        chain(p, [(CX + 200, CY + 160), (CX - 60, CY + 260), (CX - 240, CY), (CX - 40, CY - 240), (CX + 180, CY - 120)])
        shard(p, CX, CY, 65, 55, 40)

    G["V"] = glyph(V)

    def W(p):
        # tres púas desde un nodo descentrado
        node = (CX - 40, CY + 100)
        for ang, length in [(200, 300), (250, 320), (300, 280)]:
            a = math.radians(ang)
            add_bar(p, node[0], node[1], node[0] + length * math.cos(a), node[1] + length * math.sin(a))
        shard(p, node[0], node[1], 70, 60, 20)

    G["W"] = glyph(W)

    def X(p):
        # tres shards en triángulo (rompe X/asterisco)
        shard(p, CX, CY + 160, 100, 80, 0)
        shard(p, CX - 140, CY - 120, 110, 90, 55)
        shard(p, CX + 150, CY - 100, 105, 85, -40)

    G["X"] = glyph(X)

    def Y(p):
        # espiral corta de shards
        shard(p, CX - 100, CY + 160, 90, 75, 20)
        shard(p, CX + 120, CY + 40, 100, 70, -35)
        shard(p, CX - 20, CY - 180, 110, 90, 60)
        add_bar(p, CX - 40, CY + 60, CX + 60, CY - 40, 55)

    G["Y"] = glyph(Y)

    def Z(p):
        # constelación: 3 cuñas (rompe Z/2)
        wedge(p, CX - 80, CY + 100, 210, math.radians(10), math.radians(70))
        wedge(p, CX + 60, CY - 40, 200, math.radians(130), math.radians(190))
        wedge(p, CX, CY - 60, 190, math.radians(240), math.radians(300))

    G["Z"] = glyph(Z)

    # Dígitos — mismo idioma, distintos “pesos”
    def zero(p):
        pts = []
        for i, r in enumerate([200, 170, 220, 180, 210, 160]):
            a = math.radians(i * 60 + 12)
            pts.append((CX + r * math.cos(a), CY + r * math.sin(a)))
        add_poly(p, pts)

    G["zero"] = glyph(zero)

    def one(p):
        chain(p, [(CX - 160, CY + 200), (CX + 40, CY + 280), (CX + 120, CY - 280)])
        shard(p, CX - 40, CY + 40, 50, 40, 30)

    G["one"] = glyph(one)

    def two(p):
        chain(
            p,
            [
                (CX - 220, CY + 160),
                (CX + 100, CY + 280),
                (CX + 220, CY + 40),
                (CX - 80, CY - 40),
                (CX - 200, CY - 280),
                (CX + 200, CY - 200),
            ],
        )

    G["two"] = glyph(two)

    def three(p):
        wedge(p, CX - 80, CY, 250, math.radians(-20), math.radians(40))
        wedge(p, CX - 80, CY, 230, math.radians(70), math.radians(130))
        wedge(p, CX - 80, CY, 240, math.radians(200), math.radians(250))

    G["three"] = glyph(three)

    def four(p):
        shard(p, CX + 60, CY + 80, 130, 150, -40)
        chain(p, [(CX - 220, CY + 40), (CX + 40, CY - 40), (CX + 200, CY - 260)])

    G["four"] = glyph(four)

    def five(p):
        chain(
            p,
            [
                (CX + 220, CY + 260),
                (CX - 200, CY + 200),
                (CX - 120, CY + 20),
                (CX + 180, CY - 20),
                (CX + 100, CY - 280),
                (CX - 220, CY - 180),
            ],
        )

    G["five"] = glyph(five)

    def six(p):
        chain(p, [(CX + 200, CY + 100), (CX - 40, CY + 280), (CX - 240, CY), (CX - 40, CY - 260), (CX + 180, CY - 100)])
        add_bar(p, CX - 40, CY + 40, CX + 100, CY - 40)

    G["six"] = glyph(six)

    def seven(p):
        chain(p, [(CX - 240, CY + 200), (CX + 220, CY + 280), (CX + 40, CY - 40), (CX + 160, CY - 280)])
        shard(p, CX + 40, CY - 40, 55, 45, 25)

    G["seven"] = glyph(seven)

    def eight(p):
        shard(p, CX - 40, CY + 160, 120, 100, 15)
        shard(p, CX + 60, CY - 160, 130, 110, -25)
        add_bar(p, CX - 20, CY + 60, CX + 40, CY - 60, 55)

    G["eight"] = glyph(eight)

    def nine(p):
        wedge(p, CX, CY + 60, 230, math.radians(160), math.radians(250))
        chain(p, [(CX + 80, CY + 40), (CX + 220, CY - 40), (CX + 100, CY - 280)])

    G["nine"] = glyph(nine)

    def period(p):
        shard(p, CX, CY - 40, 55, 50, 20)

    G["period"] = glyph(period)

    def comma(p):
        shard(p, CX, CY, 55, 50, -10)
        add_bar(p, CX + 10, CY - 30, CX - 70, CY - 200, 60)

    G["comma"] = glyph(comma)

    def question(p):
        chain(p, [(CX + 180, CY + 200), (CX - 60, CY + 280), (CX - 220, CY + 40), (CX + 40, CY - 40)])
        shard(p, CX, CY - 240, 50, 45, 0)

    G["question"] = glyph(question)

    def exclam(p):
        add_bar(p, CX + 40, CY + 280, CX - 40, CY - 40)
        shard(p, CX - 20, CY - 240, 50, 45, 15)

    G["exclam"] = glyph(exclam)

    def hyphen(p):
        # barra quebrada (no guion latino limpio)
        chain(p, [(280, CY + 40), (480, CY - 20), (720, CY + 30)])

    G["hyphen"] = glyph(hyphen)

    def ellipsis(p):
        for i, xx in enumerate((CX - 200, CX, CX + 200)):
            shard(p, xx, CY - 40, 40, 35, 15 * i)

    G["ellipsis"] = glyph(ellipsis)

    return G


def advance_for(name: str) -> int:
    if name == "space":
        return 420
    if name in ("period", "comma"):
        return 520
    return 1000


def main():
    paths = glyph_set()
    cmap = {32: "space"}
    glyph_order = [".notdef", "space"]
    glyphs = {".notdef": make_empty(), "space": make_empty()}
    contour_map = {}

    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        glyph_order.append(ch)
        g, contours = build_glyph_from_path(paths[ch])
        glyphs[ch] = g
        contour_map[ch] = contours
        cmap[ord(ch)] = ch
        cmap[ord(ch.lower())] = ch

    for ch, name in [
        ("0", "zero"), ("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"),
        ("5", "five"), ("6", "six"), ("7", "seven"), ("8", "eight"), ("9", "nine"),
    ]:
        glyph_order.append(name)
        g, contours = build_glyph_from_path(paths[name])
        glyphs[name] = g
        contour_map[name] = contours
        cmap[ord(ch)] = name

    for ch, name in [(".", "period"), (",", "comma"), ("?", "question"), ("!", "exclam"), ("-", "hyphen")]:
        glyph_order.append(name)
        g, contours = build_glyph_from_path(paths[name])
        glyphs[name] = g
        contour_map[name] = contours
        cmap[ord(ch)] = name

    glyph_order.append("ellipsis")
    g, contours = build_glyph_from_path(paths["ellipsis"])
    glyphs["ellipsis"] = g
    contour_map["ellipsis"] = contours
    cmap[0x2026] = "ellipsis"

    metrics = {}
    for name in glyph_order:
        if name in (".notdef", "space"):
            metrics[name] = (advance_for(name), 0)
            continue
        xs = [x for c in contour_map[name] for x, _y in c]
        if not xs:
            metrics[name] = (advance_for(name), 0)
            continue
        x_min, x_max = min(xs), max(xs)
        metrics[name] = (max(advance_for(name), int(math.ceil(x_max)) + 90), int(math.floor(x_min)))

    fb = FontBuilder(EM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=ASCENDER, descent=DESCENDER)
    fb.setupNameTable(
        {
            "familyName": "Aphonic",
            "styleName": "Regular",
            "uniqueFontIdentifier": "Aphonic Regular: abstract angular alien",
            "fullName": "Aphonic Regular",
            "psName": "Aphonic-Regular",
            "version": "Version 5.100",
            "designer": "Game design — opaque language project",
            "description": (
                "Aphonic v5: abstract angular alien glyphs. No eyes. "
                "Intentionally avoids Latin/Spanish letterform silhouettes."
            ),
            "licenseDescription": "Project asset for this game design repository.",
        }
    )
    fb.setupOS2(
        sTypoAscender=ASCENDER,
        sTypoDescender=DESCENDER,
        usWinAscent=ASCENDER,
        usWinDescent=-DESCENDER,
    )
    fb.setupPost()
    fb.setupGlyf(glyphs)
    fb.setupMaxp()
    fb.setupHead(unitsPerEm=EM)

    out = OUT_DIR / "Aphonic-Regular.ttf"
    fb.save(str(out))
    print(f"Saved {out}")

    (OUT_DIR / "Aphonic-mapping.json").write_text(
        json.dumps(
            {
                "fontFamily": "Aphonic",
                "version": "5.100",
                "file": "Aphonic-Regular.ttf",
                "scriptType": "abstract angular alien unicase",
                "aesthetic": "No eyes. Wedges/shards/clusters. Extra pass to break M/S/U/V/X/Z/Q Latin silhouettes.",
                "rebuild": "python3 fonts/build_aphonic.py",
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
