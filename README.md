# Configuración Proyecto Django-Python para aplicativos en CONFIVAL

Desarrollo para migración de aplicativos de areas comercial, juridica entre otras que estan
implementadas en la actualidad en php y bases de datos Mysql. El objetivo es cambiar lenguaje de programación a Python 
para mayor escalabilidad y analisis de datos con los procesos de la empresa. 

## Instalación
A continuacion se presentan los requerimientos para configuracion de ambiente de trabajo en cualquier maquina. 
Esta se realiza en computador con sistema operativo WINDOWS 10 para su desarrollo. Posteriormente se publicara las configuraciones en ambiente de 
trabajo en LINUX-UBUNTU

1. Desinstalar versiones de python nativas en la maquina

## (OPCIONAL) instalación de PYTHON nativo

2. Instalar [python](https://www.python.org/downloads/windows/) 64 ultima version 3.7
```bash
Download Windows x86-64 executable installer
```

## Ambiente Virtual CONDA (distribución oficial de ANACONDA)

3. Instalación distribución Anaconda
```bash
instalar anaconda descargar desde https://www.anaconda.com/

```
4. Creación del ambiente virtual
```bash
conda update -n base -c defaults conda
conda create -n confival python=3.7.4
conda activate confival
conda deactivate
pip list 

```


5. instalar django CMD o linea de comandos en Windows; tambien aplica para ambiente virtual en conda

```bash
pip install Django==2.2.6
python -m django --version
```
6. instalar https://visualstudio.microsoft.com/es/downloads/?rr=https%3A%2F%2Fwww.google.com%2F ARM64 o 64x segun procesador.
Esto con el objetivo de solucionar error de dependencias 
```bash
cd error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.
```
7. Crear proyecto python startproject "nombre_del_proyecto"
```bash
django-admin startproject crm
```
cambiar nombre del directorio raiz

```bash
CRM/
    manage.py
    crm/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
correr el servidor de desarrollo
```bash
python manage.py runserver

ctrl + c  
```
8. Instalar libreria de conexión a base de datos en Mysql en terminal 
```bash
pip install mysqlclient
```
9. Crear applicativo asesores dentro del directorio raiz del proyecto CRM
```bash
python manage.py startapp asesores
```
```bash
asesores/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
10. Configurar crm/setting.py para conexion a base de datos existente Mysql en variable DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',#asignar ruta de archivo conexion.cnf
        },
    }
}
```

11. crear archivo 'conexion.cnf' en directorio crm  registro_abogados => registro_abogados/conexion.cnf

```bash
[client]
database = NAME #(nombre de la base de datos)
user = USER #(usuario)
password = PASSWORD #(contraseña)
default-character-set = utf8
```


## Para la configuración de bases de datos existente y conexión a Django importando contenido de tablas 

12. Eliminar sistema de seguridad que esta contenido en script.msql como son
```bash
.auth
.django
.sc_
```
	
13. Se guarda el archivo de la base de datos limpia con un nombre "confival.msql" para ser utilizada en 
app registro_abogados django

14. Aplicar comando de migración para detectar base de datos y creacion de tablas de seguridad
```bash
python manage.py migrate
```

15. (OPCIONAL) Traer las tablas en db confival al modelo de nuestra aplicacion models.py de registro_abogados
con el siguiente comando (Me jala todas las tablas de la base de datos)

```bash
python manage.py inspectdb > registro_abogados/models.py
```

16. activar modelos en setting.py incluir la app: asesores con el nombre de la clase creada en apps.py
```python
INSTALLED_APPS = [
    'asesores',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Modelo entidad relacion asesores

17. se deben agregar las forinkeys desde mysql en la base de datos confival

18. inspecionar tablas debase de datos 

```bash
python manage.py inspectdb asesores_db municipio perfilasesor genero comisiones > registro_asesores/models.py
```
19. Ajustar tipo de archivo generado para models.py por inspectdb utf16 -> utf8

20. Aplicar comando de migración
```bash
python manage.py migrate
```
21. Aplicar comando de migracion a la app
```bash
python manage.py makemigrations registro_abogados
```

22. Aplicar comando de migración al archivo del directorio migrations para que Django reconsca todos los modelos 
como tablas y campos respectivos para su utilización

```bash
python manage.py sqlmigrate registro_abogados 000x  # x es el numero de la migración creada
```	

## Para la creación de vista administrador en Django

23. Ejecutar usuario de app con comando python 
```bash
python manage.py createsuperuser
```
```bash
Username: confival
Email:prueba@prueba.com
Password:12345
```

24. Ejecutar servidor para ingresar a la vista de administrador http://localhost:8000/admin/
```bash
python manage.py runserver
```

25. Configurar archivo admin.py de app registro_abogados para reconocimiento de modelos desde administrador
```python

from django.contrib import admin
from .models import DbAbogados

admin.site.register(DbAbogados)
```
26. Configurar archivo models.py de app registro_abogados registro_asesores seguimiento en inspectdb con las tablas necesarias

```python
python manage.py inspectdb municipio db_abogados perfil genero asesores_db comisiones origen_contacto perfilasesor > registro_abogados/models.py
python manage.py inspectdb asesores_db municipio perfilasesor genero comisiones > registro_asesores/models.py
python manage.py inspectdb db_abogados perfil seguimiento tipo_seguimiento subitemseguimiento asesores_db municipio comisiones genero > seguimiento/models.py

```

27. Configuraciones de Sesión

```bash
configuracion establecida de sesion en settings.py INSTALLED_APPS y MIDDLEWARE

agregar en settings.py

# Para cambiar el comportamiento donde el sitio actualice la base de datos y envie la cookie en cada solicitud
SESSION_SAVE_EVERY_REQUEST = True

```
```python
def index(request):
    .
    .
    .
    # Numero de visitas de esta vista, contadas en la variable sesion
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'registro_abogados/index.html',
        context={'num_abogados':num_abogados,'num_municipios':num_municipios, 'num_visits':num_visits},
    )

```
28. registro Usuario por medio de forms en django

```bash
instalar apps form // pip install django-crispy-forms

luego en settings. py agregar en lista de aplicaciones
    
'crispy_forms',

configurar variable 
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
29. app archivo

```bash
python manage.py inspectdb municipio db_abogados perfil genero asesores_db comisiones perfilasesor pagador sentencia_conciliacion reg_sentencia perfil_abogadosentencia abogadosentencia antecedentesabd juzgados_tribunales tipo_documento clase_docuemento > archivo/models.py

```

30. LIBREIAS

```bash
https://pypi.org/project/django-autocompletefilter/
https://pypi.org/project/django-admin-autocomplete-filter/ => ESTA SE PROBO PARA EL APLICATIVO ASESORES Y ABOGADOS

```

APIKEY
AIzaSyAlh26VcPja1buQhDNqSnhxKt55zpLZDkc