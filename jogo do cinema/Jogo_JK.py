
import pygame
import random
import sys
import os
import time
from config import *

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Tamanho da tela
LARGURA, ALTURA = 400, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Fonte
fonte = pygame.font.SysFont('Arial', 26)

# Função auxiliar para carregar imagem com mensagens de debug
def carregar_imagem(caminho, tamanho):
    if os.path.exists(caminho):
        print(f"[OK] Carregando imagem: {caminho}")
        imagem = pygame.image.load(caminho).convert_alpha()
        return pygame.transform.scale(imagem, tamanho)
    else:
        print(f"[ERRO] Imagem não encontrada: {caminho}")
        superficie = pygame.Surface(tamanho)
        superficie.fill(BRANCO)
        return superficie

# Carrega imagem de fundo
fundo = carregar_imagem("c:/Users/lipec/Downloads/fundo_jogo.png", (LARGURA, ALTURA))

# Função para desenhar texto com fundo transparente
def desenhar_texto(texto, fonte, cor_texto, superficie, x, y):
    texto_renderizado = fonte.render(texto, True, cor_texto)
    texto_rect = texto_renderizado.get_rect(topleft=(x, y))
    caixa = pygame.Surface((texto_rect.width + 10, texto_rect.height + 6), pygame.SRCALPHA)
    caixa.fill((255, 255, 255, 180))  # Branco com transparência
    superficie.blit(caixa, (x - 5, y - 3))
    superficie.blit(texto_renderizado, texto_rect)

# Classe do bloco maior
class BlocoMaior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carregar_imagem("c:/Users/lipec/Downloads/a434cd17-74fe-40f8-aff9-3f2b3f00e2d9-removebg-preview.png", (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA // 2, ALTURA - 30)
        self.velocidade = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

# Classe dos blocos menores
class BlocoMenor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carregar_imagem("c:/Users/lipec/Downloads/096c776a-c67a-4308-9a49-7a399c80a897-removebg-preview (1).png", (25, 25))
        self.rect = self.image.get_rect()
        self.resetar()

    def resetar(self):
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidade = random.randint(3, 10)

    def update(self):
        self.rect.y += self.velocidade

# Função principal
def tela_pipoca(screen):
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 26)

    fundo = carregar_imagem("fundo_jogo.png", (WIDTH, HEIGHT))

    som_vitoria = carregar_som("vitoria.wav")
    som_derrota = carregar_som("derrota.wav")
    som_ponto = carregar_som("ponto.wav")
    som_erro = carregar_som("erro.wav")

    todos_sprites = pygame.sprite.Group()
    blocos_menores = pygame.sprite.Group()

    jogador = BlocoMaior()
    todos_sprites.add(jogador)

    coletados = 0
    perdidos = 0
    tempo_total = 90
    tempo_inicio = time.time()

    estado = None
    rodando = True

    while rodando:
        tempo_restante = max(0, int(tempo_total - (time.time() - tempo_inicio)))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                return state

        if random.random() < 0.02:
            bloco = BlocoMenor()
            todos_sprites.add(bloco)
            blocos_menores.add(bloco)

        for bloco in list(blocos_menores):
            bloco.update()
            if bloco.rect.top > HEIGHT:
                bloco.kill()
                perdidos += 1
                if som_erro: som_erro.play()
            elif jogador.rect.colliderect(bloco.rect):
                bloco.kill()
                coletados += 1
                if som_ponto: som_ponto.play()

        jogador.update()

        if coletados >= 50:
            if som_vitoria: som_vitoria.play()
            state = MAPA
            return state

        elif perdidos >= 10 or tempo_restante <= 0:
            if som_derrota: som_derrota.play()
            state = GAMEOVER
            return state

        screen.blit(fundo, (0, 0))
        todos_sprites.draw(screen)
        desenhar_texto(f'Coletados: {coletados}', fonte, PRETO, screen, 10, 10)
        desenhar_texto(f'Perdidos: {perdidos}', fonte, PRETO, screen, 10, 50)
        desenhar_texto(f'Tempo: {tempo_restante}s', fonte, PRETO, screen, 10, 90)
        pygame.display.flip()
        clock.tick(FPS)
