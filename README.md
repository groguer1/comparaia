# CompararIA 🤖

Sitio web estático de comparativas de herramientas de IA para freelancers y autónomos en España.  
Alojado en **GitHub Pages** — gratuito, rápido, sin servidor.

---

## Estructura del repositorio

```
comparaia.es/
├── index.html                          ← Página de inicio
├── sitemap.xml                         ← Sitemap para Google
├── robots.txt                          ← Instrucciones para bots
├── README.md                           ← Este archivo
│
├── comparativas/
│   ├── chatgpt-vs-claude/
│   │   └── index.html
│   ├── mejores-ia-escribir/
│   │   └── index.html
│   ├── mejores-ia-diseno/
│   │   └── index.html
│   ├── ia-gratis-vs-pago/
│   │   └── index.html
│   ├── chatgpt-vs-gemini/
│   │   └── index.html
│   └── mejores-ia-codigo/
│       └── index.html
│
├── herramientas/
│   ├── chatgpt/
│   │   └── index.html
│   ├── claude/
│   │   └── index.html
│   ├── midjourney/
│   │   └── index.html
│   └── notion-ia/
│       └── index.html
│
├── guias/
│   ├── ia-para-autonomos-espana/
│   │   └── index.html
│   ├── ia-para-freelancers/
│   │   └── index.html
│   ├── herramientas-ia-gratis/
│   │   └── index.html
│   └── ia-facturas-contabilidad/
│       └── index.html
│
├── blog/
│   └── index.html
│
└── assets/
    ├── og-image.png                    ← Imagen Open Graph principal (1200×630)
    ├── og-chatgpt-vs-claude.png
    ├── og-guia-autonomos.png
    ├── og-chatgpt.png
    ├── og-claude.png
    └── logo.png
```

> **Regla importante:** cada sección usa `index.html` dentro de su carpeta.  
> Así la URL queda limpia: `comparaia.es/comparativas/chatgpt-vs-claude/`  
> en lugar de `comparaia.es/comparativas/chatgpt-vs-claude.html`

---

## Cómo subir el sitio a GitHub Pages — paso a paso

### 1. Crear la cuenta en GitHub (si no tienes una)

1. Ve a [github.com](https://github.com) y crea una cuenta gratuita
2. Elige un nombre de usuario — este aparecerá en la URL temporal del sitio

### 2. Crear el repositorio

1. Haz clic en **"New repository"** (botón verde, arriba a la derecha)
2. Nombre del repositorio: `comparaia` (o el que prefieras)
3. Marca la opción **"Public"** — necesario para GitHub Pages gratuito
4. Deja el resto por defecto y haz clic en **"Create repository"**

### 3. Subir los archivos

**Opción A — Desde el navegador (más fácil):**

1. En la página del repositorio, haz clic en **"uploading an existing file"**
2. Arrastra todos los archivos y carpetas al área de subida
3. Escribe un mensaje como `"Primer commit: estructura inicial"`
4. Haz clic en **"Commit changes"**

> ⚠️ GitHub no permite subir carpetas vacías. Asegúrate de que cada carpeta tenga al menos un `index.html`.

**Opción B — Con Git desde terminal (más eficiente a largo plazo):**

```bash
# Clonar el repositorio vacío
git clone https://github.com/TU_USUARIO/comparaia.git
cd comparaia

# Copiar aquí todos los archivos del sitio
# ...

# Subir
git add .
git commit -m "Primer commit: estructura inicial"
git push origin main
```

### 4. Activar GitHub Pages

1. En tu repositorio, ve a **Settings** (pestaña superior)
2. En el menú lateral izquierdo, haz clic en **"Pages"**
3. En **"Source"**, selecciona **"Deploy from a branch"**
4. En **"Branch"**, selecciona `main` y carpeta `/ (root)`
5. Haz clic en **"Save"**

En 1-2 minutos tu sitio estará en:  
`https://TU_USUARIO.github.io/comparaia/`

---

## Conectar un dominio propio (cuando lo compres)

Una vez tengas el dominio `comparaia.es`:

### Paso 1 — Crear el archivo CNAME

Crea un archivo llamado `CNAME` (sin extensión) en la raíz del repositorio con este contenido:

```
comparaia.es
```

### Paso 2 — Configurar los DNS del dominio

En el panel de tu registrador de dominio, añade estos registros DNS:

| Tipo | Nombre | Valor |
|------|--------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | TU_USUARIO.github.io |

### Paso 3 — Activar HTTPS

1. En **Settings → Pages**, en el campo **"Custom domain"**, escribe `comparaia.es`
2. Marca la casilla **"Enforce HTTPS"**
3. Espera 24-48 horas a que los DNS propaguen

---

## Cómo actualizar el sitio

Cada vez que modifiques un archivo y lo subas a GitHub, el sitio se actualiza automáticamente en menos de 2 minutos.

**Desde el navegador:**
1. Navega al archivo que quieres editar en GitHub
2. Haz clic en el icono del lápiz (editar)
3. Haz los cambios
4. Haz clic en **"Commit changes"**

**Actualizar el sitemap tras añadir una página nueva:**
1. Abre `sitemap.xml`
2. Añade el bloque `<url>` correspondiente
3. Actualiza el `<lastmod>` de las páginas modificadas

---

## Tareas pendientes

- [ ] Conectar dominio `comparaia.es` cuando se compre
- [ ] Configurar Cloudflare delante de GitHub Pages (CDN + SSL + protección)
- [ ] Subir sitemap a Google Search Console
- [ ] Crear imágenes Open Graph (`assets/og-*.png`, tamaño 1200×630px)
- [ ] Crear páginas de herramientas: Midjourney, Notion IA
- [ ] Crear páginas de comparativas pendientes
- [ ] Crear páginas de guías pendientes
- [ ] Crear página `aviso-legal/index.html`
- [ ] Crear página `privacidad/index.html`
- [ ] Crear página `contacto/index.html`
- [ ] Primer artículo de blog (1 al mes)

---

## Cómo añadir una nueva página

1. Crea la carpeta correspondiente dentro de la sección adecuada
2. Crea el `index.html` dentro de esa carpeta con la estructura de las páginas existentes
3. Añade la URL al `sitemap.xml`
4. Añade el enlace en las páginas relacionadas y en la navegación si procede
5. Sube los cambios a GitHub

**Ejemplo — Nueva comparativa "Claude vs Gemini":**

```
comparativas/
└── claude-vs-gemini/
    └── index.html       ← URL: comparaia.es/comparativas/claude-vs-gemini/
```

---

## SEO — Checklist por página

Cada página nueva debe incluir:

- [ ] `<title>` único con keyword principal (máx. 60 caracteres)
- [ ] `<meta name="description">` (máx. 155 caracteres)
- [ ] `<link rel="canonical">` apuntando a su propia URL
- [ ] Open Graph: `og:title`, `og:description`, `og:image`, `og:url`
- [ ] Twitter Card
- [ ] Schema.org apropiado (Article, FAQPage, SoftwareApplication...)
- [ ] Un solo `<h1>` por página
- [ ] Breadcrumb navegable con `<nav aria-label="Ruta de navegación">`
- [ ] URL en `sitemap.xml`
- [ ] `alt` en todas las imágenes

---

*Construido con HTML estático puro. Sin frameworks, sin base de datos, sin dependencias.*
