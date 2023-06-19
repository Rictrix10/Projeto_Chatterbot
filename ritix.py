import nltk
import combs
import jogogalo
import jogodamas
from nltk.chat.util import Chat, reflections
import seaborn as sns

# Faça o download dos dados necessários
nltk.download('punkt')

chatbot = Chat(combs.pares, reflections)


def converse():
    print("Olá! Inicie a conversa digitando uma mensagem ou digite 'sair' para encerrar.")
    jogo_iniciado = False

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Até logo!")
            break
        elif user_input.lower() == "jogo do galo":
            jogo1 = jogogalo.JogoDoGalo()
            jogo1.jogar()
            jogo_iniciado = True
        elif user_input.lower() == "jogo das damas":
            jogo2 = jogodamas.JogoDamas()
            jogo2.jogar()
            jogo_iniciado = True

        elif not jogo_iniciado:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)


converse()
