import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((500,500))
ludo = pygame.image.load("match the following /ludo.png")
subway_surfs = pygame.image.load("match the following /subway surfs .png") 
temple_run = pygame.image.load("match the following /temple run.png")
candy_crush = pygame.image.load("match the following /candy crush.jpg")
screen.blit(ludo,(50,10))
screen.blit(subway_surfs,(50,110))
screen.blit(temple_run,(50,210))
screen.blit(candy_crush,(50,310))
font = pygame.font.SysFont("Arial",15,True)
store_text = font.render("Candy Crush",0,"White")
screen.blit(store_text,(300,140))
store_text2 = font.render("Subway Surfs",0,"White")
screen.blit(store_text2,(300,50))
store_text3 = font.render("Ludo",0,"white")
screen.blit(store_text3,(300,240))
store_text4 = font.render("Temple Run",0,"white")
screen.blit(store_text4,(300,340))
while True :
  event = pygame.event.poll()
  if event.type==pygame.MOUSEBUTTONDOWN:
     position = pygame.mouse.get_pos()
     pygame.draw.circle(screen,"white", position,10)
  if event.type==pygame.MOUSEBUTTONUP:
     position2 = pygame.mouse.get_pos()
     pygame.draw.line(screen,"white",position,position2,5)
     pygame.draw.circle(screen,"white", position2,10)
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :  
        sys.exit()
    pygame.display.update()   

