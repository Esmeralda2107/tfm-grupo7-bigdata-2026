# 🗂️ Datos

Esta carpeta organiza los datos del proyecto según su etapa de procesamiento.

- `crudos/`: fuentes originales del proyecto.
- `limpios/`: salidas del proceso de limpieza.
- `base_datos/`: entidades estructuradas para su implementación en SQL.
- `maestro/`: versiones finales del dataset maestro.

La trazabilidad general del repositorio sigue esta secuencia:

`datos/crudos/` → `notebooks/01_limpieza/` → `datos/limpios/`  
`datos/limpios/` → `notebooks/02_integracion/` → `datos/base_datos/`  
`datos/base_datos/` → `notebooks/03_dataset_maestro/` → `datos/maestro/`
