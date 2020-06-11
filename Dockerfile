FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6
RUN python --version
RUN pip install --upgrade pip
RUN mkdir -p /usr/src/tests/
WORKDIR /usr/src/tests/
COPY  . /usr/src/tests/
RUN pip3 install -r requirements.txt

