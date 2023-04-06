import pygame
pygame.init()


width = 640
height = 480
screen = pygame.display.set_mode((width, height))


pygame.display.set_caption('Pygame Paint')


brush_color = pygame.Color('black')
brush_thickness = 5


shape = 'rectangle'


drawing_surface = pygame.Surface((width, height))
drawing_surface.fill(pygame.Color('white'))


def draw_shape(start_pos, end_pos):
    if shape == 'rectangle':
        pygame.draw.rect(drawing_surface, brush_color, (start_pos, end_pos), brush_thickness)
    elif shape == 'circle':
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
        center = (start_pos[0] + radius, start_pos[1] + radius)
        pygame.draw.circle(drawing_surface, brush_color, center, radius, brush_thickness)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_pos = event.pos
                draw_shape(start_pos, end_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_e:
                brush_color = pygame.Color('white')
                shape = 'erase'
            elif event.key == pygame.K_b:
                brush_color = pygame.Color('black')
                shape = 'brush'
            elif event.key == pygame.K_g:
                brush_color = pygame.Color('green')
            elif event.key == pygame.K_y:
                brush_color = pygame.Color('yellow')
            elif event.key == pygame.K_p:
                brush_color = pygame.Color('purple')
            elif event.key == pygame.K_o:
                brush_color = pygame.Color('orange')

    screen.blit(drawing_surface, (0, 0))
    pygame.display.update()


pygame.quit()
