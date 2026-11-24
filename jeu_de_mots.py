import pygame
import DICIONARIO
import random

#Initialisation de valeurs et du pygame pour pouvoir travailler avec la bibliothèque
pygame.init()
verde = (0, 255, 0)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (65, 105, 225)
c = 6 #Nombre d'essais
l = 5 #Nombre de lettres
letras = 0
tentativa = 0
gagne = False
tentativa_ativa = True
error = False
altura = 500
largura = 360
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 30)
font_1 = pygame.font.Font('freesansbold.ttf', 20)
screen = pygame.display.set_mode((largura, altura))
# resposta = ''

#Definition de fonctions
#1.
def choix_du_mot(list):
    """On selécitonne aléatoirement un mot d'une liste qui contient plusieurs mots de 5 lettres"""
    nombre = random.randint(1, len(list) - 1)
    #mot est le mot qui va être la réponse, ce qu'on cherche
    mot = list[nombre]
    mot = mot.upper()
    return mot
# resposta = choix_du_mot(DICIONARIO.mot_5_br) + '2'
# print(resposta)

#2.
def tabuleiro(l, c, list):
    """Crée une tableau de carrés noirs dans une liste2D déjà existante
    Crée aussi une ligne plus fort dans la lettre actuel d'essai"""
    global tabuleiro
    for col in range(l):
        for ligne in range(c):
            font = pygame.font.Font('freesansbold.ttf', 35)
            pygame.draw.rect(screen, (30, 10, 20), [col * 60 + 40, ligne * 60 + 80, 50, 50], 1, 4)
            letra = font.render(list[ligne][col], True, preto)
            screen.blit(letra, (col * 60 + 50, ligne * 60 + 90))
    if not gagne and letras != l and tentativa != c:
            pygame.draw.rect(screen, preto, [letras * 60 + 40, tentativa * 60 + 80, 50, 50], 3, 5)
    if letras >= 5:
            pygame.draw.rect(screen, preto, [(l - 1) * 60 + 40, tentativa * 60 + 80, 50, 50], 3, 5)

#3.
def regles(quadrados, str):
    """Les règles sont appliqués dans une autre liste 2D avec que des couleurs
    Le tableau est superposée à l'autre en raison des problèmes d'affichage dans le loop while infini"""
    global cor
    for i in range(c):
        dicionario = dictionnaire_lettres(str)

        for j in range(l):
            global tentativa
            a = str[j]
            if quadrados[i][j] == a and dicionario[a] > 0:
                dicionario[quadrados[i][j]] -= 1
                cor[i][j] = 1 #Correto e lugar certo
                
            elif cor[i][j] != 1 and quadrados[i][j] in str and dicionario[quadrados[i][j]] > 0:
                dicionario[quadrados[i][j]] -= 1
                cor[i][j] = 2 #Correto e lugar errado

#4.
def colocar_cor(cor):
    """Mettre des couleurs dans le nouveau tableau qui a déjà verifié les règles du jeu"""
    for i in range(len(cor)):
        for j in range(len(cor[i])):
            if cor[i][j] == 1:
                pygame.draw.rect(screen, verde, [j * 60 + 40, i * 60 + 80, 50, 50], 0, 3)
            if cor[i][j] == 2:
                pygame.draw.rect(screen, amarelo, [j * 60 + 40, i * 60 + 80, 50, 50], 0, 3)        

#5.
def dictionnaire_lettres(resposta):
    """Crée un dictionnaire pour vérfier la quantité de chaque lettre du mot"""
    dictionnaire = {}
    for lettre in resposta:
        dictionnaire[lettre] = dictionnaire.get(lettre, 0) + 1
    return dictionnaire

#6.
quadrados = []
def criar_tabela(c, l, s):
    """Crée une liste 2D vide qui sert a déssiner les carrés vides et mettre les lettres dédans"""
    for i in range(c):
        linha = []
        for j in range(l):
            linha.append(s)
        quadrados.append(linha)

#7.
cor = []
def criar_tabela_cores(c, l, s):
    """Crée un tableau de 0 où les règles du jeu seront verifiées (en raison du loop infini)"""
    for i in range(c):
        linha = []
        for j in range(l):
            linha.append(s)
        cor.append(linha)

#8.
def verifier_victoire(s1, s2):
    """Vérifie si le mot saisie est le mot secret"""
    global gagne
    if s1 == s2:
        gagne = True

#9.
def verifier_mot(s1, list):
    """Vérifie si le mot existe, c'est-à-dire, si le mot est contenu dans la liste de mot qu'on a crée"""
    global error
    if s1 in list:
        error = False
    else:
        error = True

#10.
error_message = font_1.render("CE MOT N'EXISTE PAS", True, preto)
winning_message = font_1.render("VOUS AVEZ GAGNÉ ! :)", True, preto)
# mensagem_certa = font_1.render(f"La réponse était: {resposta}", True, preto)

def show_message_top(string, cor):
    """Affiche un message choisie dans un carré de couleur choisi en haut de la fenêtre"""
    pygame.draw.rect(screen, cor, [0, 40, largura, 40], 0, 3, 20, 20, 20, 20)
    screen.blit(string, (70, 50))
    pygame.display.update()
    pygame.time.delay(1500)


#11.
def show_message_bottom(string, cor):
    """Affiche un message choisi, dans un carré de couleur choisi en bas de la fenêtre"""
    pygame.draw.rect(screen, cor, [10, 440, 340, 35], 0, 3, 20, 20, 20, 20)
    screen.blit(string, (25, 445))
    pygame.display.update()
    pygame.time.delay(2000)

#12.
def call_images():
    """Fait le download et affiche les images (MOTUS et drapeaux - décoration)"""
    imagens = [
        ('m.png', (60, 5)),
        ('o.png', (93, 5)),
        ('t.png', (120, 5)),
        ('u.png', (150, 5)),
        ('s.png', (180, 5)),
        ('brasil.png', (215, 5)),
        ('mexico.png', (250, 5)),
        ('france.png', (285, 5)),
    ]
    for arquivo, posicao in imagens:
        try:
            screen.blit(pygame.image.load(arquivo), posicao)
        except FileNotFoundError:
            pass  # image absente : on l'ignore
   
#13.
def define_icon():
    """Définit l'icon de la fênetre avec une image aussi - décoration"""
    pygame.display.set_caption("LA MEILLEURE VERSION DE MOTUS")
    icon = pygame.image.load('brain.png')
    pygame.display.set_icon(icon)

#14.
def apagar_letra(x):
    """Efface une lettre et reviens une case du tableau"""
    global letras
    if x < l:
        quadrados[tentativa][letras] = ' '
    if x > 0 or x >= l:
        letras -= 1

#Loop inifi où se passe le jeu
#On a transformé le jeu en fonction , pour pouvoir faire une menun où le jeu est appellé quand on veut
def motus(idioma, resposta):
    global letras
    global tentativa
    mensagem_certa = font_1.render(f"La réponse était: {resposta}", True, preto)

    running = True
    while running:  
        #Mets les choses dans la fênetre infini, ce sont des choses qui vont être toujours dans la fenêtre
        screen.fill((210, 180, 140))
        define_icon()
        call_images()
        colocar_cor(cor)
        criar_tabela(c, l, " ")
        tabuleiro(l, c, quadrados)
        
        #Le jeu s'arrête si on appui le X de fermer la fenêtre - condition de fin
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                #Si backspace est appuyée :
                if event.key == pygame.K_BACKSPACE:
                    apagar_letra(letras)

                #Si flèche à gauche est appuyée : On va une case à gauche sans effacer des lettres
                if event.key == pygame.K_LEFT and letras > 0:
                    letras -= 1

                #Si flèche à droite est appuyée: On va une case à droite sans effacer des lettres
                if event.key == pygame.K_RIGHT and letras < l:
                    letras += 1

                #Si return est appuyée: Les règles sont appliquées ( en raison du loop infini, on a besoin de faire vérifier les règles dans un moment specifique)
                #On a choisi ce moment comme le moment où on appui la tecle return
                #Comme ça, les règles ne sont pas toujours verifiées et le jeu marche bien
                if event.key == pygame.K_RETURN:
                    #On enregistre le mot saisie par l'utilisateur
                    palpite = ''
                    for i in range(l):
                        palpite = palpite + quadrados[tentativa][i]

                    #On vérifie si le mot existe
                    verifier_mot(palpite, idioma)

                    #Si le mot n'existe pas ou n'est pas du bon taille, un message d'erreur s'affiche
                    if error:
                        show_message_top(error_message, azul)

                    #Si le mot saisie existe, on effectue les règles (Carrés colorés)  
                    if not error:
                        criar_tabela_cores(c, l, 0)
                        regles(quadrados, resposta)
                        tentativa += 1
                        letras = 0
                        
                        #On verifie si l'utilisateur a gagné le jeu
                        verifier_victoire(resposta, palpite)

                        #Si l'utilisateur a gagné, on affiche un message
                        if gagne:
                            show_message_top(winning_message, azul)
                            
            #Ici on prends ce qui tappe l'utilisateur et sauvegarde
            if event.type == pygame.TEXTINPUT and tentativa_ativa and not gagne and letras < l:
                entry = event.__getattribute__('text')
                #On le mets en majuscule pour ne pas avoir de problèmes quand comparé avec la réponse(majuscule)
                entry = entry.upper()

                #On vérifie si l'utilisateur tappe bien des lettres et pas des chiffres(mots avec accents ont eu leurs accents enlevés pour mieux comparer)
                if entry in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    quadrados[tentativa][letras] = entry
                    letras += 1

        #On finit l'essai s'il est plus grand que la taille accepté
        if letras == l:
            tentativa_ativa = False
        if letras < l:
            tentativa_ativa = True

        #Si on a pas trouvé la réponse, la réponse va être affichée
        if tentativa == c and not gagne:
            show_message_top(mensagem_certa, azul)
        pygame.display.update()
    pygame.quit()