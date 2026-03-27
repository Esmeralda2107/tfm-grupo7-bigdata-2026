# 🗂️ Dataset Maestro

Este directorio reúne los **datasets maestros del proyecto**, resultado de la fase final de consolidación y preparación analítica de los datos.

Los archivos contenidos en esta carpeta representan la capa más integrada del TFM, ya que concentran en una sola estructura la información procedente de las distintas dimensiones trabajadas en etapas anteriores: **censo, competencia, seguridad, movilidad, lugares de interés, zonas y precio de alquiler**.

En esta etapa, las entidades previamente estructuradas en la carpeta **`datos/base_datos/`** fueron combinadas y transformadas para construir una base analítica única, preparada para su uso en las siguientes fases del proyecto.

Los archivos contenidos en este directorio son el **producto de la ejecución de los notebooks** organizados en la carpeta **`notebooks/03_dataset_maestro/`** del repositorio.

En esta carpeta se incluyen, entre otros, los siguientes resultados:

- **`MASTER_DATASET_MANHATTAN.csv`**: versión consolidada inicial del dataset maestro.
- **`MASTER_DATASET_MANHATTAN_DENSIDAD.csv`**: versión con transformaciones asociadas a métricas de densidad.
- **`MASTER_DATASET_MANHATTAN_LIMPIO.csv`**: versión depurada para preparación analítica.
- **`MASTER_DATASET_MANHATTAN_ML.csv`**: versión final del dataset maestro utilizada como base para las etapas posteriores de análisis.
- **`MASTER_DATASET_MANHATTAN_ZSCORE.csv`**: versión estandarizada del dataset maestro, preparada para su uso en técnicas analíticas comparativas.
- **`DATASET_REVISION_TOTAL.zip`**: archivo auxiliar de revisión y control de consistencia del proceso de consolidación, almacenado en formato comprimido por limitaciones de tamaño.

Los archivos aquí almacenados constituyen la **salida final de la fase de construcción de datos** y el punto de partida para las etapas posteriores de **clustering, scoring y escenarios** desarrolladas en el proyecto.
