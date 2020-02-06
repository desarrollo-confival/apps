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

## inpecionar tablas de bases de datos para aplicativos individuales

26. Configurar archivo models.py de app abogados, asesores en inspectdb con las tablas necesarias

```python
python manage.py inspectdb db_abogados  > abogados/models.py
python manage.py inspectdb asesores_db  > asesores/models.py

```
## Librerias utilizadas

27. Libreria para filtro en administrador de aplicativos

A continuacion se presentan las librerias para filtro

```bash
https://pypi.org/project/django-autocompletefilter/
https://pypi.org/project/django-admin-autocomplete-filter/ => ESTA SE PROBO PARA EL APLICATIVO ASESORES Y ABOGADOS

pip install django-admin-autocomplete-filter

```
Se pretende mostrar la funcionalidad de la libreria en juridico lo cual queremos filtrar
al personal juridico de acuerdo a su perfil y para lograr la funcionalidad
se necesita del modelo perfiljurido. Por lo tanto se tienen 
siguientes clases

juridico
```python

class Juridicos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, on_delete=models.PROTECT, db_column='ciudad', blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    fijo = models.CharField(max_length=15, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    tarjetaprofesional = models.CharField(db_column='tarjetaProfesional', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fecha_s = models.DateField(blank=True, null=True)
    perfil = models.ForeignKey(Perfiljuridico, on_delete=models.PROTECT, db_column='perfil', blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, db_column='genero', blank=True, null=True)
    login = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'juridicos'
        verbose_name= 'Jurídico'
        verbose_name_plural ='Jurídicos'
        ordering = ["codigo"]
    
    def __str__(self):
        return '%s - %s' %(self.nombre, self.apellido)

```
perfil juridico

```python
class Perfilasesor(models.Model):
    codigo = models.AutoField(primary_key=True,verbose_name='Codigo')
    perfil = models.CharField(max_length=50, verbose_name='Perfil Asesor')

    class Meta:
        managed = False
        db_table = 'perfilasesor'
        verbose_name= 'Perfil del Asesores'
        verbose_name_plural='Perfiles de Asesores'

    def __str__(self):
        return self.perfil

```

a continuacion realizamos las configuraciones en admin.py de perfiljuridico de la siguiente manera

```python
from django.contrib import admin
from .models import Perfiljuridico
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

class PerfiljuridicoFilter(AutocompleteFilter):
    title = 'Perfil Juridico' # display title
    field_name = 'perfil' # name of the foreign key field (de modelo juridico)

class PerfiljuridicoAdmin(admin.ModelAdmin):
    search_fields = [
        'codigo',
        'perfil',
    ]

admin.site.register(Perfiljuridico, PerfiljuridicoAdmin)
```
Finalmente en nuestro admin.py de juridico invocamos a la clase PerfiljuridicoFilter para pasarle en nuestra varialble list_filter.

si se realiza esta configuracion del filter normal de admin django funciona pero mostrando todos los filtros en ese modelo lo cual no es eficiente para fitrar modelos con grandes registros

```python
from django.contrib import admin
from .models import Juridicos

# Register your models here.
class JuridicosAdmin(admin.ModelAdmin):
   
    list_display = ('codigo', 'nombre', 'apellido', 'direccion', 'ciudad', 'mail', 'cedula', 'tarjetaprofesional', 'perfil')
    list_filter = ['perfil', 'codigo'] #=> configuracion normal
    radio_fields = {
        'genero': admin.HORIZONTAL,
        'perfil': admin.HORIZONTAL,        
    }
    readonly_fields = ("fecha", "fecha_s", "codigo")

    autocomplete_fields = [        
        'ciudad',        
    ]
admin.site.register(Juridicos, JuridicosAdmin)

```

Configuracion con libreria de filtrado

```python
from django.contrib import admin
from .models import Juridicos
from perfiljuridico.admin import PerfiljuridicoFilter

# Register your models here.
class JuridicosAdmin(admin.ModelAdmin):
   
    list_display = ('codigo', 'nombre', 'apellido', 'direccion', 'ciudad', 'mail', 'cedula', 'tarjetaprofesional', 'perfil')
    list_filter = [PerfiljuridicoFilter] #=> configuracion libreria
    radio_fields = {
        'genero': admin.HORIZONTAL,
        'perfil': admin.HORIZONTAL,        
    }
    readonly_fields = ("fecha", "fecha_s", "codigo")

    autocomplete_fields = [        
        'ciudad',        
    ]
    
    # esto es para el bug de error del propoetario de libreria
    class Media:
        pass 

admin.site.register(Juridicos, JuridicosAdmin)

```

## Llenado de campos

28. Guardando autollenado de campos

en el modelo asesores se realizo la funcion save

```python
def save(self, *args, **kwargs):
    self.cod_ciudad = self.ciudad.codigo_dane
    self.departamento = self.ciudad.departamento
    super(AsesoresDb, self).save(*args, **kwargs)

```
en admin asesores se crea la funcion para actualizar campos

```python
def actualizar_campos(AsesoresDbAdmin, request, queryset):
    queryset.update(departamento, cod_ciudad)

```
## DESPLIEGUE APACHE XAAMP

29. prueba despliegue

WSGIScriptAlias / /path/to/crm.com/crm/wsgi.py
WSGIPythonHome /C:/Anaconda3/envs/confival
WSGIPythonPath /path/to/crm.com

<Directory /path/to/crm.com/crm>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

<!-- 27. Configuraciones de Sesión

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

``` -->