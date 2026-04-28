# 🗂️ Datos del Proyecto

Este directorio reúne los **datos utilizados en el desarrollo del TFM**, organizados según su nivel de procesamiento y su función dentro del trabajo. Su contenido permite seguir la evolución de la información desde las fuentes originales hasta la construcción del dataset maestro final.

Los datos aquí almacenados constituyen la **base operativa del sistema de análisis** y recogen tanto los archivos de entrada como las salidas intermedias y finales generadas durante las fases de limpieza, integración y consolidación.

La organización de esta carpeta responde a las principales etapas del tratamiento de datos:

- **`crudos/`**: contiene las fuentes originales recopiladas para el proyecto.
- **`limpios/`**: incluye los datos resultantes de los procesos de depuración, transformación y estructuración inicial.
- **`base_datos/`**: reúne las entidades estructuradas para su integración en la base de datos relacional del proyecto.
- **`maestro/`**: contiene las versiones finales del dataset maestro utilizadas como base para el análisis posterior.

En conjunto, esta carpeta constituye el soporte central del flujo de datos del proyecto y se relaciona directamente con las carpetas **`notebooks/`**, **`sql/`**, **`resultados/`** y **`anexos/`** del repositorio.
