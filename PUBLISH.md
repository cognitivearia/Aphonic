# Publicar en GitHub + GitHub Pages

**Repositorio:** [cognitivearia/Aphonic](https://github.com/cognitivearia/Aphonic)  
**Visor (Pages):** https://cognitivearia.github.io/Aphonic/

---

## Si ya clonaste el repo en Windows (recomendado)

En tu clon local, `origin` **ya apunta** a GitHub. **No** uses `git remote add github` (eso era solo para el entorno de Cursor).

### Opción A — Pegar el zip del diseño

1. Descarga `Aphonic-design.zip` desde el chat / artifacts del agente.
2. En PowerShell:

```powershell
cd ruta\a\tu\clon\Aphonic
# Extrae el zip AQUÍ (sobrescribe README vacío si lo hay)
Expand-Archive -Path "$HOME\Downloads\Aphonic-design.zip" -DestinationPath . -Force

git add .
git status
git commit -m "Add design docs, assets, and mockup viewer"
git push -u origin main
```

3. Activa Pages: [Settings → Pages](https://github.com/cognitivearia/Aphonic/settings/pages) → **Source: GitHub Actions**.
4. En la pestaña **Actions**, espera el workflow *Deploy mockup viewer to GitHub Pages*.

### Opción B — Solo si trabajas desde el remoto de Cursor

No aplica en la mayoría de PCs (ese remoto no es GitHub). Ignórala si ya tienes el clon de `cognitivearia/Aphonic`.

---

## Errores frecuentes

| Mensaje | Causa | Qué hacer |
|---------|--------|-----------|
| `repository not found` | URL mal / sin permiso / sin login | `gh auth login` o revisa que seas colaborador de `cognitivearia/Aphonic` |
| `remote github already exists` / confusión de remotos | Mezclaste instrucciones de Cursor | En tu clon solo debe existir `origin` → GitHub |
| `failed to push some refs` | `main` remoto tiene commits distintos (README inicial) | `git pull origin main --rebase` y luego `git push` |

Comprobar remotos en tu PC:

```powershell
git remote -v
# Debe verse algo como:
# origin  https://github.com/cognitivearia/Aphonic.git (fetch)
# origin  https://github.com/cognitivearia/Aphonic.git (push)
```

---

## Verificar el build en local (opcional)

```powershell
cd mockup-viewer
npm ci
npm run build
npm run preview
```

---

## Contenido

| En el repo | En Pages |
|------------|----------|
| GDD, one-pager, fonts, assets, mockups | Visor estático (`mockup-viewer/dist`) |
