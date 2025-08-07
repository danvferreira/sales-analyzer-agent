# Usa imagem leve do Python 3.11
FROM python:3.11-slim

# Evita prompts durante instalação
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define diretório de trabalho
WORKDIR /app

# Copia só requirements primeiro para cache de build
COPY requirements.txt .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Cria um entrypoint para log mais claro
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Usa o entrypoint customizado
ENTRYPOINT ["/entrypoint.sh"]

# Garante que os imports funcionem com "from app..."
ENV PYTHONPATH=/app

# Expondo a porta padrão do Streamlit
EXPOSE 8501
