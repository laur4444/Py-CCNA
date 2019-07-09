import pygame
import random
from pygame.locals import *

class Ship():

    def __init__(self, window):

        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        self.rect.bottom = window.bottom
        self.rect.centerx = window.centerx

        self.move_x = 0

        self.shots = []
        self.shots_count = 0

        self.max_shots = 2

        self.score = 0

    def event_handler(self, event):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.move_x = -5
            elif event.key == K_RIGHT:
                self.move_x = 5
            elif event.key == K_SPACE:
                if len(self.shots) < self.max_shots:
                    self.shots.append(Bullet(self.rect.centerx, self.rect.top, 1, self.rect.bottom))

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                self.move_x = 0

    def update(self):

        self.rect.x += self.move_x

        for s in self.shots:
            s.update()

        for i in range(len(self.shots)-1, -1, -1):
            if not self.shots[i].is_alive:
                del self.shots[i]

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

        for s in self.shots:
            s.draw(screen)

    def bullet_detect_collison(self, enemy_list, effect):

        for s in self.shots:
            for e in enemy_list:
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    e.is_alive = False
                    self.score += 100

class Bullet():

    def __init__(self, x, y, direction, screen_height):

        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.direction = direction
        self.screen_height = screen_height

        self.is_alive = True


    def update(self):

        self.rect.y -= 15 * self.direction

        if self.rect.y < 0 or self.rect.y > self.screen_height:
            self.is_alive = False

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)


class Enemy_1():

    def __init__(self, x, y):

        # Load the image and rescale to fit the screen
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Set position on the screen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # When is_alive is False the enemy will auto-destroy
        self.is_alive = True

    def update(self):
        # Movement
        self.rect.y += 1

        # Destroy if outside the screen
        if self.rect.centery > pygame.display.get_surface().get_size()[1]:
            self.is_alive = False

    def draw(self, screen):
        # Draw the image
        screen.blit(self.image, self.rect.topleft)


class Enemy_2():

    def __init__(self, x, y, range):

        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # TODO 2 - Initialize class members


        self.is_alive = True

    def update(self):
        self.rect.y += 1

        # TODO 2 - Use class members to make object move left to right


        if self.rect.centery > pygame.display.get_surface().get_size()[1]:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Enemy_3():

    def __init__(self, x, y, range):

        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # TODO 3 - Initialize class members


        self.is_alive = True

    def update(self):

        self.rect.x += self.direction

        # TODO 3 - Use class members to make object move side to side and up down.
        # You may use other variables (globals)


        if self.rect.centery > pygame.display.get_surface().get_size()[1]:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Game():

    def __init__(self):

        pygame.init()

        width, height = 800, 800
        self.screen = pygame.display.set_mode((width, height))

        self.ship = Ship(self.screen.get_rect())

        self.enemies = []


        # TODO 2, 3 Spawn enemies here
        for i in range(100, 900, 200):
            self.enemies.append(Enemy_1(i, 100))


    # -----MAIN GAME LOOP-----

    def run(self):

        clock = pygame.time.Clock()


        # TODO 1 - Initialize mixer module and put the sound in "effect" variable
        effect = None



        global time
        time = 0

        RUNNING = True
        PAUSED = False

        while RUNNING:

            clock.tick(30)

            # --- events ---

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        RUNNING = False

                    if event.key == K_p:
                        PAUSED = not PAUSED

                if not PAUSED:
                    self.ship.event_handler(event)

            # --- updates ---

            if not PAUSED:
                time += 1
                self.ship.update()

                for e in self.enemies:
                    e.update()

                self.ship.bullet_detect_collison(self.enemies, effect)

                for i in range(len(self.enemies)-1, -1, -1):
                    if not self.enemies[i].is_alive:
                        del self.enemies[i]

            # TODO 4 - Put infinite generator code here



            # --- draws ---

            self.screen.fill((0,0,0))

            self.ship.draw(self.screen)

            for e in self.enemies:
                e.draw(self.screen)

            if PAUSED:
                self.screen.blit(self.text_paused, self.text_paused_rect)

            pygame.display.update()

        # --- quit ---
        print ("Score: ", self.ship.score)
        pygame.quit()

Game().run()
