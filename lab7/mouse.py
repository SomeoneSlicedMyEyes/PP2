import pygame
import sys
import math
from datetime import datetime
import os

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Applications")

directory = "C:\\Visual Studio Code\\PP2\\PP2\\PP2\\lab7\\"

clock_face_img = pygame.image.load(os.path.join(directory, "mainclock.png"))
clock_face_img = pygame.transform.scale(clock_face_img, (int(clock_face_img.get_width() / 2), int(clock_face_img.get_height() / 1.5)))
mickey_left_img = pygame.image.load(os.path.join(directory, "leftarm.png"))
mickey_right_img = pygame.image.load(os.path.join(directory, "rightarm.png"))

scale_factor = 0.8
mickey_left_img = pygame.transform.scale(mickey_left_img, (int(mickey_left_img.get_width() * scale_factor), int(mickey_left_img.get_height() * scale_factor)))
mickey_right_img = pygame.transform.scale(mickey_right_img, (int(mickey_right_img.get_width() * scale_factor), int(mickey_right_img.get_height() * scale_factor)))

clock_x = (WINDOW_WIDTH - clock_face_img.get_width()) // 2
clock_y = (WINDOW_HEIGHT - clock_face_img.get_height()) // 2

hand_offset_y = -100

def draw_clock():
    window.blit(clock_face_img, (clock_x, clock_y))

    current_time = datetime.now()
    hour_angle = -(current_time.hour % 12) * (360 / 12) - (current_time.minute / 60) * (360 / 12)
    minute_angle = -current_time.minute * (360 / 60)

    mickey_left_rotated = pygame.transform.rotate(mickey_left_img, hour_angle)
    mickey_right_rotated = pygame.transform.rotate(mickey_right_img, minute_angle)

    mickey_left_pos = mickey_left_rotated.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.5 + hand_offset_y))
    mickey_right_pos = mickey_right_rotated.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.5 + hand_offset_y))

    window.blit(mickey_left_rotated, mickey_left_pos)
    window.blit(mickey_right_rotated, mickey_right_pos)

def main():
    running = True
    while running:
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_clock()

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
