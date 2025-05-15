import pygame
import random
from os import path
from config import *

# --- Caminhos relativos a este script ---
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
NADADORES_DIR = path.join(SCRIPT_DIR, "Fotos Nadador")
FUNDOS_DIR    = path.join(SCRIPT_DIR, "Fundos")
PISCINA_FILE  = path.join(FUNDOS_DIR, "piscina.jpg")

def tela_pscina(screen):
    pygame.mixer.init()
    clock        = pygame.time.Clock()
    fonte        = pygame.font.SysFont("arial", 32)
    fonte_grande = pygame.font.SysFont("arial", 100)

    VERMELHO     = (255, 0, 0)
    BRANCO       = (255, 255, 255)

    # carrega e escala o fundo de piscina
    piscina = pygame.image.load(PISCINA_FILE).convert()
    piscina = pygame.transform.scale(piscina, (WIDTH, HEIGHT))

    # carrega nadadores
    jogador_img = pygame.image.load(path.join(NADADORES_DIR, "nadador_jogador.png")).convert_alpha()
    bot_img     = pygame.image.load(path.join(NADADORES_DIR, "nadador_bot.png")).convert_alpha()
    jogador_img = pygame.transform.scale(jogador_img, (80, 40))
    bot_img     = pygame.transform.scale(bot_img,     (80, 40))

    # posições iniciais
    jogador_x, bot_x = 50, 50
    y_jogador, y_bot = 150, 250
    distancia_vitoria = 700

    # --- CONTAGEM REGRESSIVA EM VERMELHO ---
    contagem = 3
    ultimo_t = pygame.time.get_ticks()
    while contagem >= 0:
        agora = pygame.time.get_ticks()
        if agora - ultimo_t >= 1000:
            contagem -= 1
            ultimo_t = agora

        screen.blit(piscina, (0, 0))

        # frase em vermelho
        frase = "A competição irá começar em:"
        txt_frase = fonte.render(frase, True, VERMELHO)
        fx = WIDTH // 2 - txt_frase.get_width() // 2
        fy = HEIGHT // 2 - 100
        screen.blit(txt_frase, (fx, fy))

        # número ou "Já!" em vermelho
        texto = "Já!" if contagem == 0 else str(contagem)
        txt_num = fonte_grande.render(texto, True, VERMELHO)
        nx = WIDTH // 2 - txt_num.get_width() // 2
        ny = HEIGHT // 2 - txt_num.get_height() // 2
        screen.blit(txt_num, (nx, ny))

        pygame.display.flip()
        clock.tick(FPS)

    # --- INÍCIO DA CORRIDA ---
    jogo_ativo = True
    vencedor   = ""

    while True:
        clock.tick(FPS)
        screen.blit(piscina, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return QUIT
            # cada aperto único de espaço
            if jogo_ativo and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jogador_x += 20

        if jogo_ativo:
            bot_x += random.randint(1, 3)
            if jogador_x >= distancia_vitoria:
                vencedor   = "Você venceu! 🏆"
                jogo_ativo = False
            elif bot_x >= distancia_vitoria:
                vencedor   = "O Mentão venceu! 🤖"
                jogo_ativo = False

            if not jogo_ativo:
                render_v = fonte.render(vencedor, True, BRANCO)
                screen.blit(render_v, (WIDTH // 2 - render_v.get_width() // 2, 20))
                pygame.display.flip()
                pygame.time.delay(2000)
                return MAPA

        # desenha nadadores
        screen.blit(jogador_img, (jogador_x, y_jogador))
        screen.blit(bot_img,     (bot_x,     y_bot))

        pygame.display.flip()