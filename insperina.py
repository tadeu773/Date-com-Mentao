import pygame
import random
from os import path

from config import *
from classes import *
import narrativas
import moods

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR     = path.dirname(path.abspath(__file__))
FUNDOS_DIR     = path.join(SCRIPT_DIR, "Fundos")
MOODS_DIR      = SCRIPT_DIR  # supondo que carrega_imagem anime relativo ao script
NARRATIVAS_DIR = SCRIPT_DIR  # narrativas e moods já importados como módulos

def tela_insperina(screen):
    clock = pygame.time.Clock()

    # Carrega o fundo usando caminho absoluto
    background_path = path.join(FUNDOS_DIR, 'insperina.jpg')
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Carrega as imagens dos moods
    imagens_mood = {
        "feliz":    carrega_imagem(path.join('feliz.png')),
        "surpreso": carrega_imagem(path.join('surpreso.png')),
        "briga":    carrega_imagem(path.join('briga.png')),
        "bravo":    carrega_imagem(path.join('bravo.png')),
        "bebendo":  carrega_imagem(path.join('bebendo.png'))
    }

    state   = INSPERINA
    running = True

    def gameover():
        nonlocal state, running
        state   = GAMEOVER
        running = False

    def ir_para_tela_final():
        nonlocal state, running
        state = TELA_FINAL
        running = False

    narrativas.iniciar_narrativa_insperina(ir_para_tela_final, gameover)    

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state   = QUIT
                running = False

            # Trata cliques nos botões de narrativa
            for botao in narrativas.botoes_atuais:
                botao.checar_clique(event)

        # Atualiza imagem do personagem de acordo com o mood atual
        personagem_img  = imagens_mood[moods.mood_mentao]
        personagem_img  = pygame.transform.scale(personagem_img, (300, 300))
        personagem_rect = personagem_img.get_rect(center=(WIDTH // 2, 150))

        # Desenha tudo
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        screen.blit(personagem_img, personagem_rect)

        if narrativas.fala_mentao is not None:
            Mentao.exibir(screen, narrativas.fala_mentao)

        for botao in narrativas.botoes_atuais:
            botao.desenhar(screen)

        pygame.display.flip()

    return state