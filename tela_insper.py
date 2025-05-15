import pygame
import random
from os import path
from config import *
from classes import *
import narrativas
import moods

def tela_insper(screen):
    clock = pygame.time.Clock()

    # Carrega o fundo
    background = pygame.image.load(path.join("Fundos", 'insper_inside.jpeg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Carrega as imagens dos moods após a tela existir
    imagens_mood = {
        "feliz": carrega_imagem('feliz.png'),
        "surpreso": carrega_imagem('surpreso.png'),
        "briga": carrega_imagem('briga.png'),
        "bravo": carrega_imagem('bravo.png'),
        "bebendo": carrega_imagem('bebendo.png')
    }

    # Começa a narrativa
    narrativas.criar_cena_inicial()

    # Define estado inicial da tela
    state = INSPER
    running = True

    def sair_para_mapa():
        nonlocal state, running
        state = MAPA
        running = False

    botao_sair = BotaoSair(sair_para_mapa)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            # Verifica cliques nos botões da narrativa
            for botao in narrativas.botoes_atuais:
                botao.checar_clique(event)

            # Verifica clique no botão sair
            botao_sair.checar_clique(event)

        # Atualiza o humor do personagem baseado no estado atual
        personagem_img = imagens_mood[moods.mood_mentao]
        personagem_rect = personagem_img.get_rect(center=(WIDTH // 2, 150))

        # Desenha a interface da tela
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        screen.blit(personagem_img, personagem_rect)

        if narrativas.fala_mentao is not None:
            Mentao.exibir(screen, narrativas.fala_mentao)

        for botao in narrativas.botoes_atuais:
            botao.desenhar(screen)

        botao_sair.desenhar(screen)

        pygame.display.flip()

    return state