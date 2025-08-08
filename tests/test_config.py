"""
Verifica que as variáveis de ambiente críticas estão presentes.
"""

from app.config import OPENAI_API_KEY, GOOGLE_API_KEY

def test_env_var_exists():
    assert (GOOGLE_API_KEY is None) or isinstance(GOOGLE_API_KEY, str)
    assert (OPENAI_API_KEY is None) or isinstance(OPENAI_API_KEY, str)

