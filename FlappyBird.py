import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
PIPE_WIDTH = 60
PIPE_HEIGHT = 500
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_SPEED = 3
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill(BLUE)

# Font for score
font = pygame.font.SysFont("Arial", 32)

# Bird class
class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity

        # Prevent bird from going out of bounds
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - BIRD_HEIGHT:
            self.y = SCREEN_HEIGHT - BIRD_HEIGHT

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self, surface):
        surface.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.top = self.height
        self.bottom = self.height + PIPE_GAP

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, 0, PIPE_WIDTH, self.top))
        pygame.draw.rect(surface, GREEN, (self.x, self.bottom, PIPE_WIDTH, SCREEN_HEIGHT - self.bottom))

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top)
        bottom_rect = pygame.Rect(self.x, self.bottom, PIPE_WIDTH, SCREEN_HEIGHT - self.bottom)

        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

# Game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Update bird and pipes
        bird.update()

        # Add new pipe
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        # Update pipes
        for pipe in pipes:
            pipe.update()

        # Remove off-screen pipes
        if pipes[0].off_screen():
            pipes.pop(0)

        # Check for collisions
        for pipe in pipes:
            if pipe.collide(bird):
                running = False

        # Update score
        for pipe in pipes:
            if pipe.x + PIPE_WIDTH < bird.x and not hasattr(pipe, "scored"):
                score += 1
                pipe.scored = True

        # Draw everything
        screen.fill(WHITE)
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.flip()

    # Game Over
    game_over_text = font.render("Game Over", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

    pygame.quit()

if __name__ == "__main__":
    main()
