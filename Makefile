.PHONY: up test land
up:
	docker compose up -d
test:
	pytest -q
land:
	python -m scripts.land --day $(DAY)
