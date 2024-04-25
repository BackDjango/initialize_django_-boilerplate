build:
	docker compose -f dev.yml up --build -d

down:
	docker compose -f dev.yml down

down-v:
	docker compose -f dev.yml down -v

logs:
	docker compose -f dev.yml logs