# DJANGO REST FRAMEWORK

**Instruction for Build image**

docker-compose build

**Add Dependencies to app folder**

 docker-compose run web sh -c "django-admin.py startproject api ."
 
**Add Super User Password: secret1234**
 
  docker-compose run  web sh -c "python manage.py createsuperuser --email admin@example.com --username admin"

**Applying Migrations**
 
 docker-compose run  web sh -c "python manage.py migrate"

**Up docker container**

docker-compose up web
