### Crear proyectos de DJANGO
```
django-admin startproject biblioteca
```

### Ejecutar proyecto
```
python3 manage.py runserver
```

### Crear Aplicaciones
```
mkdir applications
cd applications
django-admin startapp libro
```

### short cuts
```
fk: llaves foraneas
mc: char field
md: date field
```

### migraciones
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### crear usuarios
```
python3 manage.py createsuperuser
```

### Actualizar version de DJANGO a la 5.2.12 compatible con la version de python 3.14.2
```
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade "Django>=5.2.8,<5.3"
python -m django --version
python manage.py check
python manage.py runserver
```

### Instalar DRF
```
pip install djangorestframework
```

### instalar los paquetes del proyecto
```
pip install -r requirements.txt
```

### ejecutar django con un arcchivo settings personalizado
python3 manage.py runserver --settings=bibliotecapro.settings.local

### configuracion db
```
psql postgres
postgres=# CREATE DATABASE bibliodb;
postgres=# CREATE USER biblioadmin;
postgres=# \c bibliodb;
You are now connected to database "bibliodb" as user "jota".
bibliodb=# ALTER USER biblioadmin WITH password 'biblio123';
bibliodb=# \c postgres
You are now connected to database "postgres" as user "jota".
postgres=# ALTER DATABASE bibliodb OWNER TO biblioadmin;
```

### Configuracion path de postgres
```
echo 'export PATH="/Library/PostgreSQL/17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
psql --version
pg_isready
```

### para borrar el cache de python
```
git rm -r --cached .
git add .
git commit -m "Ignorar archivos compilados de Python y __pycache__"
```