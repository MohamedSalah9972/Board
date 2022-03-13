FROM python:3
ADD . /code                         
WORKDIR /code                        
RUN pip install -r requirements.txt  
WORKDIR /code/wait-for-it
RUN ./wait-for-it.sh -t 60 db:5432 -- python /code/manage.py migrate
