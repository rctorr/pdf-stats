# pdf-stats 📊

Herramienta multiplataforma para analizar estadísticas de archivos PDF (páginas, líneas, palabras y caracteres), disponible con **interfaz gráfica (GUI)** intuitiva o desde la **línea de comandos (CLI)**.

---

## 🚀 Uso para Usuarios No Técnicos (Sin instalar Python)

Si solo deseas usar la aplicación sin configurar entornos ni usar comandos:

1. Ve a la sección de **[Releases de GitHub](https://github.com/tu-usuario/pdf-stats/releases)**.
2. Descarga el ejecutable comprimido para tu sistema operativo:
   - 🪟 **Windows:** `pdf-stats-windows.zip`
   - 🍏 **macOS:** `pdf-stats-macos.zip`
   - 🐧 **Linux:** `pdf-stats-linux.tar.gz`
3. Descomprime el archivo y haz **doble clic** sobre el ejecutable `pdf-stats` para abrir la interfaz gráfica.

---

## 🖥️ Interfaz Gráfica (GUI)

Al ejecutar `pdf-stats` sin argumentos (o haciendo doble clic en el ejecutable), se abrirá una ventana limpia e intuitiva donde podrás seleccionar cualquier archivo PDF usando el explorador de archivos nativo.

---

## 📊 Estadísticas que Reporta

| Métrica | Descripción |
|---|---|
| **Páginas** | Número total de páginas del documento |
| **Líneas** | Número de líneas de texto no vacías |
| **Palabras** | Número total de palabras extraídas |
| **Caracteres** | Número de caracteres sin contar espacios en blanco |

---

## 💻 Instalación para Desarrolladores

Si deseas instalar el paquete en tu entorno Python utilizando [`uv`](https://github.com/astral-sh/uv):

### 1. Crear entorno virtual e instalar dependencias

```bash
# Crear entorno virtual aislado
uv venv

# Activar entorno (Linux/macOS)
source .venv/bin/activate

# Instalar el proyecto en modo editable y sus herramientas
uv pip install -e .
uv pip install gooey pyinstaller six
```

### 2. Uso desde Línea de Comandos (CLI)

```bash
pdf-stats documento.pdf
```

#### Ejemplo de salida en consola:
```text
----------------------------------------
  Archivo : documento.pdf
----------------------------------------
  Páginas :          6
  Líneas  :        354
  Palabras:      3,253
  Caracteres:   17,324
----------------------------------------
```

---

## 📦 Compilación de Ejecutables Autónomos (PyInstaller)

Para generar el paquete ejecutable standalone en tu máquina local:

```bash
uv run pyinstaller --noconfirm --onedir --windowed --name "pdf-stats" --add-data "$(python3 -c 'import gooey, os; print(os.path.dirname(gooey.__file__))'):gooey" pdf_stats/__main__.py
```

El ejecutable generado se guardará en `dist/pdf-stats/`.

---

## ⚙️ Uso como Librería Python

También puedes importar los módulos directamente en tu propio código Python:

```python
from pathlib import Path
from pdf_stats import compute_stats

stats = compute_stats(Path("documento.pdf"))
print(f"Páginas: {stats.pages}, Palabras: {stats.words}, Caracteres: {stats.chars}")
```

---

## 🛠️ Requisitos del Entorno

- **Python:** ≥ 3.10
- **Librerías principales:** `pdfplumber` ≥ 0.10, `gooey` ≥ 1.0.8, `wxpython` ≥ 4.3.1
