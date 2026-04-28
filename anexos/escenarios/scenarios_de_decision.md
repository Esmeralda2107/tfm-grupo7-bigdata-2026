# 🧭 Escenarios de decisión del modelo de localización

Este documento presenta la lógica metodológica de los **escenarios de decisión** construidos en el proyecto para comparar las zonas de Manhattan bajo distintos enfoques estratégicos de implantación comercial.

Una vez obtenidas las puntuaciones por dimensión, el modelo incorpora un **segundo nivel de ponderación** orientado a construir escenarios de decisión. En esta etapa, las seis dimensiones del modelo no se combinan con la misma importancia, sino que se ponderan de forma diferenciada según el objetivo estratégico de cada escenario.

## 1. Regla general de construcción

Para la construcción de escenarios se definió una regla de distribución **60/40**:

- **Dimensiones principales**: concentran el **60 %** del peso total.
- **Dimensiones de contexto**: concentran el **40 %** restante.

Esta proporción se adoptó para dar un predominio claro al enfoque estratégico principal sin volver marginales las demás dimensiones, cuya influencia sigue siendo relevante en la decisión de localización. De este modo, se busca mantener escenarios diferenciados, pero suficientemente equilibrados.

Las seis dimensiones utilizadas en el modelo son:

- **Censo (Demanda)**
- **Movilidad**
- **Seguridad**
- **Puntos de interés**
- **Competencia**
- **Coste**

## 2. Criterio de selección de escenarios

La selección de las dimensiones principales en cada escenario responde a los **tres ejes estratégicos del modelo de localización**:

- **Potencial de demanda**
- **Eficiencia operativa y atracción de flujo**
- **Viabilidad comercial y riesgo controlado**

A partir de esta lógica, se construyeron tres escenarios de decisión.

## 3. Escenarios definidos en el proyecto

### Escenario 1. Potencial de demanda

Este escenario prioriza las dimensiones más vinculadas con la capacidad de atracción comercial de la zona.

#### Dimensiones principales (60 %)
- **Censo (Demanda)**: 35 %
- **Puntos de interés**: 25 %

#### Dimensiones de contexto (40 %)
- **Movilidad**: 15 %
- **Seguridad**: 10 %
- **Coste**: 10 %
- **Competencia**: 5 %

#### Lectura estratégica
Este escenario permite identificar zonas con mayor capacidad de atracción comercial, apoyándose en variables demográficas, urbanas y funcionales asociadas a la demanda potencial.

---

### Escenario 2. Eficiencia y flujo

Este escenario otorga mayor peso a las condiciones urbanas más relevantes para un modelo fast casual orientado al take-away.

#### Dimensiones principales (60 %)
- **Movilidad**: 35 %
- **Puntos de interés**: 25 %

#### Dimensiones de contexto (40 %)
- **Censo (Demanda)**: 15 %
- **Seguridad**: 10 %
- **Coste**: 10 %
- **Competencia**: 5 %

#### Lectura estratégica
Este escenario permite priorizar zonas con alta conectividad, intensidad de flujo y actividad urbana compatible con un negocio de servicio rápido y consumo ágil.

---

### Escenario 3. Viabilidad y riesgo

Este escenario enfatiza los factores que inciden con mayor fuerza en la estabilidad operativa y económica de la implantación, así como en la saturación competitiva del entorno.

#### Dimensiones principales (60 %)
- **Seguridad**: 20 %
- **Coste**: 25 %
- **Competencia**: 15 %

#### Dimensiones de contexto (40 %)
- **Censo (Demanda)**: 15 %
- **Movilidad**: 10 %
- **Puntos de interés**: 15 %

#### Lectura estratégica
Este escenario permite priorizar zonas potencialmente más equilibradas desde el punto de vista operativo, económico y competitivo, incorporando una lectura más defensiva del territorio.

## 4. Cálculo de la puntuación final por escenario

Con estas ponderaciones, se calcula una puntuación final para cada zona en cada escenario mediante una suma ponderada de las puntuaciones obtenidas previamente en las seis dimensiones.

En términos simples, la puntuación final de cada zona en un escenario se obtiene al **multiplicar la puntuación de cada dimensión por su peso correspondiente** y luego **sumar todos los resultados**.

La expresión general puede representarse así:

**Puntuación final = (peso de la dimensión 1 × puntuación de la dimensión 1) + ... + (peso de la dimensión 6 × puntuación de la dimensión 6)**

donde:

- el **peso** representa la importancia asignada a cada dimensión dentro del escenario;
- la **puntuación de la dimensión** corresponde al valor previamente calculado para la zona en esa dimensión.

Bajo esta estructura, el modelo genera una puntuación global de **0 a 100** para cada zona en cada escenario, permitiendo comparar cómo cambia la priorización territorial según el énfasis estratégico aplicado.

## 5. Finalidad dentro del modelo

La construcción de escenarios constituye la fase en la que el sistema de scoring se transforma en una herramienta de apoyo a la decisión. Su finalidad es permitir una lectura estratégica diferenciada del territorio, mostrando cómo varía la recomendación de localización cuando cambian las prioridades del negocio.
