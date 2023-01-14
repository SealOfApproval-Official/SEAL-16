import pygame, os, time, math


os.system('cls' if os.name == 'nt' else 'clear')

def get_best_size():
  smaller = min(winW, winH)
  nearest = smaller - (smaller % 127)
  return nearest
def find_origin_x():
  return winW / 2 - get_best_size() / 2

def find_origin_y():
  return winH / 2 - get_best_size() / 2

pygame.init()
pygame.font.init()

# Create the window, saving it to a variable.
surface = pygame.display.set_mode((127, 127), pygame.RESIZABLE)
pygame.display.set_caption("SEAL-16")
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)

winW, winH = pygame.display.get_window_size()
sizeP = min(winW, winH) / 127

sealBlock = pygame.font.Font("SealBlock.ttf", math.floor((get_best_size() / 127) * 30))

running = True

while running:
  winW, winH = pygame.display.get_window_size()
  smaller = (winW if winW < winH else winH)
  sizeP = (winW if winW < winH else winH)/127
  sealBlock = pygame.font.Font("SealBlock.ttf", max(5, math.floor(get_best_size() / 127) * 5))

  surface.fill((0,0,0))

  if get_best_size() >= 127:
    pygame.draw.rect(surface, (255,255,255), (find_origin_x(),
                                              find_origin_y(),
                                              get_best_size(),
                                              get_best_size()
                                              ))
    # surface.blit(sealBlock.render("Hello, World!", 0, (0,0,0)), (find_origin_x(),find_origin_y()))
  else:
    for i in range(3):
      if i == 0:
        label = sealBlock.render("Small", 0, (255,255,255))
      elif i == 1:
        label = sealBlock.render("Screen", 0, (255,255,255))
      elif i == 2:
        label = sealBlock.render("Warning", 0, (255,255,255))
      surface.blit(label, (0, i*5))
  
  with open('cool.py') as f:
    toRun = f.read()
    eval(toRun)
  
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False