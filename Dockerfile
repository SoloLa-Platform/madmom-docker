FROM python:3.6.7-stretch

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y libfftw3-dev libfftw3-doc
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 
# COPY requirements.txt ./
RUN pip install --no-cache-dir pyfftw
RUN pip install --no-cache-dir madmom==0.15.1

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
