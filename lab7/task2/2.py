import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))

music_files = ["music1.wav", "music2.wav", "music3.wav"]
current_song = 0

pygame.mixer.music.load(music_files[current_song])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()

    pygame.display.update()