from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from app.loader import load_sales_data
from app.config import OPENAI_API_KEY, GOOGLE_API_KEY

SUPPORTED_MODELS = {
    "gpt": {
        "class": ChatOpenAI,
        "kwargs": {"model": "gpt-4", "temperature": 0}
    },
    "gemini": {
        "class": ChatGoogleGenerativeAI,
        "kwargs": {"model": "gemini-2.5-flash", "temperature": 0}
    }
}

def create_agent(model: str = 'gemini'):
    df = load_sales_data()

    if model not in SUPPORTED_MODELS:
        raise ValueError(f"Modelo '{model}' não suportado. Use: {list(SUPPORTED_MODELS.keys())}")

    llm_config = SUPPORTED_MODELS[model]
    llm = llm_config["class"](**llm_config["kwargs"])

    agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
    return agent
