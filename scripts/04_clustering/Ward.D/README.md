# ⚙️ Script de Clustering Ward.D

Este directorio contiene el **script de clusterización jerárquica Ward.D** desarrollado en el proyecto como parte de la fase de segmentación territorial de Manhattan.

Su función principal es aplicar el método **Ward.D** sobre la versión estandarizada del dataset maestro, con el objetivo de identificar patrones territoriales y construir una tipología de zonas según sus características sociodemográficas, urbanas y comerciales.

En esta fase se desarrollan procesos como:

- la carga de la base analítica estandarizada,
- la selección de variables numéricas relevantes para el clustering,
- la aplicación del método jerárquico **Ward.D**,
- la evaluación e interpretación de la solución de agrupamiento,
- la generación de visualizaciones analíticas,
- y la exportación de resultados para su uso posterior en la comparación metodológica del proyecto.

El script incluido en esta carpeta es:

- **`Ward_D_k4.Rmd`**: script en R Markdown utilizado para ejecutar la solución de **Ward.D con k = 4**, documentar el análisis y generar las salidas finales asociadas a esta solución.

Los resultados de esta fase se almacenan en **`resultados/04_clustering/Ward.D/`** y constituyen una solución alternativa de clusterización conservada en el proyecto con fines comparativos frente a la solución finalmente adoptada.
