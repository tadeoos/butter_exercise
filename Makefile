up:
	@docker-compose -f local.yml up

serve:
	@docker-compose -f local.yml run --rm --service-ports django

build:
	@docker-compose -f local.yml up --force-recreate --build

shell:
	@docker-compose -f local.yml run --rm django python ./manage.py shell_plus

bash:
	@docker-compose -f local.yml run --rm django /bin/sh

manage:
	@docker-compose -f local.yml run --rm django python ./manage.py $(filter-out $@,$(MAKECMDGOALS))

test:
	@docker-compose -f local.yml run --rm django pytest

stop:
	docker-compose -f local.yml stop

redeploy:
	@docker-compose -f production.yml stop
	@git pull
	@docker-compose -f production.yml up -d --build

# https://stackoverflow.com/a/6273809/1826109
%:
	@:

