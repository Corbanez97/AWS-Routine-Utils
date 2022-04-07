FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

RUN mkdir src
WORKDIR src/
COPY . .

##Installing required packages
RUN pip3 install -r requirements.txt

##Running test script
RUN python3 docker_test.py
RUN rm /src/data/raw_data.csv

##Cloning data repository! P.S.: Do not know if this is a good idea... It is worth a shot... I guess ¯\_(ツ)_/¯
WORKDIR src/data
RUN git clone https://github.com/astrocatalogs/sne-2015-2019.git

WORKDIR /src/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
