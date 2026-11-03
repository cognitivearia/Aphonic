# One-pager de producción — [Título TBD]

Documento de una página (producción). Detalle completo: `GDD.md`.

| | |
|--|--|
| **Pitch** | Premio de viaje → aduana alienígena. Completas el trámite **X5j9-2a** sin traducciones, con **BGJAO#%5**. |
| **Mensaje** | No dar por hecho que podemos comunicarnos. |
| **Formato** | PC · itch.io · 1P · pixel art (RPG Maker-like) · **20–40 min** |
| **Motor** | Unity 2D (tentativo) · fuente **Aphonic** ya en repo |
| **Público** | 19–30 |

---

## Curva (emoción)

`Beat 0 legible` → **Confusión** (Lobby) → **Risa** → **Ansiedad** (Buffet) → **Terror** (Archivo) → **Calidez / revelación** (Oficina)  
Final completo **con BG** · Final malo **sin BG** (atajo comida).

---

## Presupuesto (techo duro)

| Recurso | Máx. | Contenido |
|---------|------|-----------|
| Mapas | **5** | Beat 0 (ligero) + Lobby + Buffet + Archivo + Oficina |
| NPCs (tipos) | **8** | BG, 2 guardias, 2 flavor lobby, culto/comensales, servidor buffet, bibliotecario/autoridad |
| Objetos | **5** | Inútil · Sagrado (buffet) · Comida · Libro (clave final) · Formulario BG |

---

## Flujo por sala

| Sala | Objetivo | Castigo / nota |
|------|----------|----------------|
| **0 Premio** | Canje viaje; corte español → Aphonic | Sin mecánicas de gesto |
| **1 Lobby** | BG enseña **P1**; guardia da **Sello 1** | Gesto antes de BG = **FATAL** |
| **2 Buffet** | Copiar rito BG con artefacto sagrado; **sello doble** juntos | Resets suaves; sin ítem / ítem malo |
| **3 Archivo** | Ordenar 3/4 libros; salir **con BG** | **Sin sello**; comida = atajo sin BG |
| **4 Oficina** | Espejo **P1→T2→P3→P4** ante mujer mayor | **Sello 3**; sin BG = final malo |

**Gestos:** léxico P1–P4 / T1–T4 → `GDD.md` §6.1.1 y §7.11.

---

## Sistemas a construir (prioridad)

1. Movimiento + interacción + inventario (5 slots)  
2. Diálogo Aphonic + gestos mundo (W-GO, W-DEMO, W-DOUBT)  
3. Prompt ritual: elegir **postura / tono / ofrenda**  
4. Documento X5j9-2a (0→3 sellos) + flag `BG_acompañando`  
5. Resets suaves (Sala 2) · fatal Lobby · ramas ending  
6. Puzzle estanterías (Sala 3) · seguidora BG (Sala 4)

---

## Assets mínimos

- **Arte:** 5 mapas · tileset aduana · 8 tipos NPC · 5 props · UI sello/documento · iconos P/T  
- **Audio:** 4 tonos (T1–T4) · ambients por sala · stingers fatal/sello/ending  
- **Texto mundo:** solo **Aphonic** post-Beat 0  
- **Fuente:** `fonts/Aphonic-Regular.ttf`

---

## Fuera de alcance (jam)

Combate · online · traductor · mapa grande · más de 2 endings de trama · crafting.

---

## Estado

- [x] Concepto, mecánicas, tipografía, niveles, gestos, Beat 0  
- [ ] Vertical slice (Lobby jugable)  
- [ ] Dirección visual final · título  

**Siguiente producción recomendado:** vertical slice = Beat 0 corto + **Sala 1 completa**.
