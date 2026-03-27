# 🧹 Notebooks de Limpieza

Este directorio contiene los **notebooks de limpieza** utilizados en la primera fase de procesamiento de las fuentes del proyecto.

Su función principal es transformar los datos originales almacenados en **`datos/crudos/`** en versiones más estructuradas, legibles y analíticamente útiles, que posteriormente se almacenan en **`datos/limpios/`**.

En esta fase se desarrollan procesos como:

- la depuración de registros,
- el filtrado espacial y temático,
- la reorganización de estructuras,
- la reclasificación de categorías,
- la generación de variables,
- y la preparación de salidas limpias para su uso posterior.

Los notebooks incluidos en esta carpeta son:

- **`01_Limpieza_Inspecciones_DOHMH.ipynb`**: limpieza y clasificación inicial de la fuente de competencia gastronómica.
- **`02_Limpieza_Seguridad_NYPD.ipynb`**: depuración y reclasificación de la fuente de seguridad urbana.
- **`03_Data_Cleaning_FactFinder.ipynb`**: reorganización inicial de los archivos crudos del censo.
- **`04_Limpieza_Censo.ipynb`**: limpieza final y estructuración temática de la información censal.
- **`05_Limpieza_MTA.ipynb`**: tratamiento inicial de la fuente de movilidad y generación de métricas agregadas.
- **`06_Limpieza_Common_Places.ipynb`**: depuración y categorización de la fuente de lugares de interés.
- **`08_Filtrado_y_Limpieza_Cartografia_Manhattan.ipynb`**: filtrado y limpieza de la cartografía base de zonas.

Los resultados de esta fase se almacenan en **`datos/limpios/`** y constituyen el insumo directo para la etapa posterior de integración territorial.
