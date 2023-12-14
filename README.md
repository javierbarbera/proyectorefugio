# Tercer Entrega Coder House - Python Flex

#### Comisión: 56055

#### Alumno: Javier Barbera

## Nombre del Proyecto

EL REFUGIO DEL NERD

## Versión
1.0

## Descripción del Proyecto
Página web tipo "blog" donde los usuarios armaran ellos mismos la base de datos de libros, discos y películas, con el fin de hacer recomendaciones al resto de los usuarios de la comunidad e intercambiar opiniones por medio de reseñas.

Para poder hacer uso del blog, el usuario deberá iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Los usuarios podrán realizar lo siguiente:
- Publicar libros, discos y/o películas. Tendrán la opción de escribir una breve reseña dando su opinión y valoración sobre los mismos para que los otros usuarios puedan leerlos.
- Visualizar publicaciones de otros usuarios y comentar sobre ellas.
- Editar el perfil de Usuario
- Cambiar la contraseña de Usuario
- Cerrar Sesión
- Login en caso de haber cerrado sesión

## Funcionalidades

## Formularios de carga:
Se crearon 3 clases en el archivo "models.py": "Libro", "Disco" y "Pelicula".
Cada modelo cuenta con su formulario para cargar información a la base de datos. Las rutas para la carga de cada uno de los tres formularios se encuentra en el archivo "urls.py" dentro de la aplicación:

Para cargar info en libros: AppRefugio/libros
Para cargar info en discos: AppRefugio/discos
Para cargar info en películas: AppRefugio/peliculas

## Formulario de busqueda:
Se creo un formulario de busqueda, para buscar en la base de datos de la clase "Libro".

Para la busqueda: AppRefugio/buscarLibros

## Log In (inicio de sesión):

Se configuró el log in para iniciar sesión en caso de tener un usuario registrado.

## Registro:

Se configuró el registro de usuario para iniciar sesión en caso de no contar con un usuario registrado.

## Se ha utilizado para la elaboración del proyecto:
- HTML 5
- Bootstrap 5.2
- Python 3.10.4
- Django 4.0