FROM python

RUN mkdir /building
WORKDIR /building

COPY app /building
COPY .docker/build-python/docker-entrypoint.sh /building

RUN chmod +x /building/docker-entrypoint.sh
RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt-get install -y cron && touch /var/log/cron.log
RUN apt-get install -y iputils-ping

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
