# Menu management REST API

## Requirements
- Docker
- Docker-compose

## Installation
- Clone the repository
- Run the following command to build the docker image

```sh
docker compose --env-file ./pgdb.env --env-file ./api.env build
```

- Run the following command to start the docker container

```sh
docker compose --env-file ./pgdb.env --env-file ./api.env up
```
