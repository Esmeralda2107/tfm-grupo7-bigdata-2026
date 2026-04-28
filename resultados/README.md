# 📈 Resultados del Proyecto

Este directorio reúne los **resultados generados en las fases analíticas del proyecto**, una vez completada la construcción del dataset maestro.

Su función principal es almacenar las salidas producidas por los procesos de **clustering**, **scoring** y **escenarios**, permitiendo conservar tanto los resultados intermedios de análisis como las versiones finales utilizadas en la interpretación estratégica y en la aplicación desarrollada en **Streamlit**.

La organización de esta carpeta responde a las principales fases analíticas del proyecto:

- **`04_clustering/`**: contiene los resultados de la segmentación territorial de Manhattan mediante distintas técnicas de agrupamiento. Aunque se conservan varias soluciones para fines comparativos, la solución finalmente adoptada en el proyecto para las fases posteriores es **K-Means con k = 4**.
- **`05_scoring/`**: incluye los resultados del sistema de scoring construido a partir del dataset maestro y de las dimensiones estratégicas del estudio.
- **`06_escenarios/`**: reúne los resultados derivados de la aplicación de distintos escenarios de decisión sobre el sistema de scoring.

En conjunto, esta carpeta representa la salida de las fases analíticas del proyecto y se relaciona directamente con las carpetas **`datos/maestro/`**, **`notebooks/`**, **`scripts/`**, **`streamlit_app.py`** y **`anexos/`** del repositorio.
