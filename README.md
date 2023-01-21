# Demo for load testing FastAPI

In this repo we are using [Apache Jmeter](https://jmeter.apache.org/) to load
test [FastAPI](https://fastapi.tiangolo.com/).

## Requirements

- Apache Jmeter >= 5.5
- Docker >= 20.10.17

## Steps to run load test

- Build both apps:
   - FastAPI: `docker build -t api-flask .`
   - Flask: `docker build -t api-flask .`
- Run both API apps:
    - FastAPI: `docker run -it --rm -e PORT=7100 -p 7100:7100 api-fastapi` 
    - Flask: `docker run -it --rm -e PORT=6000 -p 6000:6000 api-flask` 
- Create Jmeter output directory:
    - FastAPI: `mkdir -p api-fastapi/output/`
    - Flask: `mkdir -p api-flask/output/`
- Run Jmeter load test:
    - FastAPI: `jmeter -e -f -n -t requests.jmx -Jport=7100 -Jusers=100 -Jrampup=0.01 -o api-fastai/output/ -l api-fastapi/output/j.logs`
    - Flask: `jmeter -e -f -n -t requests.jmx -Jport=6000 -Jusers=100 -Jrampup=0.01 -o api-flask/output/ -l api-flask/output/j.logs`


