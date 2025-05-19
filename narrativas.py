from classes import Mentao, BotaoEscolha
from moods import *
from config import *

# Variáveis globais para a narrativa
fala_mentao = None
botoes_atuais = []

def criar_cena_inicial():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Eae viado você ta bem? Tava indo pra aula de Dessoft")
    botoes_atuais = [
        BotaoEscolha("Dessoft o caralho Mentão! Bora comer!", 1, criar_cena_comida),
        BotaoEscolha("Boa, também to indo lá", 2, criar_cena_conversa),
        BotaoEscolha("Seloko Mentao, muito dificil dessoft. Voce ta entendendo?", 3, criar_cena_deco)
    ]

def criar_cena_comida():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("Hmmmm, se bem que me deu fome de Madeiro, vamo?")
    botoes_atuais = [
        BotaoEscolha("Pra já caralho", 1, criar_fim_hamburguer),
        BotaoEscolha("Na real to afim de um pastel", 2, criar_fim_pastel)
    ]

def criar_cena_conversa():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Demoro! Te encontro lá")
    botoes_atuais = [
        BotaoEscolha("Espera...", 1, criar_cena_cu)
    ]

def criar_cena_deco():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("SERIO!?!? Eu tambem tenho muita dificuldade! Meu amigo Deco é muito bom em Dessoft")
    botoes_atuais = [
        BotaoEscolha("Deco? Aquele pastel?", 1, criar_cena_cu),
        BotaoEscolha("Vamos falar com ele", 2, criar_cena_cu)
    ]

def criar_fim_hamburguer():
    mudar_mood("bebendo")
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Boa escolha! Vamos comer então.")
    botoes_atuais = []

def criar_fim_pastel():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Pastel? Você que é pastel!")
    botoes_atuais = [
        BotaoEscolha("Vai se fuder mentao", 1, criar_fim_vsf)
    ]

def criar_fim_vsf():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("E eu sou o Bozo!")
    botoes_atuais = []

def criar_cena_cu():
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Sim eu adoro dar o cu, eu dou o cu 100% do meu tempo, dou sim o cu e vou continuar dando")
    botoes_atuais = []

def criar_cena_pre_jogo_pscina(callback_proxima_fase):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Irmao, eu duvido voce me vencer!")
    botoes_atuais = [BotaoEscolha("Continuar", 1, callback_proxima_fase)]
    