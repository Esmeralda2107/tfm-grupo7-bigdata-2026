# 🧩 Resultados de Clustering

Este directorio reúne los **resultados de la fase de clustering** del proyecto, orientada a la segmentación territorial de Manhattan a partir de las características integradas del dataset maestro.

Su función principal es almacenar las salidas generadas por las distintas técnicas de agrupamiento aplicadas en el análisis, permitiendo comparar soluciones alternativas de clusterización y conservar tanto los resultados tabulares como los informes analíticos asociados.

Los resultados se organizan según el método empleado:

- **`K-Means/`**: contiene la solución de clustering obtenida mediante el algoritmo **K-Means**, incluyendo la asignación final de clusters y el informe analítico correspondiente.
- **`Ward.D/`**: contiene la solución de clustering obtenida mediante el método jerárquico **Ward.D**, incluyendo la asignación final de clusters y el informe analítico correspondiente.

Los archivos aquí almacenados constituyen la salida de la fase de segmentación territorial del proyecto. Aunque en esta carpeta se conservan distintas soluciones de clusterización para fines comparativos, la solución finalmente adoptada para las etapas posteriores de **scoring**, **escenarios** y visualización en **Streamlit** es **K-Means con k = 4**.
