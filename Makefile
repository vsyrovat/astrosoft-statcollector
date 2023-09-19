.PHONY: fmt checkfmt clean test

fmt:
	isort --profile black .
	black .

checkfmt:
	black . --check --diff

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

test:
	python manage.py test
