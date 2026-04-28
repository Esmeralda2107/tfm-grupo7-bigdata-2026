# ⚙️ Scripts de Clustering

Este directorio reúne los **scripts de clusterización** desarrollados en el proyecto como parte de la fase de segmentación territorial de Manhattan.

Su función principal es aplicar distintas metodologías de agrupamiento sobre la versión estandarizada del dataset maestro, con el objetivo de identificar patrones territoriales y construir tipologías de zonas según sus características sociodemográficas, urbanas y comerciales.

En esta fase se desarrollan procesos como:

- la carga de la base analítica estandarizada,
- la selección de variables numéricas relevantes para el clustering,
- la aplicación de distintas técnicas de agrupamiento,
- la evaluación e interpretación de las soluciones obtenidas,
- la generación de visualizaciones analíticas,
- y la exportación de resultados para su análisis comparativo y uso posterior en las fases del proyecto.

Los scripts se organizan según el método empleado:

- **`K-Means/`**: contiene el script correspondiente a la solución de clustering obtenida mediante el algoritmo **K-Means**.
- **`Ward.D/`**: contiene el script correspondiente a la solución de clustering obtenida mediante el método jerárquico **Ward.D**.

Los resultados de esta fase se almacenan en **`resultados/04_clustering/`**. Aunque en esta carpeta se conservan distintas soluciones de clusterización con fines comparativos, la solución finalmente adoptada en el proyecto para las etapas posteriores de **scoring**, **escenarios** y visualización en **Streamlit** es **K-Means con k = 4**.
