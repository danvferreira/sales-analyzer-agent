from app.config import OPENAI_API_KEY, GOOGLE_API_KEY

def test_env_var_exists():
    assert OPENAI_API_KEY is not None
    assert GOOGLE_API_KEY is not None

