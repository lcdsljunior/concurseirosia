from core.engine import EstudoAgente

def rodar_sistema():
    print("Iniciando Mentor de Concursos...")
    try:
        agente = EstudoAgente()
        print("Bot ativo! Digite 'sair' para parar.\n")
        
        while True:
            pergunta = input("Sua dúvida: ")
            if pergunta.lower() == 'sair':
                break
                
            resposta = agente.perguntar(pergunta)
            print(f"\nMENTOR:\n{resposta}\n" + "-"*30)
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    rodar_sistema()