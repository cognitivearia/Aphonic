# Aphonic — fuente del lenguaje opaco

Fuente geométrica alienígena para el texto que el jugador **no debe poder leer**.

| Archivo | Qué es |
|---------|--------|
| `Aphonic-Regular.ttf` | Fuente instalable / usable en diseño y (luego) en Unity |
| `Aphonic-mapping.json` | Mapa de uso (qué teclas producen qué) |
| `build_aphonic.py` | Script para regenerar la TTF |
| `preview/` | Hojas de muestra (PNG / SVG) |

## Principio de diseño (v5)

- **Unicase:** `A` y `a` muestran el mismo glifo.
- **Sin ojos.**
- **Abstracto y angular:** cuñas, shards, cadenas quebradas, polígonos irregulares.
- **Sin parentesco deliberado** con el alfabeto latino/español (rompe siluetas tipo A/E/H/M/S/V…).
- **Formas originales** del proyecto.

## Cómo usarla (ahora, en diseño)

1. Descarga / abre `Aphonic-Regular.ttf`.
2. Instálala en el sistema **o** cárgala en Figma / Affinity / Word / etc.
3. Escribe en teclado normal (`X5J9-2A`, nombres, letreros).
4. Al aplicar la fuente Aphonic, el texto se vuelve ilegible a propósito.

Caracteres soportados: **A–Z**, **a–z**, **0–9**, espacio, `. , ? ! -` y `…` (ellipsis).

No están (aún): `#`, `%` y otros símbolos — por eso `BGJAO#%5` solo renderiza bien la parte `BGJAO` / dígitos si los escribes aparte.

## Regenerar

```bash
python3 fonts/build_aphonic.py
```

## Rol en el juego

Esta fuente es el **sistema de escritura del mundo**. Refuerza la regla del GDD: nunca hay traducción in-game. El jugador ve Aphonic en carteles, el documento **X5j9-2a**, UI alienígena, etc.
