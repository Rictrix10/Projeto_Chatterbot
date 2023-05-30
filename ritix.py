import nltk
import combs
from nltk.chat.util import Chat, reflections

# Faça o download dos dados necessários
nltk.download('punkt')

chatbot = Chat(combs.pares, reflections)

def converse():
    print("Olá! Inicie a conversa digitando uma mensagem ou digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Até logo!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

converse()