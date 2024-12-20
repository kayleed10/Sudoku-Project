import pygame, sys
from sudoku_generator import SudokuGenerator
from sudoku_generator import Board
from sudoku_generator import Cell

##These grid functions will be deleted later on today
# def draw_big_grid():
#     #draw horizontal lines
#     for i in range(1, 4):
#         pygame.draw.line(
#             screen,
#             (0,0,0),
#             (0, i*145),
#             (500, i*145),
#             6
#         )
#
#     #draw vertical lines
#     for i in range(1, 3):
#         pygame.draw.line(
#             screen, ##surface
#             (0,0,0), ##color
#             (i*166, 0), ##start position
#             (i*166, 438), ##end position
#             6
#
#         )
#
# def draw_small_grid():
#     #draw horizontal lines
#     for i in range(0, 9):
#         pygame.draw.line(
#             screen,
#             (0,0,0),
#             (0, i*48.8),
#             (500, i*48.8),
#             2
#         )
#
#     #draw vertical lines
#     for i in range(0, 10):
#         pygame.draw.line(
#             screen, ##surface
#             (0,0,0), ##color
#             (i*55.4, 0), ##start position
#             (i*55.4, 438), ##end position
#             2
#
#         )

def game_over(screen):
  title_font = pygame.font.Font("font/artifakt/Artifakt Element Black.ttf", 47)
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 20) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (540, 600))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((265,75), pygame.SRCALPHA) #For showing title
  title_surface.fill((255, 255, 255, 200))
  title_text = title_font.render("Game Over", 1, (0,0,0))
  title_rectangle = title_surface.get_rect(center = (540 //2, 600 // 2 - 100))
  title_rec = title_text.get_rect(center=(540 // 2, 600 // 2 - 100))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_rec)

  ## Restart button
  restart_text = button_font.render("RESTART", 1, (255,255,255))


  ## Button background
  restart_surface = pygame.Surface((130, 40))

  ## Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (17,5))

  restart_rectangle = restart_surface.get_rect(
    center = (540 // 2, 600 // 2 + 5))

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
  title_font = pygame.font.Font("font/artifakt/Artifakt Element Black.ttf", 47)
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 20) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (540, 600))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((270,75), pygame.SRCALPHA) #For showing title
  title_surface.fill((255, 255, 255, 200))
  title_text = title_font.render("Game Won!", 1, (0,0,0))
  title_rectangle = title_surface.get_rect(center = (540 //2, 600 // 2 - 100))
  title_rec = title_text.get_rect(center=(540 // 2, 600 // 2 - 100))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_rec)

  ## Exit button
  exit_text = button_font.render("EXIT", 1, (255,255,255))


  ## Button background
  exit_surface = pygame.Surface((130, 40))

  ## Putting restart button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (38,5))

  exit_rectangle = exit_surface.get_rect(
    center = (540 // 2, 600 // 2 + 5))

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
  # draw_big_grid()
  # draw_small_grid()

  sudoku_board = Board(540, 540, screen, 30)
  # for row in sudoku_board.cells:
  #   for cell in row:


  sudoku_board.draw()

  ##Buttons at bottom of screen
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 16)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 1, (255,255,255))
  restart_text = button_font.render("RESTART", 1, (255,255,255))
  exit_text = button_font.render("EXIT", 1, (255,255,255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85,30))
  exit_surface = pygame.Surface((85,30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15,3))

  reset_rectangle = reset_surface.get_rect(
    center = (540 // 2 - 95, 570))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5,3))

  restart_rectangle = restart_surface.get_rect(
    center = (540 // 2, 570))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20,3))

  exit_rectangle = exit_surface.get_rect(
    center = (540 // 2 + 95, 570))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()
  x, y = 0,0
  while True:
    if sudoku_board.is_full() == True:
      if sudoku_board.check_board() == True:
        game_won(screen)
      if sudoku_board.check_board() == False:
        game_over(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          sudoku_board.reset_to_original()
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()
        else:
          x, y = event.pos
          # if not sudoku_board.is_full:
          sudoku_board.click(x, y)
      elif event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:
          user_input = event.key - pygame.K_0
          sudoku_board.sketch(user_input)
        if pygame.K_KP_1 <= event.key <= pygame.K_KP_9:
          user_input = event.key - pygame.K_KP_1 + 1
          sudoku_board.sketch(user_input)
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
          sudoku_board.place_number(user_input)
        elif event.key == pygame.K_BACKSPACE:
          if sudoku_board.selected_cell:
            sudoku_board.selected_cell.set_sketched_value(0)
        elif event.key == pygame.K_UP:

          original_x, original_y = x, y

          while True:
            y -= 60
            if y <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break

        elif event.key == pygame.K_DOWN:
          original_x, original_y = x, y
          while True:
            y += 60
            if y >= 540:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_LEFT:
          original_x, original_y = x, y
          while True:
            x -= 60
            if x <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_RIGHT:
          original_x, original_y = x,y
          while True:
            x+=60
            if x>=540:
              x,y = original_x, original_y
              sudoku_board.click(x,y)
              break
            sudoku_board.click(x,y)

            if sudoku_board.selected_cell.value == 0:
              break

    screen_surface = pygame.Surface((540,540))
    screen_surface.fill((202,228,241))
    sudoku_board.draw()
    pygame.display.update()


def med_screen(screen):
  screen.fill((202, 228, 241))
  # draw_big_grid()
  # draw_small_grid()

  sudoku_board = Board(540, 540, screen, 40)
  # for row in sudoku_board.cells:
  #   for cell in row:

  sudoku_board.draw()

  ##Buttons at bottom of screen
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 16)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 1, (255, 255, 255))
  restart_text = button_font.render("RESTART", 1, (255, 255, 255))
  exit_text = button_font.render("EXIT", 1, (255, 255, 255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85, 30))
  exit_surface = pygame.Surface((85, 30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15, 3))

  reset_rectangle = reset_surface.get_rect(
    center=(540 // 2 - 95, 570))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5, 3))

  restart_rectangle = restart_surface.get_rect(
    center=(540 // 2, 570))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20, 3))

  exit_rectangle = exit_surface.get_rect(
    center=(540 // 2 + 95, 570))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()
  x, y = 0, 0
  while True:
    if sudoku_board.is_full() == True:
      if sudoku_board.check_board() == True:
        game_won(screen)
      if sudoku_board.check_board() == False:
        game_over(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          sudoku_board.reset_to_original()
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()
        else:
          x, y = event.pos
          # if not sudoku_board.is_full:
          sudoku_board.click(x, y)
      elif event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:
          user_input = event.key - pygame.K_0
          sudoku_board.sketch(user_input)
        if pygame.K_KP_1 <= event.key <= pygame.K_KP_9:
          user_input = event.key - pygame.K_KP_1 + 1
          sudoku_board.sketch(user_input)
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
          sudoku_board.place_number(user_input)
        elif event.key == pygame.K_BACKSPACE:
          if sudoku_board.selected_cell:
            sudoku_board.selected_cell.set_sketched_value(0)
        elif event.key == pygame.K_UP:
          original_x, original_y = x, y
          while True:
            y -= 60
            if y <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break

        elif event.key == pygame.K_DOWN:
          original_x, original_y = x, y
          while True:
            y += 60
            if y >= 540:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_LEFT:
          original_x, original_y = x, y
          while True:
            x -= 60
            if x <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_RIGHT:
          original_x, original_y = x, y
          while True:
            x += 60
            if x >= 540:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break

    screen_surface = pygame.Surface((540, 540))
    screen_surface.fill((202, 228, 241))
    sudoku_board.draw()
    pygame.display.update()


def hard_screen(screen):
  screen.fill((202, 228, 241))
  # draw_big_grid()
  # draw_small_grid()

  sudoku_board = Board(540, 540, screen, 50)
  # for row in sudoku_board.cells:
  #   for cell in row:

  sudoku_board.draw()

  ##Buttons at bottom of screen
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 16)
  ## Difficulty buttons
  reset_text = button_font.render("RESET", 1, (255, 255, 255))
  restart_text = button_font.render("RESTART", 1, (255, 255, 255))
  exit_text = button_font.render("EXIT", 1, (255, 255, 255))

  ## Button background
  reset_surface = pygame.Surface((85, 30))
  restart_surface = pygame.Surface((85, 30))
  exit_surface = pygame.Surface((85, 30))

  ## Putting reset button on screen
  reset_surface.fill((92, 64, 51))
  reset_surface.blit(reset_text, (15, 3))

  reset_rectangle = reset_surface.get_rect(
    center=(540 // 2 - 95, 570))

  screen.blit(reset_surface, reset_rectangle)

  ##Putting restart button on screen
  restart_surface.fill((92, 64, 51))
  restart_surface.blit(restart_text, (5, 3))

  restart_rectangle = restart_surface.get_rect(
    center=(540 // 2, 570))

  screen.blit(restart_surface, restart_rectangle)

  ##Putting exit button on screen
  exit_surface.fill((92, 64, 51))
  exit_surface.blit(exit_text, (20, 3))

  exit_rectangle = exit_surface.get_rect(
    center=(540 // 2 + 95, 570))

  screen.blit(exit_surface, exit_rectangle)

  pygame.display.update()
  x, y = 0, 0
  while True:
    if sudoku_board.is_full() == True:
      if sudoku_board.check_board() == True:
        game_won(screen)
      if sudoku_board.check_board() == False:
        game_over(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          sudoku_board.reset_to_original()
        elif restart_rectangle.collidepoint(event.pos):
          main_menu_draw(screen)
        elif exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          sys.exit()
        else:
          x, y = event.pos
          # if not sudoku_board.is_full:
          sudoku_board.click(x, y)
      elif event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:
          user_input = event.key - pygame.K_0
          sudoku_board.sketch(user_input)
        if pygame.K_KP_1 <= event.key <= pygame.K_KP_9:
          user_input = event.key - pygame.K_KP_1 + 1
          sudoku_board.sketch(user_input)
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
          sudoku_board.place_number(user_input)
        elif event.key == pygame.K_BACKSPACE:
          if sudoku_board.selected_cell:
            sudoku_board.selected_cell.set_sketched_value(0)
        elif event.key == pygame.K_UP:
          original_x, original_y = x, y
          while True:
            y -= 60
            if y <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break

        elif event.key == pygame.K_DOWN:
          original_x, original_y = x, y
          while True:
            y += 60
            if y >= 540:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_LEFT:
          original_x, original_y = x, y
          while True:
            x -= 60
            if x <= 0:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break
        elif event.key == pygame.K_RIGHT:
          original_x, original_y = x, y
          while True:
            x += 60
            if x >= 540:
              x, y = original_x, original_y
              sudoku_board.click(x, y)
              break
            sudoku_board.click(x, y)

            if sudoku_board.selected_cell.value == 0:
              break

    screen_surface = pygame.Surface((540, 540))
    screen_surface.fill((202, 228, 241))
    sudoku_board.draw()
    pygame.display.update()


def main_menu_draw(screen):
  title_font = pygame.font.Font("font/artifakt/Artifakt Element Black.ttf", 37)
  game_mode_font = pygame.font.Font("font/artifakt/Artifakt Element Black.ttf", 23)
  button_font = pygame.font.Font("font/comicsansms/comicbd.ttf", 20) #lucidasans or rockwellextra are other possible fonts

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (540, 600))
  screen.blit(sudoku_image, (0,0))


  title_surface = pygame.Surface((375,50), pygame.SRCALPHA) #For showing title
  title_surface.fill((255, 255, 255, 200))
  title_text = title_font.render("Welcome to Sudoku", 1, (0,0,0))
  title_rectangle = title_surface.get_rect(center =(540 // 2, (600 // 2) - 125))
  title_text_rec = title_text.get_rect(center =(540 // 2, (600 // 2) - 125 ))
  screen.blit(title_surface, title_rectangle)
  screen.blit(title_text, title_text_rec)

  game_mode_surface = pygame.Surface((230,40), pygame.SRCALPHA) #For showing "game mode select" text
  game_mode_surface.fill((255, 255, 255, 200))
  game_mode_text = game_mode_font.render("Select Game Mode:", 1, (0,0,0))
  game_mode_rectangle = game_mode_surface.get_rect(center = (540 //2, (600 // 2) - 15))
  game_mode_rec = game_mode_text.get_rect(center=(540 // 2, (600 // 2) - 15))
  screen.blit(game_mode_surface, game_mode_rectangle)
  screen.blit(game_mode_text, game_mode_rec)

  ## Difficulty buttons
  easy_text = button_font.render("EASY", 1, (255,255,255))
  medium_text = button_font.render("MEDIUM", 1, (255,255,255))
  hard_text = button_font.render("HARD", 1, (255,255,255))

  ## Button background
  easy_surface = pygame.Surface((90, 40))
  medium_surface = pygame.Surface((125,40))
  hard_surface = pygame.Surface((90,40))

  ## Putting easy button on screen
  easy_surface.fill((92, 64, 51))
  easy_surface.blit(easy_text, (17,5))

  easy_rectangle = easy_surface.get_rect(
    center = (540 // 2 - 150, 600 // 2 + 110))

  screen.blit(easy_surface, easy_rectangle)

  ##Putting medium button on screen
  medium_surface.fill((92, 64, 51))
  medium_surface.blit(medium_text, (17,5))

  medium_rectangle = medium_surface.get_rect(
    center = (540 // 2, 600 // 2 + 110))

  screen.blit(medium_surface, medium_rectangle)

  ##Putting hard button on screen
  hard_surface.fill((92, 64, 51))
  hard_surface.blit(hard_text, (17,5))

  hard_rectangle = hard_surface.get_rect(
    center = (540 // 2 + 150, 600 // 2 + 110))

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
          med_screen(screen)
        elif hard_rectangle.collidepoint(event.pos):
          hard_screen(screen)

    pygame.display.update()

if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode((540, 600))
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