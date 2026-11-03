# Game Design Document — [Título TBD]

Documento vivo de diseño. Este proyecto, por ahora, es solo conceptual: no incluye prototipo jugable.

| Campo | Valor |
|--------|--------|
| Plataforma | PC |
| Distribución | itch.io |
| Jugadores | 1 |
| Estilo visual | Pixel art (referencia RPG Maker); **mundo visual aún por decidir** |
| Duración objetivo | 20–40 minutos |
| Público | Adultos 19–30 |
| Motor tentativo | Unity 2D (cuando pase a desarrollo) |
| Estado | Conceptos, mecánicas, tipografía y estructura de niveles v1 |

---

## 1. Pitch

Ganas un premio: un viaje todo pago. Al redimirlo, caes en un mundo de ciencia ficción cuyo idioma no entiendes. Para quedarte debes completar el trámite **X5j9-2a** dentro de una **oficina de aduanas** (espacio reducido, exploración social). Nadie traduce. Solo tonos, ofrendas, posturas… y **BGJAO#%5**, una compañera que se ve en ti y decide que no serás otra víctima.

**Mensaje central:** no tomar por hecho que podemos comunicarnos con los demás.

---

## 2. Pilares de diseño

1. **Lenguaje opaco permanente** — sin traducciones, subtítulos clarificadores ni diccionario en ningún momento.
2. **Malentendido como sistema** — fuente de terror y de comedia.
3. **Vínculo con BGJAO#%5** — ella es safeguard emocional y jugable.
4. **Trámite absurdo (X5j9-2a)** — columna vertebral de la progresión.
5. **Mecánicas primero** — la narrativa sirve al loop, no al revés.

---

## 3. Experiencia objetivo

| Dimensión | Objetivo |
|-----------|----------|
| Sensación | Perdido, atraído por el mundo y el lenguaje, vulnerable |
| Tono | Oscila entre terror y comedia |
| Fantasía | Nadie especial; completar un trámite para quedarte en esta comunidad |
| Ending | **Completo** con BG: te quedas; comunicación frágil. **Final malo** si cierras el trámite sin ella (p. ej. atajo de la comida) |

El ending completo puede variar de **tono** (más cálido / más siniestro) según malentendidos acumulados, sin ramificar la trama buena.

---

## 4. Personajes

### 4.1 Protagonista

- Silencioso.
- Nadie especial: turista accidental por un **premio/viaje todo pago**.
- No “aprende el idioma” de forma explícita en ningún momento de la experiencia.

### 4.2 BGJAO#%5 (NPC vínculo / safeguard)

| Campo | Valor |
|--------|--------|
| Placeholder | `BGJAO#%5` |
| Rol | Compañera; actriz **estática por nivel** (punto fijo en cada sala) |
| Trasfondo | Mujer desplazada por la guerra en ese planeta; intenta entrar al país |
| Motivación | Al verte perdido, se ve en ti. Decide ayudarte para que no seas otra víctima de la violencia de un país corrupto |
| Función jugable | Da **pistas al inicio del nivel** y al **re-interactuar**; enseña por mímica; tiene **trámite paralelo** propio |
| Función emocional | Razón central para querer quedarte; el ending depende de que este vínculo exista |

**Presencia por nivel:**

- Salas 1–3: no te sigue; está en un **punto fijo**.  
  - Primera interacción → pista / modelado (sin traducir).  
  - Re-interacción → refuerzo, emoción, o trámite paralelo.  
- Tras el **Sello 2**, el jugador debe notar que **sin ella no hay ending**.  
- **Sala 4:** si llegó con ella, BG **permanece siempre a tu lado** (seguidora) y lidera los gestos del rito final.

**Regla dura de su ayuda (y de cualquier NPC que ayude):**

- Nunca texto claro, nunca diccionario, nunca “esto significa X”.
- Sí: señalar, demostrar postura, retirar un objeto peligroso, empujar suavemente a la acción correcta, interrumpir antes del desastre, contacto / presencia.

---

## 5. Loop principal (cada 30–60 segundos)

1. Entras a una situación social (cola, ventanilla, ritual, hogar).
2. Alguien exige algo en lengua opaca (gestos, ruido, objetos en escena).
3. Respondes con uno o más canales: **tono / ofrenda / postura**.
4. El mundo reacciona: avance del trámite, ayuda, o (raro) Game Over.
5. Sales con más “mapa social” (qué no hacer aquí), no con un glosario.

---

## 6. Mecánicas

### 6.1 Tres canales de respuesta (opacos)

| Canal | Qué elige el jugador | Qué percibe |
|--------|----------------------|-------------|
| **Tono** | 4 voces abstractas (ver léxico §6.1.1) | Animación + reacción del NPC |
| **Ofrenda** | Dar un objeto del inventario | Aceptación, rechazo u ofensa |
| **Postura / ritual** | 4 posturas abstractas (ver léxico §6.1.1) | Lectura social inmediata |

Sin glosas. Solo consecuencias. Tabla maestra por sala: **§7.11**.

#### 6.1.1 Léxico fijo (todo el juego)

IDs internos (el jugador **no** ve estos nombres; solo ve icono/animación).

**Posturas**

| ID | Qué hace el cuerpo (dirección de animación) | Lectura opaca sugerida |
|----|-----------------------------------------------|------------------------|
| **P1** | Mano al pecho + inclinación corta | Respeto / umbral |
| **P2** | Ambas palmas abiertas a la altura de la cintura | Oferta / vacío |
| **P3** | Señalar hacia abajo (suelo / documento / plato) | Anclar / reclamar |
| **P4** | Quedarse inmóvil 1–2 s (espera ritual) | Paciencia / cola |

**Tonos**

| ID | Cualidad sonora | Lectura opaca sugerida |
|----|-----------------|------------------------|
| **T1** | Agudo, corto | Llamada / alerta |
| **T2** | Grave, largo | Formal / sagrado |
| **T3** | Roto / entrecortado | Urgencia / error social |
| **T4** | Continuo bajo (drone) | Compañía / trámite compartido |

**Gestos de mundo (no elegibles por el jugador, solo NPCs)**

| ID | Quién | Animación |
|----|-------|-----------|
| **W-GO** | Flavor / rechazo | “Lárgate / sigue buscando” |
| **W-DOUBT** | BG en Archivo | Duda: no sabe ubicaciones |
| **W-DEMO** | BG tutorial | Demuestra la postura/tono correctos |

### 6.2 Inventario de ofrendas

- Máximo **5 objetos** en todo el juego.
- Pueden aparecer **objetos nuevos por nivel**; el inventario permite **reutilizar** objetos de salas anteriores.
- Temas culturales a cubrir con ellos: **comida local**, **artefacto**, **objeto sagrado / de respeto**, más 1–2 utilitarios del trámite.
- Lectura social, no combate.

### 6.3 Trámite X5j9-2a

- Nombre placeholder del permiso / expediente: **X5j9-2a**.
- El jugador reúne **3 sellos** visibles en el documento ilegible: **Sello 1** (Lobby), **Sello 2** doble (Buffet, con BG), **Sello 3** (Oficina central / Sala 4).  
- La **Sala 3 (Archivo) no da sello**; solo autoriza el paso (con o sin BG).  
- Señales de avance (sin traducción): sello en el documento · acceso a la siguiente sala · reacción de BGJAO#%5.  
- Completar X5j9-2a **con BG** = quedarte (ending completo). Sin BG = **final malo**.

### 6.4 Marcas / reputación (implícitas)

Sin medidor explicativo en HUD. Las reacciones y el tipo de ayuda cambian según lo acumulado. El jugador lo nota en el mundo, no en un tutorial.

### 6.5 Errores y Game Over

No hay combate. El peligro es social, ritual y burocrático.

| Tipo | Curva | Efecto |
|------|-------|--------|
| **Error recuperable** | Empieza en **3** (nivel 1) y **baja hasta 0** en el último nivel | Ayuda opaca (BG o interlocutor) sin traducir |
| **Error fatal** | Solo **2** en toda la experiencia: **nivel 1** y **nivel 4** | Game Over. Reintento desde el último sello |

#### Fatales (lista acordada v2)

1. **Nivel 1 (Lobby):** hacer **cualquier gesto** ante el **guardia** *antes* de haber hablado con BGJAO#%5 (actuar sin guía = ofensa fatal de turista).  
2. **Nivel 4 (Oficina central) / final malo:** cerrar el X5j9-2a **sin BGJAO#%5** (p. ej. tras el atajo de la **comida** en el Archivo, que te deja pasar solo).

Tone de muerte: absurdo (comedia) y a la vez frío e injusto (terror) — el sistema actúa como si fuera obvio y legítimo.

---

## 7. Estructura de niveles y experiencia (20–40 min)

### 7.1 Premisa de entrada

1. El jugador **recibe un premio**: viaje todo pago.  
2. Redime el viaje → aparece en un mundo extraño.  
3. Debe atravesar **4 salas lineales** de una **oficina de aduanas** (lobby → … → oficina central con fuerzas locales).  
4. En el camino: costumbres sagradas, respeto cultural, artefactos y **comida local** — siempre vía mecánicas opacas.

### 7.0 Beat 0 — El premio (intro, ~1–3 min)

**Función:** explicar *por qué* estás aquí sin tutorial de mecánicas; contrastar un mundo **legible** con el mundo **opaco** que viene.  
**Formato recomendado:** micro-escena interactiva corta + tránsito (cutscene). Cuenta como el **5.º mapa** ligero *o* solo cutscene si hay que ahorrar producción.

#### Regla de lenguaje (importante)
- En el Beat 0 el texto puede ser **legible** (español): es “tu” mundo.  
- En cuanto aterrizas en aduana, **todo** el texto del mundo pasa a **Aphonic**.  
Ese corte es la primera promesa del mensaje del juego.

#### Beats (secuencia)

| # | Beat | Qué ve / hace el jugador | Emoción | Notas de diseño |
|---|------|---------------------------|---------|-----------------|
| 0.1 | **Anuncio** | Pantalla o mostrador de “sorteo / premio”: *viaje todo pago*. UI clara, tono banal y alegre. | Ligereza, comedia suave | Sin mecánicas de gesto aún |
| 0.2 | **Redención** | Interactúa una vez: firmar / tocar / canjear el premio. Recibe un **boleto/comprobante** (puede ser el obj. #5 o solo prop de cutscene). | Expectativa | 1 interacción máxima |
| 0.3 | **Tránsito** | Cutscene corta: transporte abstracto (luz, ruido, ventanilla, sueño). El audio va de familiar → raro. | Transición | 15–40 s; sin controles |
| 0.4 | **Aterrizaje** | Fundido a la **Sala 1 (Lobby)**. Primer cartel en **Aphonic**. Nadie te habla. | Confusión | Aquí muere la legibilidad |
| 0.5 | **Enganche** | El jugador puede moverse; el juego ya es el loop social opaco. BG visible a lo lejos o en su punto fijo. | Curiosidad | Sin popup de tutorial |

#### Qué NO hacer en el Beat 0
- No enseñar P1–P4 / T1–T4 todavía.  
- No explicar el mensaje del juego.  
- No poner combate, menús largos ni lore denso.  
- No traducir nada “por si acaso” después del aterrizaje.

#### Checklist Beat 0
- [ ] Arte de mostrador/sorteo (o collage UI)  
- [ ] 1 interacción de canje  
- [ ] Cutscene de tránsito (o secuencia de stills)  
- [ ] Hard cut: texto legible → **Aphonic**  
- [ ] Spawn en Lobby con documento X5j9-2a vacío (0 sellos)  

#### Variante low-cost
Si no hay mapa 5: todo el Beat 0 es **cutscene no interactiva** de 60–90 s que termina en el Lobby. Se pierde un poco de agencia, se gana velocidad de producción.

### 7.2 Presupuesto de producción (techo)

| Recurso | Máximo |
|---------|--------|
| Mapas | **5** (premio/llegada opcional + 4 salas, o 4 salas + 1 auxiliar) |
| NPCs | **8** (varios solo flavor; **1 tipo de culto** repetible: mismos en apariencia/rol) |
| Objetos | **5** |

### 7.3 Curva emocional

**Confusión → risa → terror → revelación**  
(con sub-beats: confusión → ansiedad absurda → miedo burocrático → calidez → decisión frágil)

### 7.4 Las 4 salas (lineales)

| # | Sala | Emoción dominante | Interacciones | Recuperables | Fatal | Sello | Contenido cultural / mecánico |
|---|------|-------------------|---------------|--------------|-------|-------|-------------------------------|
| 1 | **Lobby** | Confusión + **risa** | 3–4 | **3** | **Sí (#1)** | **Sello 1** | Ver §7.7 (detalle) |
| 2 | **Buffet / costumbres** | Ansiedad absurda | 4–5 | **2+** (resets suaves) | No | **Sello 2 (doble)** | Ver §7.8 (detalle) |
| 3 | **Archivo** | **Terror** burocrático | 4–6 | **1** | No | **Ninguno** (bloquea el paso) | Ver §7.9 (detalle) · libro correcto o atajo de comida |
| 4 | **Oficina central (fuerzas locales)** | **Calidez** + revelación (si hay BG) | 2–3 | **0** | **Final malo** sin BG | **Sello 3** + salida del país | Ver §7.10 |

**Señales de progreso en todas las salas:** sello en el documento X5j9-2a · puerta/acceso a la siguiente sala · reacción de BGJAO#%5.

### 7.5 NPCs (reparto tentativo dentro del techo de 8)

1. **BGJAO#%5** (vínculo; todas las salas)  
2. **Guardia Lobby** (Sello 1 · fatal #1)  
3. **Flavor Lobby A**  
4. **Flavor Lobby B**  
5. **Culto / comensales** (mismo tipo visual, repetible; en Sala 2 comen y no se interrumpen)  
6. **Servidor/a del buffet** (Sala 2)  
7. **Guardia Sala 2** (sello doble simultáneo)  
8. **Bibliotecario + Guardia Archivo + Autoridad Sala 4** — *presión de cupo:* priorizar bibliotecario y autoridad; el guardia del archivo puede reusar el sprite/tipo del guardia Sala 2 si hace falta (mismo “cuerpo burocrático”, distinta función)

### 7.6 Objetos (cupo de 5 — propuesta)

| # | Objeto (placeholder) | Dónde entra | Rol |
|---|----------------------|-------------|-----|
| 1 | **Artefacto inútil (Lobby)** | Sala 1 | Baratija / easter egg en el resto del juego; en Sala 2 ofrenda incorrecta = reset suave |
| 2 | **Artefacto sagrado / correcto Sala 2** | Se recoge en Sala 1 | Clave del buffet; luego baratija / easter egg |
| 3 | **Comida local** | Sala 2 (tras pasar) | Atajo del Archivo (pasas sin BG → rumbo a final malo); si no, easter egg |
| 4 | **Libro correcto (Archivo)** | Sala 3 → **clave en Sala 4** | Protocolo visual del rito de entrada; necesario para el cierre con la autoridad |
| 5 | **Formulario paralelo de BG** (visible) | Sala 2 | Sello doble; presencia simbólica del trámite compartido |

### 7.7 Detalle — Sala 1: Lobby

#### Premisa
El jugador entra al lobby de aduanas. Nadie inicia conversación: **solo responde si el jugador interactúa**. Emoción: confusión + risa por malentendidos blandos, con un peligro duro si actúas antes de aprender.

#### Cast (4 NPCs en esta sala)
| NPC | Rol |
|-----|-----|
| **Guardia** | Control de paso; evalúa el gesto; otorga **Sello 1** |
| **BGJAO#%5** | Punto fijo; enseña el **primer gesto** correcto |
| **Flavor A** | Mundo; no avanza el trámite |
| **Flavor B** | Mundo; no avanza el trámite |

#### Reglas de interacción
1. **NPCs no-BG:** texto en **Aphonic** + gesto de **“lárgate / sigue buscando”**. No dan la solución.  
2. **BGJAO#%5 (primera vez):** muestra el **gesto** que hay que reproducir (mímica; sin traducción).  
3. **BG (re-hablar):** puede repetir / reforzar el gesto.  
4. **Guardia — gesto correcto** (después de haber visto a BG): otorga **Sello 1** + abre la siguiente sala.  
5. **Guardia — cualquier gesto *antes* de hablar con BG:** **FATAL #1** → reinicio del lobby (o desde checkpoint de llegada).  
6. **Guardia — gesto incorrecto *después* de hablar con BG:** error recuperable (rechazo; se puede reintentar / volver con BG).  
7. **Guardia — ofrendar artefactos:** los **devuelve**; no deja pasar (recuperable).

#### Objetos en la sala (2)
| Objeto | Uso en Lobby | Uso después |
|--------|--------------|-------------|
| Artefacto A (inútil) | Se puede recoger; ofrenda al guardia = rechazo | No sirve en ninguna sala |
| Artefacto B (clave Sala 2) | Se puede recoger; ofrenda al guardia = rechazo | **Correcto / necesario en Sala 2** |

Ambos se pueden llevar. El inventario los conserva al salir.

#### Los 3 errores recuperables (propuesta cerrada para Sala 1)

| # | Acción del jugador | Qué pasa | Por qué enseña |
|---|--------------------|----------|----------------|
| R1 | Hablar con Flavor A o B (o insistir) | Aphonic + gesto “lárgate” | El mundo no te guía; hay que buscar a la persona correcta |
| R2 | Ofrendar Artefacto A o B al guardia | Los **devuelve**; no abre el paso | Los objetos de esta sala **no** son la llave del lobby |
| R3 | Tras hablar con BG, hacer el **gesto incorrecto** al guardia | Rechazo opaco; puedes reintentar o reconsultar a BG | Ya hay solución en el mundo; el fallo no es mortal si aprendiste |

#### Fatal #1
**Condición:** interactuar con el guardia usando el canal de **gesto/postura/tono** (cualquier opción) **sin** haber hablado antes con BGJAO#%5.  
**Lectura de diseño:** en esta cultura no se “improvisa” el saludo de umbral; hacerlo a ciegas es imperdonable.  
**Comedia:** el castigo es desproporcionado y burocrático. **Terror:** el sistema no explica por qué.

#### Flujo feliz (resumen)
1. Explorar / chocar con flavor (R1).  
2. (Opcional) Recoger artefactos; probar ofrendarlos al guardia (R2).  
3. Hablar con BG → aprende el gesto.  
4. (Opcional) Fallar el gesto una vez (R3) → corregir.  
5. Gesto correcto al guardia → **Sello 1** + puerta + reacción de BG.  

#### Flujo de muerte
1. Ir directo al guardia y gesticular sin pasar por BG → **Game Over**.

#### Checklist de contenido Sala 1
- [x] Mapa lobby (1 de ≤5) — **mockup base A** (`assets/mockups/lobby-sala1.png`)  

- [ ] 4 NPCs + animaciones: largate, gesto-tutorial BG, rechazo guardia, muerte ritual  
- [ ] 2 props recogibles  
- [ ] Documento X5j9-2a recibe Sello 1  
- [ ] Puerta a Sala 2  

### 7.8 Detalle — Sala 2: Buffet / costumbres

#### Premisa
Sala centrada en un **buffet grande**. Una persona sirve comida a quienes pasan el rito. La ansiedad absurda viene de copiar una costumbre que ves, no que lees. Aquí el juego enseña, sin texto, que **tu trámite y el de BG van juntos**.

#### Set y atmósfera
- Buffet dominante (set principal).  
- Comensales sentados comiendo.  
- BG visible realizando la secuencia correcta (tutorial por observación).  
- Guardia de paso al final de la sala (distinto al del lobby).

#### Cast (dentro del techo global)
| NPC / grupo | Rol |
|-------------|-----|
| **Servidor/a del buffet** | Recibe ofrenda → entrega comida |
| **Comensales** (flavor / posible culto) | Comen; **no se los puede interrumpir** |
| **BGJAO#%5** | Demuestra la secuencia; luego debe **hablar a la vez** con el guardia |
| **Guardia Sala 2** | Solo otorga el **sello doble** si BG y el jugador interactúan **al mismo tiempo** |

#### Secuencia que demuestra BG (el jugador debe copiarla)
1. Se acerca al buffet.  
2. **Entrega algo** (ofrenda).  
3. **Recibe comida**.  
4. **Se sienta**.  

El jugador debe hacer lo mismo usando el **artefacto sagrado / correcto** traído del Lobby (objeto #2).

#### Reglas del buffet
| Condición | Resultado |
|-----------|-----------|
| Ofrendar el **artefacto correcto** (Lobby → Sala 2) | Recibe comida y puede sentarse → rito cumplido |
| Llegar al buffet **sin ítem** | **Reset suave** → inicio de la Sala 2 |
| Ofrendar el **ítem equivocado** (artefacto inútil u otro) | **Reset suave** → inicio de la Sala 2 |
| Interrumpir a un **comensal** | **Reset suave** → inicio de la Sala 2 |

**Reset suave ≠ Game Over:** no es fatal; repites la sala desde el inicio (inventario se mantiene, salvo decisiones de diseño menores).

#### Prueba de salida — sello doble (momento clave)
- Para salir, **BGJAO#%5 y el protagonista deben hablar con el guardia al mismo tiempo**.  
- El guardia estampa un **sello doble**: uno en el **X5j9-2a** del jugador (**Sello 2**) y otro en el **formulario paralelo de BG**.  
- Lectura de diseño: aquí el jugador **nota** que sin ella el sistema no cierra (preparación del fatal #2 / ending).

Implementación jugable sugerida (sin código aún): el guardia solo acepta la interacción si BG está en su “slot” de ventanilla / al lado del jugador; si el jugador habla solo, rechazo opaco (Aphonic + gesto) — preferible como soft fail, no fatal.

#### Después de pasar
- El jugador **puede volver** al buffet y **adquirir un ítem de comida** (objeto #3) para usar en salas posteriores.  
- La puerta a Sala 3 queda abierta.

#### Errores recuperables / resets de Sala 2
| # | Acción | Efecto | Enseñanza |
|---|--------|--------|-----------|
| R1 | Interrumpir comensales | Reset suave | Respeto: no se corta el rito ajeno |
| R2 | Buffet sin ítem o con ítem equivocado | Reset suave | La ofrenda correcta importa; observaste a BG |
| R3 (blando) | Hablar al guardia **sin** BG presente | Rechazo opaco; no hay sello | El trámite es **compartido** |

(R1 y R2 cubren la cuota de recuperables duros de la sala; R3 refuerza el tema del vínculo.)

#### Flujo feliz
1. Entras; ves a BG hacer ofrenda → comida → sentarse.  
2. Evitas molestar comensales.  
3. Ofrendas el artefacto correcto en el buffet → comes / te sientas.  
4. Te alineas con BG ante el guardia → **sello doble** en ambos formularios.  
5. (Opcional) Vuelves por el **ítem de comida**.  
6. Avanzas a Sala 3.

#### Checklist de contenido Sala 2
- [x] Mapa buffet — **mockup base** (`assets/mockups/buffet-sala2.png`)  

- [ ] Animación/demo de BG (ofrenda → comida → asiento)  
- [ ] Servidor, comensales, guardia Sala 2  
- [ ] Lógica de reset suave (3 triggers)  
- [ ] Interacción simultánea jugador + BG con guardia  
- [ ] Sello 2 en X5j9-2a + sello en formulario BG  
- [ ] Re-entrada para recoger comida  

### 7.9 Detalle — Sala 3: Archivo

#### Premisa
Sala de **archivo** custodiada. **No otorga sello**; su función es **impedir el paso** a la Oficina central hasta cumplir la norma (o tomar un atajo que abandona a BG). Tono: terror burocrático frío — reglas opacas, orden impuesto sobre un caos ya existente.

#### Set
- Interior: estanterías + libros fuera de lugar.  
- Exterior inmediato: **puerta / guardia** hacia Sala 4.  
- BG dentro del archivo (punto fijo de consulta verbal).

#### Cast
| NPC | Rol |
|-----|-----|
| **Bibliotecario/a** | Custodio en un **mostrador junto a la entrada**; **intercepta al instante** al **entrar** y al **salir** de la sala (auto-diálogo); solo permite **llevarse un libro**; hace cumplir el orden de estanterías |
| **BGJAO#%5** | Solo **información verbal** (Aphonic); **no** señala ubicaciones — ella tampoco sabe dónde van |
| **Guardia (fuera del archivo)** | Controla el paso a Sala 4 |

#### Mostrador de entrada (regla de flujo)
- El bibliotecario **no** está en el fondo del archivo: su booth flanquea el umbral sur (desde Buffet).  
- Cruzar la zona de mostrador **al entrar** → diálogo inmediato (Aphonic + gestos de custodia / reglas opacas).  
- Cruzar **al salir** (hacia el umbral del guardia o de vuelta al Buffet) → **re-chequeo** inmediato: si llevas libro sin ordenar / libro de más, rechazo soft; si el orden está OK y llevas solo el sobrante, deja pasar.  
- El jugador no puede “esquivar” al bibliotecario para entrar o salir del archivo.

#### Puzzle central — 3 estanterías / 4 libros
- Hay **3 estanterías** y **4 libros** (ya desordenados).  
- El jugador debe **colocar los 3 libros correspondientes** en las **3 estanterías** correctas.  
- El libro que **sobra** es el **libro correcto** (objeto #4): el único que puede llevarse.  
- Regla del bibliotecario: **solo un libro** sale de la sala.  
- Regla de orden: los libros **no pueden quedar** en lugares donde no van (aunque al entrar ya estén mal); el jugador debe dejar las 3 estanterías “bien” según la lógica opaca del archivo.

Señalización sin traducción: marcas Aphonic en lomos/estantes, formas, colores, o reacciones del bibliotecario (acepta / rechaza colocaciones). BG puede dar pistas verbales abstractas (Aphonic + gesto de duda), nunca un mapa.

#### Recuperable (único de la sala) — propuesta
| # | Acción | Efecto | Enseñanza |
|---|--------|--------|-----------|
| R1 | Intentar salir con un libro **antes** de ordenar, o colocar un libro en estantería **incorrecta** de forma “confirmada” | El bibliotecario **rechaza** / deshace (soft); no hay Game Over | El archivo prioriza el orden sobre tu prisa |

*(Si al playtest hace falta más fricción, el rechazo del guardia exterior sin libro correcto también es soft, no fatal.)*

#### Salidas hacia Sala 4

**A — Camino correcto (buen rumbo al ending)**  
1. Ordenar las 3 estanterías.  
2. Tomar el libro que sobra.  
3. Hablar con el guardia exterior: aparece una **opción adicional de diálogo** si llevas el libro correcto.  
4. El guardia deja pasar **al jugador y a BG**.

**B — Atajo de la comida (rumbo al final malo)**  
1. Presentar el **ítem de comida** (objeto #3, adquirido tras el buffet).  
2. El guardia te deja pasar **a ti solo**.  
3. **BG no puede pasar**.  
4. Si aun así completas los pasos de la **Sala 4**, obtienes el **final malo** (equivalente / continuidad del fatal #2: cerrar el trámite sin ella).

Lectura de diseño: la comida es “soborno cultural” que te privilegia como turista y **rompe el vínculo**. El mensaje del juego se vuelve jugable.

#### Qué no hay en Sala 3
- No hay Sello 3 aquí (el **Sello 3** queda para la Oficina central / cierre).  
- BG no hace demo espacial del puzzle.

#### Flujo feliz
1. Consultar a BG (pistas verbales insuficientes pero calmantes / confusas).  
2. Ordenar 3 libros → 3 estanterías.  
3. Llevarse el cuarto libro.  
4. Opción extra con el guardia → pasan juntos a Sala 4.

#### Checklist de contenido Sala 3
- [x] Mapa archivo + umbral exterior con guardia — **mockup base** (`assets/mockups/archivo-sala3.png`)  

- [ ] 3 estanterías + 4 libros + lógica de matching opaco  
- [ ] Bibliotecario (límite 1 libro; rechazo de desorden)  
- [ ] BG solo diálogo Aphonic  
- [ ] Opción extra de diálogo con libro correcto (pasa jugador + BG)  
- [ ] Atajo comida (pasa solo el jugador)  
- [ ] Flag interno: `BG_acompañando` true/false hacia Sala 4  

### 7.10 Detalle — Sala 4: Oficina central / fuerzas locales

#### Premisa
Última sala de la aduana. Amplia, **vacía en el centro**. El peso lo ponen las miradas y el mostrador final. Si llegaste **con BG**, ella **permanece siempre a tu lado** (ya no es NPC estático de punto fijo). Tono de los últimos minutos: **muy cálido** — el juego insiste, sin sermón traducible, en lo importante de **compartir y comunicarse** con quien no entiendes.

#### Set
- Pasillo de entrada → sala abierta.  
- **Varios militares** forman un **pasillo central** (dos filas hacia el centro de la sala) que conduce al mostrador; miran hacia el corredor por donde avanzas (presión visual; no se interactúa con ellos).  
- Al fondo: **mostrador** con una **mujer mayor** esperando.  
- Salida de aduana visible tras el rito (el juego **corta** cuando cruzan ese umbral).

#### Cast
| NPC | Rol |
|-----|-----|
| **Mujer mayor (autoridad civil de entrada)** | Única interacción jugable; otorga **Sello 3** si el rito se cumple |
| **BGJAO#%5** | Si está: compañera pegada al jugador; **hace los gestos** del protocolo frente a la mujer |
| **Militares (flavor)** | Ambiente; miran la entrada; sin diálogo útil |

#### Objeto clave
- El **libro del Archivo** muestra (en imágenes / Aphonic / diagramas opacos) el **ritual-protocolo de entrada al país**.  
- El resto de objetos del inventario son **baratijas / easter eggs** si se usan aquí u en el resto del juego.

#### Prueba del Sello 3 (camino completo — con BG)
1. El jugador solo puede interactuar con la **mujer mayor**.  
2. BG, a tu lado, **realiza gestos** frente a ella (el protocolo del libro, vivido).  
3. El jugador debe **seguir / reproducir esos gestos**.  
4. Si se logra: **Sello 3** en el X5j9-2a → el jugador y BG **entran al país**.  
5. El jugador solo ve hasta que **salen de la sala de aduana** (fund cálido, sin explicación verbal del mensaje).

**0 errores recuperables:** aquí no hay red. O estás con ella y aciertas el espejo del gesto, o no.

#### Camino sin BG (atajo de la comida u otro abandono)
- No hay quien demuestre el protocolo en vivo.  
- Interactuar solo con la mujer mayor **no produce el rito compartido**.  
- Resultado: **final malo** (el trámite se cierra en falso, te expulsan, o “entras” solo de forma vacía — sabor a definir en implementación, pero la lectura es: **sin vínculo no hay entrada verdadera**).  
- Continuidad del antiguo fatal #2.

#### Revelación (sin texto claro)
El calor del cierre —gestos juntos, sello, salir lado a lado— debe hacer sentir que **comunicarse no es entender del todo**, es **compartir el riesgo del malentendido** y elegir no abandonar al otro.

#### Flujo feliz
1. Entras con BG; militares observan; ella no se separa.  
2. Llevas el libro (protocolo).  
3. Ante la mujer mayor, BG gesticula; tú copias.  
4. Sello 3 → cruzan la salida de aduana → fundido / créditos.  

#### Checklist de contenido Sala 4
- [x] Mapa sala amplia + mostrador + anillo de militares — **mockup base** (`assets/mockups/oficina-sala4.png`)  

- [ ] BG en modo “seguidora” (solo si `BG_acompañando`)  
- [ ] Secuencia de gestos BG → input del jugador (espejo)  
- [ ] Uso/presencia del libro como protocolo  
- [ ] Sello 3 + animación de salida conjunta  
- [ ] Rama sin BG → final malo  
- [ ] Dirección de audio/luz **cálida** en el cierre bueno  

### 7.11 Tabla maestra — gestos / tonos / ofrendas por sala

Léxico: **§6.1.1**. El jugador elige entre P1–P4 y T1–T4 cuando el prompt de ritual está activo; las ofrendas usan el inventario.

#### Sala 1 — Lobby

| Momento | Canal activo | Correcto | Incorrecto / notas |
|---------|--------------|----------|-------------------|
| Flavor A/B | (NPC) | — | NPC responde **W-GO** + Aphonic |
| BG tutorial | Demo **W-DEMO** | Enseña **P1** (+ opcional **T2** como “voz” del saludo) | Re-hablar = repetir demo |
| Guardia **antes** de BG | Postura (y/o tono) | — | **Cualquier P/T → FATAL #1** |
| Guardia **después** de BG | Postura (+ tono si se usa) | **P1** (y **T2** si el prompt incluye tono) | Otra P/T → recuperable R3 |
| Guardia + ofrenda | Ofrenda | — | Artefacto A o B → los **devuelve** (R2); no abre paso |

**Sello 1** = P1 (T2) correcto al guardia tras ver a BG.

#### Sala 2 — Buffet

| Momento | Canal activo | Correcto | Incorrecto / notas |
|---------|--------------|----------|-------------------|
| Observar a BG | (Demo de mundo) | Secuencia: ofrenda → recibe comida → **P4** (sentarse/espera) | Tutorial por observación |
| Buffet (servidor) | Ofrenda | **Artefacto sagrado** (obj. #2) | Sin ítem o ítem equivocado → **reset suave** |
| Tras ofrenda correcta | Postura | **P4** en el asiento / zona de comer | Si se omite, el rito no cuenta como completo (soft) |
| Comensales | — | No interactuar | Interrumpir → **reset suave** |
| Guardia Sala 2 | Presencia + interacción | Hablar **a la vez** con BG; sello doble. Prompt ritual opcional: **T4** + **P2** (trámite compartido) | Sin BG → rechazo **W-GO** (R3 blando) |

**Sello 2 (doble)** = presencia conjunta (+ T4/P2 si se implementa el prompt).

#### Sala 3 — Archivo

| Momento | Canal activo | Correcto | Incorrecto / notas |
|---------|--------------|----------|-------------------|
| BG | Verbal Aphonic + **W-DOUBT** | Pistas sin ubicaciones | No hay demo espacial |
| Estanterías | Puzzle de colocación | 3 libros en 3 estantes “correctos” | Confirmación en estante malo → rechazo bibliotecario (R1) |
| Bibliotecario | Regla de mundo | Solo **1 libro** sale (el que sobra) | Intentar salir antes de ordenar → rechazo |
| Guardia exterior + **libro** | Diálogo / ofrenda implícita | Opción extra → pasan **jugador + BG** | Sin libro: no aparece la opción |
| Guardia exterior + **comida** | Ofrenda | Atajo: pasas **solo** | BG no pasa → flag `BG_acompañando = false` |

Aquí casi no hay menú P/T; el “gesto” crítico es el de duda de BG y el respeto al no interrumpir el orden.

#### Sala 4 — Oficina central

| Momento | Canal activo | Correcto | Incorrecto / notas |
|---------|--------------|----------|-------------------|
| Entrada con BG | — | BG en modo seguidora | Sin BG → rama final malo |
| Libro | Protocolo visual | Debe estar en inventario / mostrarse en el rito | Baratijas no sustituyen el libro |
| Mujer mayor — paso 1 | Postura | Espejo de BG: **P1** | Fallo → no hay recuperable; el rito no avanza / falla el cierre |
| Mujer mayor — paso 2 | Tono | Espejo de BG: **T2** | Idem |
| Mujer mayor — paso 3 | Postura | Espejo de BG: **P3** (anclar al documento/suelo del mostrador) | Idem |
| Mujer mayor — paso 4 | Postura | Espejo de BG: **P4** (espera compartida) | Idem |
| Cierre | — | **Sello 3** + salida juntos | Sin BG: no hay cadena de espejo → **final malo** |

Secuencia del protocolo (también dibujada de forma opaca en el libro): **P1 → T2 → P3 → P4**.  
BG la ejecuta delante de la mujer mayor; el jugador la copia paso a paso. Cierre **cálido**.

#### Resumen rápido (qué “ganar” en cada sala)

| Sala | Lo que hay que acertar | Castigo si fallas |
|------|------------------------|-------------------|
| 1 | **P1** (+**T2**) al guardia **después** de BG | Antes de BG = fatal; después = soft; ofrenda = soft |
| 2 | Ofrenda obj. #2 + **P4**; salida con BG (**T4**/**P2** opcional) | Reset suave / rechazo sin BG |
| 3 | Ordenar libros → llevar el sobrante; pasar **con** BG | Soft bibliotecario; comida = atajo sin BG |
| 4 | Espejo **P1→T2→P3→P4** con BG y el libro | Sin red; sin BG = final malo |

---

## 8. Narrativa y referentes

- Entrada: **premio → viaje → aduana alienígena**.
- Lore por ambiente y reacción, no por exposición traducida.
- Temas jugables: **respeto a costumbres**, lo sagrado, artefactos, comida local — siempre opacos.
- País / burocracia corruptos; violencia estructural de fondo (guerra, desplazamiento) en la motivación de BGJAO#%5 y el clima; **sin tabúes explícitos** forzados en esta versión.
- Referentes: **Outer Wilds**, **Fatum Betula** / **To the Moon**, **Arrival** / **The Shape of Water**.

---

## 9. Lenguaje ficcional — escritura **Aphonic**

Sistema de escritura del mundo (no es un conlang fonético completo todavía; es la **capa visual** del idioma opaco).

| Campo | Valor |
|--------|--------|
| Nombre | **Aphonic** |
| Archivo | [`fonts/Aphonic-Regular.ttf`](./fonts/Aphonic-Regular.ttf) |
| Tipo | Unicase, glifos angulares abstractos sin ojos; mínimo parentesco con alfabeto latino/español |
| Uso | Carteles, documento X5j9-2a, UI del mundo, papeles burocráticos |
| Entrada | Se escribe en teclado latino (A–Z, 0–9…); se renderiza ilegible |

**Regla:** todo texto “del mundo” usa Aphonic. Nunca se acompaña de traducción.  
Hojas de muestra: [`fonts/preview/`](./fonts/preview/). Notas de uso: [`fonts/README.md`](./fonts/README.md).

**Pendiente de diseño lingüístico (siguiente capa):** fonología / sílabas / si el habla de NPCs tiene “palabras” inventadas además de la tipografía.

## 10. Arte, audio y técnica (provisional)

| Área | Dirección |
|------|-----------|
| Arte | Pixel art estilo RPG Maker; dirección de mundo **TBD** |
| Escritura | Fuente **Aphonic** (ver §9) |
| Audio | Voces alienígenas no lingüísticas para el canal de tono; ambiente que alterne inquietud y absurdo |
| UI | Mínima; no diccionarios ni barras que “expliquen” el idioma |
| Motor | Unity 2D cuando haya desarrollo; Unreal descartado por alcance |
| Scope jam | Sin multijugador, sin combate, sin traductor, sin mapa grande, sin múltiples endings de trama |

---

## 11. Fuera de alcance

- Combate
- Multijugador / online
- Cualquier forma de traducción in-game
- Múltiples endings de trama
- Crafting profundo / sistemas de build
- Mundo abierto grande

---

## 12. Criterios de éxito

1. El jugador termina **sin haber “aprendido el idioma”** y aun así siente el mensaje.
2. **BGJAO#%5** se siente indispensable, no un tutorial con voz.
3. Al menos un momento de **risa** y uno de **miedo** nacen del mismo sistema de malentendido.
4. Una partida completa cabe en **20–40 minutos**.
5. Los fatales se sienten justos en retrospectiva (había señales sociales), no arbitrarios.

---

## 13. Decisiones abiertas

- Título definitivo del juego.
- Dirección visual de la oficina de aduanas (sci-fi / pixel art concreto).
- Nombres “reales” detrás de `X5j9-2a` y `BGJAO#%5` — o mantener opacidad.
- ~~Beat del premio~~ → ver **§7.0** (elegir en producción: micro-mapa vs cutscene low-cost).
- ~~Diseño fino de gestos/tonos por sala~~ → ver **§6.1.1** y **§7.11** (validar con playtest).
- Cómo se ve/suena el documento al ganar cada sello.
- Qué hace exactamente el **culto** (flavor puro vs una interacción clave).
- Variación de tono del ending único (métricas mínimas).
- Gramática / fonética más allá de Aphonic.

---

## 14. Historial de diseño (resumen)

- Mensaje y restricción lingüística como centro.
- Supervivencia lingüística (opción B): el malentendido puede doler.
- Protagonista silencioso; trámite absurdo para quedarte.
- Sistema de 3 canales + ofrendas + sellos + GO sin combate.
- NPC compañera como safeguard; pocos fatales; mayoría recuperables con ayuda opaca.
- Duración 20–40 min; un solo ending.
- Fuente **Aphonic** (v5.1) como escritura visual del mundo.
- Niveles: 4 salas lineales en aduana, 3 sellos, curva confusión→risa→terror→revelación; techo 5 mapas / 8 NPC / 5 objetos.
- Sala 1 (Lobby) detallada: BG enseña gesto; guardia valida; fatal si gesticulas antes de BG; 2 artefactos (1 inútil, 1 para sala 2).
- Sala 2 (Buffet) detallada: copiar rito de BG con artefacto sagrado; resets suaves; sello doble simultáneo con BG; comida tras pasar.
- Sala 3 (Archivo) detallada: ordenar 3/4 libros; sin sello; paso con libro+BG o atajo comida sin BG → final malo.
- Sala 4 (Oficina) detallada: BG a tu lado; espejo de gestos ante mujer mayor; libro = protocolo; cierre cálido; final malo sin BG.
- Léxico P1–P4 / T1–T4 y tabla maestra de gestos por sala (§7.11).
- Beat 0 del premio (§7.0): mundo legible → tránsito → aduana en Aphonic.
