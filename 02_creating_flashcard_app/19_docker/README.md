# Dockerizing Django App

- `docker build . --tag webapp:1.0`
- `docker run --publish 8000:8000 -it --name mathfc webapp:1.0` name attached to container to refrain from calling by container id everytime.
- `docker rm mathfc` to remove the container with that name reuse the command.
