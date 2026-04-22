import pygame
import sys
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)
player = MusicPlayer("music/")

while True:
    screen.fill((0, 0, 0))

    screen.blit(font.render("Music Player", True, (116, 13, 46)), (50, 50))
    screen.blit(font.render(f"Music name: {player.get_current_track_name()}", True, (243, 239, 232)), (50, 150))
    screen.blit(font.render(f"Duration: {player.get_pos_str()}", True, (243, 239, 232)), (50, 200))
    screen.blit(font.render("(P)lay  (S)top  (N)ext  (B)ack  (Q)uit", True, (116, 13, 46)), (50, 320))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q: 
                pygame.quit(); sys.exit()

    pygame.display.flip()
    clock.tick(30)