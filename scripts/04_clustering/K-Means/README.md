# ⚙️ Script de Clustering K-Means

Este directorio contiene el **script de clusterización K-Means** desarrollado en el proyecto como parte de la fase de segmentación territorial de Manhattan.

Su función principal es aplicar el algoritmo **K-Means** sobre la versión estandarizada del dataset maestro, con el objetivo de identificar patrones territoriales y construir una tipología de zonas según sus características sociodemográficas, urbanas y comerciales.

En esta fase se desarrollan procesos como:

- la carga de la base analítica estandarizada,
- la selección de variables numéricas relevantes para el clustering,
- la aplicación del algoritmo **K-Means**,
- la evaluación e interpretación de la solución de agrupamiento,
- la generación de visualizaciones analíticas,
- y la exportación de resultados para su uso posterior en las fases de **scoring**, **escenarios** y visualización en **Streamlit**.

El script incluido en esta carpeta es:

- **`K-Means_k4.Rmd`**: script en R Markdown utilizado para ejecutar la solución de **K-Means con k = 4**, documentar el análisis y generar las salidas finales asociadas a esta solución.

Los resultados de esta fase se almacenan en **`resultados/04_clustering/K-Means/`** y constituyen la solución de clustering finalmente adoptada en el proyecto para las etapas posteriores de análisis.
