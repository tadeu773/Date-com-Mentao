import pygame
import random
from os import path
from config import *
from classes import *

pygame.mixer.init()
pygame.mixer.music.load(path.join('penelope.mp3'))
pygame.mixer.music.play(-1)

def tela_pscina(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join('insper_inside.jpeg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    TAMANHO_PERSONAGEM = (300, 300)

    fala1_mentao = Mentao.fala("eae mano como se ta, tudo bem com você? Bora dar um rolê depois da aula?")

    imagens_mood = {
    "feliz": carrega_imagem('feliz.png'),
    "surpreso": carrega_imagem('surpreso.png'),
    "briga": carrega_imagem('briga.png'),
    "bravo": carrega_imagem('bravo.png'),
    "bebendo": carrega_imagem('bebendo.png')
}

    mood_atual = "feliz"

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mood_atual = "feliz"
                elif event.key == pygame.K_2:
                    mood_atual = "briga"
                elif event.key == pygame.K_3:
                    mood_atual = "surpreso"
                elif event.key == pygame.K_4:
                    mood_atual = "bebendo"
                elif event.key == pygame.K_5:
                    mood_atual = "bravo"

        personagem_img = imagens_mood[mood_atual]
        personagem_rect = personagem_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))



import pygame
import random
import sys

# Inicialização
pygame.init()
largura, altura = 800, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Corrida na Piscina")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 32)

# Cores
AZUL = (0, 150, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 50, 50)
VERDE = (50, 255, 100)

# Jogadores
jogador_x = 50
bot_x = 50
y_jogador = 150
y_bot = 250

# Estado do jogo
distancia_vitoria = 700
jogo_ativo = True
vencedor = ""

# Loop do jogo
while True:
    tela.fill(AZUL)  # Fundo azul = piscina

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if jogo_ativo:
        # Tecla espaço move o jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jogador_x += 5

        # Bot avança automaticamente
        bot_x += random.randint(1, 3)

        # Verifica vitória
        if jogador_x >= distancia_vitoria:
            vencedor = "Você venceu! 🏆"
            jogo_ativo = False
        elif bot_x >= distancia_vitoria:
            vencedor = "O bot venceu! 🤖"
            jogo_ativo = False

    # Desenha os "nadadores"
    pygame.draw.rect(tela, VERMELHO, (jogador_x, y_jogador, 40, 20))  # jogador
    pygame.draw.rect(tela, VERDE, (bot_x, y_bot, 40, 20))             # bot

    # Mostra o vencedor se o jogo acabou
    if not jogo_ativo:
        texto = fonte.render(vencedor, True, BRANCO)
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, 20))

    pygame.display.flip()
    relogio.tick(60)
