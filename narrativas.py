from classes import Mentao, BotaoEscolha
from moods import *
from config import *

# Variáveis globais para a narrativa
fala_mentao = None
botoes_atuais = []

#FALAS NO INSPER
def iniciar_narrativa_insper():
    if not progresso_jogador["piscina"]:
        criar_cena_pre_piscina()
    elif not progresso_jogador["madero"]:
        criar_cena_inicial()
    elif not progresso_jogador["jk"]:
        criar_cena_cu()
    else:
        criar_cena_cu()
#PRE PISCINA
#CAMINHO CORRETO
def criar_cena_pre_piscina():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Eae, eu sou o Mentão, quem é você?")
    botoes_atuais = [
        BotaoEscolha("Meu nome é Clementina! Prazer em te conhecer!", 1, criar_cena_prazer),
        BotaoEscolha("Seu pior pesadelo", 2, criar_cena_pesadelo),
        BotaoEscolha("*ignorar ele e sair andando*", 3, criar_cena_ignorado)
    ]

def criar_cena_prazer():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Prazer muito prazer. Oque você mais gosta de fazer?")
    botoes_atuais = [
        BotaoEscolha("Sou viciada em dar green", 1, criar_cena_bet),
        BotaoEscolha("Eu faço natação", 2, criar_cena_nadar),
        BotaoEscolha("*Vou atrás de homens altos e fortes*", 3, criar_cena_fora)
    ]

def criar_cena_nadar():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("SERIO!? Eu sou muito rapido nas águas!")
    botoes_atuais = [
        BotaoEscolha("Vamos nadar um contra o outro?", 1, criar_cena_desbloqueio_piscina),
        BotaoEscolha("Fodasse", 2, criar_fim_vsf),
    ]

def criar_cena_desbloqueio_piscina():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    progresso_jogador["piscina"] = True 
    fala_mentao = Mentao.fala("Te vejo na piscina então!")
    botoes_atuais = [
        BotaoEscolha("*PISCINA DESBLOQUEADA*", 1, criar_cena_desbloqueio_piscina),
    ]
#FIM CAMINHO CORRETO
#CAMINHOS ALTERNATIVOS PRE PISCINA

def criar_cena_pesadelo():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Pesadelo? Eu não gosto de pesadelo")
    botoes_atuais = [
        BotaoEscolha("E eu não gosto de pastel", 1, criar_fim_pastel),
        BotaoEscolha("Desculpa, vamos nos reintroduzir", 2, criar_cena_pre_piscina)
    ]

def criar_cena_ignorado():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Que mina estranha!")
    botoes_atuais = [
        BotaoEscolha("*GAME OVER*", 1, criar_fim_pastel),
    ]

def criar_cena_bet():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("ETA, meus amigos Deco e Teo tem problema com isso!")
    botoes_atuais = [
        BotaoEscolha("Também acho que tenho...", 1, criar_cena_oquemais),
        BotaoEscolha("Também né, dois pasteis", 2, criar_fim_pastel),
        BotaoEscolha("Bora betar mentão, chega de estudar!", 3, criar_cena_estudo)
    ]

def criar_cena_estudo():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("NÃO POSSO! Já perdi muito dinheiro com isso!")
    botoes_atuais = [
        BotaoEscolha("Cagão!", 1, criar_cena_oquemais),
        BotaoEscolha("Tabom então...", 2, criar_cena_oquemais),
        ]

def criar_cena_oquemais():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Oque mais você gosta de fazer?")
    botoes_atuais = [
        BotaoEscolha("Eu faço natação", 2, criar_cena_nadar),
        BotaoEscolha("Vou atrás de homens altos e fortes", 3, criar_cena_fora)
    ]

def criar_cena_fora():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Eu sei que sou lindo, mas nem te conheço! Sai fora!")
    botoes_atuais = [
        BotaoEscolha("GAME OVER", 2, criar_cena_nadar),
    ]

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

#FALAS PISCINA

def criar_cena_pre_jogo_pscina(callback_proxima_fase):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Irmao, eu duvido voce me vencer!")
    botoes_atuais = [BotaoEscolha("Continuar", 1, callback_proxima_fase)]
    