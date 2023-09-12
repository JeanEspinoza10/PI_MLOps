
# Machine Learning Operations (MLOps)

El presente repositorio muestra una solución al problema planteado en el siguiente enlace: [Enlace a GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/FT). En él se detalla que debemos asumir el rol de Data Engineer para obtener un MVP (Minimum Viable Product), realizando las siguientes actividades:
* Realizar un análisis exploratorio de datos.
* Crear una API Rest de acuerdo con los endpoints requeridos.
* Seleccionar un modelo de predicción basado en nuestros datos.
* Desarrollar una NLP según las indicaciones del repositorio de GitHub.

![Flujograma del pryecto](img/p1.jpg)

# Descripción
Para cualquier proceso que involucre datos, debemos comenzar primero con una exploración de los datos para poder obtener información sobre las variables, las relaciones entre ellas, la calidad de los datos, etc.

Para este proyecto, los datos se encuentran en el siguiente enlace:
[Datos en Google Drive](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

## Análisis Exploratorio
<img width="48" height="48" src="https://img.icons8.com/color/48/google-colab.png" alt="google-colab"/>

Para esta etapa utilizaremos Google Colab para realizar las transformaciones, completar y exportar los datos. En el siguiente enlace [Google Colab](https://colab.research.google.com/drive/1Hh-jz6DX86fWewBpI8b735thQJtpp2hf?usp=drive_link), esta el archivo donde detallo el paso a paso de las transformaciones realizadas en los datos para nuestro caso específico.
Al finalizar esta etapa, obtenemos los siguientes archivos en formato *.json, los cuales utilizaremos posteriormente, estos tienen el nombre de:
* corregido_user_reviews.json
* corregido_output_steam_games.json
* corregido_australian_users_items.json __corregir despues

## Base de Datos
<img width="48" height="48" src="https://img.icons8.com/color/48/mongodb.png" alt="mongodb"/>

Para trabajar de una manera eficiente a la hora de realizar las consultas, opte por la opción de utilizar una base de datos no relacional. 
En este proyecto no ayudaremos de la herramienta de MongoAtlas, es aquí donde subiremos nuestros archivos json.
Nuestra base de datos, tendrá la siguiente estructura:
1. Nombre de Base de datos: ProyectosoyHenry
2. Nombre de nuestra Colección: Cada nombre del archivo json será el de la colección.
3. El archivo json tiene los documentos para cada colección.


## API Rest
<img width="50" height="50" src="https://img.icons8.com/ios-filled/50/api-settings.png" alt="api-settings"/>

El desarrollo de esta servicio esta desarrollo en el framework FLASK. A su vez, esta API tendra los siguientes endpoints, los cuales todos son metodos GET.
* def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

* def countreviews( YYYY-MM-DD y YYYY-MM-DD : str ): Cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos en base a reviews.recommend.

* def genre( género : str ): Devuelve el puesto en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.

* def userforgenre( género : str ): Top 5 de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

* def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

* def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

## Machine Learning
<img width="64" height="64" src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/external-machine-learning-robotics-flaticons-lineal-color-flat-icons.png" alt="external-machine-learning-robotics-flaticons-lineal-color-flat-icons"/>

Para este sección seleccionamos la ténica de Collaborative Filtering, teniendo como antecedente la documentación https://www.aprendemachinelearning.com/sistemas-de-recomendacion/ .
Posteriormente a la elección del algoritmo, debemos exponerlo en API con los siguientes endpoints:
* def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
Si es un sistema de recomendación user-item:

* def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.


# Habilidades Desarrolladas
En este proyecto, he aplicado y desarrollado las siguientes habilidades y tecnologías:
* Desarrollo de __API REST__ con el framework __FLASK__.
* Aplicación del patron de diseño __MVC__ (modelo vista controlador).
* Utilización de herramientas de control de versiones como __Git__.
* Aplicación de __Base de datos No Relacionales__ - __MongoDB__.
* Despliegue del servicio en __Render__.