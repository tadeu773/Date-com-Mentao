from classes import Mentao, BotaoEscolha
from moods import *
from config import *

# Variáveis globais para a narrativa
fala_mentao = None
botoes_atuais = []

def iniciar_narrativa_insperina(callback_final, callback_gameover):
    global callback_tela_final, callback_gameover_global
    callback_tela_final = callback_final
    callback_gameover_global = callback_gameover
    criar_cena_inicial_insperina()

#FALAS NO INSPER
def iniciar_narrativa_insper(callback_gameover, callback_mapa):
    global callback_gameover_global, callback_aceitar_insperina
    callback_gameover_global = callback_gameover
    callback_aceitar_insperina = callback_mapa  # necessário para a última fase da narrativa (insperina)

    if not progresso_jogador["piscina"]:
        criar_cena_pre_piscina()
    elif not progresso_jogador["jk"]:
        criar_cena_inicial_jk()
    elif not progresso_jogador["madero"]:
        criar_inicial_madero()
    else:
        pre_insperina(callback_mapa)



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
        BotaoEscolha("*GAME OVER*", 1, callback_gameover_global),
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
        BotaoEscolha("GAME OVER", 2, callback_gameover_global),
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

#FALAS PRE MADERO
def criar_inicial_madero():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Eai Clementina! Nossa, depois desse filme animal, só preciso de um X-Burguer")
    botoes_atuais = [
        BotaoEscolha("Que filme?", 1, criar_madero_sonho),
        BotaoEscolha("Ta com fome gordinho?", 2, criar_cena_deco2),
        BotaoEscolha("Hmm, eu aceitaria um burgão, que restaurantes você gosta?", 3, criar_madero_restaurantes)
    ]

def criar_madero_restaurantes():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Hoje é um dia que combina com hamburguerzinho do Madero")
    botoes_atuais = [
        BotaoEscolha("Bora quebrar um Madero então!", 1, criar_madero_quebrar_madero),
        BotaoEscolha("Mentão... Madero não é romântico!", 2, criar_madero_romantico)
    ]

def criar_madero_quebrar_madero():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Mentão está com fome. Mentão ama comida")
    botoes_atuais = [
        BotaoEscolha("Eu... já entendi", 1, criar_cena_madero_convite),
        BotaoEscolha("*Olhar fixamente para o mentão*", 2, criar_madero_olhar_fixo)
    ]

def criar_cena_madero_convite():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Madero 20:00 amanhã... NÃO! 19:30, tem prova de ModSim e preciso dormir cedo")
    botoes_atuais = [
        BotaoEscolha("Xuxu-beleza", 1, desbloquear_madero)
    ]

def desbloquear_madero():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    progresso_jogador["madero"] = True
    fala_mentao = Mentao.fala("")
    botoes_atuais = [
        BotaoEscolha("MADERO DESBLOQUEADO", 1, desbloquear_madero)
    ]
#FIM CAMINHO CORRETO MADERO
#INICIO CAMINHOS ALTERNATIVOS
def criar_madero_romantico():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("COMO NAAAO? Eu levei minha ex no Madero varias vezes, ela adorava!")
    botoes_atuais = [
        BotaoEscolha("Por isso que virou ex...", 1, criar_fim_ex),
        BotaoEscolha("E a sua atual você não vai levar?", 2, criar_cena_madero_convite),
        BotaoEscolha("Que gosto pessimo, vamo comer um pastel na feira vai", 3, criar_fim_pastel)
    ]

def criar_madero_sonho():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Que? Como assim? Jurava que tava de rolê com uma mina")
    botoes_atuais = [
        BotaoEscolha("Que mina oque eu sou o bozo!", 1, criar_fim_vsf),
        BotaoEscolha("To gastando contigo, logico que era eu", 2, criar_madero_ETA),
    ]

def criar_madero_ETA():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("ETA, nessa você me pegou mesmo em!")
    botoes_atuais = [
        BotaoEscolha("kkk eu sou palhaça...", 1, criar_madero_restaurantes),
    ]

def criar_cena_deco2():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Ta achando que eu sou o coxinha? Aqui é massa!")
    botoes_atuais = [
        BotaoEscolha("Eita, assustei", 1, criar_madero_restaurantes),
        BotaoEscolha("Coxinha?", 2, criar_madero_apelidos),
    ]

def criar_madero_apelidos():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("É apelido de um amigo meu, eu sempre do apelidos para amigos meus, você quer ouvir eles?")
    botoes_atuais = [
        BotaoEscolha("Não, to de boa", 1, criar_madero_restaurantes),
        BotaoEscolha("Mentão to com muita fome cara", 2, criar_madero_quebrar_madero),
    ]

def criar_madero_olhar_fixo():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("*Mentão te encara de volta*")
    botoes_atuais = [
        BotaoEscolha("*Continuar encarando*", 1, criar_madero_olhar_fixo),
        BotaoEscolha("Desisto!", 2, criar_fim_desisto),
    ]

#FINAIS GAMEOVER
def criar_fim_pastel():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Pastel? Você que é pastel!")
    botoes_atuais = [
        BotaoEscolha("Vai se fuder mentao", 1, criar_fim_vsf)
    ]

def criar_fim_desisto():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("HA! Você perdeu!")
    botoes_atuais = [
        BotaoEscolha("Pera eu perdi?...", 1, callback_gameover_global)
    ]

def criar_fim_vsf():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("E eu sou o Bozo!")
    botoes_atuais = [BotaoEscolha("Vai se fuder mentão", 1, callback_gameover_global)]

def criar_fim_ex():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("E você vai virar a outra!")
    botoes_atuais = [
        BotaoEscolha("*GAMEOVER*", 1, callback_gameover_global),
    ]

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

#FALAS MADERO
def criar_cena_inicial_pre_madero(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("*Enquanto você come seu combo de mini-hamburguers madero, Mentão se estraga com 2 Super Madero*")
    mudar_mood("feliz")
    botoes_atuais = [
        BotaoEscolha("*CONTINUAR*", 1, lambda: fala_madero1(callback_jogo_madero)),
    ]

def fala_madero1(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Hmmmm, esse hamburguinho tava uma delicinha em! Hmmmm")
    mudar_mood("feliz")
    botoes_atuais = [
        BotaoEscolha("Também gostei muito do meu!", 1, lambda: chamar_garçom(callback_jogo_madero)),
        BotaoEscolha("Garçom! Mais guardanapo pra ele porfavor... e a conta!", 2, lambda: fala_conta(callback_jogo_madero)),
    ]

def chamar_garçom(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Belezura, vou pedir a conta! Mestre vem ca!")
    mudar_mood("bebendo")
    botoes_atuais = [
        BotaoEscolha("*CONTINUAR*", 1, lambda: fala_conta(callback_jogo_madero)),
    ]

def fala_conta(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("*O garçom entrega a conta. Mentão parece estar muito incomodado*")
    mudar_mood("bravo")
    botoes_atuais = [
        BotaoEscolha("Que foi querido", 1, lambda: sem_dinheiro(callback_jogo_madero)),
        BotaoEscolha("No primeiro date você tem que pagar pra mim né!", 2, lambda: sem_dinheiro(callback_jogo_madero)),
        BotaoEscolha("Eu também to dura", 3, lambda: sem_dinheiro(callback_jogo_madero)),
    ]

def sem_dinheiro(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("Então, é que eu to sem dinheiro fofinha...")
    mudar_mood("bebendo")
    botoes_atuais = [
        BotaoEscolha("E agora?", 1, lambda: inicio_jogo_madero(callback_jogo_madero)),
        BotaoEscolha("Bora lavar prato!", 2, lambda: inicio_jogo_madero(callback_jogo_madero)),
    ]

def inicio_jogo_madero(callback_jogo_madero):
    global fala_mentao, botoes_atuais
    fala_mentao = Mentao.fala("AGORA A GENTE CORRE! CORRE DA POLICIA CORRE VAI VAI VAI!")
    mudar_mood("surpreso")
    botoes_atuais = [
        BotaoEscolha("*FUGIR DA POLICIA COM O CLEMENTAO*", 1, callback_jogo_madero),
    ]
    
#FALAS PRE INSPERINA
def pre_insperina(callback_mapa):
    global callback_aceitar_insperina
    callback_aceitar_insperina = callback_mapa
    cena_inicial_insperina()

def cena_inicial_insperina():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("Sextou Clementina! E acabou as provas, aleluia! Tô me sentindo LIVRE!")
    botoes_atuais = [
        BotaoEscolha("Nem me fala, parecia que essa semana não acabava nunca...", 1, insperina_resposta_cansaco),
        BotaoEscolha("Você fez alguma prova ou só ficou colando mesmo?", 2, insperina_resposta_safado),
        BotaoEscolha("Se tá livre? então bora fazer merda?", 3, insperina_resposta_livre)
    ]

def insperina_resposta_cansaco():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Real! Tô só o pó do pastel. Mas hoje é dia de ressuscitar!")
    botoes_atuais = [
        BotaoEscolha("Vai fazer o que hoje?", 1, convite_insperina),
        BotaoEscolha("Descansar, né? (sqn)", 2, convite_insperina)
    ]

def insperina_resposta_safado():
    global fala_mentao, botoes_atuais
    mudar_mood("bravo")
    fala_mentao = Mentao.fala("Óbvio que eu colei! Você acha que eu sei o que é um odeint?")
    botoes_atuais = [
        BotaoEscolha("Hahaha, pelo menos é sincero...", 1, convite_insperina),
        BotaoEscolha("Você é uma vergonha, bora comemorar mesmo assim", 2, convite_insperina)
    ]

def insperina_resposta_livre():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("É ISSO! Bora esquecer que ModSim existe!")
    botoes_atuais = [
        BotaoEscolha("Tem rolê hoje?", 1, convite_insperina),
        BotaoEscolha("Partiu curtir!", 2, convite_insperina)
    ]

def convite_insperina():
    global fala_mentao, botoes_atuais, callback_aceitar_insperina
    mudar_mood("feliz")
    progresso_jogador["insperina desbloqueada"] = True
    fala_mentao = Mentao.fala("Então vamo pra Insperina! Vai ter funk, suquinho... adoro suquinho!")
    botoes_atuais = [
        BotaoEscolha("*ACEITAR O CONVITE E IR COM MENTÃO*", 1, callback_aceitar_insperina)
    ]

#FALAS NA INSPERINA
callback_tela_final = None

def criar_cena_inicial_insperina():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("CHEGAMOS NA INSPERINA! Olha essa vibe Clementina! Funk bombando e o suquinho... ahhh o suquinho")
    botoes_atuais = [
        BotaoEscolha("Você já tá bêbado de suco?", 1, cena_opcao_errada_insperina),
        BotaoEscolha("Vamo dançar Mentão!", 2, cena_dancar_insperina),
        BotaoEscolha("Cuidado pra não derrubar ninguém", 3, cena_opcao_errada_insperina)
    ]

def cena_opcao_errada_insperina():
    global fala_mentao, botoes_atuais
    mudar_mood("briga")
    fala_mentao = Mentao.fala("Poxa Clementina, acabou com meu clima... vou embora dessa festa!")
    botoes_atuais = [
        BotaoEscolha("*GAME OVER*", 1, callback_gameover_global)
    ]

def cena_dancar_insperina():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("AEEE, isso que eu gosto! Mentão REBOLA e o mundo gira!")
    botoes_atuais = [
        BotaoEscolha("Você tá demais hoje kkkkk", 1, cena_reacao_danca),
        BotaoEscolha("*Dançar com o Mentão*", 2, cena_reacao_danca)
    ]

def cena_reacao_danca():
    global fala_mentao, botoes_atuais
    mudar_mood("surpreso")
    fala_mentao = Mentao.fala("Essa ai ta no mexidão do mentão! AGORA SIM!")
    botoes_atuais = [
        BotaoEscolha("Mentão do céu, chico buarque?", 1, cena_pergunta_danca),
        BotaoEscolha("PQP EU AMO MEXIDAO DO MENTAO", 2, cena_pergunta_danca),
        BotaoEscolha("Vem pro canto comigo...", 3, cena_opcao_errada_insperina)
    ]

def cena_pergunta_danca():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("ÉÉÉÉÉÉÉÉÉÉ O MEXIDAO PORRAAA!")
    botoes_atuais = [
        BotaoEscolha("Então mostra!", 1, cena_mostrar_danca),
        BotaoEscolha("VAI CLEMENTÃO", 2, cena_mostrar_danca),
        BotaoEscolha("Não, por favor...", 3, cena_opcao_errada_insperina)
    ]

def cena_mostrar_danca():
    global fala_mentao, botoes_atuais
    mudar_mood("bebendo")
    fala_mentao = Mentao.fala("Calmae vou beber do meu stanley")
    botoes_atuais = [
        BotaoEscolha("Só você mentão!", 1, cena_reacao_final),
        BotaoEscolha("Para! Você já ta muito bebado", 2, cena_opcao_errada_insperina)
    ]

def cena_reacao_final():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Clementina... eu tenho algo para te falar")
    botoes_atuais = [
        BotaoEscolha("Late Mentão", 1, cena_final_feliz),
    ]

def cena_final_feliz():
    global fala_mentao, botoes_atuais
    mudar_mood("feliz")
    fala_mentao = Mentao.fala("Eu sou ninja de Dessoft, e eu quero te beijar")
    botoes_atuais = [
        BotaoEscolha("Meu deus, vem logo!", 1, callback_tela_final)
    ]
