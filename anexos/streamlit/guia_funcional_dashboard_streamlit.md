# 📊 Guía funcional del dashboard interactivo en Streamlit

El dashboard interactivo en Streamlit constituye la **aplicación final del proyecto**, ya que reúne en una misma interfaz los resultados construidos en las fases de **clustering**, **scoring** y **escenarios**. Su función principal es facilitar la exploración territorial de Manhattan y apoyar la interpretación de la recomendación de localización para DonTaquirou. El TFM describe esta herramienta como una interfaz que integra escenarios de decisión, dimensiones del modelo, indicadores clave, gráficos, tablas resumen, mapas, metodología, limitaciones y la descripción de la mejor zona según los criterios seleccionados. :contentReference[oaicite:1]{index=1}

## 1. Finalidad de la aplicación

La aplicación permite consultar de forma interactiva los resultados del modelo de localización. No sustituye el análisis metodológico desarrollado en el TFM, sino que lo convierte en una herramienta visual y operativa de apoyo a la decisión. Su utilidad principal es permitir al usuario explorar las zonas, revisar su desempeño territorial y entender cómo cambia la priorización según el escenario y la configuración seleccionada. :contentReference[oaicite:2]{index=2}

## 2. Diferencia principal respecto al resultado final del TFM

Mientras que el TFM cierra con una **recomendación final de localización** apoyada en la lectura conjunta del modelo, el dashboard trabaja sobre un **escenario activo** y permite explorar los resultados desde ese enfoque concreto. Por tanto, la aplicación no está pensada como una comparativa cerrada entre escenarios, sino como una herramienta de visualización y exploración territorial por escenario. Esto es coherente con la lógica funcional actual de la app, donde el usuario selecciona un escenario y a partir de ahí consulta ranking, mapa, gráficos y tablas asociados a esa configuración. 

## 3. Ventaja funcional del dashboard

La principal ventaja funcional del dashboard es que permite **redistribuir los pesos macro** de las dimensiones, diferenciando entre **dimensiones principales** y **dimensiones de contexto**, sin romper la lógica metodológica del modelo. El TFM indica que este ajuste se realiza dentro de límites predefinidos: las dimensiones principales mantienen un peso mínimo del **16 %**, mientras que las dimensiones de contexto conservan una participación mínima del **5 %** y máxima del **15 %**, evitando así que una dimensión de contexto supere a una principal. :contentReference[oaicite:4]{index=4}

Esta funcionalidad convierte la aplicación en una herramienta de exploración sensible al criterio estratégico del usuario, permitiendo probar distintas configuraciones sin alterar la coherencia general del modelo.

## 4. Estructura general de la aplicación

La aplicación se organiza en una barra lateral de configuración y en varias pestañas de consulta.

En la **barra lateral**, el usuario puede:
- seleccionar el escenario de decisión;
- ajustar los pesos por dimensión dentro de las reglas del modelo;
- y aplicar filtros para acotar la exploración.

En la parte principal del dashboard se muestran indicadores sintéticos y varias vistas de análisis. En su versión actual, la aplicación incluye las pestañas de:
- **Mapa**
- **Ranking**
- **Gráficos**
- **Metodología**
- **Limitaciones del modelo** :contentReference[oaicite:5]{index=5}

## 5. Qué permite consultar

Funcionalmente, el dashboard permite consultar:

- la **mejor zona** bajo la configuración activa;
- el **score del escenario**;
- el **ranking** de zonas;
- la visualización territorial en **mapa**;
- gráficos de apoyo a la decisión;
- el comportamiento por **dimensiones**;
- y la explicación metodológica básica del modelo. 

Además, el TFM incluye una **galería del dashboard interactivo** en el Anexo 5, donde se documentan visualizaciones como el top 10 de zonas por score, el desempeño por dimensiones del top 5, el perfil promedio por clúster y la relación entre alquiler y movilidad. :contentReference[oaicite:7]{index=7}

## 6. Papel del dashboard dentro del proyecto

El dashboard cumple una función de **visualización aplicada** del modelo de localización. Su valor no está en reemplazar la lógica analítica del TFM, sino en hacerla más accesible, interpretable y útil para la exploración de resultados. En ese sentido, actúa como la capa final de explotación del proyecto, conectando la base metodológica con una herramienta interactiva orientada a la consulta y apoyo a la decisión. :contentReference[oaicite:8]{index=8}
