# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/)
y este proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

---

## [Unreleased]

> Los próximos cambios se documentarán aquí automáticamente.

---

## [0.1.4] - 2026-10-01

### Correcciones

- **CI:** Eliminar la opción `releases: write` en la sección `permissions` porque GitHub la marca como valor inesperado (no es una clave válida en el contexto de workflow-level permissions).

---

## [0.1.3] - 2026-10-01

### Correcciones

- **CI:** Agregar el bloque `permissions: contents: write` al workflow para que el `GITHUB_TOKEN` tenga permisos de crear releases al ser disparado por un push de tag.

---

## [0.1.2] - 2026-10-01

### Correcciones

- **CI (Windows):** Reemplazar el comando `zip` (no disponible en runners de Windows) por `Compress-Archive` de PowerShell.
- **CI (Linux):** Agregar `--find-links` apuntando a las ruedas precompiladas de wxPython para Ubuntu 22.04, evitando la compilación desde fuente y reduciendo el tiempo de build.

---

## [0.1.1] - 2026-10-01

### Correcciones

- **CI (Linux):** Instalar dependencias del sistema `libgtk-3-dev`, `libgstreamer-plugins-base1.0-dev` y `freeglut3-dev` antes de instalar wxPython, solucionando el error `Package 'gtk+-3.0' not found` durante la compilación.

---

## [0.1.0] - 2026-10-01

### Primera Release Pública 🎉

Esta es la primera versión estable y pública de **pdf-stats**.

### Añadido

- **Interfaz gráfica (GUI)** construida con [Gooey](https://github.com/chriskiehl/Gooey): selector de archivos nativo, barra de progreso y visualización de resultados.
- **Soporte multiplataforma** — ejecutables autónomos para Windows, macOS y Linux generados con PyInstaller.
- **Pipeline CI/CD** con GitHub Actions: compilación y publicación automática de releases al crear un tag `v*`.
- **Licencia GNU GPL v3** (`LICENSE.md`).
- **README** completo con instrucciones para usuarios no técnicos (descarga y doble clic) y para desarrolladores (entorno `uv`, CLI, librería Python, compilación local).
- **Guía de Gooey** (`guia-gooey.md`): documentación interna de las opciones del módulo, buenas prácticas y limitaciones conocidas.

### Funcionalidades

- Análisis de archivos PDF: número de páginas, líneas de texto no vacías, palabras y caracteres (sin espacios).
- Modo CLI: `pdf-stats documento.pdf`.
- Modo librería Python: `from pdf_stats import compute_stats`.
- `.gitignore` configurado para el proyecto.

---

[Unreleased]: https://github.com/rctorr/pdf-stats/compare/v0.1.4...HEAD
[0.1.4]: https://github.com/rctorr/pdf-stats/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/rctorr/pdf-stats/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/rctorr/pdf-stats/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/rctorr/pdf-stats/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/rctorr/pdf-stats/releases/tag/v0.1.0
