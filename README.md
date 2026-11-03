# Aphonic — diseño de juego (lenguaje opaco)

Repositorio de **diseño de juego** (no hay prototipo jugable todavía).

- GitHub: [cognitivearia/Aphonic](https://github.com/cognitivearia/Aphonic)
- Pages (visor, tras activar Actions): [cognitivearia.github.io/Aphonic](https://cognitivearia.github.io/Aphonic/)

Entregables de diseño actuales:

- **[GDD.md](./GDD.md)** / **[GDD.docx](./GDD.docx)** — documento de diseño completo
- **[ONEPAGER.md](./ONEPAGER.md)** / **[ONEPAGER.docx](./ONEPAGER.docx)** — one-pager de producción
- **[fonts/](./fonts/)** — fuente **Aphonic** (escritura alienígena del juego)
- **[assets/](./assets/)** — dirección de arte + tileset/props aduana (CC0 base)
- **[assets/mockups/](./assets/mockups/)** — 4 salas: Lobby **A** · Buffet · Archivo · Oficina
- **[mockup-viewer/](./mockup-viewer/)** — visor (`npm i && npm run dev` → **3847**)
- **[PUBLISH.md](./PUBLISH.md)** — publicar en GitHub + GitHub Pages

## De qué va (resumen)

Experiencia corta (20–40 min) para PC / itch.io: ciencia ficción, pixel art, un jugador. Debes completar el trámite **X5j9-2a** en un mundo cuyo idioma nunca se traduce. Las mecánicas (tono, ofrenda, postura) y el vínculo con **BGJAO#%5** son el centro.

## Cómo usar este repo

1. Lee y comenta `GDD.md`.
2. Para mockups de texto del mundo: instala `fonts/Aphonic-Regular.ttf` (ver `fonts/README.md`).
3. Revisa las salas: `cd mockup-viewer && npm i && npm run dev`.
4. Para publicar en GitHub Pages: sigue **[PUBLISH.md](./PUBLISH.md)**.
5. Cuando pase a producción, el motor tentativo es Unity 2D.

## Estado

- [x] Conceptos, mecánicas, tipografía, niveles, gestos, Beat 0
- [x] GDD + one-pager de producción
- [x] Pack tileset/props + mockups de las 4 salas
- [x] Build/Pages listo para GitHub (`PUBLISH.md`)
- [ ] Dirección visual final · título · sprites NPC
- [ ] Vertical slice (Beat 0 + Lobby)
