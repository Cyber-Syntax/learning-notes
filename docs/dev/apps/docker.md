---
title: Docker
id: docker
created: 2026-10-11
updated: 2026-10-11
tags:
  - docker
  - containers
  - devops
---

<!-- TOC -->

## Start Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker # enable on every boot
sudo systemctl enable docker.socket # enable the socket as needed

# containerd may also need to be started
sudo systemctl start containerd
```

### Example: start a Kali Linux container

- `docker ps -a` – list all containers
- `docker start <container_id>` – start a stopped container
- `docker attach <container_id>` – attach to running container

## Remove containers and images

### Image

```bash
docker rmi -f leantime/leantime
```

### Container

```bash
docker rm <container_id>
```

## Inspect a container

```bash
docker inspect <container_id>
```

## List containers and images

### Containers

```bash
docker ps -a
```

### Images

```bash
docker images
```

## Run a container

```bash
docker run
```

## Docker Compose

### Start

```bash
docker-compose up -d
```

### Stop

```bash
docker-compose down
```

### Start Penpot

```bash
docker compose -p penpot -f docker-compose.yaml up -d
```

This will start the service and make it available at [http://localhost:9001](http://localhost:9001).

### Stop Penpot

If you want to stop a running Penpot environment, run:

```bash
docker compose -p penpot -f docker-compose.yaml down
```

## Install WordPress with Docker
>
> [!NOTE]
> Source: <https://www.lionbloggertech.com/how-to-setup-wordpress-with-docker-desktop/>

1. Install Docker Desktop on your computer.
2. Create a new project directory for your WordPress installation.
3. In that directory, create a file called `docker-compose.yml`.
4. Open `docker-compose.yml` in a text editor and paste the following configuration:

```yaml
version: "3"

services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: password

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    volumes:
      - wordpress_data:/var/www/html
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: password
      WORDPRESS_DB_NAME: wordpress

volumes:
  db_data:
  wordpress_data:
```

1. Save the file and close the editor.
2. Open a terminal and navigate to the project directory.
3. Run `docker-compose up -d` to create and start the containers.
4. Open your browser and visit [http://localhost:8000/](http://localhost:8000/) to complete the WordPress installation.
5. Choose your preferred language and continue.
6. Enter a site name and create an admin account.
7. Click "Install WordPress" to finish setup.

## Connect to a VNC session for any Linux distro

1. Install the required metapackages.
2. Install the required packages: `dbus-x11 xauth x11-apps`.
3. Install a desktop environment or window manager:

```bash
apt-cache search kali-desktop
```

<!-- /TOC -->
