build:
	docker build -t toy-passthrough .

run:
	docker run -p 8080:8080 toy-passthrough
	
run-local:
	uvicorn src.app:app --reload --port 8080