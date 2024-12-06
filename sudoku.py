import pygame, sys

def draw_big_grid():
    #draw horizontal lines
    for i in range(1, 4):
        pygame.draw.line(
            screen,
            (0,0,0),
            (0, i*145),
            (500, i*145),
            6
        )

    #draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(
            screen, ##surface
            (0,0,0), ##color
            (i*166, 0), ##start position
            (i*166, 438), ##end position
            6

        )

def draw_small_grid():
    #draw horizontal lines
    for i in range(0, 9):
        pygame.draw.line(
            screen,
            (0,0,0),
            (0, i*48.8),
            (500, i*48.8),
            2
        )

    #draw vertical lines
    for i in range(0, 10):
        pygame.draw.line(
            screen, ##surface
            (0,0,0), ##color
            (i*55.4, 0), ##start position
            (i*55.4, 438), ##end position
            2

        )

def game_over(screen):
  title_font = pygame.font.SysFont("artifaktelement", 50)
  button_font = pygame.font.SysFont("comicsansms", 20, bold=True) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (500, 500))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((265,75)) #For showing title
  title_surface.fill((255, 255, 255))
  title_text = title_font.render("Game Over", 0, (0,0,0))
  title_rectangle = title_surface.get_rect(center = (500 //2, 500 // 2 - 100))
  title_rec = title_text.get_rect(center=(500 // 2, 500 // 2 - 100))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_rec)

  ## Restart button
  restart_text = button_font.render("RESTART", 0, (255,255,255))


  ## Button background
  restart_surface = pygame.Surface((130, 40))

  ## Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (17,5))

  restart_rectangle = restart_surface.get_rect(
    center = (500 // 2, 500 // 2 + 5))

  screen.blit(restart_surface, restart_rectangle)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)

    pygame.display.update()

def game_won(screen):
  title_font = pygame.font.SysFont("artifaktelement", 50)
  button_font = pygame.font.SysFont("comicsansms", 20, bold=True) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (500, 500))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((270,75)) #For showing title
  title_surface.fill((255, 255, 255))
  title_text = title_font.render("Game Won!", 0, (0,0,0))
  title_rectangle = title_surface.get_rect(center = (500 //2, 500 // 2 - 100))
  title_rec = title_text.get_rect(center=(500 // 2, 500 // 2 - 100))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_rec)

  ## Exit button
  exit_text = button_font.render("EXIT", 0, (255,255,255))


  ## Button background
  exit_surface = pygame.Surface((130, 40))

  ## Putting restart button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (38,5))

  exit_rectangle = exit_surface.get_rect(
    center = (500 // 2, 500 // 2 + 5))

  screen.blit(exit_surface, exit_rectangle)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()

    pygame.display.update()


def easy_screen(screen):
  screen.fill((202, 228, 241))
  draw_big_grid()
  draw_small_grid()

  ##Buttons at bottom of screen
  button_font = pygame.font.SysFont("comicsansms", 16, bold=True)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 0, (255,255,255))
  restart_text = button_font.render("RESTART", 0, (255,255,255))
  exit_text = button_font.render("EXIT", 0, (255,255,255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85,30))
  exit_surface = pygame.Surface((85,30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15,3))

  reset_rectangle = reset_surface.get_rect(
    center = (500 // 2 - 95, 500 // 2 + 219))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5,3))

  restart_rectangle = restart_surface.get_rect(
    center = (500 // 2, 500 // 2 + 219))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20,3))

  exit_rectangle = exit_surface.get_rect(
    center = (500 // 2 + 95, 500 // 2 + 219))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          easy_screen(screen)
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()

    pygame.display.update()


def med_screen(screen):
  screen.fill((202, 228, 241))
  draw_big_grid()
  draw_small_grid()

  ##Buttons at bottom of screen
  button_font = pygame.font.SysFont("comicsansms", 16, bold=True)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 0, (255,255,255))
  restart_text = button_font.render("RESTART", 0, (255,255,255))
  exit_text = button_font.render("EXIT", 0, (255,255,255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85,30))
  exit_surface = pygame.Surface((85,30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15,3))

  reset_rectangle = reset_surface.get_rect(
    center = (500 // 2 - 95, 500 // 2 + 219))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5,3))

  restart_rectangle = restart_surface.get_rect(
    center = (500 // 2, 500 // 2 + 219))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20,3))

  exit_rectangle = exit_surface.get_rect(
    center = (500 // 2 + 95, 500 // 2 + 219))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          med_screen(screen)
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()

    pygame.display.update()

def hard_screen(screen):
  screen.fill((202, 228, 241))
  draw_big_grid()
  draw_small_grid()

  ##Buttons at bottom of screen
  button_font = pygame.font.SysFont("comicsansms", 16, bold=True)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 0, (255,255,255))
  restart_text = button_font.render("RESTART", 0, (255,255,255))
  exit_text = button_font.render("EXIT", 0, (255,255,255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85,30))
  exit_surface = pygame.Surface((85,30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15,3))

  reset_rectangle = reset_surface.get_rect(
    center = (500 // 2 - 95, 500 // 2 + 219))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5,3))

  restart_rectangle = restart_surface.get_rect(
    center = (500 // 2, 500 // 2 + 219))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20,3))

  exit_rectangle = exit_surface.get_rect(
    center = (500 // 2 + 95, 500 // 2 + 219))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          hard_screen(screen)
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()

    pygame.display.update()



def main_menu_draw(screen):
  title_font = pygame.font.SysFont("artifaktelement", 40)
  game_mode_font = pygame.font.SysFont("artifaktelement", 25)
  button_font = pygame.font.SysFont("comicsansms", 20, bold=True) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (500, 500))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((375,50)) #For showing title
  title_surface.fill((255, 255, 255))
  title_text = title_font.render("Welcome to Sudoku", 1, (0,0,0))
  title_rectangle = title_surface.get_rect(center =(500 // 2, (500 // 2) - 125))
  title_text_rec = title_text.get_rect(center =(500 // 2, (500 // 2) - 125 ))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_text_rec)

  game_mode_surface = pygame.Surface((230,40)) #For showing "game mode select" text
  game_mode_surface.fill((255, 255, 255))
  game_mode_text = game_mode_font.render("Select Game Mode:", 1, (0,0,0))
  game_mode_rectangle = game_mode_surface.get_rect(center = (500 //2, (500 // 2) - 15))
  game_mode_rec = game_mode_text.get_rect(center=(500 // 2, (500 // 2) - 15))
  screen.blit(game_mode_surface, game_mode_rectangle)
  screen.blit(game_mode_text, game_mode_rec)

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
        if easy_rectangle.collidepoint(event.pos):
          easy_screen(screen)
        elif medium_rectangle.collidepoint(event.pos):
          game_over(screen)
        elif hard_rectangle.collidepoint(event.pos):
          game_won(screen)

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