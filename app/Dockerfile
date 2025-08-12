FROM python:3.10-slim

WORKDIR /app

# Copiar arquivos
COPY main.py /app
COPY requirements.txt /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta do Streamlit
EXPOSE 8501

# Comando para iniciar Streamlit
CMD ["streamlit", "run", "main.py"]
