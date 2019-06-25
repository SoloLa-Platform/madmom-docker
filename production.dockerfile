FROM python:3.6.7-stretch

RUN apt-get update && apt-get install -y libfftw3-dev libfftw3-doc ffmpeg
WORKDIR /
RUN git clone https://github.com/SoloLa-Platform/madmom-docker.git
WORKDIR /madmom-docker
RUN pip install --no-cache-dir -r requirements.txt 
RUN pip install --no-cache-dir pyfftw madmom==0.15.1