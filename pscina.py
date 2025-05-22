# pscina.py

import pygame
import random
from os import path
from config import WIDTH, HEIGHT, FPS, PSCINA, MAPA, QUIT

# Caminhos
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
NADADORES_DIR = path.join(SCRIPT_DIR, "Fotos Nadador")
FUNDOS_DIR    = path.join(SCRIPT_DIR, "Fundos")
FONTS_DIR     = path.join(SCRIPT_DIR, "assets", "fonts")  # ajuste conforme sua estrutura

# Cores
VERDE = (200, 0, 0)
PRETO = (0, 0, 0)

# Função de renderização de texto com contorno
def render_text_outline(surface, text, font, pos, fg, outline, width=2):
    base = font.render(text, True, fg)
    x, y = pos
    for dx in range(-width, width+1):
        for dy in range(-width, width+1):
            if dx or dy:
                surf = font.render(text, True, outline)
                surface.blit(surf, (x+dx, y+dy))
    surface.blit(base, (x, y))


def load_font(file_name, size):
    """
    Tenta carregar uma fonte TTF do diretório assets/fonts;
    se falhar, usa fonte do sistema.
    """
    pygame.font.init()
    font_path = path.join(FONTS_DIR, file_name)
    if path.isfile(font_path):
        try:
            return pygame.font.Font(font_path, size)
        except Exception:
            pass
    # fallback para SysFont
    return pygame.font.SysFont("arial", size)


def tela_pscina(screen):
    clock = pygame.time.Clock()

    # Carrega fontes: big para contagem, small para textos
    font_big   = load_font("gamer_font.ttf", 80)
    font_small = load_font("gamer_font.ttf", 32)

    # Carrega e escala o fundo
    bg = pygame.image.load(path.join(FUNDOS_DIR, "piscina.jpg")).convert()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    # Carrega sprites do jogador e bot
    sprites_j = []
    sprites_b = []
    for name in ("nadador1.png", "nadador2.png"):
        img = pygame.image.load(path.join(NADADORES_DIR, name)).convert_alpha()
        sprites_j.append(pygame.transform.scale(img, (80, 40)))
    for name in ("bot1.png", "bot2.png"):
        img = pygame.image.load(path.join(NADADORES_DIR, name)).convert_alpha()
        sprites_b.append(pygame.transform.scale(img, (80, 40)))

    # Posições e variáveis
    x_j, y_j = 50, 200
    x_b, y_b = 50, 300
    goal_x    = WIDTH - 120
    anim_j    = 0
    anim_b    = 0
    timer_b   = 0
    INTERVAL  = 10
    running   = True
    vencedor  = None
    libera_movimento = False  # novo controle

    # 1) Contagem regressiva
    for cnt in ("3", "2", "1"):
        screen.blit(bg, (0, 0))
        render_text_outline(
            screen, "COMPETIÇÃO", font_small,
            (WIDTH//2 - font_small.size("COMPETIÇÃO")[0]//2, HEIGHT//2 - 140),
            VERDE, PRETO, width=3
        )
        render_text_outline(
            screen, cnt, font_big,
            (WIDTH//2 - font_big.size(cnt)[0]//2, HEIGHT//2 - font_big.size(cnt)[1]//2),
            VERDE, PRETO, width=4
        )
        render_text_outline(
            screen, "Pressione Espaço para nadar", font_small,
            (WIDTH//2 - font_small.size("Pressione Espaço para nadar")[0]//2, HEIGHT//2 + 80),
            VERDE, PRETO, width=2
        )
        pygame.display.flip()
        pygame.time.delay(800)

    # 🔁 Correção: limpa eventos antes de liberar entrada
    pygame.event.clear()
    libera_movimento = True

    # 2) Loop principal
    while True:
        clock.tick(FPS)
        screen.blit(bg, (0, 0))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            # Espaço para nadar (só se permitido)
            if running and libera_movimento and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                x_j += 20
                anim_j = (anim_j + 1) % len(sprites_j)

        # Bot se move e anima
        if running:
            x_b += 2
            timer_b += 1
            if timer_b >= INTERVAL:
                anim_b = (anim_b + 1) % len(sprites_b)
                timer_b = 0

            # Verifica vitória
            if x_j >= goal_x:
                vencedor = "Você venceu!"
                running = False
            elif x_b >= goal_x:
                vencedor = "Mentão venceu!"
                running = False

        # Exibe vencedor
        if vencedor:
            render_text_outline(
                screen, vencedor, font_small,
                (WIDTH//2 - font_small.size(vencedor)[0]//2, 20),
                VERDE, PRETO, width=3
            )

        # Desenha sprites
        screen.blit(sprites_j[anim_j], (x_j, y_j))
        screen.blit(sprites_b[anim_b], (x_b, y_b))

        pygame.display.flip()

        if vencedor:
            pygame.time.delay(2000)
            return MAPA


