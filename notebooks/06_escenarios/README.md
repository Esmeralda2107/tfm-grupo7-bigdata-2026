# 🧭 Notebooks de Escenarios

Este directorio contiene los **notebooks dedicados a la construcción de escenarios de decisión** del proyecto.

Su función principal es tomar los resultados del sistema de **scoring** ya calculado y combinarlos en modelos de ponderación estratégica, permitiendo comparar las zonas de Manhattan según distintos enfoques de implantación comercial.

En esta fase se desarrollan procesos como:

- la definición de escenarios de decisión,
- la asignación de pesos a las dimensiones estratégicas,
- el cálculo de puntuaciones finales por escenario,
- la comparación del desempeño territorial bajo distintos criterios,
- y la generación de salidas consolidadas para su interpretación y visualización posterior.

El notebook incluido en esta carpeta es:

- **`14_Escenarios.ipynb`**: construcción de los escenarios de decisión del proyecto, cálculo de puntuaciones finales por zona y generación de resultados comparativos entre escenarios.

Los resultados de esta fase se almacenan en **`resultados/06_escenarios/`** y constituyen la base para la interpretación estratégica final del proyecto, así como para su explotación en la aplicación desarrollada en **Streamlit**.
