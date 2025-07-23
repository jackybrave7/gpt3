import pygame
import sys

# Game constants
WIDTH, HEIGHT = 800, 450
FPS = 60
GRAVITY = 1
JUMP_SPEED = -15
PLAYER_SPEED = 5
ATTACK_COOLDOWN = 500  # milliseconds
DAMAGE = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
BLUE = (30, 144, 255)


class Player:
    def __init__(self, x, controls, color):
        self.rect = pygame.Rect(x, HEIGHT - 120, 50, 100)
        self.color = color
        self.controls = controls
        self.velocity_y = 0
        self.on_ground = True
        self.health = 100
        self.last_attack = 0

    def handle_input(self, keys, current_time):
        if keys[self.controls['left']]:
            self.rect.x -= PLAYER_SPEED
        if keys[self.controls['right']]:
            self.rect.x += PLAYER_SPEED
        if self.on_ground and keys[self.controls['jump']]:
            self.velocity_y = JUMP_SPEED
            self.on_ground = False
        if keys[self.controls['attack']] and current_time - self.last_attack > ATTACK_COOLDOWN:
            self.last_attack = current_time
            return True
        return False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.bottom >= HEIGHT - 20:
            self.rect.bottom = HEIGHT - 20
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minimal Fighter")
        self.clock = pygame.time.Clock()
        self.players = [
            Player(150, {
                'left': pygame.K_a,
                'right': pygame.K_d,
                'jump': pygame.K_w,
                'attack': pygame.K_SPACE
            }, RED),
            Player(WIDTH - 200, {
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT,
                'jump': pygame.K_UP,
                'attack': pygame.K_RETURN
            }, BLUE)
        ]

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            attacks = []
            for player in self.players:
                if player.handle_input(keys, current_time):
                    attacks.append(player)

            for player in self.players:
                player.update()

            # Attack collision detection
            for attacker in attacks:
                for target in self.players:
                    if attacker is not target and attacker.rect.colliderect(target.rect.inflate(20, 20)):
                        target.health = max(0, target.health - DAMAGE)

            self.screen.fill(WHITE)
            pygame.draw.rect(self.screen, BLACK, (0, HEIGHT - 20, WIDTH, 20))
            for player in self.players:
                player.draw(self.screen)

            self.draw_health_bars()
            pygame.display.flip()

            if any(p.health == 0 for p in self.players):
                self.show_winner()
                running = False

        pygame.quit()
        sys.exit()

    def draw_health_bars(self):
        bar_width = 200
        bar_height = 20
        for index, player in enumerate(self.players):
            x = 20 if index == 0 else WIDTH - bar_width - 20
            pygame.draw.rect(self.screen, BLACK, (x, 20, bar_width, bar_height), 2)
            inner_width = bar_width * (player.health / 100)
            pygame.draw.rect(self.screen, player.color, (x + 2, 22, inner_width - 4, bar_height - 4))

    def show_winner(self):
        font = pygame.font.SysFont(None, 48)
        winner = "Red" if self.players[0].health > 0 else "Blue"
        text = font.render(f"{winner} wins!", True, BLACK)
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)


if __name__ == "__main__":
    Game().run()

