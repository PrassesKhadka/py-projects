# Build -> docker build -t myimage .
# Start the docker container -> docker run -d --name mycontainer -p 80:80 myimage
FROM python:3.10

WORKDIR /code

# There's an important trick in this Dockerfile, 
# we first copy the file with the dependencies alone, 
# not the rest of the code.
# Why???
# Docker and other tools build these container images incrementally, adding one layer on top of the other,
# starting from the top of the Dockerfile and adding any files created by each of the instructions of the Dockerfile.
# Docker and similar tools also use an internal cache when building the image,
# if a file hasn't changed since the last time building the container image, 
# then it will reuse the same layer created the last time, instead of copying the file again and creating a new layer from scratch.
# Just avoiding the copy of files doesn't necessarily improve things too much,
# but because it used the cache for that step, it can use the cache for the next step. For example, it could use the cache for the instruction that installs dependencies with:
COPY ./requirements.txt /code/requirements.txt

# The --no-cache-dir option tells pip to not save the downloaded packages locally,
# as that is only if pip was going to be run again to install the same packages,
# but that's not the case when working with containers.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PYTHONPATH=/code
COPY ./app /code/app

CMD ["python3","app/main.py"]