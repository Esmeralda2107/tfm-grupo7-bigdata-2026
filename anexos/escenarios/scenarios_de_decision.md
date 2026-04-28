# 🧭 Escenarios de Decisión del Proyecto

Este documento presenta la lógica metodológica de los **escenarios de decisión** construidos en el proyecto para comparar las zonas de Manhattan bajo distintos enfoques estratégicos de implantación comercial.

Los escenarios se apoyan en el sistema de **scoring** desarrollado previamente y permiten ponderar de forma diferente las dimensiones del modelo según el objetivo de análisis.

## 1. Lógica general de construcción

Cada escenario se organiza en dos bloques de ponderación:

- **Dimensiones principales**: concentran el **60 %** del peso total.
- **Dimensiones de contexto**: concentran el **40 %** del peso total.

Esta estructura permite priorizar determinadas dimensiones estratégicas sin perder la visión integral del entorno urbano, económico y territorial.

Las dimensiones utilizadas en el modelo son:

- **Censo (Demanda)**
- **Movilidad**
- **Seguridad**
- **Puntos de interés**
- **Competencia**
- **Coste**

## 2. Escenarios definidos en el proyecto

### Escenario 1. Potencial de demanda

Este escenario prioriza la capacidad de atracción comercial de la zona, poniendo el foco en la presencia de demanda potencial y en aquellos atributos territoriales que favorecen la captación de clientes.

#### Dimensiones principales (60 %)
- **Censo (Demanda)**: 35 %
- **Puntos de interés**: 25 %

#### Dimensiones de contexto (40 %)
- **Movilidad**: 15 %
- **Seguridad**: 10 %
- **Coste**: 10 %
- **Competencia**: 5 %

#### Lectura estratégica
Este escenario resulta especialmente útil cuando el objetivo es identificar zonas con mayor capacidad de consumo potencial, dinamismo comercial y presencia de perfiles demográficos compatibles con la propuesta del negocio.

---

### Escenario 2. Eficiencia y flujo

Este escenario prioriza las condiciones urbanas que favorecen la operación cotidiana del negocio, especialmente en modelos orientados a la rotación, el take-away y la captación de flujo peatonal.

#### Dimensiones principales (60 %)
- **Movilidad**: 35 %
- **Puntos de interés**: 25 %

#### Dimensiones de contexto (40 %)
- **Censo (Demanda)**: 15 %
- **Seguridad**: 10 %
- **Coste**: 10 %
- **Competencia**: 5 %

#### Lectura estratégica
Este escenario permite identificar zonas con elevada accesibilidad, intensidad de tránsito y visibilidad comercial, especialmente favorables para formatos de restauración rápida o consumo de conveniencia.

---

### Escenario 3. Viabilidad y riesgo

Este escenario prioriza los factores que inciden en la estabilidad operativa y económica de la implantación, incorporando una lectura más defensiva orientada a coste, seguridad y saturación competitiva.

#### Dimensiones principales (60 %)
- **Seguridad**: 20 %
- **Coste**: 25 %
- **Competencia**: 15 %

#### Dimensiones de contexto (40 %)
- **Censo (Demanda)**: 15 %
- **Movilidad**: 10 %
- **Puntos de interés**: 15 %

#### Lectura estratégica
Este escenario permite identificar zonas potencialmente más equilibradas desde el punto de vista operativo, económico y competitivo, especialmente en contextos donde la viabilidad de implantación y el control del riesgo son prioritarios.

## 3. Interpretación de los escenarios

Los tres escenarios no representan resultados incompatibles, sino **formas alternativas de leer el territorio** según distintos criterios estratégicos de decisión.

En consecuencia:

- una zona puede mostrar un rendimiento elevado en un escenario y moderado en otro,
- las diferencias entre escenarios permiten identificar fortalezas y debilidades territoriales,
- y la comparación conjunta facilita una evaluación más rica de las alternativas de implantación.

## 4. Relación con la aplicación Streamlit

La aplicación desarrollada en **Streamlit** toma estos escenarios como configuraciones de referencia para la exploración interactiva del territorio.

Aunque cada escenario parte de los pesos por defecto aquí descritos, la aplicación permite **ajustar los pesos** dentro de la lógica general del modelo para explorar distintas sensibilidades de decisión.

## 5. Finalidad dentro del proyecto

La construcción de escenarios constituye la última fase analítica del proyecto y permite traducir el sistema de scoring en una herramienta útil para la interpretación estratégica del territorio, apoyando la comparación de alternativas y la toma de decisiones en contexto urbano.
