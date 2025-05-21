
import pygame
import random
import sys
import os

# Inicialização
pygame.init()

# Dimensões da tela
largura = 400
altura = 600
colunas = 10
bloco_largura = 40
bloco_altura = 60

# Cores
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Funções para carregar recursos com fallback
def carregar_som(caminho):
    if os.path.exists(caminho):
        return pygame.mixer.Sound(caminho)
    return None

def carregar_imagem(caminho):
    if os.path.exists(caminho):
        return pygame.image.load(caminho)
    return None

# Sons
pygame.mixer.init()
som_contagem = [carregar_som("3.wav"), carregar_som("2.wav"), carregar_som("1.wav")]
som_inicio = carregar_som("go.wav")
som_colisao = carregar_som("colisao.wav")
som_gameover = carregar_som("gameover.wav")
som_vitoria = carregar_som("vitoria.wav")

# Imagens
img_game_over = carregar_imagem("game_over.png")
img_vitoria = carregar_imagem("vitoria.png")
img_bloco_vermelho = carregar_imagem("bloco_vermelho.png")
img_bloco_verde = carregar_imagem("bloco_verde.png")

# Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desvie dos Blocos")

# Jogador
jogador_coluna = colunas // 2
jogador_y = altura - bloco_altura

# Blocos
blocos = []
tempo_para_criar = 30
contador = 0
velocidade = 4

# Fonte
fonte = pygame.font.SysFont(None, 48)
fonte_pequena = pygame.font.SysFont(None, 32)

# Pré-jogo
tempo_pre_jogo = 3000
inicio_preparacao = pygame.time.get_ticks()
preparando = True
cronometro_anterior = 4

# Jogo
tempo_total = 45000
relogio = pygame.time.Clock()
jogo_rodando = True
tempo_inicial = 0
vitoria = None

while jogo_rodando:
    tela.fill(PRETO)
    tempo_atual = pygame.time.get_ticks()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if preparando:
        tempo_restante = max(0, (tempo_pre_jogo - (tempo_atual - inicio_preparacao)) // 1000 + 1)
        if tempo_restante != cronometro_anterior:
            cronometro_anterior = tempo_restante
            if 1 <= tempo_restante <= 3:
                som = som_contagem[3 - tempo_restante]
                if som: som.play()
            elif tempo_restante == 0 and som_inicio:
                som_inicio.play()
        texto_inicio = fonte.render(str(tempo_restante), True, BRANCO)
        tela.blit(texto_inicio, (largura // 2 - texto_inicio.get_width() // 2, altura // 2))
        pygame.display.flip()
        if tempo_atual - inicio_preparacao >= tempo_pre_jogo:
            preparando = False
            tempo_inicial = pygame.time.get_ticks()
        relogio.tick(60)
        continue

    tempo_passado = tempo_atual - tempo_inicial
    if tempo_passado >= tempo_total:
        vitoria = True
        if som_vitoria: som_vitoria.play()
        jogo_rodando = False
        continue

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_coluna > 0:
        jogador_coluna -= 0.3
    if teclas[pygame.K_RIGHT] and jogador_coluna < colunas - 1:
        jogador_coluna += 0.3
    jogador_coluna = max(0, min(jogador_coluna, colunas - 1))

    segundos = tempo_passado // 5000
    velocidade = 4 + segundos
    tempo_para_criar = max(10, 30 - segundos)

    for bloco in blocos:
        bloco['y'] += velocidade
    blocos = [bloco for bloco in blocos if bloco['y'] < altura]

    contador += 1
    if contador >= tempo_para_criar:
        nova_coluna = random.randint(0, colunas - 1)
        blocos.append({'coluna': nova_coluna, 'y': 0})
        contador = 0

    colidiu = any(int(bloco['coluna']) == int(jogador_coluna) and bloco['y'] + bloco_altura > jogador_y for bloco in blocos)
    if colidiu:
        vitoria = False
        if som_colisao: som_colisao.play()
        if som_gameover: som_gameover.play()
        jogo_rodando = False

    for bloco in blocos:
        if 0 <= bloco['coluna'] < colunas:
            x = bloco['coluna'] * bloco_largura
            y = bloco['y']
            if img_bloco_vermelho:
                tela.blit(pygame.transform.scale(img_bloco_vermelho, (bloco_largura, bloco_altura)), (x, y))
            else:
                pygame.draw.rect(tela, VERMELHO, (x, y, bloco_largura, bloco_altura))

    x = int(jogador_coluna * bloco_largura)
    if img_bloco_verde:
        tela.blit(pygame.transform.scale(img_bloco_verde, (bloco_largura, bloco_altura)), (x, jogador_y))
    else:
        pygame.draw.rect(tela, VERDE, (x, jogador_y, bloco_largura, bloco_altura))

    tempo_restante = max(0, (tempo_total - tempo_passado) // 1000)
    texto_tempo = fonte_pequena.render(f"Tempo: {tempo_restante}s", True, BRANCO)
    tela.blit(texto_tempo, (10, 10))

    pygame.display.flip()
    relogio.tick(60)

# Tela final
while True:
    tela.fill(PRETO)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if vitoria:
        if img_vitoria:
            tela.blit(pygame.transform.scale(img_vitoria, (largura, altura)), (0, 0))
        else:
            texto = fonte.render("Você venceu!", True, BRANCO)
            tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2))
    else:
        if img_game_over:
            tela.blit(pygame.transform.scale(img_game_over, (largura, altura)), (0, 0))
        else:
            texto = fonte.render("Game Over", True, BRANCO)
            tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2))

    pygame.display.flip()
    relogio.tick(60)
