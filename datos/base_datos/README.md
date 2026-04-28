# 🗂️ Base de Datos

Este directorio reúne las **entidades estructuradas** del proyecto en la etapa de base de datos, resultado del procesamiento, integración y organización territorial aplicados sobre las fuentes limpias.

Los archivos contenidos en esta carpeta corresponden a una versión consolidada de la información, organizada según la lógica del modelo de datos del proyecto y preparada para su implementación en SQL y para la posterior construcción del dataset maestro.

Las entidades se distribuyen por dimensión temática:

- **`alquiler/`**: tabla estructurada con la información de precio de alquiler comercial por zona.
- **`censo/`**: tabla consolidada con los indicadores sociodemográficos relevantes para el análisis.
- **`competencia/`**: tabla estructurada con los establecimientos clasificados como competencia dentro del área de estudio.
- **`seguridad/`**: tabla con los registros delictivos organizados para su agregación y análisis territorial.
- **`movilidad/`**: tabla con la información de estaciones y métricas agregadas de movilidad.
- **`lugares_interes/`**: tabla estructurada de equipamientos y puntos de interés con utilidad analítica.
- **`zonas/`**: tabla territorial base con los identificadores y atributos espaciales de referencia.

Los archivos de este directorio son el resultado de las etapas de integración y estructuración desarrolladas en los notebooks del repositorio, y constituyen la base para la implementación del modelo relacional y para la posterior construcción del **dataset maestro**.

Esta carpeta representa la etapa en la que las fuentes ya limpias pasan a una estructura común y consistente, sirviendo como insumo directo para las siguientes fases del proyecto, en particular para la construcción del **dataset maestro**, proceso desarrollado en la carpeta **`notebooks/03_dataset_maestro/`**.
