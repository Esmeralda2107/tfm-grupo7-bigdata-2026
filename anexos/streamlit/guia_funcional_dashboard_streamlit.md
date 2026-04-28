# 📊 Guía funcional del dashboard interactivo en Streamlit

El dashboard interactivo en Streamlit es la **aplicación final del proyecto**. Reúne en una misma interfaz los resultados construidos en las fases de **clustering**, **scoring** y **escenarios**, y permite explorar de forma visual la recomendación de localización para DonTaquirou.

## 1. Finalidad de la aplicación

La aplicación permite consultar los resultados del modelo de localización de forma interactiva. Su función es facilitar la exploración de las zonas de Manhattan, revisar su desempeño territorial y apoyar la interpretación de la recomendación final.

## 2. Diferencia respecto al resultado final del TFM

El TFM concluye con una **recomendación final de localización** apoyada en una lectura conjunta del modelo.

El dashboard, en cambio, trabaja sobre un **escenario activo**. El usuario selecciona un escenario y, a partir de esa configuración, consulta el ranking, el mapa, los gráficos y las tablas asociadas. Por ello, la aplicación funciona como una herramienta de exploración territorial por escenario y no como una comparativa cerrada entre escenarios. 

## 3. Ventaja funcional del dashboard

La principal ventaja funcional del dashboard es que permite **redistribuir los pesos macro** de las dimensiones del modelo, diferenciando entre:

- **dimensiones principales**
- **dimensiones de contexto**

Este ajuste se realiza dentro de reglas definidas para preservar la estructura del modelo. En la configuración actual de la aplicación:

- las **dimensiones principales** mantienen un peso mínimo de **16 %**;
- las **dimensiones de contexto** mantienen un peso mínimo de **5 %** y un máximo de **15 %**;
- la estructura general del escenario conserva la lógica **60 % / 40 %**, donde el 60 % del peso total se concentra en las dimensiones principales y el 40 % restante en las dimensiones de contexto;
- el reajuste automático de pesos mantiene la suma total del bloque y evita que se rompa la lógica del escenario. :contentReference[oaicite:2]{index=2}

La aplicación conserva además los **pesos por defecto del escenario** seleccionado y, cuando el usuario modifica una dimensión, reajusta automáticamente las demás dentro de su bloque. Esto permite explorar distintas sensibilidades estratégicas sin alterar la estructura general del sistema. :contentReference[oaicite:3]{index=3}

## 4. Estructura general de la aplicación

La aplicación se organiza en tres niveles principales:

- **barra lateral de configuración**
- **bloque superior de indicadores clave**
- **pestañas de análisis**

### 4.1 Barra lateral

La barra lateral concentra la interacción principal del usuario. Desde este espacio se puede:

- seleccionar el **escenario de decisión**;
- ajustar los pesos de las **dimensiones principales** y de las **dimensiones de contexto**;
- aplicar filtros sobre **score**, **alquiler**, **competencia directa**, **movilidad**, **zonas** y **clusters**;
- restablecer filtros y volver a la configuración de referencia. :contentReference[oaicite:4]{index=4}

### 4.2 Indicadores clave (KPI)

En la parte superior de la aplicación se presenta un bloque de **KPI** que resume el estado actual del análisis. En la versión actual del dashboard se incluyen:

- **Mejor zona**
- **Score del escenario**
- **Zonas visibles**
- **Subdimensiones dominantes** :contentReference[oaicite:5]{index=5}

Estos indicadores permiten obtener una lectura rápida del resultado antes de entrar al detalle territorial, tabular o gráfico.

### 4.3 Pestañas de análisis

La aplicación incluye las siguientes pestañas:

- **Mapa**
- **Ranking**
- **Gráficos**
- **Metodología**
- **Limitaciones del modelo** :contentReference[oaicite:6]{index=6}

Cada una de estas pestañas permite consultar los resultados desde una perspectiva distinta: espacial, comparativa, gráfica o metodológica.

## 5. Qué permite consultar

El dashboard permite consultar, bajo la configuración activa del escenario:

- la **mejor zona**;
- el **score del escenario**;
- el **ranking de zonas**;
- la visualización territorial en **mapa**;
- los resultados por **dimensiones**;
- gráficos de apoyo a la decisión;
- la metodología general del modelo;
- y las limitaciones del sistema. :contentReference[oaicite:7]{index=7}

Además, la aplicación permite revisar los resultados después de aplicar filtros y ajustes de pesos, lo que facilita una exploración más fina del territorio según distintas prioridades estratégicas.

## 6. Papel del dashboard dentro del proyecto

El dashboard cumple la función de **aplicación de visualización y exploración** del modelo de localización. No reemplaza el desarrollo metodológico del TFM ni la recomendación final del documento, sino que convierte los resultados de **clustering**, **scoring** y **escenarios** en una interfaz consultable e interactiva.

Su papel dentro del proyecto es permitir que el usuario:

- explore el comportamiento territorial de las zonas;
- interprete el resultado desde un escenario específico;
- ajuste pesos dentro de las reglas del modelo;
- y consulte de forma visual la recomendación y sus alternativas. 
