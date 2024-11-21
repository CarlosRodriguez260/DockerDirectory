#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="carlos"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY . .
# Now the structure looks like this '/usr/app/src/test.py'

RUN chmod +x MMRTracker.py
RUN pip install bs4
RUN pip install selenium
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./MMRTracker.py"]