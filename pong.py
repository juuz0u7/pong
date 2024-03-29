import random

from button import *
from other_variables import *

ball_dx, ball_dy = -5, 5
state_menu = True
state_menu2 = False
state_1 = False
state_2 = False

is_over = False


def move_player():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def move_player2():
    bot.y += player2_speed
    if bot.top <= 0:
        bot.top = 0
    if bot.bottom >= SCREEN_HEIGHT:
        bot.bottom = SCREEN_HEIGHT


def move_ball(dx, dy):
    global pause_len
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        dy = -dy

    if ball.colliderect(player) and dx < 0 and on_state_lvl1:
        pong.play()
        if abs(ball.left - player.right) < 10:
            dx = -dx
        elif abs(ball.top - player.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(player.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    if ball.colliderect(bot) and dx > 0:
        pong.play()
        if abs(ball.right - bot.left) < 10:
            dx = -dx
        elif abs(ball.top - bot.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(bot.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    now = pygame.time.get_ticks()
    if now - score_time > pause_len and not is_over and now - START_game > pause_len:
        ball.x += dx
        ball.y += dy

    return dx, dy


def restart_ball():
    ball.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    dx = random.choice((random.randint(-ball_max_speed, -ball_min_speed),
                        random.randint(ball_min_speed, ball_max_speed)))
    dy = random.choice((random.randint(-ball_max_speed, -ball_min_speed),
                        random.randint(ball_min_speed, ball_max_speed)))

    return dx, dy


def move_bot():
    if ball.centerx > SCREEN_WIDTH // 2 and ball_dx > 0:
        if ball.top >= bot.bottom:
            bot.y += bot_speed
        if ball.bottom <= bot.top:
            bot.y -= bot_speed


def move_bot2():
    if ball.centerx < SCREEN_WIDTH // 2 and ball_dx < 0:
        if ball.top >= player.bottom:
            player.y += bot_speed
        if ball.bottom <= player.top:
            player.y -= bot_speed


def win_or_lose():
    if state_2:
        win.play()
    elif player_score == win_score:
        win.play()
    elif bot_score == win_score:
        lose.play()
    else:
        score.play()


def on_state_menu_2():
    global state_menu, state_menu2, state_1, state_2
    state_menu = False
    state_menu2 = True
    state_1 = False
    state_2 = False


def on_state_lvl1():
    global state_menu, state_menu2, state_1, state_2, ball_max_speed, ball_min_speed, bot_speed, ball_dx, ball_dy
    ball_max_speed = 5
    ball_min_speed = 3
    bot_speed = 4
    ball_dx, ball_dy = restart_ball()
    state_menu = False
    state_menu2 = False
    state_1 = True
    state_2 = False


def on_state_lvl2():
    global state_menu, state_menu2, state_1, state_2, ball_max_speed, ball_min_speed, bot_speed, ball_dx, ball_dy
    ball_max_speed = 7
    ball_min_speed = 5
    bot_speed = 6
    ball_dx, ball_dy = restart_ball()
    state_menu = False
    state_menu2 = False
    state_1 = True
    state_2 = False


def on_state_lvl3():
    global state_menu, state_menu2, state_1, state_2, ball_max_speed, ball_min_speed, bot_speed
    ball_max_speed = 9
    ball_min_speed = 7
    bot_speed = 8
    state_menu = False
    state_menu2 = False
    state_1 = True
    state_2 = False


def on_state_2():
    global state_menu, state_1, state_2
    state_menu = False
    state_1 = False
    state_2 = True


player = pygame.Rect(10, SCREEN_HEIGHT // 2, 10, 100)
bot = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)

customButton1 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 5, 400, 100, 'Player VS PC', on_state_menu_2)
customButton2 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 2, 400, 100, 'Player VS Player', on_state_2)
customButtonlvl1 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT - 400, 400, 100, 'Easy', on_state_lvl1, True)
customButtonlvl2 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT - 300, 400, 100, 'Normal', on_state_lvl2, True)
customButtonlvl3 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT - 200, 400, 100, 'HARDCORE', on_state_lvl3, True)

PP_surf = pygame.image.load("image/PB.jpg")
PP_surf = pygame.transform.scale(PP_surf, (PP_surf.get_width() // 15, PP_surf.get_height() // 15))

PP_rect = PP_surf.get_rect()
PP_rect.center = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)

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
            if event.key == pygame.K_UP:
                player2_speed -= 7
            if event.key == pygame.K_DOWN:
                player2_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player2_speed += 7
            if event.key == pygame.K_DOWN:
                player2_speed -= 7

    # Физика игры
    if state_menu or state_menu2:  # Динамика меню
        move_bot2()
        move_bot()
        ball_dx, ball_dy = move_ball(ball_dx, ball_dy)
    elif state_1:
        move_player()
        move_bot()
        ball_dx, ball_dy = move_ball(ball_dx, ball_dy)
    elif state_2:
        move_player()
        move_player2()
        ball_dx, ball_dy = move_ball(ball_dx, ball_dy)

    # Изменение счёта
    if ball.right <= 0:
        score_time = pygame.time.get_ticks()
        bot_score += 1
        win_or_lose()
        ball_dy *= -1
        if bot_score == win_score:
            is_over = True
    if ball.left >= SCREEN_WIDTH:
        score_time = pygame.time.get_ticks()
        player_score += 1
        win_or_lose()
        ball_dy *= 1
        if player_score == win_score:
            is_over = True

    # Рестарт мяча после гола
    if ball.right <= 0 or ball.left >= SCREEN_WIDTH:
        ball_dx, ball_dy = restart_ball()

    screen.fill(BG_COLOR)
    # Отрисовки
    if state_menu:  # Рисуем меню
        for object in objects:
            object.process()
            if state_1:
                score_time = pygame.time.get_ticks()
                restart_ball()
        pygame.draw.rect(screen, PADDLE_COLOR, player)
        pygame.draw.rect(screen, PADDLE_COLOR, bot)
        pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
    elif state_menu2:
        for object in objects_lvl:
            object.process()
            if state_1:
                score_time = pygame.time.get_ticks()
                restart_ball()
        pygame.draw.rect(screen, PADDLE_COLOR, player)
        pygame.draw.rect(screen, PADDLE_COLOR, bot)
        pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
    elif state_1:
        main_font.render_to(screen, (330, 25), str(player_score))
        main_font.render_to(screen, (550, 25), str(bot_score))
        pygame.draw.rect(screen, PADDLE_COLOR, player)
        pygame.draw.rect(screen, PADDLE_COLOR, bot)
        pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
        pygame.draw.line(screen, PADDLE_COLOR, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), width=3)
        # screen.blit(PP_surf, PP_rect)
    elif state_2:
        main_font.render_to(screen, (330, 25), str(player_score))
        main_font.render_to(screen, (550, 25), str(bot_score))
        pygame.draw.rect(screen, PADDLE_COLOR, player)
        pygame.draw.rect(screen, PADDLE_COLOR, bot)
        pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
        pygame.draw.line(screen, PADDLE_COLOR, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), width=3)

    # Отрисовка конечного экрана
    if is_over:
        screen.fill(BG_COLOR)
        main_font.render_to(screen, (260, 200), "Game over, Press F")

    clock.tick(FPS)
    pygame.display.update()
