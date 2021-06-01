FROM python:3

WORKDIR /usr/src/app

COPY requirments.txt .
COPY entrypoint.sh .

RUN pip install -r requirments.txt
RUN chmod +x entrypoint.sh

COPY ./testapp .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]