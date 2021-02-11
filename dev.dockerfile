FROM python:3.9.1-buster

RUN apt-get update && apt-get install -y libfftw3-dev libfftw3-doc ffmpeg
WORKDIR /beat_tracker

COPY requirements.txt ./
COPY . /beat_tracker
RUN pip install --no-cache-dir -r requirements.txt 
RUN pip install --no-cache-dir pyfftw madmom==0.15.1

# COPY . .
# CMD [ "python", "./your-daemon-or-script.py" ]
