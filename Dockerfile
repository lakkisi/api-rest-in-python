####### Build image with : 
# docker build -t api-rest-in-python .
####### Deploy container with : 
# docker run -p 5000:5000 -d api-rest-in-python
####### if you want persistent storage share volume /app/database like 
# docker run -v /path/to/your/local/database:/app/database -p 5000:5000 -d api-rest-in-python

FROM python:2.7.16

# copy python project artefacts
COPY rest_api_framework /app/rest_api_framework
COPY ["*.py", "*.txt", "/app/"]

# create database directory
RUN mkdir -p /app/database

# set WORKDIR and get python dependencies
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose PORT and run API REST application
EXPOSE 5000
CMD ["python", "app.py"]


