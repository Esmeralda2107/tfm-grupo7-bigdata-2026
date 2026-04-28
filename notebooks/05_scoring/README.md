# 🎯 Notebooks de Scoring

Este directorio contiene los **notebooks dedicados a la construcción del sistema de scoring** del proyecto.

Su función principal es tomar el **dataset maestro** ya consolidado en **`datos/maestro/`** y transformarlo en una estructura de puntuaciones comparable entre zonas, permitiendo evaluar el desempeño relativo de Manhattan en las distintas dimensiones estratégicas del estudio.

En esta fase se desarrollan procesos como:

- la transformación de variables a una escala común,
- la definición de ponderaciones locales por dimensión,
- la construcción de puntuaciones a nivel micro y macro,
- la integración del resultado de clusterización seleccionado en el proyecto,
- y la generación de salidas preparadas para la etapa posterior de escenarios y visualización en Streamlit.

El notebook incluido en esta carpeta es:

- **`13_Scoring.ipynb`**: construcción del sistema de scoring del proyecto, cálculo de puntuaciones micro y macro por zona e integración de la solución de clustering seleccionada.

Los resultados de esta fase se almacenan en **`resultados/05_scoring/`** y constituyen el insumo directo para la fase posterior de **escenarios**, así como para la aplicación desarrollada en **Streamlit**.
