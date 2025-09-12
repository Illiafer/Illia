class Player:
    def __init__(self):
        self.image = dino_img
        self.rect = make_rect_for_midbottom(self.image, 120, GROUND_Y)
        self.vel_y = 0
        self.gravity = 0.7
        self.jump_power = -14
        self.in_air = False

    def input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.in_air:
            self.vel_y = self.jump_power
            self.in_air = True

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += int(self.vel_y)
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.in_air = False

    def update(self):
        self.input()
        self.apply_gravity()

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class Cactus:
    def __init__(self):
        self.image = random.choice(cactus_imgs)
        self.rect = make_rect_for_midbottom(self.image, WIDTH + 50, GROUND_Y)

    def update(self):
        self.rect.x -= SPEED

    def draw(self, surf):
        surf.blit(self.image, self.rect)
