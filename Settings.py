import pygame.freetype
import pygame.mixer
import pygame

pygame.init()

icon = pygame.image.load("ping_pong.ico")
pong = pygame.mixer.Sound("pong.wav")
score = pygame.mixer.Sound("score.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
START_game = 0
main_font = pygame.freetype.Font(None, 42)
font = pygame.font.SysFont('Arial', 40)
objects = []
objects_lvl = []
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)
button_time = 0

player = pygame.Rect(10, SCREEN_HEIGHT // 2, 10, 100)
bot = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)



PP_surf = pygame.image.load("image/PB.jpg")
PP_surf = pygame.transform.scale(PP_surf, (PP_surf.get_width() // 15, PP_surf.get_height() // 15))

PP_rect = PP_surf.get_rect()
PP_rect.center = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)