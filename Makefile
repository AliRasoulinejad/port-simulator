prepare-configs:
	if [ ! -f configsww.ini ]; then cp ./configs.example.ini ./configsww.ini; fi
# ------ Manually ------
run:
	python main.py
# ------- Docker --------
build-image:
	sudo docker build . -t port-simulator:latest

run-image:
	sudo docker run --name port-simulator -v ${pwd}/configs.ini:/app/configs.ini port-simulator:latest

run-docker: build-image run-image

.PHONY: prepare-configs run build