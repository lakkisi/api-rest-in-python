compile:
	go build -o bin/main buildImage.go
	go build -o bin/main runContainer.go

build:	
	go run buildImage.go

run:
	go run runContainer.go
	