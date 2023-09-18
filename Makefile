.PHONY: fmt checkfmt

fmt:
	isort --profile black .
	black .

checkfmt:
	black . --check --diff
