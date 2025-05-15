import pygame
from os import path

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor, cor_texto=(255, 255, 255), fonte=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_texto = cor_texto
        self.fonte = fonte or pygame.font.Font(None, 40)  # Fonte padrão se não for passada

        # Pré-renderiza o texto
        self.texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        self.texto_rect = self.texto_renderizado.get_rect(center=self.rect.center)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect, border_radius=12)
        tela.blit(self.texto_renderizado, self.texto_rect)

    def foi_clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(evento.pos):
                return True
        return False
    
class BotaoImagem:
    def __init__(self, imagem, x, y):
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def foi_clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(evento.pos):
                return True
        return False
    
def carrega_imagem(nome_arquivo):
    imagem = pygame.image.load(path.join("fotos_mentao", nome_arquivo)).convert_alpha()
    imagem = pygame.transform.scale(imagem, (450, 450))
    return imagem

class Mentao:
    @staticmethod
    def fala(texto, largura_caixa=600, altura_caixa=120, margem=20):
        # Fonte Comic Sans MS azul
        fonte = pygame.font.SysFont("Comic Sans MS", 24)
        
        # Quebra o texto em várias linhas se necessário
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""
        
        for palavra in palavras:
            teste_linha = linha_atual + palavra + " "
            if fonte.size(teste_linha)[0] <= largura_caixa - 2 * margem:
                linha_atual = teste_linha
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "
        linhas.append(linha_atual.strip())

        # Recalcula a altura da caixa com base no número de linhas
        altura_caixa = max(altura_caixa, margem * 2 + len(linhas) * fonte.get_height())

        # Cria a superfície da caixa
        caixa = pygame.Surface((largura_caixa, altura_caixa))
        caixa.fill((255, 255, 255))  # Fundo branco

        # Renderiza cada linha e posiciona dentro da caixa
        y_offset = margem
        for linha in linhas:
            texto_renderizado = fonte.render(linha, True, (0, 0, 255))  # Azul
            texto_rect = texto_renderizado.get_rect(midtop=(largura_caixa // 2, y_offset))
            caixa.blit(texto_renderizado, texto_rect)
            y_offset += fonte.get_height()

        return caixa

    @staticmethod
    def exibir(screen, caixa):
        """Posiciona a fala automaticamente na parte inferior central da tela"""
        pos_x = screen.get_width() // 2 - caixa.get_width() // 2
        pos_y = 300
        screen.blit(caixa, (pos_x, pos_y))

class BotaoEscolha:
    def __init__(self, texto, posicao, acao):
        # Tamanho e estilo fixos
        self.largura = 500
        self.altura = 50
        self.cor_fundo = (255, 255, 255)  # Branco
        self.cor_borda = (0, 0, 0)        # Preto
        self.cor_texto = (0, 0, 255)      # Azul
        self.fonte = pygame.font.SysFont("Comic Sans MS", 24)
        self.texto = texto
        self.acao = acao

        # Cálculo da posição baseado na posição da fala (400, 300)
        base_y = 365  # Posição base próxima à fala
        espaco = 60   # Espaçamento entre botões
        self.x = 150  # Alinhamento horizontal fixo (ajuste conforme necessário)
        self.y = base_y + (posicao * espaco)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        # Caixa do botão
        pygame.draw.rect(screen, self.cor_fundo, self.rect)
        pygame.draw.rect(screen, self.cor_borda, self.rect, 2)  # Contorno preto

        # Texto centralizado
        texto_render = self.fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        screen.blit(texto_render, texto_rect)

    def checar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(evento.pos):
            self.acao()

class BotaoSair:
    def __init__(self, acao):
        self.x = 20
        self.y = 20
        self.largura = 100
        self.altura = 40
        self.cor_fundo = (255, 255, 255)  # Branco
        self.cor_borda = (0, 0, 0)        # Preto
        self.cor_texto = (0, 0, 0)        # Preto
        self.fonte = pygame.font.SysFont("Comic Sans MS", 24)
        self.texto = "Sair"
        self.acao = acao
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor_fundo, self.rect)
        pygame.draw.rect(screen, self.cor_borda, self.rect, 2)
        texto_render = self.fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        screen.blit(texto_render, texto_rect)

    def checar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(evento.pos):
            self.acao()