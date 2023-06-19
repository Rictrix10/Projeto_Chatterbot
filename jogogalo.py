import nltk
from nltk.chat.util import Chat, reflections
import random


class JogoDoGalo:
    def __init__(self):
        self.tabuleiro = [[' '] * 3 for _ in range(3)]
        self.jogador_atual = 'X'
        self.jogador_chatbot = 'O'

    def exibir_tabuleiro(self):
        print('-------------')
        for linha in self.tabuleiro:
            print(f'| {linha[0]} | {linha[1]} | {linha[2]} |')
            print('-------------')

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha-1][coluna-1] == ' ':
            self.tabuleiro[linha-1][coluna-1] = self.jogador_atual
            self.jogador_atual, self.jogador_chatbot = self.jogador_chatbot, self.jogador_atual
        else:
            print('Posição inválida. Tente novamente.')

    def verificar_vitoria(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return True

        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != ' ':
                return True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

    def jogar(self):
        print("Iniciando Jogo do Galo!")
        self.exibir_tabuleiro()

        while True:
            linha = int(input("Escolha a linha (1-3): "))
            coluna = int(input("Escolha a coluna (1-3): "))
            self.fazer_jogada(linha, coluna)
            self.exibir_tabuleiro()

            if self.verificar_vitoria():
                print(f"Parabéns! O jogador {self.jogador_atual} venceu!")
                break

            if self.verificar_empate():
                print("Empate!")
                break


class JogoDoGaloComChatbot(JogoDoGalo):
    def obter_jogada_chatbot(self):
        posicoes_disponiveis = [(linha, coluna) for linha in range(
            1, 4) for coluna in range(1, 4) if self.tabuleiro[linha-1][coluna-1] == ' ']
        return random.choice(posicoes_disponiveis)

    def jogar_com_chatbot(self):
        print("Iniciando Jogo do Galo contra o ChatBot!")
        self.exibir_tabuleiro()

        while True:
            linha = int(input("Escolha a linha (1-3): "))
            coluna = int(input("Escolha a coluna (1-3): "))
            self.fazer_jogada(linha, coluna)
            self.exibir_tabuleiro()

            if self.verificar_vitoria():
                print(f"Parabéns! Você venceu!")
                break

            if self.verificar_empate():
                print("Empate!")
                break

            linha_chatbot, coluna_chatbot = self.obter_jogada_chatbot()
            self.fazer_jogada(linha_chatbot, coluna_chatbot)
            print(
                f"O ChatBot fez a jogada na posição ({linha_chatbot}, {coluna_chatbot})")
            self.exibir_tabuleiro()

            if self.verificar_vitoria():
                print(f"O ChatBot venceu!")
                break

            if self.verificar_empate():
                print("Empate!")
                break


jogo = JogoDoGaloComChatbot()
jogo.jogar_com_chatbot()
