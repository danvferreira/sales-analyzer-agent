# Sales Analyzer powered by AI Agents

Uma aplicação de IA interativa que responde perguntas em linguagem natural sobre um arquivo de vendas (`sales.csv`). Utiliza modelos de linguagem como **Gemini** (Google) ou **GPT-4** (OpenAI) por meio do **LangChain**, com suporte tanto a execução local quanto via Docker.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **LangChain** (agentes baseados em DataFrames)
- **Gemini (Google Generative AI)** via `langchain-google-genai`
- **OpenAI (GPT-4)** via `langchain-openai`
- **Pandas** para manipulação do CSV
- **python-dotenv** para carregar variáveis de ambiente
- **Streamlit** para interface web
- **Pytest** para testes automatizados
- **Docker** (opcional) para ambiente controlado

---

## Estrutura de Arquivos

```

project/
├── app/
│   ├── agent.py         # Criação do agente LLM
│   ├── config.py        # Carregamento do .env
│   ├── loader.py        # Leitura do CSV com pandas
│   ├── main.py          # Interface CLI principal
│   └── streamlit_app.py # Interface Web com Streamlit
|
├── dataset/
│   └── sales.csv        # Arquivo de vendas (input)
|
├── tests/
│   ├── test_agent.py    # Teste para funcionamento do agente e robustez de perguntas
│   ├── test_config.py   # Teste para configuração das variaveis de ambiente
│   └── test_loader.py   # Teste para carregamento de dados
|
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de API (a ser criado)
├── Dockerfile           # Build da imagem Docker
├── .gitignore           
├── .dockerignore        
└── README.md

```

---

## Configuração das Chaves API (.env)

Crie um arquivo `.env` na raiz com suas chaves:

```
# Para usar o modelo Gemini (Google AI Studio)

GOOGLE_API_KEY=your_google_api_key_here

# Para usar o modelo GPT (OpenAI)

OPENAI_API_KEY=your_openai_api_key_here

````

---

## Instruções de Uso

### Ambiente Virtual (Recomendado para desenvolvimento)

```
# Crie o venv Conda ou virtualenv
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate no Windows

# Instale as dependências
pip install -r requirements.txt
````

#### Interface de Linha de Comando (CLI)

````
# Execute a aplicação
python app/main.py
````

#### Interface Web com Streamlit

````
# Execute a aplicação
streamlit run app/streamlit_app.py
````

---

### Docker

#### Build da imagem:

```
docker build -t sales-agent .
```

#### Execução (modo **CLI** por padrão):

```
docker run --env-file .env -it sales-agent
```

#### Usar Interface Web com **Streamlit** no Docker

Por padrão, o Docker executa a versão CLI. Para usar a interface web, edite o arquivo `docker-entrypoint.sh`, e, **descomente** a linha do streamlit e **comente** a linha de execução do main.py:

```
# python app/main.py

streamlit run app/streamlit_app.py --server.port=8501 --server.address=0.0.0.0
```

Depois, execute com:

```
docker build -t sales-agent .

docker run --env-file .env -p 8501:8501 sales-agent
```

Acesse no navegador:

```
http://localhost:8501
```

---

## Modelos Suportados

O agente suporta múltiplos modelos via o parâmetro `model`:

| Modelo           | Valor    | Requisitos                 |
| ---------------- | -------- | -------------------------- |
| Gemini 2.5 Flash | "gemini" | `GOOGLE_API_KEY` no `.env` |
| GPT-4            | "gpt"    | `OPENAI_API_KEY` no `.env` |

Escolha o modelo editando o `main.py` ou passando o valor ao `create_agent("gemini")` ou `create_agent("gpt")`.

O modelo "gemini" foi escolhido como `default` pelo acesso gratuito a chave API para fins de experimentação.

---

## Exemplos de Perguntas Suportadas

* Qual produto foi mais vendido?
* Qual local teve maior volume de vendas?
* Qual foi o total de vendas em julho?
* Qual a diferença total entre quantidade planejada e realizada?
* Qual o impacto das promoções no preço e volume vendido?

---

## Testes 

Testes de execução com `pytest` foram dispoinibilizados em `tests/`. Exemplo básico:

```python
from app.agent import create_agent

def test_basic_question():
    agent = create_agent("gemini")
    question = "Qual o produto mais vendido?"
    answer = agent.invoke(question)['output']
    assert isinstance(answer, str)
    assert len(answer) > 0
```

Execute os testes com:

```bash
set PYTHONPATH=. && pytest -v tests/
```

---

## Observações Finais

* **Não versionar `.env`** com as chaves de API.
* Interface modular: CLI e Web podem ser ativadas facilmente

---

Desenvolvido para o desafio **Analisador de Dados com Agentes**.




