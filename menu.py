import jeu_de_mots
import pygame
import DICIONARIO

pygame.init()
largura = 360
altura = 500
screen = pygame.display.set_mode((largura, altura))
font_1 = pygame.font.Font('freesansbold.ttf', 20)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (65, 105, 225)
cinza = (128, 128, 128)
mensagem_jogo = font_1.render("Choisissez la langue :", True, preto)
mensagem_pt = font_1.render("Portugais  - Tappez 1", True, preto)
mensagem_en = font_1.render("Anglais     - Tappez 2", True, preto)
mensagem_fr = font_1.render("Français    - Tappez 3", True, preto)
mensagem_es = font_1.render("Espagnol   - Tappez 4", True, preto)
mensagem_regra = font_1.render("Explication :", True, preto)
regra_errado = font_1. render("Lettre n'est pas dans mot", True, preto)
regra_quase = font_1.render("Lettre existe, mauvauis endroit", True, preto)
regra_certo = font_1.render("Lettre existe, bon endroit", True, preto)
mensagem_objetivo = font_1.render("*Le but est de trouver le mot secret", True, preto)

resposta = ''

clock = pygame.time.Clock()


def show_message(string, x, y):
    """Montre une message aux coordonnées x, y"""
    screen.blit(string, (x, y))
    pygame.display.update()

def show_square(x, y, z, t, cor, f):
    """Montre un carré de couleur choisie, qui est aux coordonnées x,y
    de largeur z et hauteur t, de forme f (soit vide, soit remplie)"""
    pygame.draw.rect(screen, cor, [x, y, z, t], f, 3, 10, 10, 10, 10)
    pygame.display.update()

def empty_square(l, c, liste, x, y, z, t):
    """Montre un carré vide remplie d'une liste(lettre) pour être plus facil de placer la lettre dedans"""
    for col in range(l):
        for ligne in range(c):
            font = pygame.font.Font('freesansbold.ttf', 30)
            pygame.draw.rect(screen, (30, 10, 20), [x, y, z, t], 1, 4)
            letra = font.render(liste[ligne][col], True, preto)
            screen.blit(letra, (x + 8, y + 5))
            pygame.display.update()

def appeler_jeu(idioma, resposta):
    jeu_de_mots.define_icon()
    resposta = jeu_de_mots.choix_du_mot(idioma) 
    print(f"A resposta é {resposta}")
    jeu_de_mots.motus(idioma, resposta)

evento = True
while evento:
    #Menu du jeu, où des messages vont être affichées
    screen.fill((210, 180, 140)) 
    jeu_de_mots.call_images()
    clock.tick(1)
    show_square(0, 50, 230, 35, cinza, 0)
    show_message(mensagem_jogo, 5, 60)
    show_message(mensagem_pt, 20, altura / 5)
    show_message(mensagem_en, 20, altura / 5 + 30)
    show_message(mensagem_fr, 20, altura / 5 + 60)
    show_message(mensagem_es, 20, altura / 5 + 90)

    show_square(0, altura / 5 + 150, 140, 30, cinza, 0)
    show_message(mensagem_regra, 5, altura / 5 + 160)

    empty_square(1, 1, ['A'], 5, 290, 40, 40)
    show_message(regra_errado, 50, 300)

    show_square(5, 340, 40, 40, amarelo, 0)
    empty_square(1, 1, ['B'], 5, 340, 40, 40)
    show_message(regra_quase, 50, 350)

    show_square(5, 390, 40, 40, verde, 0)
    empty_square(1, 1, ['C'], 5, 390, 40, 40)
    show_message(regra_certo, 50, 400)

    show_message(mensagem_objetivo, 5, 470)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             evento = False

        #Logique du menu : Dès que le jouer tappe le numero, le jeu se derrouléra dans la langue choisie
        #Pour ça, il faut que le jeu soit une fonction et quand le jouer tappe, la fonction jeu sera appelée
        if event.type == pygame.KEYDOWN:
            #Pour choisir portugais
            if event.key == pygame.K_1:
                evento = False
                appeler_jeu(DICIONARIO.mot_5_br, jeu_de_mots.choix_du_mot(DICIONARIO.mot_5_br))
                print(resposta)

            #Pour choisir anglais
            if event.key == pygame.K_2:
                appeler_jeu(DICIONARIO.mot_5_en, jeu_de_mots.choix_du_mot(DICIONARIO.mot_5_en))

            #Pour choisir français
            if event.key == pygame.K_3:
                 appeler_jeu(DICIONARIO.dicionario_5_fr, jeu_de_mots.choix_du_mot(DICIONARIO.dicionario_5_fr))

            #Pour chousir espagnol
            if event.key == pygame.K_4:
                appeler_jeu(DICIONARIO.mot_5_es, jeu_de_mots.choix_du_mot(DICIONARIO.mot_5_es))

    pygame.display.update()
pygame.quit()