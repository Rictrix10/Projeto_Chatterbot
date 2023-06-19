import sys
from termcolor import colored


class JogoDamas:
    def __init__(self):
        self.tabuleiro = [
            [' ', colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red')],
            [colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red'), ' '],
            [' ', colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red'), ' ', colored('O', 'red')],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green'), ' '],
            [' ', colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green')],
            [colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green'), ' ', colored('O', 'green'), ' ']
        ]
        self.jogador_atual = 'O'
        self.jogador_oponente = 'X'

    def exibir_tabuleiro(self):
        print('    A   B   C   D   E   F   G   H')
        print('  ---------------------------------')
        for i in range(8):
            row = ''
            for j in range(8):
                peca = self.tabuleiro[i][j]
                if peca == ' ':
                    row += '|   '
                else:
                    cor = 'red' if peca == colored('O', 'red') else 'green'
                    row += "| " + colored(peca, cor) + " "
            row += '|'
            print(f"{i+1} {row}\n  ---------------------------------")

    def converter_coluna(self, coluna):
        return ord(coluna.upper()) - ord('A')

    def fazer_jogada(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        peca = self.tabuleiro[linha_origem][coluna_origem]
        if peca == self.jogador_atual:
            self.tabuleiro[linha_origem][coluna_origem] = ' '
            self.tabuleiro[linha_destino][coluna_destino] = peca
        else:
            print('Posição inválida. Tente novamente.')

    def jogar(self):
        print("Iniciando Jogo de Damas!")
        self.exibir_tabuleiro()

        while True:
            origem = input("Escolha a peça de origem (ex: A1): ")
            destino = input("Escolha o destino (ex: B2): ")

            coluna_origem = self.converter_coluna(origem[0])
            linha_origem = int(origem[1]) - 1

            coluna_destino = self.converter_coluna(destino[0])
            linha_destino = int(destino[1]) - 1

            self.fazer_jogada(linha_origem, coluna_origem, linha_destino, coluna_destino)
            self.exibir_tabuleiro()


jogo = JogoDamas()
jogo.jogar()




