# IV-18-19-Proyecto

[![Build Status](https://travis-ci.com/Thejokeri/IV-18-19-Proyecto.svg?branch=master)](https://travis-ci.com/Thejokeri/IV-18-19-Proyecto)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## CloudyCloud

Proyecto de la asignatura de Infraestructura Virtual (2018-2019)

### Idea Principal

Crear un microservicio para encriptar documentos (PDF) y alojarlos en la nube. El objetivo principal, es la creación de un servicio para que usuarios (en nuestro caso, personal sanitario) puedan almacenar archivos cifrados con información personal de los pacientes, garantizando la ley de protección de datos y de poder enviar dichos archivos a otros personales sanitarios, a través de una red segura.

---

### Herramientas

Estas son las herramientas que voy a utilizar parar la creación del microservicio:

* [Python](https://www.python.org)
* [pyPdf 1.13](https://pypi.org/project/pyPdf/)
* [Flask](http://flask.pocoo.org/)
* [DEPOT - File Storage Made Easy](https://depot.readthedocs.io/en/latest/)
* [POSTGRESQL](https://www.postgresql.org)
* [psycopg](http://initd.org/psycopg/)

---

### Descripción del microservicio

El microservicio consta de una clase en la que se llevará a cabo todas las operaciones relacionadas con el microservicio, como la creación y eliminación de los usuarios determinados por un identificador correcto, además de toda la funcionalidades de añadido, eliminación y búsqueda de archivos. [Documentación de la clase](http://htmlpreview.github.io/?https://github.com/Thejokeri/IV-18-19-Proyecto/blob/master/doc/pdfupload.html) (Generado con pydoc):

```bash
pydoc -w pdfupload.py
```

La versión de Python que voy a utilizar es Python 2.7.15 ya que la versión mas reciente, no me permite ejecutar DEPOT.

Las [dependencias](./requirements.txt) que se han usado son las siguientes:

* filedepot: permite almacenar los ficheros pdf en un directorio con nombre, el identificador del fichero, y en dentro del directorio, se alojará el binario del archivo, con un .json con los metadatos del fichero (nombre, fecha de creación, etc).
  
* pyPdf: se encarga de cifrar y descifrar el fichero.
  
* Flask: para la creación del microservicio web.
  
* psycopg2: es el adaptador PostgreSQL más popular para el lenguaje de programación Python. Permite realizar cualquier tipo de query de manera sencilla.

#### Para la instalación

```bash
pip install -r requirements.txt
```

#### Para arrancar los test

```bash
pytest test.py
```

#### Para arrancar el programa principal

```bash
python pdfupload.py
```

---

### Sistema de integración continua

Voy a utilizar [Travis](https://travis-ci.org/) como sistema de integración contínua, para el testeo de la clase. Está totalmente configurada y vinculada con la cuenta de GitHub.

---

### Despliegue

![Heroku](https://heroku-badge.herokuapp.com/?app=cloudncloud)

* [Despliegue en Heroku](https://cloudncloud.herokuapp.com/)

---

#### Colaboración

Proyecto en colaboración con el proyecto: [Microservicio de Carlos](https://github.com/AGCarlos/IV_1819_Proyecto). Que se encargará de enviar los documentos a destinatarios.

| [![Carlos Ariza García](https://github.com/AGCarlos.png?size=100)](https://github.com/AGCarlos) | [![Fernando Talavera Mendoza](https://github.com/Thejokeri.png?size=100)](https://github.com/Thejokeri) |
| :---: | :---: |
| [Carlos Ariza García](https://github.com/AGCarlos) | [Fernando Talavera Mendoza](https://github.com/Thejokeri) |

---
