import pygame
import os

# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#PROGRESSO DO JOGADOR

progresso_jogador = {
    "piscina": False,
    "madero": False,
    "jk": False,
}

# Estados para controle do fluxo da aplicação
INIT = 0
MAPA = 1
QUIT = 2
INSPER = 3
PSCINA = 4
PRE_PSCI = 5
GAMEOVER = 6
JK = 7
MADERO = 8