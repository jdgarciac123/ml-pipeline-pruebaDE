# 📊 Proyecto de Recomendación – Prueba Mercado Libre
Este repositorio contiene el desarrollo de un sistema de recomendación construido como parte de una prueba técnica. El objetivo principal fue explorar diferentes modelos de recomendación a partir de la estructura de datos solicitada, dejando en el pipeline final la estructura necesaria para el modelo que se consideró más adecuado, basado en SVD (Singular Value Decomposition).

Adicionalmente, se documentan en los notebooks las otras propuestas de tablas y modelos que fueron probadas:

- 📓 Notebook_prueba_modelos.ipynb: pruebas con diferentes algoritmos de recomendación.
- 📓 Notebook_prueba_tablas.ipynb: exploración de diferentes estructuras de tablas para alimentar los modelos.

Las salidas generadas en este proceso pueden encontrarse en la carpeta data/processed.

## ⚙️ Anexos Técnicos
📄 Documento explicativo adicional solicitado en la prueba (Google Docs): https://docs.google.com/document/d/1MiqdZZBxuPn3mfOYxHIjB2OgfplAp2hO9I2e2EhUbpY/edit?usp=sharing

## ✅ ¿Qué es y qué hace el artefacto?

El sistema desarrollado es un pipeline de machine learning que:

- Procesa eventos de impresión, tap y pagos de usuarios.
- Construye una tabla de características que pondera la interacción de cada usuario con diferentes servicios (value_props).
- Entrena un modelo de recomendación colaborativo con SVD.
- Genera un archivo con las recomendaciones personalizadas para cada usuario.

- 🛠️ Preprocesamiento: Limpieza y normalización de datos crudos (JSON y CSV).
- 🔍 Feature Engineering: Generación de variables (interacciones, compras, clics y visualizaciones destacadas).
- 📉 Entrenamiento SVD: Reducción dimensional de la matriz usuario-producto para capturar patrones latentes.
- 🎁 Generación de recomendaciones: Ranking de los productos más relevantes para cada usuario.
- 📂 Resultados exportables: Archivos CSV con las recomendaciones personalizadas.

## ⚠️ Consideraciones

- Los datos fuente no están en el repositorio por políticas de seguridad (fueron añadidos al .gitignore).
- El pipeline requiere que el usuario disponga los archivos fuente en la ruta data/raw.

## 🛠️ ¿Cómo ponerlo en funcionamiento?
### 1. Prerrequisitos
- Tener instalado Python 3.11

### 2. Clonar el repositorio
```bash
git clone https://github.com/jdgarciac123/ml-pipeline-pruebaDE.git
cd ml-pipeline-pruebaDE
```

### 3. Preparar el entorno
```bash
# (Opcional, recomendado) Crear un entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 4. Ubicar los datos fuente
Guardar los archivos en la carpeta data/raw/ con la siguiente estructura:
```
data/
 ├── raw/
 │   ├── prints.json
 │   ├── taps.json
 │   └── pays.csv
 ├── processed/
 └── output_models/
```

### 5. Ejecutar el pipeline
```bash
python pipeline.py
```
Esto generará:
- 📄 data/processed/SVD_model_df.csv → Tabla base para el modelo.
- - 📄 data/processed/df_final.csv → Archivo con la estructura final solicitada en la prueba.
- 📄 data/output_models/recommendations_SVD.csv → Archivo con las recomendaciones finales.

# 👤 Casos de uso
- Recomendaciones periódicas: el pipeline permite generar recomendaciones de manera recurrente, simplemente actualizando los archivos fuente en data/raw y ejecutando nuevamente el proceso.
- Adaptabilidad a datos cambiantes: el sistema está diseñado para manejar fluctuaciones tanto en la base de usuarios como en los patrones de uso de los servicios, garantizando que las recomendaciones siempre reflejen el comportamiento más reciente.
  
## 📁 Estructura del repositorio
```bash
ml-pipeline-pruebaDE/
├── data/
│   ├── raw/                  # Archivos fuente (prints.json, taps.json, pays.csv)
│   ├── processed/            # Salidas intermedias, pruebas de tablas y estructura solicitada
│   └── output_models/        # Recomendaciones finales
├── notebooks/
│   ├── Notebook_prueba_modelos.ipynb
│   └── Notebook_prueba_tablas.ipynb
├── src/
│   ├── config.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── svd_model.py
│   └── recommend.py
├── pipeline.py               # Script principal del pipeline
├── requirements.txt          # Dependencias del proyecto
└── README.md
```



