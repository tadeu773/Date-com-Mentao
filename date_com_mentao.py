# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
pygame.init()
import random
from config import *
from init_screen import init_screen
from mapa import tela_mapa
from classes import *
from tela_insper import tela_insper
from pscina import *
from pre_jogo_piscina import *
from Jogo_JK import *
from madero import *
from gameover import *
from pre_jk import *
from pre_madero import *
from insperina import *
from tela_final import *


pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Date com Mentao')

state = INIT

while state != QUIT:
    if state == INIT:
        state = init_screen(tela)
    if state == MAPA:
        state = tela_mapa(tela)
    if state == INSPER:
        state = tela_insper(tela)
    if state == PSCINA:
        state = tela_pscina(tela)
    if state == PRE_PSCI:
        state = pre_jogo_piscina(tela)
    if state == JK:
        state = tela_pipoca(tela)
    if state == MADERO:
        state = jogo_madero(tela)
    if state == GAMEOVER:
        state = game_over(tela)
    if state == PRE_JK:
        state = pre_jogo_jk(tela)
    if state == PRE_MADERO:
        state = pre_madero(tela)
    if state == INSPERINA:
        state = tela_insperina(tela)
    if state == TELA_FINAL:
        state = tela_final(tela)
    

    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados