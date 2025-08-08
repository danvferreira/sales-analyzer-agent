"""
app.main
Interface de linha de comando para interação com o agente.
"""

from app.agent import create_agent

def main():
    agent = create_agent('gemini') # ou 'gpt'
    while True:
        question = input("Digite sua pergunta sobre os dados (ou 'sair'): ")
        if question.lower() == 'sair':
            break
        response = agent.invoke(question)['output']
        print(f"\nResposta: {response}\n")

if __name__ == "__main__":
    main()