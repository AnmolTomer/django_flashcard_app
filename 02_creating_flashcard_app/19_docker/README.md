# Dockerizing Django App

- `docker build . --tag webapp:1.0`
- `docker run --publish 8000:8000 -it --name mathfc webapp:1.0` name attached to container to refrain from calling by container id everytime.
- `docker rm mathfc` to remove the container with that name reuse the command.

---

- If you are having a docker-compose.yml file, for first time you would run `docker-compose up --build` to build and run the image
- After you are done press `Ctrl+C` or do a `docker-compose stop`
- To start the docker-compose from second time onwards after build is succesful just do a simple `docker-compose up` and that's it.
