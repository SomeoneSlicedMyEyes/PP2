import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MUSIC_DIR = r'C:\Музыка'
BACKGROUND_IMAGE = os.path.join(MUSIC_DIR, "IMAGEFORPLAYER.png")

def load_music_files():
    music_files = []
    for file in os.listdir(MUSIC_DIR):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(MUSIC_DIR, file))
    return music_files

def play_music(music_files, index, position=0):
    pygame.mixer.music.load(music_files[index])
    pygame.mixer.music.play(start=position)

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_music(music_files, index):
    index = (index + 1) % len(music_files)
    return index

def prev_music(music_files, index):
    index = (index - 1) % len(music_files)
    return index

def update_volume(direction):
    volume = pygame.mixer.music.get_volume()
    if direction == "up":
        volume = min(1.0, volume + 0.1)
    elif direction == "down":
        volume = max(0.0, volume - 0.1)
    pygame.mixer.music.set_volume(volume)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Music Player")

    music_files = load_music_files()
    current_index = 0

    pygame.mixer.init()

    background_image = pygame.image.load(BACKGROUND_IMAGE)
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.SysFont("Arial", 24)

    running = True
    playing = False
    paused = False
    pause_time = 0
    while running:
        volume = pygame.mixer.music.get_volume() * 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused:
                        unpause_music()
                        paused = False
                    elif playing:
                        pause_music()
                        paused = True
                    else:
                        play_music(music_files, current_index)
                        playing = True
                elif event.key == pygame.K_RIGHT:
                    current_index = next_music(music_files, current_index)
                    if playing:
                        stop_music()
                        play_music(music_files, current_index)
                elif event.key == pygame.K_LEFT:
                    current_index = prev_music(music_files, current_index)
                    if playing:
                        stop_music()
                        play_music(music_files, current_index)
                elif event.key == pygame.K_UP:
                    update_volume("up")
                elif event.key == pygame.K_DOWN:
                    update_volume("down")

        screen.blit(background_image, (0, 0))

        current_track_text = font.render(os.path.basename(music_files[current_index]), True, WHITE)
        current_track_rect = current_track_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(current_track_text, current_track_rect)

        volume_text = font.render("Volume: {:.1f}".format(volume), True, WHITE)
        volume_rect = volume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(volume_text, volume_rect)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
