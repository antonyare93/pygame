import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dim_std = 30

player1_pos = pygame.Vector2(dim_std , screen.get_height()/2)
player2_pos = pygame.Vector2(screen.get_width() - dim_std, screen.get_height()/2)
ball_pos = pygame.Vector2(player1_pos.x + 3.0 * dim_std, player1_pos.y + dim_std/2)
ball_running = False # Ball is quiet
ball_direction = ["down", "right"] # [down, left] or [up, right] or [up, left]
player1_scores: int = 0
player2_scores: int = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, "white", pygame.Rect(player1_pos.x, player1_pos.y - dim_std , dim_std * 1.0, dim_std * 3.0))
    pygame.draw.rect(screen, "white", pygame.Rect(player2_pos.x - dim_std, player2_pos.y - dim_std, dim_std * 1.0, dim_std * 3.0))
    if not ball_running:
        ball_pos = pygame.Vector2(player1_pos.x + 3.0 * dim_std, player1_pos.y + dim_std/2)

    pygame.draw.circle(screen, "white", ball_pos, dim_std)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player1_pos.y >= 2 * dim_std:
            player1_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        if player1_pos.y <= screen.get_height() - 4 * dim_std:
            player1_pos.y += 300 * dt
    if keys[pygame.K_UP]:
        if player2_pos.y >= 2 * dim_std:
            player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        if player2_pos.y <= screen.get_height() - 4 * dim_std:
            player2_pos.y += 300 * dt
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        ball_running = True

    if ball_running:
        if "down" in ball_direction:
            if ball_pos.y <= screen.get_height() - 2 * dim_std:
                ball_pos.y += 300 * dt
            else:
                ball_direction[0] = "up"
                ball_pos.y -= 300 * dt
        elif "up" in ball_direction:
            if ball_pos.y >= 2 * dim_std:
                ball_pos.y -= 300 * dt
            else:
                ball_direction[0] = "down"
                ball_pos.y += 300 * dt
        if "right" in ball_direction:
            if ball_pos.x < player2_pos.x - 2 * dim_std:
                ball_pos.x += 300 * dt
            elif ball_pos.x < player2_pos.x - dim_std and ball_pos.y >= player2_pos.y and ball_pos.y <= player2_pos.y + 3 * dim_std:
                ball_direction[1] = "left"
                ball_pos.x -= 300 * dt
            else:
                ball_running = not ball_running
        elif "left" in ball_direction:
            if ball_pos.x > player1_pos.x + 3 * dim_std:
                ball_pos.x -= 300 * dt
            elif ball_pos.x > player1_pos.x + 2 * dim_std and ball_pos.y >= player1_pos.y and ball_pos.y <= player1_pos.y + 3 * dim_std:
                ball_direction[1] = "right"
                ball_pos.x += 300 * dt
            else:
                ball_running = not ball_running



    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()