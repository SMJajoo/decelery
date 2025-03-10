FROM python:3.11.9-alpine

WORKDIR /usr/src/app

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTOHNUNBUFFERED=1

RUN pip install --upgrade pip

 # copy dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project code
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
