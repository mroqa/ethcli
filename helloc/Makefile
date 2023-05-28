.PHONY: build
build:
	gcc ./cmd/hello/helloworld.c -o ./bin/hello

.PHONY: deploy
deploy: build
	cp ./bin/hello ./roles/install-hello-c/files/hello 
	ansible-playbook -e svrname=$(svr) -i ./hosts hello.yml
