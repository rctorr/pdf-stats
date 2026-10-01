# Guía de Documentación y Buenas Prácticas de Gooey (v1.0.8+)

Este documento recopila las reglas oficiales, estructura y configuraciones comprobadas de **Gooey** para el proyecto `pdf-stats`.

---

## 📌 1. Estructura Recomendada y Zen de Python

### Principios aplicados:
* **"Explicit is better than implicit":** Se usan únicamente los parámetros documentados oficialmente en `@Gooey` y `GooeyParser`.
* **"Simple is better than complex":** Evitar hackear diccionarios privados internos (como `_language_pack` o `_TRANSLATIONS`). Si Gooey no ofrece un parámetro oficial para un botón o icono en cierta plataforma, no se debe adivinar ni forzar mediante monkey-patching frágil.
* **Separación clara:** Mantener la lógica de cálculo (`compute_stats`) totalmente desacoplada de la interfaz gráfica (`parse_args`).

---

## ⚙️ 2. Parámetros Oficiales del Decorador `@Gooey`

| Parámetro | Tipo | Descripción | Comprobado |
| :--- | :--- | :--- | :---: |
| `program_name` | `str` | Título de la aplicación en la ventana principal. | ✅ |
| `program_description` | `str` | Subtítulo descriptivo en el panel superior. | ✅ |
| `default_size` | `tuple` | Ancho y alto inicial de la ventana en píxeles: `(ancho, alto)`. | ✅ |
| `language` | `str` | Idioma de la interfaz (ej. `'spanish'`). | ✅ |
| `navigation` | `str` | Modo de navegación (`'NONE'`, `'TABBED'`, `'SIDEBAR'`). Usar `'NONE'` para 1 solo argumento. | ✅ |
| `header_bg_color` | `str (HEX)` | Color de fondo del encabezado superior (ej. `#1e293b`). | ✅ |
| `header_title_color` | `str (HEX)` | Color de texto del título en la cabecera. | ✅ |
| `header_subtitle_color`| `str (HEX)` | Color de texto del subtítulo en la cabecera. | ✅ |
| `body_bg_color` | `str (HEX)` | Color de fondo del área principal de inputs. | ✅ |
| `footer_bg_color` | `str (HEX)` | Color de fondo de la barra de botones inferior. | ✅ |
| `terminal_panel_color` | `str (HEX)` | Color de fondo de la consola de resultados. | ✅ |
| `terminal_font_color` | `str (HEX)` | Color de texto de la salida de consola. | ✅ |
| `show_success_modal` | `bool` | Muestra u oculta el modal emergente de éxito al terminar (`False` recomendado). | ✅ |
| `header_show_icon` | `bool` | Muestra u oculta el icono por defecto en la cabecera. | ✅ |
| `richtext_controls` | `bool` | Habilita/Deshabilita el formateo rich-text en consola (dejar en `False` por incompatibilidad con la librería `colored`). | ✅ |

---

## 🎨 3. Personalización de Widgets (`GooeyParser`)

Para los argumentos, se utiliza `GooeyParser` en lugar del `argparse` estándar:

```python
parser = GooeyParser(description="...")
parser.add_argument(
    "pdf_file",
    metavar="Archivo PDF",
    help="Selecciona el archivo PDF a analizar",
    widget="FileChooser",
    gooey_options={
        "wildcard": "Archivos PDF (*.pdf)|*.pdf"
    }
)
```

---

## ❓ 4. Limitaciones y Comportamientos de Plataforma (Lo que no se debe forzar)

1. **Modificación de Cadenas Internas de Botones:**
   * **Estado:** En Gooey v1.0.8+, la modificación manual de `i18n._language_pack` o `i18n._TRANSLATIONS` falla porque la API interna de internacionalización es privada y varía según la versión.
   * **Solución Estándar:** Usar `language='spanish'`. Las etiquetas nativas del paquete de idioma español son `"Cancelar"`, `"Examinar"` y `"Empezar"`. No se debe realizar monkey-patching sobre atributos privados.

2. **Renderizado de GTK3 en Linux (Ubuntu Dark Mode):**
   * El color de los campos de texto e inputs es gestionado por la integración de `wxPython` con GTK3. Al usar `body_bg_color="#ffffff"`, Gooey dibuja el fondo blanco mientras que GTK3 mantiene los botones nativos del sistema.
