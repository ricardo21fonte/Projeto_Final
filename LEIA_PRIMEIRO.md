# Kit inicial - Trabalho Pratico Integrador Aulas 01-06

Este kit acompanha a ficha de avaliacao em Word. Os ficheiros com TODO sao para completar.

## Estrutura
- app.py + requirements*.txt + tests/: API FastAPI e testes ja fornecidos.
- Dockerfile + .dockerignore: completar no Exercicio 01.
- compose.yaml: completar no Exercicio 02.
- incidente.yaml: overlay defeituoso para o Exercicio 03 (nao corrigir antes desse passo).
- Jenkinsfile: completar no Exercicio 05.
- RELATORIO.md: evidencias e registo curto a entregar.

## Regras
Nao correr `docker system prune` nem `docker compose down -v` durante a avaliacao.
Nao incluir credenciais, tokens nem ficheiros .env no repositorio.
O Jenkins, Git remoto e agente com Docker/Python devem estar previamente disponiveis.
Os comandos de criacao da .venv no Jenkins destinam-se a agente Linux.

Consulte o documento Word para os passos, tempos e criterios de avaliacao.
