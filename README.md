# ChallengeAJMATree
Este proyecto es parte de un conjunto de programas que se desarrollaron para la entrega a la empresa AJMA. 
En este programa, se implementa un sistema que permite codificar y decodificar diferentes tipos de códigos utilizando árboles binarios. 
Los códigos pueden ser en formato Morse, binario u otros. El programa utiliza la estructura de árboles binarios para realizar las operaciones de codificación y decodificación de manera eficiente.

## Tabla de contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Créditos](#créditos)
- [Licencia](#licencia)

## Instalación

### 1. Abre una terminal:
Algunos comandos son:
- Windows: "Windows + R" para abrir el cuadro de diálogo Ejecutar, luego escribe "cmd" y presiona Enter.
- MacOS: "Command + Barra espaciadora", luego escribiendo "Terminal" y presiona Enter.
- Linux: "Ctrl + Alt + T"
### 2. Clona el repositorio a tu máquina local: 
- git clone https://github.com/EstructuraDeDatosUSB/ChallengeAJMATree.git
### 3. Accede al directorio:
- cd ChallengeAJMATree
### 4. Crear un entorno virtual (Opcional - Si deseas no llenar tu máquina local de librerías):
- pip install virtualenv
- mkdir venv
- cd venv

#### - En Windows:
- venv\Scripts\activate

#### - En macOS y Linux:
- source venv/bin/activate
  
### 5. Instala los requerimientos
- pip install -r requirements.txt

## Uso

### 1. Abra la terminal en el proyecto
### 2. Inicia el servidor de desarrollo de Django
- python manage.py runserver

## Caracteristicas

### TDA CodeTreeADT:
- El TDA utiliza un árbol binario para almacenar los códigos y los caracteres asociados.
- Los códigos pueden ser en formato Morse o binario, dependiendo de los parámetros proporcionados al constructor.
- Los códigos se agregan al árbol utilizando el método add(code, char), donde code es el código y char es el carácter asociado.
- El árbol se construye de manera recursiva utilizando el método _recursive_add.
- Se puede buscar un código utilizando el método search(code), el cual realiza una búsqueda recursiva en el árbol y devuelve el carácter asociado al código.
- Se puede realizar una búsqueda inversa, es decir, obtener el código correspondiente a un carácter, utilizando el método reverse_search(char).
- Se puede obtener la altura del árbol utilizando el método height().
- Se puede codificar un mensaje utilizando el método encode(message), donde el mensaje se recorre caracter por caracter y se obtiene el código correspondiente a cada uno.
- Se puede decodificar un mensaje utilizando el método decode(message), donde el mensaje se divide en códigos y se busca el carácter asociado a cada código.

## Aplicacion:


## Créditos

Este proyecto fue desarrollado por los siguientes miembros de la organización EstructuraDeDatosUSB en Github:

- Gustavo Camargo (Dueño de la organización)
- Dillan Asprilla
- Mariana Cruz
- Juan Manuel Conde
- Jhon Mario Diaz
- Juan David Diaz

Agradecemos a todos los miembros de la organización por su contribución a este proyecto

## Licencia

Este proyecto se encuentra bajo la siguiente licencia:

[![Licencia CC-BY-NC-ND 4.0](https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)

El contenido de este proyecto está protegido por la licencia Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internacional. Esto significa que puedes utilizar y compartir este proyecto con otros bajo las siguientes condiciones:

- *Atribución (Attribution):* Debes otorgar crédito adecuado, proporcionando un enlace a la licencia y mencionando a los autores originales.
- *No Comercial (NonCommercial):* No puedes utilizar este proyecto con fines comerciales.
- *No Derivados (NoDerivatives):* No puedes modificar, adaptar o crear obras derivadas a partir de este proyecto.

Para obtener más información sobre los términos y condiciones de esta licencia, puedes visitar el siguiente enlace: [Licencia CC-BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es).
