import pygame
import random
import pygame.freetype
import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
print("hello")
print("hello")
print('Hello')
def move_player():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def move_ball(dx, dy):
    global FPS, pause_len
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        dy = -dy

    if ball.colliderect(player) and dx < 0:
        pong.play()
        if abs(ball.left - player.right) < 10:
            dx = -dx
            FPS += 10
        elif abs(ball.top - player.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(player.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    if ball.colliderect(bot) and dx > 0:
        pong.play()
        if abs(ball.right - bot.left) < 10:
            dx = -dx
            FPS += 10
        elif abs(ball.top - bot.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(bot.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    now = pygame.time.get_ticks()
    if now - score_time > pause_len and not is_over:
        ball.x += dx
        ball.y += dy

    return dx, dy


def restart_ball(dx, dy):
    ball.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    dx = random.choice((random.randint(-ball_max_speed, -3),
                        random.randint(3, ball_max_speed)))
    dy = random.choice((random.randint(-ball_max_speed, -3),
                        random.randint(3, ball_max_speed)))

    return dx, dy


def move_bot():
    if ball.centerx > SCREEN_WIDTH // 2 and ball_dx > 0:
        if ball.top >= bot.bottom:
            bot.y += bot_speed
        if ball.bottom <= bot.top:
            bot.y -= bot_speed


def win_or_lose():
    if player_score == win_score:
        win.play()
    elif bot_score == win_score:
        lose.play()
    else:
        score.play()


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()  # (x, y)

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    global state_menu, state_1
    state_menu = False
    state_1 = True


state_menu = True
state_1 = False

start_game = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
icon = pygame.image.load("ping_pong.ico")
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)

main_font = pygame.freetype.Font(None, 42)
font = pygame.font.SysFont('Arial', 40)

objects = []

player = pygame.Rect(10, SCREEN_HEIGHT // 2, 10, 100)
bot = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)

player_speed = 0
bot_speed = 9
ball_max_speed = 9
ball_dx, ball_dy = -9, 9

score_time = 0
pause_len = 1000

BG_COLOR = (255, 255, 255)
PADDLE_COLOR = (0, 0, 0)
FPS = 60

player_score = 0
bot_score = 0
win_score = 1
is_over = False

pong = pygame.mixer.Sound("pong.wav")
score = pygame.mixer.Sound("score.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")

customButton1 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 5, 400, 100, 'Игра против компьютера', myFunction)
customButton2 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 2, 400, 100, 'Игра против друга', myFunction)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and is_over:
                is_over = False
                player_score, bot_score = 0, 0
                score_time = pygame.time.get_ticks()
            if event.key == pygame.K_w:
                player_speed -= 7
            if event.key == pygame.K_s:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7

    if state_1:
        move_player()
        move_bot()
        ball_dx, ball_dy = move_ball(ball_dx, ball_dy)

    if ball.right <= 0:
        bot_score += 1
        win_or_lose()
        ball_dy *= -1
        if bot_score == win_score:
            is_over = True
    if ball.left >= SCREEN_WIDTH:
        player_score += 1
        win_or_lose()
        ball_dy *= 1
        if player_score == win_score:
            is_over = True

    if ball.right <= 0 or ball.left >= SCREEN_WIDTH:
        ball_dx, ball_dy = restart_ball(ball_dx, ball_dy)

    screen.fill(BG_COLOR)

    if state_1:
        main_font.render_to(screen, (330, 25), str(player_score))
        main_font.render_to(screen, (550, 25), str(bot_score))
        pygame.draw.rect(screen, PADDLE_COLOR, player)
        pygame.draw.rect(screen, PADDLE_COLOR, bot)
        pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
        pygame.draw.line(screen, PADDLE_COLOR, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), width=3)

    if is_over:
        screen.fill(BG_COLOR)
        main_font.render_to(screen, (260, 200), "Game over, Press F")

    if state_menu:
        for object in objects:
            object.process()
    elif start_game:
        start_game = False

    clock.tick(FPS)
    pygame.display.update()
