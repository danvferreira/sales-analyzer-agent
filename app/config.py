"""
app.config
Responsável por carregar variáveis sensíveis do .env e expor configurações centrais.
"""

from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
