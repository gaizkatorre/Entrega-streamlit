Predicción de Ingresos de Películas utilizando Machine Learning
Descripción del Proyecto
Este proyecto tiene como objetivo predecir los ingresos de las películas utilizando modelos de Machine Learning. Utilizando un conjunto de datos que contiene diversas características de muchas películas, entrenamos varios modelos para identificar cuál proporciona las predicciones más precisas.

Estructura del Proyecto
El proyecto sigue la siguiente estructura:

Introducción

Contexto del problema y justificación.
Objetivos y alcance del proyecto.
Dataset

Descripción del dataset utilizado.
Análisis Exploratorio de Datos (EDA).
Preprocesamiento de Datos

Verificación de la calidad de los datos.
Imputación y transformación de variables.
Modelado

Entrenamiento de modelos supervisados.
Evaluación de los diferentes modelos e iteraciones.
Selección e interpretación del modelo final.
Predicción y Resultados Finales

Descripción de la solución final y su impacto en el negocio.
Visualización de los resultados finales y predicciones.
Conclusiones y Futuros Pasos

Análisis de los resultados y fortalezas/debilidades del proyecto.
Propuesta de futuras mejoras y optimizaciones.
Modelos Utilizados
Regresión Lineal
Random Forest
XGBoost
Resultados
Regresión Lineal

MAE: 58,284,982.69
RMSE: 90,421,474.11
Regression Score: 0.51
Regression Coefficient: 2.90
Random Forest

MAE: 1.33
RMSE: 1.93
MAPE: 11.33%
XGBoost

MAE: 1.39
RMSE: 1.98
MAPE: 11.67%
Conclusiones
El modelo de Random Forest proporcionó las predicciones más precisas en comparación con la Regresión Lineal y XGBoost. Sin embargo, cada modelo tiene sus ventajas y limitaciones, y hay espacio para futuras mejoras y optimizaciones.

Requisitos
Para ejecutar este proyecto, necesitarás:

Python 3.x
Bibliotecas: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn
Instrucciones de Uso
Clona este repositorio: git clone https://github.com/tu_usuario/tu_repositorio.git
Instala las dependencias: pip install -r requirements.txt
Ejecuta el notebook: jupyter notebook

