import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Dragon Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('data/skyimg.jpeg')
sky_surface = pygame.transform.scale(sky_surface, (1000, 600))

ground_surface = pygame.image.load('data/ground.jpeg')
ground_surface = pygame.transform.scale(ground_surface, (1000, 200))

dragon_surface = pygame.image.load("data/dragon.png")
dragon_surface = pygame.transform.scale(dragon_surface, (150, 150))

player_surface = pygame.image.load("data/player.png")
player_surface = pygame.transform.scale(player_surface, (150, 150))

font = pygame.font.Font(None, 50)

ground_y = 700
player_gravity = 0

player_rect = player_surface.get_rect()
player_rect.midbottom = (150, ground_y)

dragon_rect = dragon_surface.get_rect()
dragon_rect.midbottom = (1000, ground_y)

dragon_speed = 12
score = 0
dragon_passed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 700:
                player_gravity = -25
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 700:
            player_gravity = -25

    dragon_rect.x -= dragon_speed

    if dragon_rect.right < player_rect.left and not dragon_passed:
        score += 1
        dragon_passed = True

    if dragon_rect.right < 0:
        dragon_rect.left = 1000
        dragon_passed = False

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 700:
        player_rect.bottom = 700
        player_gravity = 0

    smaller_player_rect = player_rect.inflate(-40, -40)
    smaller_dragon_rect = dragon_rect.inflate(-40, -40)

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))

    score_surface = font.render(f"Score: {score}", False, "white")
    score_rect = score_surface.get_rect(center=(500, 30))
    screen.blit(score_surface, score_rect)

    screen.blit(player_surface, player_rect)
    screen.blit(dragon_surface, dragon_rect)

    if smaller_player_rect.colliderect(smaller_dragon_rect):
        screen.fill((0, 0, 0))
        final_score_surface = font.render(f"Game Over! Score: {score}", False, "white")
        final_score_rect = final_score_surface.get_rect(center=(500, 400))
        screen.blit(final_score_surface, final_score_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)