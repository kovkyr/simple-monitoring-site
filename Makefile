include .env

help:
	@echo ""
	@echo "usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  docker-create                Create containers, then start containers and create database"
	@echo "  docker-delete                Destroy containers and database"
	@echo "  docker-recreate              Execute docker-delete and docker-create"
	@echo ""
	@echo "  docker-start                 Start containers"
	@echo "  docker-stop                  Stop containers"
	@echo "  docker-restart               Execute docker-stop and docker-start"
	@echo ""
	@echo "  psql-backup                  Backup database"
	@echo "  psql-restore                 Restore database"
	@echo ""
	@echo "  django-migrate               Migrate database to last release"
	@echo "  django-shell                 Enter django shell"
	@echo ""
	@echo "  shell-python                 Enter python container"
	@echo "  shell-cron                   Enter cron container"
	@echo "  shell-psql                   Enter psql container"
	@echo ""

docker-create:
	@mkdir -p ./dumps
	@docker compose build
	@docker compose up -d --wait
	@docker compose run python /bin/sh -c "python /app/manage.py makemigrations"
	@docker compose run python /bin/sh -c "python /app/manage.py migrate"
	@docker compose run python /bin/sh -c "python /app/manage.py shell -c \"from django.contrib.auth.models import User; User.objects.create_superuser('$(SUPERUSER_NAME)', '$(SUPERUSER_EMAIL)', '$(SUPERUSER_PASSWORD)')\""
	@if [ -n "$(DEBUG)" ] && [ $(DEBUG) = "False" ]; then \
		docker compose run python python /app/manage.py collectstatic --noinput; \
	fi
	@docker compose down
	@docker compose up -d --wait

docker-delete:
	@docker compose down
	@rm -rf ./postgresql-data

docker-recreate: docker-delete docker-create

docker-start:
	@if [ -n "$(DEBUG)" ] && [ $(DEBUG) = "False" ]; then \
		docker compose run python python /app/manage.py collectstatic --noinput; \
	fi
	@docker compose up -d --wait

docker-stop:
	@docker compose down

docker-restart: docker-stop docker-start

django-migrate:
	@docker compose exec python /bin/sh -c "python /app/manage.py makemigrations"
	@docker compose exec python /bin/sh -c "python /app/manage.py migrate"

django-shell:
	@docker compose exec python python /app/manage.py shell

psql-backup:
	@docker compose exec -t psql pg_dump $(DB_NAME) -c -U $(DB_USER) > dumps/db.sql

psql-restore:
	@docker compose exec -T psql psql $(DB_NAME) -U $(DB_USER) < dumps/db.sql

shell-python:
	@docker compose exec -it python /bin/bash

shell-cron:
	@docker compose exec -it cron /bin/bash

shell-psql:
	@docker compose exec -it psql /bin/bash
