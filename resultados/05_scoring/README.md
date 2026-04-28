# 🎯 Resultados de Scoring

Este directorio reúne los **resultados de la fase de scoring** del proyecto, orientada a transformar el dataset maestro en un sistema de puntuaciones comparable entre zonas de Manhattan.

Su función principal es almacenar las salidas generadas por el modelo de scoring, construido a partir de las distintas dimensiones estratégicas del estudio y apoyado en la solución de clusterización finalmente adoptada en el proyecto: **K-Means con k = 4**.

En esta carpeta se incluyen los siguientes resultados:

- **`scoring_micro.csv`**: archivo con las puntuaciones a nivel micro, correspondientes a las variables o subdimensiones que componen cada dimensión estratégica.
- **`scoring_macro.csv`**: archivo con las puntuaciones agregadas a nivel macro, correspondientes a las dimensiones estratégicas consolidadas por zona.

Los archivos aquí almacenados constituyen la salida de la fase de **scoring** y sirven como insumo directo para la construcción de **escenarios de decisión**, así como para su posterior explotación en la aplicación desarrollada en **Streamlit**.
