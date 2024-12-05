#python3 sudoku.py
#C:\Users\chris\AppData\Local\Programs\Python\Python312\python.exe
import pygame, sys

if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Sudoku")
  screen.fill((255,255,255))
  pygame.display.update()

  sudoku_image = pygame.image.load("sudoku_image.jpg")
  sudoku_image = pygame.transform.scale(sudoku_image, (500, 500))


  game_over = False

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        x, y = event.pos
    screen.blit(sudoku_image, (0,0))
    pygame.display.update()