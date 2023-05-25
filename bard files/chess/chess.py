import pygame
import sys

# Define the colors of the pieces
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the size of the board
BOARD_SIZE = 800

# Create the game window
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

# Create the pieces
pieces = []
for i in range(8):
    for j in range(8):
        if i % 2 == j % 2:
            pieces.append(pygame.image.load("assets/white_pawn.png"))
        else:
            pieces.append(pygame.image.load("assets/black_pawn.png"))

# Create the board
board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
board.fill((255, 255, 255))

# Draw the board
for i in range(8):
    pygame.draw.line(board, (0, 0, 0), (i * 100, 0), (i * 100, BOARD_SIZE))
    pygame.draw.line(board, (0, 0, 0), (0, i * 100), (BOARD_SIZE, i * 100))

# Draw the pieces
for i in range(8):
    for j in range(8):
        board.blit(pieces[i * 8 + j], (i * 100, j * 100))

# Update the screen
pygame.display.update()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Find the piece that was clicked
            for i in range(8):
                for j in range(8):
                    if (x >= i * 100 and x < (i + 1) * 100) and (y >= j * 100 and y < (j + 1) * 100):
                        piece = pieces[i * 8 + j]

            # Move the piece
            piece.rect.x = x - piece.rect.width / 2
            piece.rect.y = y - piece.rect.height / 2

            # Update the screen
            board.blit(piece, piece.rect)
            pygame.display.update()

