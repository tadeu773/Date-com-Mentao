import pygame
import random
from os import path
from config import *
from classes import *

pygame.mixer.init()
pygame.mixer.music.load(path.join('penelope.mp3'))
pygame.mixer.music.play(-1)

def tela_insper(screen):
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

        

        # Dentro do loop de desenho
        

        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        screen.blit(personagem_img, personagem_rect)
        Mentao.exibir(screen, fala1_mentao)
        pygame.display.flip()

    return state