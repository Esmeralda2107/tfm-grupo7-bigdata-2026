# TFM Grupo 7 Big Data 2026

Repositorio técnico del proyecto de **Location Intelligence** desarrollado para el análisis territorial de Manhattan y la priorización de zonas para apertura de negocio.

Este repositorio reúne los datos, notebooks, scripts, resultados, documentación complementaria y la aplicación interactiva necesarios para reproducir el flujo principal del proyecto, desde las fuentes originales hasta la visualización final de resultados.

## 📂 Estructura del repositorio

- **`datos/`**: datos organizados según su etapa de procesamiento.
  - **`crudos/`**: fuentes originales del proyecto.
  - **`limpios/`**: salidas del proceso de limpieza y transformación inicial.
  - **`base_datos/`**: entidades estructuradas para su implementación en SQL.
  - **`maestro/`**: versiones finales del dataset maestro.
- **`notebooks/`**: notebooks de Python utilizados en las fases de limpieza, integración, construcción del dataset maestro, scoring y escenarios.
- **`scripts/`**: scripts desarrollados en R Markdown para la fase de clustering.
- **`sql/`**: implementación de la base de datos relacional y modelo entidad–relación.
- **`resultados/`**: salidas analíticas generadas en las fases de clustering, scoring y escenarios.
- **`anexos/`**: documentación complementaria del proyecto.
- **`streamlit_app.py`**: aplicación interactiva para la exploración visual de resultados.
- **`.streamlit/`**: configuración de la aplicación Streamlit.
- **`requirements.txt`**: dependencias principales de Python para la ejecución local.

## 🧭 Alcance del repositorio

Este repositorio incluye el flujo completo de trabajo del proyecto:

- recopilación y organización de fuentes;
- limpieza y transformación inicial de datos;
- integración territorial;
- estructuración de entidades para base de datos;
- construcción del dataset maestro;
- segmentación territorial mediante clustering;
- construcción del sistema de scoring;
- generación de escenarios de decisión;
- y visualización final mediante Streamlit.

## ⚙️ Requisitos previos

Para ejecutar localmente el proyecto se recomienda contar con:

- **Python 3.10 o superior**
- **Jupyter Notebook** o **JupyterLab**
- **MySQL Server 8.x**
- **MySQL Workbench**
- entorno con soporte para ejecución de **R Markdown** en la fase de clustering

Las dependencias principales de Python se encuentran recogidas en el archivo **`requirements.txt`** del repositorio.

## ▶️ Orden general de ejecución del flujo de trabajo

La lógica general de ejecución del proyecto sigue esta secuencia:

### 1. Limpieza de datos

Ejecutar los notebooks de:

**`notebooks/01_limpieza/`**

Estos notebooks toman como entrada los archivos de **`datos/crudos/`** y generan las salidas correspondientes en **`datos/limpios/`**.

### 2. Integración territorial

Ejecutar los notebooks de:

**`notebooks/02_integracion/`**

Este proceso toma como entrada los archivos de **`datos/limpios/`** y genera las entidades estructuradas almacenadas en **`datos/base_datos/`**.

### 3. Construcción del dataset maestro

Ejecutar los notebooks de:

**`notebooks/03_dataset_maestro/`**

Estos notebooks toman como entrada los archivos de **`datos/base_datos/`** y generan las distintas versiones del dataset maestro en **`datos/maestro/`**.

### 4. Clustering

Ejecutar los scripts de:

**`scripts/04_clustering/`**

Esta fase utiliza como base las versiones analíticas del dataset maestro y genera los resultados de clusterización en **`resultados/04_clustering/`**.

### 5. Scoring

Ejecutar los notebooks de:

**`notebooks/05_scoring/`**

Esta fase toma como entrada el dataset maestro y la solución de clustering seleccionada, y genera las salidas de scoring en **`resultados/05_scoring/`**.

### 6. Escenarios

Ejecutar los notebooks de:

**`notebooks/06_escenarios/`**

Esta fase toma como entrada los resultados de scoring y genera las salidas de escenarios en **`resultados/06_escenarios/`**.

### 7. Visualización interactiva

Ejecutar la aplicación:

**`streamlit_app.py`**

La aplicación permite explorar de forma visual los resultados del modelo a partir de los datos y salidas analíticas del repositorio.

## 🗄️ Reproducción de la base de datos SQL

La implementación SQL del proyecto se encuentra en la carpeta **`sql/`** y se apoya en las tablas contenidas en **`datos/base_datos/`**.

La carpeta **`sql/`** incluye:

- el script principal de creación de la base de datos;
- y el archivo editable del modelo entidad–relación en MySQL Workbench.

## 🔄 Trazabilidad general del repositorio

La trazabilidad principal del flujo de trabajo puede resumirse así:

**`datos/crudos/`** → **`notebooks/01_limpieza/`** → **`datos/limpios/`**  
**`datos/limpios/`** → **`notebooks/02_integracion/`** → **`datos/base_datos/`**  
**`datos/base_datos/`** → **`notebooks/03_dataset_maestro/`** → **`datos/maestro/`**  
**`datos/maestro/`** → **`scripts/04_clustering/`** → **`resultados/04_clustering/`**  
**`datos/maestro/`** + **`resultados/04_clustering/`** → **`notebooks/05_scoring/`** → **`resultados/05_scoring/`**  
**`resultados/05_scoring/`** → **`notebooks/06_escenarios/`** → **`resultados/06_escenarios/`**  
**`datos/`** + **`resultados/`** → **`streamlit_app.py`**

## 📌 Nota

Cada carpeta del repositorio incluye su propio `README.md` con una descripción más específica de su contenido, su función y su relación con el resto del flujo de trabajo.
