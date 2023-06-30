import pygame, sys
from player import Player
from obstacle import Block
import obstacle
from alien import Alien

class Game:
    def __init__(self):
        # player setup
        player_sprite = Player((screen_width/2,screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amout = 4
        self.obstacle_x_positions = [num * (screen_width/self.obstacle_amout) for num in range(self.obstacle_amout)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=screen_width/15, y_start=480)

        #Alien
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241,79,80),x,y)
                    self.blocks.add(block)
    
    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start,offset_x)

    def alien_setup(self, rows, cols):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index
                y = row_index
                alien_sprite = Alien('red',x,y)
                self.aliens.add(alien_sprite)

    def run(self):
        self.player.update()

        self.player.draw(screen)
        self.player.sprite.laser.draw(screen)

        self.blocks.draw(screen)
        self.aliens.draw(screen)
        #update all sprite group
        #draw all sprite group

if __name__=='__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((30,30,30))
        game.run()

        pygame.display.update()
        clock.tick(60)