# recipe-app-api
## Recipe API project

(YouTube Link) [Deploying Django with Docker Compose](https://www.youtube.com/watch?v=mScd-Pc_pX0)

### DockerHub Security
You need docker account and password.
[Security Page Link](https://hub.docker.com/settings/security)

### Creating New Access Token
Name: recipe-app-api
AccessToken: dckr_pat_B6-IgDekmcTCBtnMt3oclPUmugM

(Docker Security Access Token Screen Dialog)

```shell
# Shell Script
docker login -u wobblebricklayers
```

GitHub Secrets and variables


---
## Docker

## Delete
```shell
docker-compose down --rmi all --volumes --remove-orphans
```

### Create My Own Network
```shell
docker network create --attachable -d bridge mydockernetwork
```
### Network Settings in the Docker Compose File
```shell
# docker-compose.yml
version: 3.9

networks:
  default:
    external:
      name: mydockernetwork
```

## Docker
```shell
FROM python:3.9-alpine3.13
LABEL maintainer="bricklayers"

ENV PYTHONNUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \

ENV PATH="/py/bin:$PATH"

USER django-user


```

```shell
FROM python:3.9-alpine3.13
LABEL maintainer="bricklayers"

ENV PYTHONNUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk ad --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/py/bin:$PATH"

USER django-user

CMD ["run.sh"]
```




### Creating Core
```shell
docker-compose run --rm app sh -c "python manage.py startapp core"
```
### Migrations
```shell
docker-compose run --rm app sh -c "python manage.py makemigrations"
```



## Creating Django Project using Django CLI on Docker



```shell
docker-compose run --rm app sh -c "django-admin startproject app ."
```



[EC2-Docker](https://zenn.dev/ttani/articles/docker-install-deploy-ec2)



---------------
## Django Kubernetes
[Deploy Django into Production with Kubernetes, Docker, & Github Actions. Complete Tutorial Series](https://www.youtube.com/watch?v=NAOsLaB6Lfc)