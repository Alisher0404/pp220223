import pygame

pygame.init()

win_width = 800
win_height = 400
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_pos = [win_width // 2, win_height // 2]

white = (255, 255, 255)
red = (255, 0, 0)

def draw_ball():
    pygame.draw.circle(win, red, ball_pos, ball_radius)

ok = True
while ok:

    win.fill(white)

    draw_ball()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_pos[1] - 20 >= ball_radius:
                    ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                if ball_pos[1] + 20 <= win_height - ball_radius:
                    ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                if ball_pos[0] - 20 >= ball_radius:
                    ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_pos[0] + 20 <= win_width - ball_radius:
                    ball_pos[0] += 20

# pygame.quit()