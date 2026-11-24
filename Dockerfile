FROM python:3.13-slim
WORKDIR /app

# TODO 1: copiar requirements.txt antes de copiar app.py
# TODO 2: instalar as dependencias com pip --no-cache-dir
# TODO 3: copiar app.py para /app
# TODO 4: criar utilizador sem privilegios e preparar /data com permissoes de escrita
# TODO 5: definir USER para esse utilizador
COPY requirements.txt . 
  
RUN pip install --no-cache-dir \ 
    -r requirements.txt 
  
COPY app.py . 
USER 10001:10001

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
