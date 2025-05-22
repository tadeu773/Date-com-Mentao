import pygame
from os import path
import random
import time
import os
from config import *


# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
FOTOS_DIR     = path.join(SCRIPT_DIR, "fotos_mentao")

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor, cor_texto=(255, 255, 255), fonte=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_texto = cor_texto
        self.fonte = fonte or pygame.font.Font(None, 40)

        # Pré-renderiza o texto
        self.texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(center=self.rect.center)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect, border_radius=12)
        tela.blit(self.texto_renderizado, self.texto_rect)

    def foi_clicado(self, evento):
        return evento.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(evento.pos)
    
class BotaoImagem:
    def __init__(self, imagem, x, y):
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def foi_clicado(self, evento):
        return evento.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(evento.pos)
    
def carrega_imagem(nome_arquivo):
    """
    Carrega e retorna uma imagem de 'fotos_mentao', já escalonada para 450×450.
    """
    caminho = path.join(FOTOS_DIR, nome_arquivo)
    if not path.exists(caminho):
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.scale(imagem, (450, 450))
    return imagem

class Mentao:
    @staticmethod
    def fala(texto, largura_caixa=600, altura_caixa=120, margem=20):
        fonte = pygame.font.SysFont("Comic Sans MS", 24)
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""
        for palavra in palavras:
            teste = linha_atual + palavra + " "
            if fonte.size(teste)[0] <= largura_caixa - 2 * margem:
                linha_atual = teste
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "
        linhas.append(linha_atual.strip())

        altura_caixa = max(altura_caixa, margem * 2 + len(linhas) * fonte.get_height())
        caixa = pygame.Surface((largura_caixa, altura_caixa))
        caixa.fill((255, 255, 255))  

        pygame.draw.rect(caixa, (0, 0, 0), caixa.get_rect(), 3)

        y_offset = margem
        for linha in linhas:
            txt = fonte.render(linha, True, (0, 0, 255))
            txt_rect = txt.get_rect(midtop=(largura_caixa // 2, y_offset))
            caixa.blit(txt, txt_rect)
            y_offset += fonte.get_height()

        return caixa

    @staticmethod
    def exibir(screen, caixa):
        pos_x = screen.get_width() // 2 - caixa.get_width() // 2
        pos_y = 300
        screen.blit(caixa, (pos_x, pos_y))

class BotaoEscolha:
    def __init__(self, texto, posicao, acao):
        self.largura = 650
        self.altura = 50
        self.cor_fundo = (255, 192, 203)  # rosa claro
        self.cor_borda = (0, 0, 0)
        self.cor_texto = (255, 255, 255)  # branco
        self.fonte = pygame.font.SysFont("Comic Sans MS", 24)
        self.texto = texto
        self.acao = acao

        base_y = 365
        espaco = 60
        self.x = (800 - self.largura) // 2  # Centraliza na tela
        self.y = base_y + (posicao * espaco)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor_fundo, self.rect)
        pygame.draw.rect(screen, self.cor_borda, self.rect, 2)

        # Renderiza o texto com contorno preto
        txt_surface = self.fonte.render(self.texto, True, self.cor_texto)
        txt_rect = txt_surface.get_rect(center=self.rect.center)

        # Desenha contorno preto
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                borda = self.fonte.render(self.texto, True, (0, 0, 0))
                screen.blit(borda, (txt_rect.x + dx, txt_rect.y + dy))

        # Texto principal (branco)
        screen.blit(txt_surface, txt_rect)

    def checar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(evento.pos):
            self.acao()

class BotaoSair:
    def __init__(self, acao):
        self.x = 20
        self.y = 20
        self.largura = 100
        self.altura = 40
        self.cor_fundo = (255, 255, 255)
        self.cor_borda = (0, 0, 0)
        self.cor_texto = (0, 0, 0)
        self.fonte = pygame.font.SysFont("Comic Sans MS", 24)
        self.texto = "Sair"
        self.acao = acao
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor_fundo, self.rect)
        pygame.draw.rect(screen, self.cor_borda, self.rect, 2)
        txt = self.fonte.render(self.texto, True, self.cor_texto)
        txt_rect = txt.get_rect(center=self.rect.center)
        screen.blit(txt, txt_rect)

    def checar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(evento.pos):
            self.acao()

# Diretórios e constantes
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGENS_PIPOCA_DIR = os.path.join(SCRIPT_DIR, "imagens pipoca")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Função para carregar imagem
def carregar_imagem(caminho, tamanho):
    if os.path.exists(caminho):
        imagem = pygame.image.load(caminho).convert_alpha()
        return pygame.transform.scale(imagem, tamanho)
    else:
        print(f"[ERRO] Imagem não encontrada: {caminho}")
        superficie = pygame.Surface(tamanho)
        superficie.fill(BRANCO)
        return superficie

# Função para desenhar texto com fundo transparente
def desenhar_texto(texto, fonte, cor_texto, superficie, x, y):
    texto_renderizado = fonte.render(texto, True, cor_texto)
    texto_rect = texto_renderizado.get_rect(topleft=(x, y))
    caixa = pygame.Surface((texto_rect.width + 10, texto_rect.height + 6), pygame.SRCALPHA)
    caixa.fill((255, 255, 255, 180))  # Branco com transparência
    superficie.blit(caixa, (x - 5, y - 3))
    superficie.blit(texto_renderizado, texto_rect)

# Classe do balde de pipoca
class BlocoMaior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho_balde = os.path.join(IMAGENS_PIPOCA_DIR, "balde.png")
        self.image = carregar_imagem(caminho_balde, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 30)
        self.velocidade = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocidade

# Classe das pipocas
class BlocoMenor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho_pipoca = os.path.join(IMAGENS_PIPOCA_DIR, "pipoca.png")
        self.image = carregar_imagem(caminho_pipoca, (25, 25))
        self.rect = self.image.get_rect()
        self.resetar()

    def resetar(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidade = random.randint(3, 10)

    def update(self):
        self.rect.y += self.velocidade
