# Elecciones 2021 Backend

## Ejecutar en local  

Requisitos:
- Tener instalado python3.8
- Instalar virtualenv
- Tener instalado node y npm 


Python:

    virtualenv env && source env/bin/activate
    pip install -r requirements.txt

Node:

    npm install -g serverless
    npm install

Para ejecutar en local  considerar variables de entorno  de BD revisar `settings.py` 

    python manage.py migrate        #para migrar cambios de bd
    python manage.py runserver      #para ejecutar en local puerto 8000 por defecto

## Ejecutar en Docker 

Para levantar el proyecto django + postgres ejecutar 

    make up   ## internamente ejecuta docker-compose up -d 

Para detener los servicios de django + postgres ejecutar 

    make down


## Desplegar 

Desplegamos AWS:

Previamente debes tener aws cli profile configurado (Access, Secret keys)

Otra manera es configurar las credenciales por serverless

    serverless config credentials -o --provider aws --key [KEY VALUE] --secret [SECRET VALUE]


Para desplegar por defecto es:

    sls deploy