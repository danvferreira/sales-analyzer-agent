import pytest
from app.agent import create_agent

def test_basic_question():
    agent = create_agent("gemini")
    question = "Qual o produto mais vendido?"
    answer = agent.invoke(question)['output']
    assert isinstance(answer, str)
    assert len(answer) > 0

@pytest.mark.parametrize("question", [
    "Qual produto foi mais vendido?",
    "Qual local teve maior volume de vendas?",
    "Qual foi o total de vendas em junho?",
    "Qual o impacto das promoções no preço e volume vendido?"
])
def test_common_questions(question):
    agent = create_agent("gemini")
    answer = agent.invoke(question)['output']
    assert isinstance(answer, str)
    assert len(answer) > 0