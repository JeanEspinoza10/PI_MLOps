
# Machine Learning Operations (MLOps)

El presente repositorio muestra una solución al problema planteado en el siguiente enlace: [Enlace a GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/FT). En él se detalla que debemos asumir el rol de Data Engineer para obtener un MVP (Minimum Viable Product), realizando las siguientes actividades:
* Realizar un análisis exploratorio de datos.
* Crear una API Rest de acuerdo con los endpoints requeridos.
* Seleccionar un modelo de predicción basado en nuestros datos.
* Desarrollar una NLP según las indicaciones del repositorio de GitHub.

# Descripción
Para cualquier proceso que involucre datos, debemos comenzar primero con una exploración de los datos para poder obtener información sobre las variables, las relaciones entre ellas, la calidad de los datos, etc.

Para este proyecto, los datos se encuentran en el siguiente enlace:
[Datos en Google Drive](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

## Análisis Exploratorio
Para esta etapa utilizaremos Google Colab para realizar las transformaciones, completar y exportar los datos. En el siguiente enlace [Google Colab](https://colab.research.google.com/drive/1Hh-jz6DX86fWewBpI8b735thQJtpp2hf?usp=drive_link), esta el archivo donde detallo el paso a paso de las transformaciones realizadas en los datos para nuestro caso específico.
Al finalizar esta etapa, obtenemos los siguientes archivos en formato *.json, los cuales utilizaremos posteriormente, estos tienen el nombre de:
* corregido_user_reviews.json
* corregido_output_steam_games.json
* corregido_australian_users_items.json __corregir despues

## Base de Datos

Para trabajar de una manera eficiente a la hora de realizar las consultas, opte por la opción de utilizar una base de datos no relacional. 
Para este proyecto no ayudaremos de la herramienta de MongoAtlas, es aqui donde subiremos nuestros archivos json para realizar las consultas necesarias. 