#!/usr/bin/env python3
"""
__main__.py — Punto de entrada del comando pdf-stats.

Uso:
    pdf-stats archivo.pdf
"""

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import pdfplumber


# ---------------------------------------------------------------------------
# Tipos de datos
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PDFStats:
    """Estadísticas extraídas de un documento PDF."""

    filepath: Path
    pages: int
    lines: int
    words: int
    chars: int

    def __str__(self) -> str:
        separator = "-" * 40
        return (
            f"\n{separator}\n"
            f"  Archivo : {self.filepath.name}\n"
            f"{separator}\n"
            f"  Páginas : {self.pages:>10,}\n"
            f"  Líneas  : {self.lines:>10,}\n"
            f"  Palabras: {self.words:>10,}\n"
            f"  Caracteres: {self.chars:>8,}\n"
            f"{separator}\n"
        )


# ---------------------------------------------------------------------------
# Lógica principal
# ---------------------------------------------------------------------------

def extract_text_from_pdf(filepath: Path) -> list[str]:
    """Extrae todas las líneas de texto de cada página del PDF."""
    lines: list[str] = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            lines.extend(page_text.splitlines())
    return lines


def count_pages(filepath: Path) -> int:
    """Retorna el número de páginas del PDF."""
    with pdfplumber.open(filepath) as pdf:
        return len(pdf.pages)


def compute_stats(filepath: Path) -> PDFStats:
    """Calcula y retorna las estadísticas del PDF."""
    pages = count_pages(filepath)
    lines = extract_text_from_pdf(filepath)

    non_empty_lines = [line for line in lines if line.strip()]
    all_text = " ".join(non_empty_lines)

    return PDFStats(
        filepath=filepath,
        pages=pages,
        lines=len(non_empty_lines),
        words=len(all_text.split()),
        chars=len(all_text.replace(" ", "")),
    )


# ---------------------------------------------------------------------------
# Interfaz de línea de comandos
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Define y procesa los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Muestra estadísticas de un archivo PDF.",
        epilog="Ejemplo: pdf-stats documento.pdf",
    )
    parser.add_argument(
        "pdf_file",
        type=Path,
        help="Ruta al archivo PDF que se desea analizar.",
    )
    return parser.parse_args()


def validate_pdf_path(path: Path) -> None:
    """Valida que el archivo exista y tenga extensión .pdf."""
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: '{path}'")
    if not path.is_file():
        raise ValueError(f"La ruta no es un archivo: '{path}'")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"El archivo no tiene extensión .pdf: '{path}'")


def main() -> int:
    """Punto de entrada principal. Retorna el código de salida."""
    args = parse_args()

    try:
        validate_pdf_path(args.pdf_file)
        stats = compute_stats(args.pdf_file)
        print(stats)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Error inesperado al procesar el PDF: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
