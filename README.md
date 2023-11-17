# OpenFaaS

## Command
`faas-cli up` including following actions
* `faas-cli build`: create a local container image, and install any other files needed, like those in the `requirements.txt` file
* `faas-cli push`: transfer the function's container image from local Docker library up to the hosted registry
* `faas-cli deploy`: using the OpenFaaS REST API, create a Deployment inside the Kubernetes cluster and a new Pod to serve traffic

## Build
```
cd /Users/chunglun/Documents/GitHub/OpenFaaS
```

Create
```
/Users/chunglun/.arkade/bin/faas-cli new --lang python3 apitest
```

Build
```
/Users/chunglun/.arkade/bin/faas-cli up -f apitest.yml
```

## Test
```
curl http://127.0.0.1:8080/function/apitest

curl --data "bytes" http://127.0.0.1:8080/function/apitest
```
![Alt text](image.png)

```
curl http://127.0.0.1:8080/function/apitest --data-binary '{ "name": "CLLUV", "greeting": "Hallo"}'
```