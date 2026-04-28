# ⚙️ Scripts del Proyecto

Este directorio reúne los **scripts desarrollados para las fases analíticas complementarias del proyecto**, en particular aquellos implementados fuera del flujo principal de notebooks en Python.

Su función principal es documentar y ejecutar procesos específicos del análisis que, por su naturaleza metodológica, se desarrollaron en otros entornos de trabajo, permitiendo mantener separadas las tareas de construcción de datos y las de exploración analítica avanzada.

Actualmente, esta carpeta se organiza en la siguiente línea de trabajo:

- **`04_clustering/`**: contiene los scripts utilizados en la fase de segmentación territorial de Manhattan, incluyendo las soluciones de **K-Means** y **Ward.D** desarrolladas en **R Markdown**.

Los scripts aquí almacenados se relacionan directamente con la carpeta **`resultados/04_clustering/`**, donde se conservan las salidas generadas por estos procesos, y complementan el trabajo desarrollado en **`notebooks/`** y en la aplicación final de **Streamlit**.

## 📦 Dependencias utilizadas en los scripts de clustering

Los scripts de clustering desarrollados en **R Markdown** utilizan las siguientes librerías:

- **`dplyr`**
- **`tidyr`**
- **`ggplot2`**
- **`factoextra`**
- **`cluster`**
- **`FactoMineR`**
- **`sf`**
- **`writexl`**
- **`knitr`**
- **`kableExtra`**
- **`ggdendro`**
- **`fmsb`**
- **`viridis`**
- **`viridisLite`**
- **`plotly`**
