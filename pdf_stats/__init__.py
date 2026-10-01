"""
pdf_stats — Paquete para analizar estadísticas de archivos PDF.

Expone la API pública mínima para uso como librería:
    - PDFStats: dataclass con los resultados
    - compute_stats: función principal de análisis
"""

from pdf_stats.__main__ import PDFStats, compute_stats

__all__ = ["PDFStats", "compute_stats"]
__version__ = "0.1.0"
