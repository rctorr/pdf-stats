#!/usr/bin/env python3
"""
__main__.py — Punto de entrada del comando pdf-stats (con interfaz Gooey).
"""

import sys
from dataclasses import dataclass
from pathlib import Path

from gooey import Gooey, GooeyParser
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


def validate_pdf_path(path: Path) -> None:
    """Valida que el archivo exista y tenga extensión .pdf."""
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: '{path}'")
    if not path.is_file():
        raise ValueError(f"La ruta no es un archivo: '{path}'")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"El archivo no tiene extensión .pdf: '{path}'")


# ---------------------------------------------------------------------------
# Interfaz de usuario (Gooey GUI + CLI)
# ---------------------------------------------------------------------------

@Gooey(
    program_name="Analizador de Estadísticas PDF",
    header_show_title=True,
    header_show_subtitle=True,
    header_show_icon=False,          # Oculta el icono de herramientas por defecto
    default_size=(640, 440),
    language="spanish",              # Idioma oficial en español (Cancelar, Examinar, Empezar)
    navigation="NONE",               # Oculta pestañas laterales e intermedias
    # --- Paleta de Colores ---
    header_bg_color="#1e293b",       # Azul Slate Oscuro
    header_title_color="#ffffff",     # Título Blanco
    header_subtitle_color="#cbd5e1",  # Subtítulo Gris Claro
    body_bg_color="#ffffff",         # Fondo de cuerpo Blanco
    footer_bg_color="#f1f5f9",       # Pie de página Gris Suave
    terminal_panel_color="#0f172a",  # Consola Azul Noche
    terminal_font_color="#38bdf8",   # Texto Resultados Azul Cian Neón
    richtext_controls=False,          # Evita incompatibilidad con la librería 'colored'
    show_stop_button=False,
    show_restart_button=False,
    show_success_modal=False,        # Desactiva el modal emergente redundante y evita la etiqueta no traducida "(Translate me!)"
)
def parse_args():
    """Define los argumentos del programa con un selector de archivos de Gooey."""
    parser = GooeyParser(description="Obtiene el número de caracteres, palabras, líneas y páginas.")
    
    parser.add_argument(
        "pdf_file",
        metavar="Archivo PDF",
        help="Selecciona el archivo PDF a analizar",
        widget="FileChooser",
        gooey_options={"wildcard": "Archivos PDF (*.pdf)|*.pdf"}
    )
    return parser.parse_args()


def main() -> int:
    """Punto de entrada principal."""
    args = parse_args()
    pdf_path = Path(args.pdf_file)

    try:
        validate_pdf_path(pdf_path)
        stats = compute_stats(pdf_path)
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
