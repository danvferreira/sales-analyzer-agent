#!/bin/bash

echo "Verificando variáveis de ambiente..."
if [ -z "$GOOGLE_API_KEY" ] && [ -z "$OPENAI_API_KEY" ]; then
  echo "Nenhuma API KEY definida. Configure o .env e passe com --env-file."
  exit 1
fi

echo "Iniciando Sales Agent..."

# versão CLI
python app/main.py

# versão web Streamlit
# streamlit run app/streamlit_app.py --server.port=8501 --server.address=0.0.0.0