import pygame
from random import choice
from math import sqrt


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Direction({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x:3}, {self.y:3}'

    def normalized(self):
        magnitude = sqrt(self.x**2 + self.y**2) + 0.0001  # no division by zero
        return Direction(self.x / magnitude, self.y / magnitude)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def reverse(self):
        return Direction(-self.x, -self.y)


def closest_direction(displacement, directions):
    norm = displacement.normalized()
    return max(directions, key=lambda x: x.dot_product(norm))


class Puzzle:

    TILE_SIZE = 40
    SPACE_COLOR = 'black'
    TEXT_COLOR = 'black'
    TEXT_SIZE = 30
    SOLVED_COLOR = (100, 255, 100)
    BORDER_COLOR = 'black'
    BORDER_WIDTH = 5
    MOVES = {'left': Direction(-1, 0),
             'right': Direction(1, 0),
             'down': Direction(0, 1),
             'up': Direction(0, -1)}
    SHUFFLE_COUNT = 50
    LEFT_CLICK = 1

    def __init__(self, width=4, height=4):
        self.width = abs(int(width))
        self.height = abs(int(height))
        # create board
        self.board = []
        number = 1
        for x in range(self.width):
            self.board.append([])
            for y in range(self.height):
                if number < self.width * self.height:
                    self.board[x].append(str(number))
                else:
                    self.board[x].append(' ')
                number += 1
        # keep track of space so it doesn't need to be found
        self.space = (self.width - 1, self.height - 1)
        # save solution
        self.solution = str(self)
        # save history
        self.history = []

    def __eq__(self, other):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] != other.board[x][y]:
                    return False
        return True

    def __repr__(self):
        return f'Puzzle({self.width}, {self.height})'

    def __str__(self):
        result = ''
        for x in range(self.width):
            for y in range(self.height):
                result += f'\t{self.board[x][y]}'
            result += '\n'
        return result

    def move(self, direction):
        """ Try making a move in the given direction.
        Return whether the move changed the board"""
        x, y = self.space
        # left
        if direction == self.MOVES['left']:
            # move space up in row
            if y < self.height - 1:
                self.board[x][y] = self.board[x][y + 1]
                self.board[x][y + 1] = ' '
                # update space
                self.space = (x, y + 1)
                # update history
                self.history.append(self.MOVES['left'])
                return True
        # right
        if direction == self.MOVES['right']:
            # move space down in row
            if y > 0:
                self.board[x][y] = self.board[x][y - 1]
                self.board[x][y - 1] = ' '
                # update space
                self.space = (x, y - 1)
                # update history
                self.history.append(self.MOVES['right'])
                return True
        # down
        if direction == self.MOVES['down']:
            # move space up in column
            if x > 0:
                self.board[x][y] = self.board[x - 1][y]
                self.board[x - 1][y] = ' '
                # update space
                self.space = (x - 1, y)
                # update history
                self.history.append(self.MOVES['down'])
                return True
        # up
        if direction == self.MOVES['up']:
            # move space down in column
            if x < self.width - 1:
                self.board[x][y] = self.board[x + 1][y]
                self.board[x + 1][y] = ' '
                # update space
                self.space = (x + 1, y)
                # update history
                self.history.append(self.MOVES['up'])
                return True
        return False

    def shuffle(self, move_count):
        """ Make move_count moves, making sure each move changes the board """
        moves_made = 0
        while moves_made < move_count:
            moves_made += int(self.move(choice(list(self.MOVES.values()))))

    def is_solved(self):
        return str(self) == self.solution

    def prune_history(self):
        to_remove = []
        index = 0
        while index < len(self.history) - 1:
            # remove consecutive moves that are reverses
            if self.history[index] == self.history[index + 1].reverse():
                to_remove.extend([index, index + 1])
                index += 2
            else:
                index += 1
        for index in reversed(to_remove):
            self.history.pop(index)

    def solve(self):
        # shorten history where possible
        self.prune_history()
        # start from the most recent move
        for move in reversed(self.history):
            reversal = move.reverse()
            # make reverse move
            self.move(reversal)

    def show_history(self):
        for move in self.history:
            print(move)

    def draw_square(self, screen, x, y, color):
        # space
        if (x, y) == self.space:
            color = self.SPACE_COLOR
            if self.is_solved():
                color = self.SOLVED_COLOR
        # border
        pygame.draw.rect(screen, self.BORDER_COLOR, (y * self.TILE_SIZE, x * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE), self.BORDER_WIDTH)
        # background
        pygame.draw.rect(screen, color, (y * self.TILE_SIZE, x * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE), 0)
        # text
        myfont = pygame.font.SysFont('Times New Roman', self.TEXT_SIZE)
        textsurface = myfont.render(self.board[x][y], False, self.TEXT_COLOR)
        margin = (self.TILE_SIZE - self.TEXT_SIZE) // 2
        screen.blit(textsurface, (margin + self.TILE_SIZE * y, margin + self.TILE_SIZE * x))

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                number = self.board[x][y]
                # ignore space
                color = 'black'
                if number != ' ':
                    color = tuple([min(255, 255 * (int(number) + 5) // (self.width * self.height + 5))] * 3)  # shade of grey
                self.draw_square(screen, x, y, color)

    def show(self):
        """ Displays a puzzle graphically. """
        pygame.init()
        pygame.display.set_caption('Show 15 puzzle position')
        #img = pygame.image.load('icon.png')
        #pygame.display.set_icon(img)
        pygame.font.init()
        screen = pygame.display.set_mode((self.TILE_SIZE * self.width, self.TILE_SIZE * self.height))
        self.draw(screen)
        pygame.display.update()
        running = True
        while running:
            keys = pygame.key.get_pressed()
            redraw_needed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        # quit
                        running = False

    def play(self):
        pygame.init()
        pygame.display.set_caption('15 puzzle')
        pygame.font.init()
        pygame.mixer.init()
        #move_sound = pygame.mixer.Sound('move.wav')
        screen = pygame.display.set_mode((self.TILE_SIZE * self.height, self.TILE_SIZE * self.width))
        #img = pygame.image.load('icon.png')
        #pygame.display.set_icon(img)
        running = True
        initial_position = True
        while running:
            keys = pygame.key.get_pressed()
            redraw_needed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # mouse handling
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == self.LEFT_CLICK:
                        # start of displacement
                        pygame.mouse.get_rel()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == self.LEFT_CLICK:
                        # end of displacement
                        movement = pygame.mouse.get_rel()
                        displacement = Direction(*movement)
                        self.move(closest_direction(displacement, list(self.MOVES.values())))
                        redraw_needed = True
                # key handling
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        # quit
                        running = False
                    elif event.key == pygame.K_SPACE:
                        # screenshot
                        pygame.image.save(screen, "capture.png")
                    elif event.key == pygame.K_h:
                        # history
                        self.show_history()
                    elif event.key == pygame.K_r:
                        # shuffle
                        self.shuffle(self.SHUFFLE_COUNT)
                        redraw_needed = True
                    elif event.key == pygame.K_s:
                        # solve
                        self.solve()
                        redraw_needed = True
                    # movement
                    elif event.key == pygame.K_UP:
                        redraw_needed = self.move(self.MOVES['up'])
                    elif event.key == pygame.K_DOWN:
                        redraw_needed = self.move(self.MOVES['down'])
                    elif event.key == pygame.K_LEFT:
                        redraw_needed = self.move(self.MOVES['left'])
                    elif event.key == pygame.K_RIGHT:
                        redraw_needed = self.move(self.MOVES['right'])
            if initial_position or redraw_needed:
                # draw puzzle
                self.draw(screen)
                pygame.display.update()
                # play sound
                #move_sound.play()
            initial_position = False
        pygame.quit()


if __name__ == '__main__':
    p = Puzzle(5, 5)
    p.play()
