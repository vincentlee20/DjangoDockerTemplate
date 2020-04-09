# DjangoHelloWorld

To Build the Docker Image

docker build --tag myweb:latest .




To run the Docker Image

docker run --publish 8000:8080 --detach --myweb bb myweb:1.0
