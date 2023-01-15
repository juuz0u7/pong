import pygame


player = pygame.Rect(10, SCREEN_HEIGHT // 2, 10, 100)
bot = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)


customButton1 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 5, 400, 100, 'Игра против компьютера',
                       myFunction)
customButton2 = Button(SCREEN_WIDTH // 3.75, SCREEN_HEIGHT // 2, 400, 100, 'Игра против друга', myFunction)

PP_surf = pygame.image.load("image/PB.jpg")
PP_surf = pygame.transform.scale(PP_surf, (PP_surf.get_width() // 15, PP_surf.get_height() // 15))

PP_rect = PP_surf.get_rect()
PP_rect.center = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
