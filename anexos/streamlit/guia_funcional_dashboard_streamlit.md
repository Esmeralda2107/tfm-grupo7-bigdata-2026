# 📊 Guía funcional del dashboard interactivo en Streamlit

El dashboard interactivo en Streamlit es la **aplicación final del proyecto**. Reúne en una misma interfaz los resultados construidos en las fases de **clustering**, **scoring** y **escenarios**, y permite explorar de forma visual la recomendación de localización para DonTaquirou.

## 1. Finalidad de la aplicación

La aplicación permite consultar los resultados del modelo de localización de forma interactiva. Su función es facilitar la exploración de las zonas de Manhattan, revisar su desempeño territorial y apoyar la interpretación de la recomendación final.

## 2. Diferencia respecto al resultado final del TFM

El TFM concluye con una **recomendación final de localización** apoyada en una lectura conjunta del modelo.

El dashboard, en cambio, trabaja sobre un **escenario activo**. El usuario selecciona un escenario y, a partir de esa configuración, consulta el ranking, el mapa, los gráficos y las tablas asociadas. Por ello, la aplicación funciona como una herramienta de exploración territorial por escenario y no como una comparativa cerrada entre escenarios.

## 3. Ventaja funcional del dashboard

La principal ventaja funcional del dashboard es que permite **redistribuir los pesos macro** de las dimensiones, diferenciando entre:

- **dimensiones principales**
- **dimensiones de contexto**

Este ajuste se realiza respetando las reglas del modelo, de modo que el usuario puede explorar distintas configuraciones sin alterar su estructura general.

## 4. Estructura general de la aplicación

La aplicación se organiza en una barra lateral de configuración y en varias pestañas de consulta.

### 4.1 Barra lateral

En la barra lateral el usuario puede:

- seleccionar el escenario de decisión;
- ajustar los pesos por dimensión;
- aplicar filtros para acotar la exploración.

### 4.2 Área principal

En la parte principal del dashboard se muestran indicadores sintéticos y varias vistas de análisis.

La aplicación incluye las siguientes pestañas:

- **Mapa**
- **Ranking**
- **Gráficos**
- **Metodología**
- **Limitaciones del modelo**

## 5. Qué permite consultar

El dashboard permite consultar:

- la **mejor zona** bajo la configuración activa;
- el **score del escenario**;
- el **ranking** de zonas;
- la visualización territorial en **mapa**;
- gráficos de apoyo a la decisión;
- el comportamiento por **dimensiones**;
- y una explicación general de la metodología del modelo.

## 6. Papel del dashboard dentro del proyecto

El dashboard cumple una función de **visualización aplicada** del modelo de localización. Su valor está en hacer más accesibles los resultados y permitir su exploración de forma interactiva.

De esta manera, la aplicación actúa como la capa final de visualización del proyecto y conecta el trabajo metodológico con una herramienta de apoyo a la decisión.
