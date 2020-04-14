# Django Template

This is a simple Django Hello World Application. After git clone from this website, you can build the docker image and run the container using the below command. Dockerfile and requirement.txt are also ready. 

You can also add more apps to the application. However, you may need to further update the files for any additional dependency.


<b>To Build the Docker Image</b>

docker build --tag myweb:latest .


<b>To run the Docker Image</b>

docker run --publish 8000:8000 --detach --name bb myweb:1.0

<b>To test the Web</b>

input <i>"IP address:8000"</i> in the browser
