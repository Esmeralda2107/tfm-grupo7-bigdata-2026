# 🎯 Metodología del scoring multicriterio

Este documento presenta la lógica metodológica del **sistema de scoring multicriterio** construido en el proyecto para priorizar las zonas de Manhattan según su compatibilidad con las necesidades estratégicas de DonTaquirou.

Tras la segmentación territorial obtenida mediante **clustering**, se construyó un sistema de scoring orientado a asignar una puntuación comparable a cada zona. Mientras el clustering permitió agrupar las NTA según perfiles similares, el scoring permitió jerarquizarlas en función de un modelo de decisión multicriterio. Para ello, las **16 variables analíticas** del dataset maestro final se llevaron a una escala común y se integraron en una estructura de puntuación compuesta. El sistema se apoya en seis dimensiones: **demanda, movilidad, seguridad, competencia, lugares de interés y coste de alquiler**. 

## 1. Estructura general del scoring

El scoring se construyó en **dos niveles**:

- **Nivel micro**: ponderación local de variables dentro de cada dimensión estratégica.
- **Nivel macro**: combinación posterior de las dimensiones mediante escenarios de decisión.

Este documento se centra principalmente en el **nivel micro**, es decir, en la lógica de transformación y ponderación utilizada para construir las puntuaciones por dimensión. 

## 2. Escala común de puntuación

A partir del dataset maestro final, las 16 variables analíticas fueron reexpresadas en una escala común de **0 a 100 puntos**. Esta transformación permitió comparar variables de distinta naturaleza bajo un mismo criterio de interpretación y agregarlas posteriormente en puntuaciones compuestas por zona. :contentReference[oaicite:4]{index=4}

Para reducir la influencia de valores extremos, se utilizaron como límites de referencia los **percentiles 5 y 95** de la distribución de cada variable. Con ello, se buscó evitar que observaciones extremas condicionaran en exceso la escala, manteniendo una representación más estable del comportamiento general de las zonas. :contentReference[oaicite:5]{index=5}

## 3. Sentido estratégico de las variables

La asignación de puntuaciones se definió según el **sentido estratégico** de cada variable dentro del modelo:

- **Sentido directo**: se aplica a variables cuyo valor alto representa una condición favorable para el negocio. En estos casos, valores más altos reciben puntuaciones más cercanas a 100.
- **Sentido inverso**: se aplica a variables cuyo valor alto representa una condición desfavorable para el negocio. En estos casos, valores más altos reciben puntuaciones más cercanas a 0. :contentReference[oaicite:6]{index=6}

Bajo esta lógica:

- las variables vinculadas con **demanda**, **movilidad** y **lugares de interés** se trataron como favorables;
- las variables de **seguridad** y **coste de alquiler** se trataron como desfavorables;
- en **competencia**, la **competencia directa** se interpretó como desfavorable por su relación con la saturación específica del mercado, mientras que la **competencia indirecta** se mantuvo como variable complementaria. 

## 4. Lógica de transformación

En términos simples, la puntuación de cada variable se obtiene al ubicar el valor observado de la zona dentro de una escala acotada entre los percentiles 5 y 95 de esa variable.

- En variables de **sentido directo**, valores más altos implican puntuaciones más altas.
- En variables de **sentido inverso**, valores más altos implican puntuaciones más bajas.

Para mantener la escala común de interpretación:

- los valores inferiores al percentil 5 se asignan al límite inferior de la escala,
- y los valores superiores al percentil 95 se asignan al límite superior. :contentReference[oaicite:8]{index=8}

## 5. Ponderación local por dimensión

Una vez obtenidas las puntuaciones individuales de las variables, se definió una estructura de **pesos locales** para cada dimensión estratégica. Esta etapa permitió distribuir la importancia relativa de las variables antes de integrarlas en una puntuación agregada por dimensión.

La ponderación local se definió mediante un enfoque multicriterio inspirado en la lógica jerárquica del método **AHP**, asignando pesos según la relevancia analítica de cada variable dentro de su dimensión y su relación con la lógica del negocio. Como resultado, se obtuvo una estructura fija de pesos locales que refleja la importancia relativa de cada variable dentro de su grupo. 

## 6. Estructura de variables y pesos locales

La ponderación local del modelo se organiza por dimensión estratégica. En cada caso, la suma de los pesos asignados a las variables que componen la dimensión equivale al **100 %** de dicha dimensión.

La Tabla siguiente resume la estructura de ponderación local utilizada en el scoring multicriterio, indicando para cada dimensión estratégica las variables consideradas, su peso relativo y su función analítica dentro del modelo.

| No. | Dimensión Estratégica | Variable | Peso Local | Descripción |
|---|---|---|---:|---|
| - | DEMANDA | TOTAL DIMENSIÓN | 100 % | Suma de variables de demanda |
| 4 | Censo (Demanda) | POBLACION_KM2 | 30 % | Volumen potencial de clientes en la zona |
| 5 | Censo (Demanda) | PORCENTAJE_HISPANOS | 20 % | Afinidad cultural con la propuesta del negocio |
| 6 | Censo (Demanda) | EDAD_MEDIANA | 10 % | Perfil demográfico del entorno |
| 7 | Censo (Demanda) | INGRESO_MEDIANO_HOGAR | 25 % | Capacidad de gasto del área |
| 8 | Censo (Demanda) | TAMANO_HOGAR_PROMEDIO | 15 % | Patrón de consumo del hogar |
| - | MOVILIDAD | TOTAL DIMENSIÓN | 100 % | Suma de variables de flujo |
| 9 | Movilidad | MOVILIDAD_PROMEDIO_DIARIA | 80 % | Intensidad del flujo cotidiano |
| 10 | Movilidad | MOV_CANTIDAD_ESTACIONES | 20 % | Nivel de conectividad de la zona |
| - | SEGURIDAD | TOTAL DIMENSIÓN | 100 % | Suma de variables de riesgo |
| 11 | Seguridad | DELITO_PROPIEDAD_KM2 | 45 % | Riesgo para la operación del local |
| 12 | Seguridad | DELITO_TRANSPORTE_KM2 | 35 % | Seguridad de acceso y desplazamiento |
| 13 | Seguridad | DELITO_OTROS_KM2 | 20 % | Condiciones generales del entorno |
| - | PTOS. INTERÉS | TOTAL DIMENSIÓN | 100 % | Suma de variables de atracción |
| 16 | Ptos. Interés | LUGARES_COMERCIO_KM2 | 35 % | Atracción asociada a actividad comercial |
| 17 | Ptos. Interés | LUGARES_OFICINAS_KM2 | 45 % | Demanda ligada a actividad diurna |
| 18 | Ptos. Interés | LUGARES_RESIDENCIAL_KM2 | 20 % | Demanda complementaria del entorno |
| - | COMPETENCIA | TOTAL DIMENSIÓN | 100 % | Suma de variables de saturación |
| 14 | Competencia | COMPETENCIA_DIRECTA_KM2 | 90 % | Saturación de oferta similar |
| 15 | Competencia | COMPETENCIA_INDIRECTA_KM2 | 10 % | Saturación gastronómica alternativa |
| - | COSTE | TOTAL DIMENSIÓN | 100 % | Carga económica de implantación |
| 19 | Coste | ALQ_PRECIO_PIE²_ANUAL | 100 % | Carga fija principal de implantación |

## 7. Cálculo de la puntuación por dimensión

Una vez definidos los pesos locales, la puntuación de cada dimensión se obtiene al **multiplicar la puntuación normalizada de cada variable por su peso local** y luego **sumar los resultados**.

En términos simples, la expresión general puede entenderse así:

**Puntuación de la dimensión = (peso de la variable 1 × puntuación de la variable 1) + ... + (peso de la variable n × puntuación de la variable n)**

donde:

- el **peso local** representa la importancia relativa de cada variable dentro de la dimensión;
- la **puntuación normalizada** corresponde al valor transformado de la variable en la escala de 0 a 100 para la zona analizada. 

## 8. Finalidad dentro del modelo

La construcción del scoring multicriterio permite transformar variables heterogéneas —demográficas, urbanas, comerciales, operativas y económicas— en una estructura comparable de evaluación territorial.

De este modo, el scoring actúa como el puente entre la segmentación territorial obtenida mediante clustering y la construcción posterior de **escenarios de decisión**, aportando una base cuantitativa homogénea para la priorización final de zonas en Manhattan. 
