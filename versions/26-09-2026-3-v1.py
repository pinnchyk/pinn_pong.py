import pygame
import random
import math

pygame.init()
windowSurf = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
bgSurf = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf0 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf1 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf2 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf3 = pygame.Surface((1280, 720), pygame.SRCALPHA)
clock = pygame.time.Clock()
running = 1
dt = 0
p1_blockCD = 0
p2_blockCD = 0
p1_speed = 250
p2_speed = 250
ball_iv = 250
p1_pos = pygame.Vector2(0, (windowSurf.get_height() / 2) - 125)
p2_pos = pygame.Vector2(windowSurf.get_width() - 15, (windowSurf.get_height() / 2) - 125)
scrCenter = (windowSurf.get_width() / 2, windowSurf.get_height() / 2)
ball_size = [20,20]
ball_pos = pygame.Vector2(scrCenter[0] - (ball_size[0] / 2), scrCenter[1] - (ball_size[1] / 2))
if random.randint(1,2) == 1:
    ball_v = pygame.Vector2(-ball_iv, random.randint(-150,150))
else:
    ball_v = pygame.Vector2(ball_iv, random.randint(-150,150))
lastHit = 0
bounceCD = 0
bounceCDl = 0.6
score = [0,0]
grid1LinesSepparation = 100
grid2LinesSepparation = 130
grid1Thickness = 9
grid2Thickness = 7
grid1Color = [255, 0, 255, 4]
grid2Color = [255, 0, 255, 6]
grid1OscilationSpeed = 2
grid2OscilationSpeed = 2
gridProjectionDist = [0, 30]
ballBounceBoost = 1.2
ballParryBoost = 1.04




while running == 1:
    # check if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    # overlay a color over old frame
    pygame.draw.rect(drawSurf2, (0,0,0,30), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
    pygame.draw.rect(drawSurf0, (0,0,0,3), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

    ### cool grid background thingie
    gridSineOffset = math.sin(pygame.time.get_ticks() * grid1OscilationSpeed / 5000)
    i = -15
    while i < 15:
        pygame.draw.line(drawSurf0, grid1Color, (0.66 * windowSurf.get_width() * gridSineOffset - (0.66 * windowSurf.get_width()), -0.85 * windowSurf.get_height() + (grid1LinesSepparation * i)), (windowSurf.get_width() + 1.3 * windowSurf.get_height(), windowSurf.get_height() + 600 + (grid1LinesSepparation * i)), grid1Thickness + 2)
        pygame.draw.line(drawSurf0, grid1Color, (-300 + (grid1LinesSepparation * i), 900 * gridSineOffset + 1800), (windowSurf.get_height() + 300 + (grid1LinesSepparation * i), -windowSurf.get_width() - 900), grid1Thickness - 2)
        i += 1
    gridSineOffset = math.sin((pygame.time.get_ticks() + 4000) * grid2OscilationSpeed / 5000)
    i = -15
    while i < 15:
        pygame.draw.line(drawSurf0, grid2Color, (-0.66 * windowSurf.get_width() * gridSineOffset - (0.66 * windowSurf.get_width()) + gridProjectionDist[0], gridSineOffset * 0.85 * windowSurf.get_height() + (grid2LinesSepparation * i) + gridProjectionDist[1]), (windowSurf.get_width() + 3 * windowSurf.get_height() + gridProjectionDist[0], windowSurf.get_height() + (gridSineOffset / 16)*(grid2LinesSepparation * i) + gridProjectionDist[1]), grid2Thickness + 2)
        pygame.draw.line(drawSurf0, grid2Color, (-300 + (grid2LinesSepparation * i), 900 * gridSineOffset + 1800), (windowSurf.get_height() + 300 + (grid2LinesSepparation * i), -windowSurf.get_width() - 900), grid2Thickness - 2)
        i += 1

    # render players' parry trails
    if p1_blockCD > 0:
        if p1_blockCD >= 0.9:
            pygame.draw.rect(drawSurf2, (255,0,0,50), [0, p1_pos.y - 10, 25, 270], 0)
        elif p1_blockCD >= 0.85:
            pygame.draw.rect(drawSurf2, (255,0,0,20), [0, p1_pos.y - 10, 25, 270], 0)
        elif p1_blockCD >= 0.75:
            pygame.draw.rect(drawSurf2, (255,0,0,10), [0, p1_pos.y - 15, 35, 290], 0)
        elif p1_blockCD >= 0.6:
            pygame.draw.rect(drawSurf2, (255,0,0,5), [0, p1_pos.y - 25, 40, 310], 0)
        p1_blockCD -= 0.01
    if p2_blockCD > 0:
        if p2_blockCD >= 0.9:
            pygame.draw.rect(drawSurf2, (0,0,255,50), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
        elif p2_blockCD >= 0.85:
            pygame.draw.rect(drawSurf2, (0,0,255,20), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
        elif p2_blockCD >= 0.75:
            pygame.draw.rect(drawSurf2, (0,0,255,10), [windowSurf.get_width() - 25, p2_pos.y - 15, 35, 290], 0)
        elif p2_blockCD >= 0.6:
            pygame.draw.rect(drawSurf2, (0,0,255,5), [windowSurf.get_width() - 25, p2_pos.y - 25, 40, 310], 0)
        p2_blockCD -= 0.01

    # take input from players and render first frame of their parry and them too
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        if p1_blockCD <= 0:
            p1_blockCD = 1
            pygame.draw.rect(drawSurf2, (255,255,255,255), [0, p1_pos.y - 10, 25, 270], 0)
    pygame.draw.rect(drawSurf2, (255,200,200), [0, p1_pos.y, 15, 250], 0)

    if keys[pygame.K_w]:
        if p1_pos.y > 0:
            p1_pos.y -= p1_speed * dt
    if keys[pygame.K_d]:
        if p1_pos.y < windowSurf.get_height() - 250:
            p1_pos.y += p1_speed * dt


    if keys[pygame.K_o]:
        if p2_blockCD <= 0:
            p2_blockCD = 1
            pygame.draw.rect(drawSurf2, (255,255,255,255), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
    pygame.draw.rect(drawSurf2, (200,200,255), [windowSurf.get_width() - 15, p2_pos.y, 15, 250], 0)
    
    if keys[pygame.K_p]:
        if p2_pos.y > 0:
            p2_pos.y -= p2_speed * dt
    if keys[pygame.K_l]:
        if p2_pos.y < windowSurf.get_height() - 250:
            p2_pos.y += p2_speed * dt

    #### SirBall physics/render
    if bounceCD > 0:
        bounceCD -= bounceCDl * dt

    # create SirBall's trail, depending on the last player that hit them
    if lastHit != 0:
        if lastHit < 0:
            if lastHit > 0.05:
                lastHit = 0
            else:
                pygame.draw.rect (drawSurf2, (255 * abs(lastHit),70 * abs(lastHit),0,255), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)
                lastHit += 0.05
        elif lastHit > 0:
            if lastHit < 0.05:
                lastHit = 0
            else:
                pygame.draw.rect (drawSurf2, (0,100 * lastHit,255 * lastHit,255), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)
                lastHit -= 0.05
    else:
        pygame.draw.rect (drawSurf2, (255,255,255,0), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)
    ball_pos.x += ball_v.x * dt
    ball_pos.y += ball_v.y * dt

    # check for player collision
    if ball_pos.x <= 15:
        if ball_pos.y >= p1_pos.y - ball_size[1] and ball_pos.y <= p1_pos.y + 250:
            if p1_blockCD >= .7:
                ball_v.x = -ballParryBoost * ball_v.x
                ball_v.y = ballParryBoost * ball_v.y + (((ball_pos.y - p1_pos.y) - 125) * 1.5)
                lastHit = -1
                pygame.draw.rect (drawSurf2, (255,200,200,255), [ball_pos.x - (ball_size[0] / 2), ball_pos.y - (ball_size[1] / 2), ball_size[0] * 2, ball_size[1] * 2], 0)
            else:
                ball_v.x = -ballBounceBoost * ball_v.x
                ball_v.y = ball_v.y + (((ball_pos.y - p1_pos.y) - 125) * 0.1)
                lastHit = -0.5
            bounceCD = bounceCDl

    if ball_pos.x >= (windowSurf.get_width() - 30):
        if ball_pos.y >= p2_pos.y - ball_size[1] and ball_pos.y <= p2_pos.y + 250:
            if p2_blockCD >= .7:
                ball_v.x = -ballParryBoost * ball_v.x
                ball_v.y = ballParryBoost * ball_v.y + (((ball_pos.y - p2_pos.y) - 125) * 1.5)
                lastHit = 1
                pygame.draw.rect (drawSurf2, (200,200,255,255), [ball_pos.x - (ball_size[0] / 2), ball_pos.y - (ball_size[1] / 2), ball_size[0] * 2, ball_size[1] * 2], 0)
            else:
                ball_v.x = -ballBounceBoost * ball_v.x
                ball_v.y = ball_v.y + (((ball_pos.y - p2_pos.y) - 125) * 0.1)
                lastHit = 0.5
            bounceCD = bounceCDl

    # check if SirBall is out of bounds, if so, bring back and add to score
    if ball_pos.x < 0:
        ball_pos.x = scrCenter[0] - (ball_size[0] / 2)
        ball_pos.y = scrCenter[1] - (ball_size[1] / 2)
        score[1] += 1
        print(score)
        ball_v.x = ball_iv
        ball_v.y = random.randint(-150,150)
    if ball_pos.x > windowSurf.get_width():
        ball_pos.x = scrCenter[0] - (ball_size[0] / 2)
        ball_pos.y = scrCenter[1] - (ball_size[1] / 2)
        score[0] += 1
        print(score)
        ball_v.x = -ball_iv
        ball_v.y = random.randint(-150,150)

    if ball_pos.y >= windowSurf.get_height() - ball_size[1] or ball_pos.y <= 0:
        ball_pos.y = (windowSurf.get_height() + (ball_pos.y - windowSurf.get_height()))
        ball_v.y = -ball_v.y
    if lastHit < -0.5:
        pygame.draw.rect (drawSurf2, (255,0,0,255), [ball_pos.x - (ball_size[0] / 2), ball_pos.y - (ball_size[1] / 2), ball_size[0] * 2, ball_size[1] * 2], 0)
    if lastHit > 0.5:
        pygame.draw.rect (drawSurf2, (0,0,255,255), [ball_pos.x - (ball_size[0] / 2), ball_pos.y - (ball_size[1] / 2), ball_size[0] * 2, ball_size[1] * 2], 0)
    pygame.draw.rect (drawSurf2, (255,255,255), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)

    # present the surfaces
    windowSurf.blit(bgSurf, (0,0))
    windowSurf.blit(drawSurf0, (0,0))
    windowSurf.blit(drawSurf1, (0,0))
    windowSurf.blit(drawSurf2, (0,0))
    windowSurf.blit(drawSurf3, (0,0))
    pygame.display.update()

    # somehow determines the tps????? like, okay??
    dt = clock.tick(60) / 1000

pygame.quit()