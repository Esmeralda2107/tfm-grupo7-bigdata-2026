# 🗂️ Datos Limpios

Este directorio reúne las **fuentes en su versión limpia**, resultado del primer procesamiento aplicado sobre los datos originales del proyecto con el objetivo de transformar los datasets en una forma más estructurada, legible y preparada para su uso posterior.

Las bases limpias se organizan por dimensión temática:

- **`alquiler/`**: base de elaboración propia con información estructurada de precios de alquiler comercial por zona.
- **`censo/`**: archivos temáticos depurados y reorganizados a partir de la fuente censal, con información sociodemográfica clave.
- **`competencia/`**: base tratada de establecimientos gastronómicos, incluyendo clasificaciones analíticas de competencia.
- **`seguridad/`**: registros delictivos depurados y reclasificados para su análisis territorial posterior.
- **`movilidad/`**: base de estaciones y flujos de transporte con métricas agregadas útiles para el análisis de movilidad.
- **`lugares_interes/`**: base depurada y categorizada de equipamientos y puntos de interés urbanos.
- **`zonas/`**: capa geográfica limpia de las unidades territoriales de Manhattan empleadas como referencia común.

Los archivos contenidos en este directorio son el **producto de la ejecución de los notebooks de limpieza** desarrollados en Python y organizados en la carpeta **`notebooks/01_limpieza/`** del repositorio.

En esta fase, cada fuente original fue sometida a procesos de:

- depuración,
- filtrado,
- reorganización,
- reclasificación,
- generación de variables,
- y estructuración inicial de la información.

Los archivos aquí almacenados constituyen el insumo directo para las etapas posteriores de **integración territorial, consolidación de entidades y construcción del dataset maestro**, desarrolladas en las siguientes fases del repositorio.
