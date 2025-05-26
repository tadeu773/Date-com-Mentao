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
        criar_cena_inicial_jk()
    elif not progresso_jogador["jk"]:
        criar_fim_vsf()
    else:
        criar_fim_vsf()
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
#FIM CAMINHOS ALTERNATIVOS PRE PISCINA
#INICIO CAMINHOS JK
def criar_cena_inicial_jk():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Oii, saudades de você, ainda estou impressionado sobre o jeito como você nada!")
    botoes_atuais = [
        BotaoEscolha("Você também nadou bem!", 1, criar_cena_elogio),
        BotaoEscolha("Você é lerdão", 2, criar_cena_lerdao),
        BotaoEscolha("Valeu! Eai vai fazer oque agora?", 3, criar_cena_deco)
    ]

def criar_cena_elogio():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("Obrigado, você é muito gente boa!")
    botoes_atuais = [
        BotaoEscolha("Você também! *pintou um clima*", 1, criar_cena_clima),
        BotaoEscolha("Valeu", 2, criar_cena_grosso)
    ]

def criar_cena_clima():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Oque voce acha da gente ver um filme em?")
    botoes_atuais = [
        BotaoEscolha("So se for no JK", 1, criar_cena_adorojk),
        BotaoEscolha("Odeio filmes", 2, criar_cena_odeiofilmes),
        BotaoEscolha("Calma ai garotão! Ta muito emocionado!", 3, criar_cena_emocionado),
    ]

def criar_cena_adorojk():
    global fala_mentao, botoes_atuais
    progresso_jogador["jk"] = True 
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("ETA! Eu adoro o JK, vamo marcar 15:00 horas la então!")
    botoes_atuais = [
        BotaoEscolha("Feshow", 1, criar_cena_adorojk2),
    ]

def criar_cena_adorojk2():
    global fala_mentao, botoes_atuais
    progresso_jogador["jk"] = True 
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("")
    botoes_atuais = [
        BotaoEscolha("*JK DESBLOQUEADO*", 1, criar_cena_adorojk2),
    ]

#CAMINHO CERTO JK CONCLUIDO
#INICIO CAMINHOS ALTERNATIVOS

def criar_cena_grosso():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Eu não sou gente boa?")
    botoes_atuais = [
        BotaoEscolha("Volta aqui Mentão, foi mal!", 1, criar_cena_pedir_desculpa),
        BotaoEscolha("Não mentão, você é pastel!", 2, criar_fim_pastel)
    ]

def criar_cena_deco():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Tava pensando em chamar o Deco pra bater um rango... mas se você quiser, cancelo tudo!")
    botoes_atuais = [
        BotaoEscolha("Cancela mesmo, vamos pro JK", 1, criar_cena_adorojk),
        BotaoEscolha("Deixa quieto, vai lá com o Deco", 2, criar_cena_grosso)
    ]

def criar_cena_pedir_desculpa():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Tá bom... mas só porque eu sou legal. E não o bozo!")
    botoes_atuais = [
        BotaoEscolha("Prometo! Bora voltar ao assunto", 1, criar_cena_elogio),
        BotaoEscolha("Mentão emocionou", 2, criar_cena_emocionado)
    ]

def criar_cena_lerdao():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("Lerdão? Eu deixei você me vencer!")
    botoes_atuais = [
        BotaoEscolha("kkkkk beleza beleza", 1, criar_cena_clima),
        BotaoEscolha("Você não sabe mentir! Para com isso vai!", 2, criar_cena_grosso)
    ]

def criar_cena_emocionado():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Tá bom, tá bom! Fui intenso demais? É que você me deixa assim.")
    botoes_atuais = [
        BotaoEscolha("Hahaha... ok, vamo pro JK", 1, criar_cena_adorojk),
        BotaoEscolha("É melhor cada um ir pro seu lado, não me misturo com pastel", 2, criar_fim_vsf)
    ]

def criar_cena_odeiofilmes():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Odeia? Mas eu gosto, eu gosto de cinema")
    botoes_atuais = [
        BotaoEscolha("Brincadeira! Eu topo JK sim!", 1, criar_cena_adorojk),
        BotaoEscolha("Já viu o filme do bozo?", 2, criar_fim_vsf)
    ]

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

#FALAS PISCINA

def criar_cena_pre_jogo_pscina(callback_proxima_fase):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Irmão, eu duvido voce me vencer!")
    botoes_atuais = [BotaoEscolha("*NADAR CONTRA MENTÃO*", 1, callback_proxima_fase)]

def criar_cena_pos_jogo_pscina(callback_mapa, callback_nado):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Caramba você é rapida mesmo! Gostei!")
    botoes_atuais = [
        BotaoEscolha("*NOVOS DIALOGOS NO INSPER*", 1, callback_mapa),
        BotaoEscolha("*NADAR CONTRA MENTÃO*", 2, callback_nado)
    ]

#FALAS JK
def iniciar_cena_pre_jk(callback_proxima_fase):
    criar_cena_prejk(callback_proxima_fase)

def criar_cena_filme(callback_proxima_fase):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Caramba, to adorando esse filme\n*Mentão está vidrado na tela*")
    mudar_mood("surpreso")
    botoes_atuais = [
        BotaoEscolha("Bem legal mesmo...", 1, lambda: iniciar_cena_pre_jk(callback_proxima_fase)),
        BotaoEscolha("Mano que porra de filme é esse?", 2, lambda: iniciar_cena_pre_jk(callback_proxima_fase)),
        BotaoEscolha("*Continuar dormindo*", 3, lambda: iniciar_cena_pre_jk(callback_proxima_fase)),
    ]

def criar_cena_prejk(callback_proxima_fase):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("ETAAA DEIXEI TODA MINHA PIPOCA CAIR!!!!")
    botoes_atuais = [BotaoEscolha("*PEGAR AS PIPOCAS DO MENTÃO*", 1, callback_proxima_fase)]

def criar_cena_pos_jogo_jk(callback_mapa, callback_nado):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("QUE ISSO! Você é tipo aqueles ninjas sabe, que isso\n*Mentão ainda está vidrado na tela*")
    botoes_atuais = [
        BotaoEscolha("*NOVOS DIALOGOS NO INSPER*", 1, callback_mapa),
        BotaoEscolha("*PEGAR AS PIPOCAS DO MENTÃO*", 2, callback_nado)
        ]
    