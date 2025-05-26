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

def pre_jogo_jk(screen):
    clock = pygame.time.Clock()

    # Carrega o fundo usando caminho absoluto
    background_path = path.join(FUNDOS_DIR, 'cinema.jpg')
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

    # Inicia a narrativa
    def sair_para_mapa():
        nonlocal state, running
        state   = MAPA
        running = False

    def sair_para_jk():
        nonlocal state, running
        state   = JK
        running = False


    if progresso_jogador["jk completo"]:
        narrativas.criar_cena_pos_jogo_jk(
            sair_para_mapa,
            sair_para_jk 
    )
    else:
        narrativas.criar_cena_filme(sair_para_jk)

    state   = PRE_JK
    running = True

    botao_sair = BotaoSair(sair_para_mapa)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state   = QUIT
                running = False

            # Trata cliques nos botões de narrativa
            for botao in narrativas.botoes_atuais:
                botao.checar_clique(event)

            # Trata clique no botão sair
            botao_sair.checar_clique(event)

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
        botao_sair.desenhar(screen)

        pygame.display.flip()

    return state