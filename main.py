from personnage import personnage
from Menu import *
import pygame

#Const
TITLE = "Epic Noob Battle"
PATH_BACKGROUND = 'assets/background.gif'
PATH_R_ARROW = 'assets/right-arrow.png'
SCREENSIZE = (1280, 600)
PERSONNAGES = ["bleu", 'blond', "brun", "noir", "rouge", "violet"]

#init pygame
pygame.init()

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREENSIZE)

#init Menu
menu = Menu()
background = menu.loadBackground(PATH_BACKGROUND)
menu.loadArrow(PATH_R_ARROW)

#Ajout des personnages
for name in PERSONNAGES:
  menu.loadPersonnage(personnage(name))


def menuIntro():
  logo = pygame.image.load('assets/logoV1.png')
  logo = pygame.transform.scale(logo, (800, 550))
  screen.blit(logo, (200,200))


running = True

while running:
  menu.show(screen, SCREENSIZE)

  menuIntro()

  pygame.display.flip()

  for event in pygame.event.get():
    menu.onEvent(event, SCREENSIZE)

    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")
