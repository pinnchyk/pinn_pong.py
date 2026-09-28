import pygame
import random
import math
from pathlib import Path

pygame.init()
pygame.mixer.init()
windowSurf = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
bgSurf = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf0 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf1 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf2 = pygame.Surface((1280, 720), pygame.SRCALPHA)
drawSurf3 = pygame.Surface((1280, 720), pygame.SRCALPHA)
clock = pygame.time.Clock()
gameState = "titleMenu"
running = 1
dt = 0
p1_blockCD = 0
p2_blockCD = 0
p1_speed = 250
p2_speed = 250
p1_bot = False
p2_bot = False
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
ballBounceBoost = 1.04
ballParryBoost =  1.2
introSeen = False
introLength = 5
programDirectory = str(Path(__file__).resolve().parent)
print(programDirectory)
mainMenuButtonSelection = 0
keyPressCD = 0
finalCountdown = 4
lastScored = 0


img_gameTitleV1 = pygame.image.load(programDirectory + "\\assets\\image\\gameTitleV1.png")
img_txt_playSoloMatch = pygame.image.load(programDirectory + "\\assets\\image\\txt_playSoloMatch.png")
img_txt_playSoloMatch = pygame.transform.scale(img_txt_playSoloMatch, (img_txt_playSoloMatch.get_width()/3,img_txt_playSoloMatch.get_height()/3))
img_txt_playDuoMatch = pygame.image.load(programDirectory + "\\assets\\image\\txt_playDuoMatch.png")
img_txt_playDuoMatch = pygame.transform.scale(img_txt_playDuoMatch, (img_txt_playDuoMatch.get_width()/3,img_txt_playDuoMatch.get_height()/3))
img_txt_settingsHelp = pygame.image.load(programDirectory + "\\assets\\image\\txt_settingsHelp.png")
img_txt_settingsHelp = pygame.transform.scale(img_txt_settingsHelp, (img_txt_settingsHelp.get_width()/3,img_txt_settingsHelp.get_height()/3))
img_txt_exitProgram = pygame.image.load(programDirectory + "\\assets\\image\\txt_exitProgram.png")
img_txt_exitProgram = pygame.transform.scale(img_txt_exitProgram, (img_txt_exitProgram.get_width()/3,img_txt_exitProgram.get_height()/3))

pygame.mixer.music.load(programDirectory + "\\assets\\audio\\ruderBuster_anotherVersion.mp3")
titleMusicStarted = False
roundMusicStarted = False
snd_roundStart = pygame.mixer.Sound(programDirectory + "\\assets\\audio\\roundStart.mp3")

splashTxtCount = 65
#splashTxtCountingDone = False
splashTxt = []
splashTxt_52sub1 = str(programDirectory + "\\assets\\image\\splashTxt\\52-1.png")

splash_i = 0
#while splash_i < splashTxtCount:
splashTxt.append(str(programDirectory + "\\assets\\image\\splashTxt\\" + str(splash_i + 1) + ".png"))
    #splash_i += 1
randomSplash = str(random.randint(1,splashTxtCount))
#   random.randint(1,splashTxtCount)

#while splashTxtCountingDone == False:
#    try:
#        splashTxt.append(str(programDirectory + "/assets/image/splashTxt/" + str(splashTxtCount + 1) + ".png"))
#        splashTxtCount += 1
#    except:
#        splashTxtCountingDone = True

def monochromeSurface(img,r,g,b,a):
    x = img.get_width()
    y = img.get_height()
    i = 1
    j = 1
    while j <= y:
        while i <= x:
            if img.get_at(x,y)[3] > 0:
                img.set_at((x,y), (r,g,b,a))
            x += 1


while running == 1:
    # check if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    if gameState == "end":
        pygame.draw.rect(drawSurf2, (0,0,0,2), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        pygame.draw.rect(drawSurf0, (0,0,0,1), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        finalCountdown -= dt
        pygame.mixer.music.stop()
        if finalCountdown < 0:
            running = 0


    if gameState == "titleMenu":
        ### INTRO to the main menuuu
        if introLength <= 5 and introLength >= 0.9:
            i = -2
            while i < 13:
                pygame.draw.line(drawSurf0, [255, 0, 0, 2], (-windowSurf.get_width()/4,(-windowSurf.get_height()/4) + i*grid1LinesSepparation), (windowSurf.get_width()*1.25,(-windowSurf.get_height()/4) + i*grid1LinesSepparation), 8)
                i += 1
        if introLength >= 0.9 and introLength <= 4:
            i = -2
            while i < 18:
                pygame.draw.line(drawSurf0, [0, 0, 255, 2], ((-windowSurf.get_width()/4) + i*grid1LinesSepparation,-windowSurf.get_height()/4), ((-windowSurf.get_width()/4) + i*grid1LinesSepparation,windowSurf.get_height()*1.25), 8)
                i += 1
        if introLength <= 1.8 and introLength >= 1.78:
            pygame.draw.rect(drawSurf2, (255,200,255,50), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        if introLength <= 1.78 and introLength >= 1.76:
            pygame.draw.rect(drawSurf2, (0,0,0,4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        if introLength <= 1.1 and introLength >= 1.08:
            pygame.draw.rect(drawSurf2, (255,200,255,150), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        if introLength <= 1.08 and introLength >= 1.06:
            pygame.draw.rect(drawSurf2, (0,0,0,4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        if introLength <= 0.45 and introLength >= 0.3:
            pygame.draw.rect(drawSurf2, (255,255,255,255), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

        if introLength <= 4.46:
            if titleMusicStarted == False:
                pygame.mixer.music.play(-1,0.0,3000)
                titleMusicStarted = True
        
        if introSeen == False:
            if introLength > 0:
                introLength -= dt
            else:
                introSeen = True
        else:
            pygame.draw.rect(drawSurf2, (0,0,0,20), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

            ### draw the main grid of the menu, WITH oscillation ofc
            gridSineOffset = math.sin(pygame.time.get_ticks() * grid1OscilationSpeed / 3000)
            i = -2
            while i < 13:
                pygame.draw.line(drawSurf2, [255, 0, 200, 2], ((-windowSurf.get_width()/4) * gridSineOffset - (windowSurf.get_width()/2),(-windowSurf.get_height()/4) + 1.4*i*grid1LinesSepparation), (windowSurf.get_width()*1.25,(-windowSurf.get_height()/4) + i*grid1LinesSepparation), 8)
                i += 1
            i = -2
            while i < 18:
                pygame.draw.line(drawSurf2, [200, 0, 255, 2], ((-windowSurf.get_width()/4) + i*grid1LinesSepparation,-windowSurf.get_height()/4), ((-windowSurf.get_width()/4)*1.7 + i*grid1LinesSepparation - (-windowSurf.get_width()/16)*gridSineOffset,windowSurf.get_height()*1.25), 8)
                i += 1

            # interact with the buttons!!
            
            keys = pygame.key.get_pressed()
            if keyPressCD <= 0:
                if keys[pygame.K_t] or keys[pygame.K_y] or keys[pygame.K_u]:
                    if mainMenuButtonSelection > 0:
                        mainMenuButtonSelection -= 1
                        keyPressCD = 0.2
                if keys[pygame.K_v] or keys[pygame.K_b] or keys[pygame.K_n]:
                    if mainMenuButtonSelection < 3:
                        mainMenuButtonSelection += 1
                        keyPressCD = 0.2
            else:
                keyPressCD -= dt

            if keys[pygame.K_g] or keys[pygame.K_h] or keys[pygame.K_j]:
                if mainMenuButtonSelection == 0:
                    pygame.draw.rect(drawSurf2, (255,0,0,150), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],0)
                if mainMenuButtonSelection == 1:
                    snd_roundStart.play()
                    gameState = "round_default"
                if mainMenuButtonSelection == 2:
                    pygame.draw.rect(drawSurf2, (255,0,0,150), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],0)
                if mainMenuButtonSelection == 3:
                    pygame.draw.rect(drawSurf0, (255,255,255,255), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                    gameState = "end"


            # and then render the button selection indicator thingie

            defaultSineOffset = math.sin(pygame.time.get_ticks() / 1000)
            defaultCosineOffset = math.cos(pygame.time.get_ticks() / 1000)

            if gameState == "titleMenu":
                pygame.draw.rect(drawSurf2, (255,255,0,100), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                pygame.draw.rect(drawSurf2, (255,255,0,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 + defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                pygame.draw.rect(drawSurf2, (255,255,0,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 - defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,-defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
            else:
                pygame.draw.rect(drawSurf2, (255,255,150,255), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],0)

            # draw the controls tip too cuz they're confusing :p

            img_controlsTip = pygame.image.load(programDirectory + "\\assets\\image\\titleMenuControls.png")
            img_controlsTip = pygame.transform.scale(img_controlsTip, (windowSurf.get_height()/3.3,windowSurf.get_height()/4))
            img_controlsTip.set_alpha(40)
            drawSurf2.blit(img_controlsTip, (windowSurf.get_width()/18,windowSurf.get_height()/7))

            # draw the game title

            drawSurf2.blit(pygame.transform.scale(img_gameTitleV1, (windowSurf.get_width()/2,windowSurf.get_width()/7)), (windowSurf.get_width()/4,windowSurf.get_height()/9))

            # draw the whatever cool thing there could be to the right

            defaultSineOffset = (math.sin(pygame.time.get_ticks() / 1500) + 12)/16
            defaultCosineOffset = (math.cos(pygame.time.get_ticks() / 1500) + 12)/16

            img_coolThingToTheRight = pygame.image.load(programDirectory + "\\assets\\image\\placeholder.png")
            img_coolThingToTheRight = pygame.transform.scale(img_coolThingToTheRight,(windowSurf.get_width()/2.5,windowSurf.get_height()/2.5))
            img_coolThingToTheRight = pygame.transform.rotate(img_coolThingToTheRight, defaultSineOffset*50 - 41)
            drawSurf2.blit(img_coolThingToTheRight, (windowSurf.get_width()/2,windowSurf.get_height()/2.1))

            # draw the rights and lefts notice

            img_rightsAndLefts = pygame.image.load(programDirectory + "\\assets\\image\\rights_and_lefts.png")
            img_rightsAndLefts = pygame.transform.scale(img_rightsAndLefts, (img_rightsAndLefts.get_width()/4, img_rightsAndLefts.get_height()/4))
            img_rightsAndLefts.set_alpha(70)
            drawSurf2.blit(img_rightsAndLefts, (windowSurf.get_width() - img_rightsAndLefts.get_width(),windowSurf.get_height() - img_rightsAndLefts.get_height()))

            # draw the Special Effects for certain splash texts
            
            defaultSineOffset = (math.sin(pygame.time.get_ticks() / 400) + 12)/16

            if randomSplash == "52":
                i = 4
                while i >= 1:
                    img_splashTxt_52sub1 = pygame.image.load(splashTxt_52sub1)
                    img_splashTxt_52sub1 = pygame.transform.scale(img_splashTxt_52sub1, (defaultSineOffset*img_splashTxt_52sub1.get_width()/5,defaultSineOffset*img_splashTxt_52sub1.get_height()/5))
                    img_splashTxt_52sub1 = pygame.transform.rotate(img_splashTxt_52sub1, 8)
                    img_splashTxt_52sub1.set_alpha(130 - 20*i)
                    drawSurf2.blit(img_splashTxt_52sub1, (((5.25+i*0.1)*windowSurf.get_width()/8) - img_splashTxt_52sub1.get_width()/2,((4.5+i*0.02)*windowSurf.get_height()/16) - img_splashTxt_52sub1.get_height()/2))
                    i -= 1

            # draw the splash text

            img_splashTxt = pygame.image.load(programDirectory + "\\assets\\image\\splashTxt\\" + randomSplash + ".png")
            img_splashTxt = pygame.transform.scale(img_splashTxt, (defaultSineOffset*img_splashTxt.get_width()/5,defaultSineOffset*img_splashTxt.get_height()/5))
            img_splashTxt = pygame.transform.rotate(img_splashTxt, 8)
            drawSurf2.blit(img_splashTxt, ((5.25*windowSurf.get_width()/8) - img_splashTxt.get_width()/2,(4.5*windowSurf.get_height()/16) - img_splashTxt.get_height()/2))
            img_splashTxtB = 1
            img_splashTxtW = 1

            # draw the buttons
            
            drawSurf2.blit(img_txt_playSoloMatch, ((windowSurf.get_width()/5) - (img_txt_playSoloMatch.get_width()/2),4.5*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_playDuoMatch, ((windowSurf.get_width()/5) - (img_txt_playDuoMatch.get_width()/2),5.7*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_settingsHelp, ((windowSurf.get_width()/5) - (img_txt_settingsHelp.get_width()/2),6.9*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_exitProgram, ((windowSurf.get_width()/5) - (img_txt_exitProgram.get_width()/2),8.1*windowSurf.get_height()/10))

            

    elif gameState == "round_default":
        # overlay a color over old frame
        pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        pygame.draw.rect(drawSurf2, (0,0,0,30), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        pygame.draw.rect(drawSurf1, (0,0,0,4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
        pygame.draw.rect(drawSurf0, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)


        if roundMusicStarted == False:
            pygame.mixer.music.load(programDirectory + "\\assets\\audio\\burnBrighter.mp3")
            pygame.mixer.music.play(-1,0.0,0)
            roundMusicStarted = True

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

        # change grid colors based on the last scored player

        if lastScored <= 0.05 and lastScored >= -0.5 and lastScored != 0:
            lastScored = 0
            grid2Color = [255,0,255,6]
        if lastScored > 0.05:
            grid2Color = [255,0,255 * (-lastScored + 1),20]
            lastScored -= dt/1.3
        if lastScored < -0.05:
            grid2Color = [255 * (lastScored + 1),0,255,40]
            lastScored += dt/2
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
                if lastHit > -0.05:
                    lastHit = 0
                else:
                    pygame.draw.rect (drawSurf2, (255,0,0,255), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)
                    lastHit += 0.01
            elif lastHit > 0:
                if lastHit < 0.05:
                    lastHit = 0
                else:
                    pygame.draw.rect (drawSurf2, (0,0,255,255), [ball_pos.x, ball_pos.y, ball_size[0], ball_size[1]], 0)
                    lastHit -= 0.01
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
            lastScored = -1
            pygame.draw.rect(drawSurf1, (100,100,255,50), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            print(score)
            ball_v.x = ball_iv
            ball_v.y = random.randint(-150,150)
        if ball_pos.x > windowSurf.get_width():
            ball_pos.x = scrCenter[0] - (ball_size[0] / 2)
            ball_pos.y = scrCenter[1] - (ball_size[1] / 2)
            score[0] += 1
            lastScored = 1
            pygame.draw.rect(drawSurf1, (255,100,100,50), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
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

pygame.display.quit()
pygame.mixer.quit()
pygame.quit()