# Dockerfile azure-cli w/python
FROM mcr.microsoft.com/azure-cli:latest
COPY file.py .
CMD ["python", "file.py"]

# docker #
# docker info
# docker images
# docker pull image
# docker run -it -d image
# docker ps -a
# docker rmi ...
# docker stop ...
# docker run ...

# docker run --name aname ...
# docker run -p 38282:8080 kodekloud/simple-webapp:blue
#             port host:   instancecontainer:tag

# docker inspect container-name/container-id
# docker run -p 38282:8080 --name blue-app -e APP_COLOR=blue -d kodekloud/simple-webapp
# docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db mysql

# docker build image and then run image
# docker build -t mysql-db .
# docker run -p 8282:8080 mysql-db

# docker run python:3.6 cat /etc/*release*
# docker push geekflare/httpd_image # upload
# docker history 09ca6feb6efc
# docker log 09ca6feb6efc

# docker run --name db -e POSTGRES_PASSWORD=mysecretpassword -d postgres

# docker run -d --name=wordpress --link db:db -p 8085:80 wordpress
# docker exec -it 09ca6feb6efc bash
#------------------------------------------------------
# YAML file #
##version: '2.0'
##services:
##    db:
##	    environment:
##		  POSTGRES_PASSWORD: passw
##		image: postgres # if not built yet build: postgres or point to location folder
##        networks:
##          - front-end
##	  wordpress:
##	    image: wordpress
##		links: # or depends_on: in later versions
##		  -db  # -db
##		ports:
##		  -8080:80
##        networks:
##          - back-end
##networks:
##  - front-end
##  - back-end
#
# docker-compose up -d #detached
#------------------------------------------------------
# docker file
##FROM node:latest
##
##RUN mkdir -p /app/src
##
##WORKDIR /app/src
##
##COPY package.json .
##
##RUN npm install
##
##COPY . . # source destination
##
##EXPOSE 8080 # port
##
##CMD ["npm", "start"]
#
# docker build . -t reactapp

# docker push image
#------------------------------------------------------
##FROM Ubuntu
##
##RUN apt-get update
##RUN apt-get install python
##
##RUN pip install fastapi
##RUN pip install anything else
##
##COPY . /opt/folder
##
##ENTRYPOINT FLASK_APP=/opt/folder/app.py flask run
##uvicorn pyfile:app --reload
