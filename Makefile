start-rabbit-mq:
	docker run -it --privileged --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

run-server:
	python3 server.py

run-client:
	python3 client.py
