# pdf-stats

Herramienta de línea de comandos para analizar estadísticas de archivos PDF.

## Estadísticas que reporta

| Métrica | Descripción |
|---|---|
| Páginas | Número total de páginas del documento |
| Líneas | Número de líneas de texto no vacías |
| Palabras | Número total de palabras |
| Caracteres | Número de caracteres sin espacios |

## Instalación

Desde la carpeta `pdf-stats/`, ejecuta:

```bash
pip install -e .
```

Esto instala el comando `pdf-stats` en tu entorno Python activo.

## Uso

```bash
pdf-stats archivo.pdf
```

### Ejemplo de salida

```
----------------------------------------
  Archivo : documento.pdf
----------------------------------------
  Páginas :          6
  Líneas  :        354
  Palabras:      3,253
  Caracteres:   17,324
----------------------------------------
```

## Requisitos

- Python 3.10+
- [pdfplumber](https://github.com/jsvine/pdfplumber) ≥ 0.10 (se instala automáticamente)

## Uso como librería

También puedes importar las funciones directamente en tus scripts:

```python
from pdf_stats import compute_stats
from pathlib import Path

stats = compute_stats(Path("documento.pdf"))
print(f"Páginas: {stats.pages}, Palabras: {stats.words}")
```
