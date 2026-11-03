const roomsEl = document.getElementById("rooms");
const variantsEl = document.getElementById("variants");
const map = document.getElementById("map");
const layer = document.getElementById("hotspots");
const hover = document.getElementById("hover");
const blurb = document.getElementById("blurb");
const panelTitle = document.getElementById("panelTitle");
const subtitle = document.getElementById("subtitle");
const zoom = document.getElementById("zoom");
const showLabels = document.getElementById("showLabels");
const showAnnotated = document.getElementById("showAnnotated");

let rooms = [];
let currentRoom = null;
let maps = [];
let current = null;
let hotspots = null;

async function loadRooms() {
  const res = await fetch("/assets/rooms.json");
  const data = await res.json();
  rooms = data.rooms;
  roomsEl.innerHTML = "";
  for (const r of rooms) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = r.title;
    btn.dataset.id = r.id;
    btn.addEventListener("click", () => selectRoom(r.id));
    roomsEl.appendChild(btn);
  }
  const params = new URLSearchParams(location.search);
  const startRoom = params.get("room") || "oficina";
  await selectRoom(startRoom, params.get("v"));
}

async function selectRoom(roomId, mapOverride) {
  currentRoom = rooms.find((r) => r.id === roomId) || rooms[0];
  if (!currentRoom) return;
  roomsEl.querySelectorAll("button").forEach((b) => {
    b.classList.toggle("active", b.dataset.id === currentRoom.id);
  });
  const res = await fetch(`/assets/${currentRoom.variantsFile}`);
  const data = await res.json();
  maps = data.maps;
  variantsEl.innerHTML = "";
  for (const m of maps) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = m.title;
    btn.dataset.id = m.id;
    btn.addEventListener("click", () => selectMap(m.id));
    variantsEl.appendChild(btn);
  }
  const chosen = data.chosen || currentRoom.defaultMap || maps[0]?.id;
  await selectMap(mapOverride || chosen);
}

async function selectMap(id) {
  current = maps.find((m) => m.id === id) || maps[0];
  if (!current) return;
  variantsEl.querySelectorAll("button").forEach((b) => {
    b.classList.toggle("active", b.dataset.id === current.id);
  });
  panelTitle.textContent = current.title;
  blurb.textContent = current.blurb;
  subtitle.textContent = `${currentRoom.title} — ${current.blurb}`;
  const hotRes = await fetch(`/assets/${current.file}-hotspots.json`);
  hotspots = await hotRes.json();
  if (hotspots.blurb) blurb.textContent = hotspots.blurb;
  map.src = showAnnotated.checked
    ? `/assets/${current.file}-annotated.png`
    : `/assets/${current.file}.png`;
  buildHotspots();
  history.replaceState(
    null,
    "",
    `?room=${currentRoom.id}&v=${current.id}`,
  );
}

function applyZoom() {
  if (!hotspots) return;
  const z = Number(zoom.value);
  map.style.width = `${hotspots.map_w * hotspots.tile * z}px`;
  map.style.height = `${hotspots.map_h * hotspots.tile * z}px`;
  layer.style.width = map.style.width;
  layer.style.height = map.style.height;
  layer.querySelectorAll(".hotspot").forEach((el) => {
    const x = Number(el.dataset.x);
    const y = Number(el.dataset.y);
    el.style.left = `${(x + 0.5) * hotspots.tile * z}px`;
    el.style.top = `${(y + 0.5) * hotspots.tile * z}px`;
  });
}

function buildHotspots() {
  layer.innerHTML = "";
  for (const e of hotspots.entities) {
    const el = document.createElement("button");
    el.type = "button";
    el.className = "hotspot";
    el.dataset.kind = e.kind;
    el.dataset.x = e.x;
    el.dataset.y = e.y;
    el.title = e.label;
    el.setAttribute("aria-label", e.label);
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = e.label.split("—")[0].trim();
    el.appendChild(tag);
    el.addEventListener("mouseenter", () => {
      hover.textContent = e.label;
    });
    el.addEventListener("focus", () => {
      hover.textContent = e.label;
    });
    layer.appendChild(el);
  }
  layer.classList.toggle("hide-labels", !showLabels.checked);
  applyZoom();
}

showLabels.addEventListener("change", () => {
  layer.classList.toggle("hide-labels", !showLabels.checked);
});
showAnnotated.addEventListener("change", () => {
  if (!current) return;
  map.src = showAnnotated.checked
    ? `/assets/${current.file}-annotated.png`
    : `/assets/${current.file}.png`;
});
zoom.addEventListener("input", applyZoom);

loadRooms();
