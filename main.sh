#python3 sudoku.py

import pygame, sys

def main_menu_draw(screen):
  title_font = pygame.font.SysFont("artifaktelement", 40)
  game_mode_font = pygame.font.SysFont("artifaktelement", 25)
  button_font = pygame.font.SysFont("comicsansms", 20, bold=True) #lucidasansrockwellextra

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (500, 500))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((375,50)) #For showing title
  title_surface.fill((255, 255, 255))
  title_text = title_font.render("Welcome to Sudoku", 0, (0,0,0))
  title_rectangle = title_surface.get_rect(
  center = (500 //2, 500 // 2 - 125))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_rectangle)

  game_mode_surface = pygame.Surface((230,40)) #For showing "game mode select" text
  game_mode_surface.fill((255, 255, 255))
  game_mode_text = game_mode_font.render("Select Game Mode:", 0, (0,0,0))
  game_mode_rectangle = game_mode_surface.get_rect(
  center = (500 //2, 500 // 2 - 15))
  screen.blit(game_mode_surface, game_mode_rectangle)
  screen.blit(game_mode_text, game_mode_rectangle)

  ## Difficulty buttons
  easy_text = button_font.render("EASY", 0, (255,255,255))
  medium_text = button_font.render("MEDIUM", 0, (255,255,255))
  hard_text = button_font.render("HARD", 0, (255,255,255))

  ## Button background
  easy_surface = pygame.Surface((90, 40))
  medium_surface = pygame.Surface((125,40))
  hard_surface = pygame.Surface((90,40))

  ## Putting easy button on screen
  easy_surface.fill((92, 64, 51))
  easy_surface.blit(easy_text, (17,5))

  easy_rectangle = easy_surface.get_rect(
    center = (500 // 2 - 150, 500 // 2 + 110))

  screen.blit(easy_surface, easy_rectangle)

  ##Putting medium button on screen
  medium_surface.fill((92, 64, 51))
  medium_surface.blit(medium_text, (17,5))

  medium_rectangle = medium_surface.get_rect(
    center = (500 // 2, 500 // 2 + 110))

  screen.blit(medium_surface, medium_rectangle)

  ##Putting hard button on screen
  hard_surface.fill((92, 64, 51))
  hard_surface.blit(hard_text, (17,5))

  hard_rectangle = hard_surface.get_rect(
    center = (500 // 2 + 150, 500 // 2 + 110))

  screen.blit(hard_surface, hard_rectangle)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        pygame.display.update()
#        if start_rectangle.collidepoint(event.pos):
#        return


    pygame.display.update()

if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Sudoku")

  main_menu_draw(screen)
#  screen.fill((255,255,255))
#  pygame.display.update()
#
#
#
#
#  game_over = False
#
#  while True:
#    for event in pygame.event.get():
#      if event.type == pygame.QUIT:
#        pygame.quit()
#        sys.exit()
#      if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#        x, y = event.pos
#    screen.blit(sudoku_image, (0,0))
#    pygame.display.update()