import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino — Template")
clock = pygame.time.Clock()

GROUND_Y = 420
SPEED = 7

# картинкиdino_img = pygame.image.load("DinoRun1.png").convert_alpha()
cactus_imgs = [
    pygame.image.load("SmallCactus1.png").convert_alpha(),
    pygame.image.load("SmallCactus2.png").convert_alpha()
]
track_img = pygame.image.load("Track.png").convert_alpha()



def make_rect_for_midbottom(img, mid_x, bottom_y):
    w, h = img.get_width(), img.get_height()
    x = int(mid_x - w // 2)
    y = int(bottom_y - h)
    return pygame.Rect(x, y, w, h)


# ================= Player =================
class Player:
    def __init__(self):
        self.image = dino_img
        self.rect = make_rect_for_midbottom(self.image, 120, GROUND_Y)
        self.vel_y = 0
        self.gravity = 0.7
        self.jump_power = -14
        self.in_air = False

    def input(self):
        # TODO: зробити стрибок, якщо натиснуто пробіл або ↑ і гравець не в повітрі
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.in_air:
            self.vel_y = self.jump_power
            self.in_air = True


    def apply_gravity(self):
        # TODO: додати гравітацію до швидкості
        # TODO: змінити координату динозавра по Y
        # TODO: перевірити, щоб він не провалювався нижче землі
        self.vel_y+=self.gravity
        self.rect.y+=int(self.vel_y)
        if self.rect.bottom>=GROUND_Y:
            self.rect.bottom=GROUND_Y
            self.vel_y=0
            self.in_air=False

    def update(self):
        self.input()
        self.apply_gravity()

    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))


# ================= Cactus =================
class Cactus:
    def __init__(self):
        self.image = random.choice(cactus_imgs)
        self.rect = make_rect_for_midbottom(self.image, WIDTH + 50, GROUND_Y)

    def update(self):
        # TODO: рухати кактус вліво
        self.rect.x-=SPEED

    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))


# ================= Game =================
player = Player()
cacti = []
next_spawn_time = pygame.time.get_ticks() + random.randint(900, 1500)

score = 0
font = pygame.font.Font(None, 32)
game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.update()

        # обновлення кактусів
        for cactus in cacti[:]:
            cactus.update()
            if cactus.rect.right < 0:
                cacti.remove(cactus)

     
        now = pygame.time.get_ticks()
        if now >= next_spawn_time:
            if len(cacti) < 2:  # максимум 2 кактуси
                cacti.append(Cactus())
            next_spawn_time = now + random.randint(900, 1500)


        for cactus in cacti:
            if player.rect.colliderect(cactus.rect):
                game_over = True

        score += 1

    
    screen.fill((255, 255, 255))
    screen.blit(track_img, (0, GROUND_Y - 20))

 
    player.draw(screen)
    for cactus in cacti:
        cactus.draw(screen)

  
    txt = font.render(f"Score: {score // 10}", True, (40, 40, 40))
    screen.blit(txt, (10, 10))

    if game_over:
        msg = font.render("Game Over — SPACE to restart", True, (200, 40, 40))
        msg_x = WIDTH // 2 - msg.get_width() // 2
        msg_y = 60
        screen.blit(msg, (msg_x, msg_y))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player = Player()
            cacti = []
            score = 0
            game_over = False
            next_spawn_time = pygame.time.get_ticks() + random.randint(900, 1500)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
