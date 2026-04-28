# 📊 Guía funcional del dashboard interactivo en Streamlit

Este documento presenta la guía funcional del **dashboard interactivo desarrollado en Streamlit** como capa de visualización y exploración del modelo de localización construido en el proyecto.

La aplicación permite consultar de forma dinámica los resultados del análisis territorial, facilitando la comparación entre zonas de Manhattan y la interpretación de la recomendación final de localización para DonTaquirou. Su papel dentro del proyecto no es sustituir el modelo analítico, sino **hacerlo explorable, interpretable y utilizable como herramienta de apoyo a la decisión**. En el TFM, la visualización interactiva aparece como parte de los objetivos específicos del proyecto y Streamlit se incorpora explícitamente como la herramienta utilizada para mostrar y explorar de forma dinámica los resultados del modelo. 

## 1. Finalidad de la aplicación

El dashboard se concibe como una herramienta de exploración territorial orientada a:

- visualizar los resultados del modelo de localización de forma comprensible;
- comparar zonas bajo distintos enfoques estratégicos;
- facilitar la lectura del comportamiento de cada dimensión del modelo;
- y apoyar la interpretación de la recomendación final y de las alternativas territoriales.

Desde una perspectiva funcional, la aplicación transforma el resultado técnico del pipeline analítico en una interfaz de consulta accesible para el usuario. De este modo, la lógica de **clustering**, **scoring** y **escenarios** puede ser explorada de forma interactiva, sin necesidad de revisar directamente notebooks, scripts o tablas de resultados. El TFM establece precisamente que el proceso metodológico culmina en una fase de **“scoring, escenarios y consistencia de resultados”**, y posteriormente incorpora una capa de **reporting y visualización de datos**, lo que justifica la función del dashboard como instrumento de explotación del modelo. :contentReference[oaicite:1]{index=1}

## 2. Relación del dashboard con el modelo del proyecto

La aplicación Streamlit debe entenderse como la **capa final de visualización** del sistema de análisis construido en el TFM.

El flujo lógico del proyecto sigue una secuencia que parte de la recopilación e integración de datos, pasa por la construcción del dataset maestro, continúa con la segmentación territorial y el scoring multicriterio, y culmina en la construcción de escenarios de decisión. El dashboard se apoya en esas salidas analíticas para ofrecer una lectura interactiva del territorio. En el documento metodológico del TFM, esta secuencia se expresa mediante las fases de **ETL**, **feature engineering**, **clustering**, **scoring**, **escenarios** y visualización final. :contentReference[oaicite:2]{index=2}

En términos funcionales, la aplicación consume información procedente de:

- la **versión final del dataset maestro**;
- la solución de **clustering** seleccionada;
- los resultados del sistema de **scoring**;
- los resultados de los **escenarios de decisión**;
- y la cartografía base de las zonas de Manhattan.

Esto permite que el usuario consulte, filtre y compare zonas sin alterar el modelo metodológico de base, sino trabajando sobre los resultados ya procesados.

## 3. Estructura general del dashboard

La aplicación se organiza como un tablero interactivo con una estructura funcional compuesta por:

- una **barra lateral de configuración y filtros**;
- un bloque de **indicadores principales**;
- y un conjunto de **pestañas temáticas** para explorar los resultados desde distintas perspectivas.

### 3.1 Barra lateral

La barra lateral es el espacio donde el usuario define las condiciones de exploración del modelo. Desde ahí puede:

- seleccionar el **escenario de decisión**;
- modificar pesos dentro de la lógica establecida;
- aplicar filtros sobre variables clave;
- y acotar el conjunto de zonas visibles en pantalla.

La barra lateral funciona, por tanto, como el principal punto de interacción analítica del dashboard.

### 3.2 Indicadores principales

En la parte superior de la aplicación se muestran indicadores sintéticos que resumen el estado de la exploración actual, tales como:

- la **mejor zona** bajo la configuración vigente;
- el **score del escenario**;
- el número de **zonas visibles** tras aplicar filtros;
- y las **subdimensiones dominantes** o factores con mayor aporte relativo.

Estos indicadores ofrecen una lectura rápida del resultado sin necesidad de entrar inmediatamente en el detalle gráfico o tabular.

### 3.3 Pestañas funcionales

El tablero se organiza en varias pestañas, cada una con una finalidad específica dentro del análisis:

- **Mapa**
- **Ranking**
- **Gráficos**
- **Metodología**
- **Limitaciones del modelo**

Esta estructura permite que el usuario combine una lectura visual, comparativa, metodológica e interpretativa del modelo.

## 4. Escenarios de decisión

Una de las funciones centrales del dashboard es permitir la exploración del territorio a partir de distintos **escenarios de decisión**.

En el TFM, los escenarios se construyen como configuraciones estratégicas distintas que permiten comparar las zonas de Manhattan según prioridades diferentes. La lógica metodológica del modelo plantea tres grandes ejes estratégicos: **potencial de demanda**, **eficiencia operativa y atracción de flujo**, y **viabilidad comercial y riesgo controlado**. Sobre esta base, la fase final del análisis incorpora un sistema de escenarios que modifica la importancia relativa de las dimensiones del modelo. :contentReference[oaicite:3]{index=3}

Funcionalmente, el dashboard permite consultar tres escenarios:

- **Potencial de demanda**
- **Eficiencia y flujo**
- **Viabilidad y riesgo**

Cada escenario aplica una lógica distinta de ponderación, por lo que el ranking de zonas puede cambiar en función del enfoque seleccionado. Esto permite al usuario observar cómo varía la recomendación territorial cuando cambian las prioridades estratégicas del negocio.

## 5. Ajuste de pesos

Además de seleccionar un escenario, la aplicación permite ajustar pesos dentro de la estructura del modelo.

Esta funcionalidad es especialmente importante porque convierte al dashboard en una herramienta de **análisis de sensibilidad**. El usuario no se limita a consultar una priorización fija, sino que puede explorar cómo cambia la valoración de las zonas al modificar la importancia relativa de determinadas dimensiones.

La lógica de ajuste mantiene la estructura general del modelo:

- un bloque de **dimensiones principales**;
- y un bloque de **dimensiones de contexto**.

Cuando el usuario modifica el peso de una dimensión dentro de uno de estos bloques, el resto de pesos se reajusta automáticamente para conservar la coherencia interna del sistema. De este modo, la aplicación permite experimentar con la sensibilidad del modelo sin romper la lógica de ponderación establecida.

## 6. Sistema de filtros

La aplicación incorpora un sistema de filtros que permite reducir el universo visible de zonas y enfocar la exploración en perfiles territoriales concretos.

Entre los filtros disponibles se incluyen:

- **score del escenario**;
- **alquiler**;
- **competencia directa**;
- **movilidad**;
- **zonas específicas**;
- **clusters**.

Funcionalmente, estos filtros permiten construir lecturas más finas del territorio. Por ejemplo, el usuario puede limitar la consulta a:

- zonas con alta movilidad;
- zonas con menor presión competitiva;
- zonas dentro de un determinado cluster;
- o zonas con niveles de alquiler compatibles con una lógica más conservadora de implantación.

De este modo, el dashboard no solo sirve para ver “la mejor zona”, sino también para explorar subconjuntos territoriales de interés según distintas restricciones.

## 7. Pestaña de mapa

La pestaña de **Mapa** ofrece una lectura espacial directa de los resultados.

En esta vista, las zonas de Manhattan aparecen representadas sobre la cartografía base, coloreadas según la variable seleccionada. El usuario puede visualizar:

- el **score final del escenario**;
- o el comportamiento de una **dimensión específica**.

Esta funcionalidad es especialmente útil porque permite observar la distribución espacial del rendimiento territorial y detectar patrones urbanos que no siempre se perciben con claridad en una tabla.

El mapa cumple una función clave dentro del modelo de localización: traducir la puntuación analítica en una lectura geográfica. Esto es coherente con el enfoque del TFM, que trabaja con las **Neighborhood Tabulation Areas (NTA)** como unidad de análisis y se apoya en una lógica explícita de análisis territorial. :contentReference[oaicite:4]{index=4}

## 8. Pestaña de ranking

La pestaña de **Ranking** permite consultar las zonas ordenadas según su desempeño bajo la configuración actual.

Esta vista presenta el resultado de forma tabular y facilita la comparación directa entre alternativas. En términos funcionales, el ranking muestra:

- posición relativa de cada zona;
- identificador territorial;
- nombre de la zona;
- score del escenario;
- cluster;
- y, según la tabla mostrada, puntuaciones por dimensión o subdimensión.

Se trata de una vista especialmente útil para:

- validar la posición de las zonas mejor puntuadas;
- comparar alternativas cercanas en score;
- e identificar rápidamente las diferencias entre ellas.

## 9. Pestaña de gráficos

La pestaña de **Gráficos** reúne visualizaciones de apoyo a la decisión orientadas a facilitar una lectura más comparativa del modelo.

Entre las funciones gráficas típicas de esta sección se incluyen:

- comparación de las mejores zonas por score;
- perfiles medios por cluster;
- relaciones entre alquiler y movilidad;
- y comparativas dimensionales del top de zonas.

Desde un punto de vista funcional, esta pestaña ayuda a responder preguntas como:

- ¿qué dimensiones explican el mejor rendimiento de una zona?;
- ¿qué diferencias existen entre clusters?;
- ¿cómo se comportan conjuntamente coste y movilidad?;
- ¿qué tan equilibradas son las zonas mejor posicionadas?

Esta capa gráfica refuerza la interpretación del modelo y reduce la dependencia de tablas extensas.

## 10. Pestaña de metodología

La pestaña de **Metodología** cumple una función de transparencia y trazabilidad.

Su finalidad es hacer visible, dentro de la propia aplicación, la lógica del modelo analítico. En esta sección se resume:

- la estructura general del scoring;
- la normalización de variables;
- la interpretación de categorías;
- la lógica de escenarios;
- y la organización por dimensiones y subdimensiones.

Esta pestaña es especialmente importante porque el TFM se apoya en una lógica metodológica explícita, basada en análisis multicriterio, clustering y escenarios de decisión. Incorporar esta información dentro del dashboard ayuda a que el usuario no vea la aplicación como una “caja negra”, sino como una herramienta sustentada en una metodología clara y documentada. :contentReference[oaicite:5]{index=5}

## 11. Pestaña de limitaciones del modelo

La pestaña de **Limitaciones del modelo** refuerza la lectura crítica del dashboard.

Su función es recordar que la aplicación representa una herramienta de apoyo a la decisión, no un sistema automático de recomendación infalible. Entre las principales limitaciones funcionales del modelo se encuentran:

- la restricción del análisis al distrito de Manhattan;
- el uso de las NTA como unidad territorial y no de locales específicos;
- la dependencia respecto a la calidad y actualización de los datos abiertos;
- la ausencia de variables cualitativas y operativas no observables en las fuentes públicas;
- y el hecho de que la recomendación final no garantiza el éxito comercial.

Esta sección cumple una función metodológica y ética fundamental: contextualizar el alcance real de la aplicación.

## 12. Interpretación funcional de los resultados

Para utilizar correctamente el dashboard, es importante comprender cómo debe interpretarse cada tipo de resultado.

### 12.1 Score del escenario
Es la puntuación final de cada zona bajo el escenario seleccionado. Resume el desempeño territorial según la configuración de pesos activa.

### 12.2 Ranking global
Indica la posición relativa de cada zona respecto al resto de zonas visibles bajo la configuración actual.

### 12.3 Cluster
Representa el grupo territorial al que pertenece la zona según la solución de clustering seleccionada. Esta clasificación permite comparar zonas con perfiles relativamente similares.

### 12.4 Subdimensiones dominantes
Indican qué variables tienen mayor aporte relativo en la construcción del resultado de una zona concreta.

### 12.5 Lectura visual
El mapa, los gráficos y las tablas deben interpretarse de forma complementaria. Ninguna vista por sí sola agota el análisis; la utilidad del dashboard está precisamente en permitir una lectura integrada del territorio.

## 13. Utilidad del dashboard dentro del TFM

La aplicación desarrollada en Streamlit cumple una función estratégica dentro del proyecto.

No se trata únicamente de una visualización estética de resultados, sino de una interfaz que permite:

- traducir el modelo técnico en una herramienta explorable;
- comunicar la lógica analítica del proyecto de forma más clara;
- facilitar la comparación entre alternativas territoriales;
- y apoyar la interpretación final de la recomendación de localización.

En este sentido, el dashboard representa la conexión entre el trabajo metodológico desarrollado en el TFM y su uso práctico como herramienta de apoyo a la decisión empresarial.

## 14. Conclusión funcional

El dashboard interactivo en Streamlit constituye la capa final de explotación del modelo de localización. Su valor radica en que permite combinar:

- exploración territorial,
- ajuste de escenarios,
- sensibilidad a pesos,
- filtrado de alternativas,
- comparación gráfica,
- y lectura metodológica del sistema.

De esta manera, la aplicación facilita que el usuario no solo identifique una zona recomendada, sino que comprenda **por qué** esa zona aparece como recomendación, **cómo** cambia el resultado bajo distintos enfoques y **qué factores territoriales** explican su comportamiento relativo dentro del modelo.
