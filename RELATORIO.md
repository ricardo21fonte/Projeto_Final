# Relatorio de evidencias - Trabalho Pratico Integrador 01-06

Nome: Ricardo Moreira da Fonte   Data: 24/11/2026
URL do repositorio Git: https://github.com/ricardo21fonte/Projeto_Final.git

## E01 - Ambiente (1 valor)
Comandos e versoes observadas:
docker --version : Docker version 29.9.2
Docker Compose version v5.6.1
git version 2.55.0.windows.2
Docker version:
    Client:
        Version:    29.9.2
        Context:    desktop-linux
    Server:
    Containers: 7
        Running: 0
        Paused: 0
        Stopped: 7
    Images: 14
    Server Version: 29.9.2

Ficheiros: 
    API: app.py
    Testes: tests/test_app.py
    Compose: compose.yaml
    Pipeline: Jenkinsfile

A API está em app.py, os testes em tests/test_app.py, a configuração Compose em compose.yaml e a pipeline em Jenkinsfile.

## E02 - Dockerfile e container (3 valores)
Tag da imagem; docker ps; HTTP /health; utilizador efetivo do container:
Tag: docker ps natixis-support:1.0
Portas:  docker ps 127.0.0.1:18080->8000/tcp 
ID: docker exec tp-api id  uid=10001 gid=10001 groups=10001
Container: docker ps tp-api
Logs: docker logs --tail 15 tp-api  INFO:     172.17.0.1:35960 - "GET /health HTTP/1.1" 200 OK
HTTP: curl -i http://127.0.0.1:18080/health
        HTTP/1.1 200 OK
        date: Tue, 24 Nov 2026 09:43:08 GMT
        server: uvicorn
        content-length: 55
        content-type: application/json

        {"status":"ok","service":"support-api","version":"1.0"}

A API respondeu com HTTP 200 e executou com UID 10001.

## E03 - Compose, DNS, healthcheck e volume (4 valores)
Resultado de docker compose config; health; teste checker -> api; contador antes/depois da recriacao:
docker compose config --quiet  correu sem apresentar erros
docker compose ps
    NAME                       IMAGE                   COMMAND                  SERVICE   CREATED         STATUS                  
    natixis-integrador-api-1   natixis-support:local   "python -m uvicorn a…"   api       9 seconds ago   Up 8 seconds (healthy)  
PORTS 127.0.0.1:18080->8000/tcp
DNS: docker compose --profile diagnostico run --rm checker -fsS http://api:8000/health       {"status":"ok","service":"support-api-integrador","version":"1.0"}

Antes contador: curl -i http://127.0.0.1:18080/visits
Contador depois: docker compose up -d --force-recreate 
    Contador antes : 0 depois da recriaçao 1

O contador foi preservado porque o ficheiro visitas estava guardado no volume app-data, e o Docker reutilizou ao recriar o novo container.

## E04 - Incidente Docker (3 valores)
Sintoma, comandos de investigacao, causa-raiz, alteracao realizada, prova da recuperacao e contador preservado:
SINTOMA: Correndo o comnado docker compose -f compose.yaml -f incidente.yaml up -d --force-recreate a api estava em execuçao com o Status healyh:starting e quando verifiquei o estado healthpela porta 18080 falhou curl: (52) Empty rely from server
COMANDOS DE INVESTIGAÇAO: docker compose -f compose.yaml -f incidente.yaml ps , docker compose -f compose.yaml -f incidente.yaml logs --tail 30 api , docker compose -f compose.yaml -f incidente.yaml config , curl.exe http://127.0.0.1:18080/health.
CAUSA: Os logs mostraram que o Uvicorn a executar em 0.0.0.8001. A porta 18080 do host encaminhava para 8000 no container e que o healthcheck também consultava 8000.
CORREÇÃO: recriar a api coom o comando docker compose up -d --force-recreate 
VALIDAÇAO: execuando curl -i http://127.0.0.1:18080/health
HTTP/1.1 200 OK
date: Tue, 24 Nov 2026 10:37:46 GMT
server: uvicorn
content-length: 66
content-type: application/json
{"status":"ok","service":"support-api-integrador","version":"1.0"}
CONTADOR: curl.exe http://127.0.0.1:18080/visits
{"visits":1}


## E05 - Git (3 valores)
Branch, hashes de commits, merge e tag v1.0.0: 
BRANCH: fix/health-info
HASH: 60662ff (HEAD -> main, tag: v1.0.0, fix/health-info) fix: acrescentar identificacao no health
      e1c3c94 feat: ambiente integrador funcional
MERGE: git merge fix/health-info
            Updating e1c3c94..60662ff
            Fast-forward
            app.py            | 3 ++-
            tests/test_app.py | 1 +
            2 files changed, 3 insertions(+), 1 deletion(-)
TAG: (HEAD -> main, tag: v1.0.0, fix/health-info)

A tag anotada v1.0.0 foi criada e aponta para 60662ff, que inclui a alteração ao endpoint e ao teste.

## E06 - Jenkins SUCCESS (4 valores)
URL/numero do build, etapas e identificador da imagem construida:
build 1 URL: sha256:84a59c6850d7680c8c822cd358657ce38668ba5291650b90486f4b92d482a0f4
ETAPAS:  Checkout SCM    Checkout     Tests     Dockerbuild
consultar pasta evidencias

As etapas Checkout SCM, Checkout, Tests e Docker Build terminaram com sucesso. A imagem foi construída e o respetivo ID foi confirmado.
## E07 - Jenkins FAILURE e recuperacao (2 valores)
Consultar pasta evidencias

A pipeline falhou na etapa Tests porque o test_health esperava offline e a API devolveu ok, pelo que a etapa Docker Build foi saltada a frente. Depois de repor o test_health para ok num novo commit, a pipeline voltou a terminar com SUCCESS

## Verificacao final
[ ] Dockerfile [ ] compose.yaml [ ] app.py [ ] tests/ [ ] Jenkinsfile
[ ] Historico Git [ ] Tag v1.0.0 [ ] Evidencias E01-E07


HISTORICO GIT

ricar@Ricardo_Fonte MINGW64 ~/Desktop/DEVOPS/TP_Integrador_Kit_Formandos (main)
$ git log --oneline --graph --decorate --all
* d2bfb86 (HEAD -> main, origin/main) resuperaçao da validaçao no teste de health
* 5bcbcd3 simulaçao de falha no teste de health
* 4f19e72 Pipeline Jenkins completa
* 60662ff (tag: v1.0.0, fix/health-info) fix: acrescentar identificacao no health
* e1c3c94 feat: ambiente integrador funcional
