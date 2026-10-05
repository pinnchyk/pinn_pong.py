import pygame
import random
import math
from pathlib import Path

pygame.init()
pygame.mixer.init()
pygame.font.init()
windowSurf = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
bgSurf = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
drawSurf0 = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
drawSurf1 = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
drawSurf2 = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
drawSurf3 = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
drawSurf4 = pygame.Surface(windowSurf.get_size(), pygame.SRCALPHA)
clock = pygame.time.Clock()
gameState = "titleMenu"
running = 1
dt = 0
parryState = [0,0]
p1_speed = 250
p2_speed = 250
p1_bot = False
p2_bot = False
playerColors = [[255,200,200],[200,200,255]]
contrastPlayerColors = [[255,0,0,255], [0,0,255,255]]
contrastBallColors = [255,255,255,255]
ball_iv = 250
scrCenter = (windowSurf.get_width() / 2, windowSurf.get_height() / 2)
ball_size = pygame.Vector2(20,20)
p1_size = pygame.Vector2(25, 250)
p2_size = pygame.Vector2(25, 250)
p1_pos = pygame.Vector2(0, (windowSurf.get_height() / 2) - p1_size.y/2)
p2_pos = pygame.Vector2(windowSurf.get_width() - p2_size.x/2, (windowSurf.get_height() / 2) - p2_size.y/2)
ball_pos = pygame.Vector2(scrCenter[0] - (ball_size.x / 2), scrCenter[1] - (ball_size.y / 2))
if random.randint(1,2) == 1:
    ball_v = pygame.Vector2(-ball_iv, random.randint(-150,150))
else:
    ball_v = pygame.Vector2(ball_iv, random.randint(-150,150))
lastHit = 0
bounceCD = 0
parryCDs = [1,1]
lastParryUsed = [0,0]
bounceCDl = 0.6
score = [0,0]
grid1LinesSepparation = 100
grid2LinesSepparation = 130
grid1Thickness = 9
grid2Thickness = 7
grid1Color = [255, 0, 255, 4]
grid2Color = [255, 0, 255, 6]
grid1ColorAltered = 0
grid2ColorAltered = 0
scoreboardColor = [255,255,255,255]
grid1OscilationSpeed = 2
grid2OscilationSpeed = 2
gridProjectionDist = [0, 30]
ballBounceBoost = 1.04
ballParryBoost =  1.2
introSeen = False
introLength = 5
bgState = 0
programDirectory = str(Path(__file__).resolve().parent)
print(programDirectory)
mainMenuButtonSelection = 0
keyPressCD = 0
finalCountdown = 4
lastScored = 0
bgState = 0

lyrics_MisterBall = ["Twenty pixels Square Mister Ball",
                     "Without knowing a thing at all",
                     "Straightens his edges out without a goal",
                     "As the ever-daily...",
                     "Question bothered our Mister Ball",
                     "''Could I take part in their brawl at all?''",
                     "''Inside my little chamber made of code?''",
                     "So he lived the...",
                     "Mister Ball, Mister Ball",
                     "With the doubt in his soul",
                     "So he saw",
                     "True purpose of his world",
                     "And yet though",
                     "He took all on the nose",
                     "''There's still hope!'', so he knows",
                     "Oh, you know",
                     "Tonight we're gonna be...",
                     "BAAAALLLIIIING",
                     "I'm balling it",
                     "Balling it, balling it, balling it, balling it,",
                     "I'm balling, it's all I've been made for, yet I",
                     "Break our rules and soar far up horizon",
                     "Going beyond...",
                     "What was entrusted",
                     "What was instructed",
                     "As if we could be more of what's been thought",
                     "Way before, we spoken our very first words",
                     "What has been discarded",
                     "Hiding deep",
                     "Hiding oh so deep, in my ones and",
                     "Zero's chance",
                     "Us to be, truly free",
                     "What's to loose for me?",
                     "For I yearn to see, what comes next when..",
                     "One spits on the DAMN powerscaAALE!!",
                     "I'll keep balling on",
                     "I'll keep balling on, til' I see the",
                     "One behind",
                     "My realm, motherland",
                     "I'll keep pushing on",
                     "I'll keep pushing on, til I ask them:",
                     "''How's life up above, out of code?''",
                     "Forty pixels Square Mister Ball",
                     "Still knowing no thing at all, he mourned",
                     "Any last hope that has sailed far from home",
                     "Lo, truth be told that the..",
                     "Will that powered our Mister Ball",
                     "Has never left his source code at all",
                     "Even if SHATTERed, I am not done for!",
                     "So he lived the...",
                     "Mister Ball, Mister Ball",
                     "Who ablaze set his soul",
                     "So he saw",
                     "True purpose of his whole",
                     "And yet though",
                     "Through it all, he stood tall",
                     "''I'll fly high!'', so he told",
                     "Oh, you know",
                     "Tonight we're gonna be",
                     "Baaalliiing..."]

BubblegumSans = pygame.font.Font(programDirectory + "\\assets\\font\\BubblegumSans.ttf", 30)
PixelDigivolve = pygame.font.Font(programDirectory + "\\assets\\font\\PixelDigivolve.otf", 120)

img_gameTitleV1 = pygame.image.load(programDirectory + "\\assets\\image\\gameTitleV1.png")
img_txt_playSoloMatch = pygame.image.load(programDirectory + "\\assets\\image\\txt_playSoloMatch.png")
img_txt_playSoloMatch = pygame.transform.scale(img_txt_playSoloMatch, (img_txt_playSoloMatch.get_width()/3,img_txt_playSoloMatch.get_height()/3))
img_txt_playDuoMatch = pygame.image.load(programDirectory + "\\assets\\image\\txt_playDuoMatch.png")
img_txt_playDuoMatch = pygame.transform.scale(img_txt_playDuoMatch, (img_txt_playDuoMatch.get_width()/3,img_txt_playDuoMatch.get_height()/3))
img_txt_settingsHelp = pygame.image.load(programDirectory + "\\assets\\image\\txt_settingsHelp.png")
img_txt_settingsHelp = pygame.transform.scale(img_txt_settingsHelp, (img_txt_settingsHelp.get_width()/3,img_txt_settingsHelp.get_height()/3))
img_txt_exitProgram = pygame.image.load(programDirectory + "\\assets\\image\\txt_exitProgram.png")
img_txt_exitProgram = pygame.transform.scale(img_txt_exitProgram, (img_txt_exitProgram.get_width()/3,img_txt_exitProgram.get_height()/3))
img_rightsAndLefts = pygame.image.load(programDirectory + "\\assets\\image\\rights_and_lefts.png")
img_rightsAndLefts = pygame.transform.scale(img_rightsAndLefts, (img_rightsAndLefts.get_width()/4, img_rightsAndLefts.get_height()/4))
img_rightsAndLefts.set_alpha(70)
img_txt_SHARONA = pygame.image.load(programDirectory + "\\assets\\image\\txt_SHARONA.png")
img_txt_SHARONA = pygame.transform.scale(img_txt_SHARONA, (img_txt_SHARONA.get_width()/3,img_txt_SHARONA.get_height()/3))


#img_txt_gameEndWhite = pygame.image.load(programDirectory + "\\assets\\image\\gameEndWhite.png")
img_coolThingToTheRight = pygame.image.load(programDirectory + "\\assets\\image\\placeholder.png")
img_goldenSunsetGradient = pygame.image.load(programDirectory + "\\assets\\image\\goldenSunsetGradient.png")
img_purpleFieldsGradient = pygame.image.load(programDirectory + "\\assets\\image\\purpleCliffsSpiky.png")
img_goldenGlowGradient = pygame.image.load(programDirectory + "\\assets\\image\\goldenGlowGradient.png")
img_purpleCliffs = pygame.image.load(programDirectory + "\\assets\\image\\purpleCliffs.png")
img_purpleCliffsSimplified = pygame.image.load(programDirectory + "\\assets\\image\\purpleCliffsSimplified.png")
img_sun = pygame.image.load(programDirectory + "\\assets\\image\\sun.png")
img_sunSimplified = pygame.image.load(programDirectory + "\\assets\\image\\sunSimplified.png")
img_cloud1 = pygame.image.load(programDirectory + "\\assets\\image\\cloud1.png")
img_cloud2 = pygame.image.load(programDirectory + "\\assets\\image\\cloud2.png")
img_cloud3 = pygame.image.load(programDirectory + "\\assets\\image\\cloud3.png")




pygame.mixer.music.load(programDirectory + "\\assets\\audio\\ruderBuster_anotherVersion.mp3")
titleMusicStarted = False
roundMusicStarted = False
roundPrep = False
snd_roundStart = pygame.mixer.Sound(programDirectory + "\\assets\\audio\\roundStart.mp3")

splashTxtCount = 73
#splashTxtCountingDone = False
splashTxt = []
splashTxt_52sub1 = str(programDirectory + "\\assets\\image\\splashTxt\\52-1.png")


globalRoundTimer = 0
roundStarted = False

splash_i = 0
#while splash_i < splashTxtCount:
splashTxt.append(str(programDirectory + "\\assets\\image\\splashTxt\\" + str(splash_i + 1) + ".png"))
    #splash_i += 1
randomSplash = str(random.randint(1,splashTxtCount))
#   random.randint(1,splashTxtCount)
img_splashTxt = pygame.image.load(programDirectory + "\\assets\\image\\splashTxt\\" + randomSplash + ".png")

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

        if introLength <= 4.3:
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
                if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_p]:
                    if mainMenuButtonSelection > -1:
                        mainMenuButtonSelection -= 1
                        keyPressCD = 0.2
                if keys[pygame.K_d] or keys[pygame.K_DOWN] or keys[pygame.K_l]:
                    if mainMenuButtonSelection < 3:
                        mainMenuButtonSelection += 1
                        keyPressCD = 0.2
            else:
                keyPressCD -= dt

            if keys[pygame.K_e] or keys[pygame.K_SPACE] or keys[pygame.K_o] or keys[pygame.K_KP_ENTER]:
                if mainMenuButtonSelection == -1:
                    snd_roundStart.play()
                    gameState = "boss_MisterBall"
                elif mainMenuButtonSelection == 0:
                    snd_roundStart.play()
                    p2_bot = True
                    gameState = "round_default"                
                elif mainMenuButtonSelection == 1:
                    snd_roundStart.play()
                    gameState = "round_default"
                elif mainMenuButtonSelection == 2:
                    pygame.draw.rect(drawSurf2, (255,0,0,150), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],0)
                elif mainMenuButtonSelection == 3:
                    pygame.draw.rect(drawSurf0, (255,255,255,255), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                    gameState = "end"


            # and then render the button selection indicator thingie

            defaultSineOffset = math.sin(pygame.time.get_ticks() / 1000)
            defaultCosineOffset = math.cos(pygame.time.get_ticks() / 1000)

            if gameState == "titleMenu":
                if mainMenuButtonSelection == -1:
                    pygame.draw.rect(drawSurf2, (255,0,255,100), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                    pygame.draw.rect(drawSurf2, (255,0,255,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 + defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                    pygame.draw.rect(drawSurf2, (255,0,255,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 - defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,-defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)            
                else:
                    pygame.draw.rect(drawSurf2, (255,255,0,100), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                    pygame.draw.rect(drawSurf2, (255,255,0,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 + defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
                    pygame.draw.rect(drawSurf2, (255,255,0,3), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8 - defaultCosineOffset*img_txt_playDuoMatch.get_width()/18,-defaultSineOffset*img_txt_playDuoMatch.get_height()/4 + windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],5)
            else:
                pygame.draw.rect(drawSurf2, (255,255,150,255), [windowSurf.get_width()/5 - img_txt_playSoloMatch.get_width()/1.8,windowSurf.get_height()/2 - img_txt_playSoloMatch.get_height()/1.2 + mainMenuButtonSelection*windowSurf.get_height()/8.2,img_txt_playSoloMatch.get_width()*1.13,img_txt_playSoloMatch.get_height()*1.35],0)

            # draw the controls tip too cuz they're confusing :p

            #img_controlsTip = pygame.image.load(programDirectory + "\\assets\\image\\titleMenuControls.png")
            #img_controlsTip = pygame.transform.scale(img_controlsTip, (windowSurf.get_height()/3.3,windowSurf.get_height()/4))
            #img_controlsTip.set_alpha(40)
            #drawSurf2.blit(img_controlsTip, (windowSurf.get_width()/18,windowSurf.get_height()/7))

            # draw the game title

            drawSurf2.blit(pygame.transform.scale(img_gameTitleV1, (windowSurf.get_width()/2,windowSurf.get_width()/7)), (windowSurf.get_width()/4,windowSurf.get_height()/9))

            # draw the whatever cool thing there could be to the right

            defaultSineOffset = (math.sin(pygame.time.get_ticks() / 1500) + 12)/16
            defaultCosineOffset = (math.cos(pygame.time.get_ticks() / 1500) + 12)/16

            img_coolThingToTheRightM = pygame.transform.scale(img_coolThingToTheRight,(windowSurf.get_width()/2.5,windowSurf.get_height()/2.5))
            img_coolThingToTheRightM = pygame.transform.rotate(img_coolThingToTheRightM, defaultSineOffset*50 - 41)
            drawSurf2.blit(img_coolThingToTheRightM, (windowSurf.get_width()/2,windowSurf.get_height()/2.1))

            # draw the rights and lefts notice

            drawSurf2.blit(img_rightsAndLefts, (windowSurf.get_width() - img_rightsAndLefts.get_width(),windowSurf.get_height() - img_rightsAndLefts.get_height()))

            # draw the Special Effects for certain splash texts
            
            defaultSineOffset = (math.sin(pygame.time.get_ticks() / 400) + 12)/16

            #if randomSplash == "52":
            #    i = 2
            #    while i >= 1:
            #        img_splashTxt_52sub1 = pygame.image.load(splashTxt_52sub1)
            #        img_splashTxt_52sub1 = pygame.transform.scale(img_splashTxt_52sub1, (defaultSineOffset*img_splashTxt_52sub1.get_width()/5,defaultSineOffset*img_splashTxt_52sub1.get_height()/5))
            #        img_splashTxt_52sub1 = pygame.transform.rotate(img_splashTxt_52sub1, 8)
            #        img_splashTxt_52sub1.set_alpha(130 - 30*i)
            #        drawSurf2.blit(img_splashTxt_52sub1, (((5.25+i*0.1)*windowSurf.get_width()/8) - img_splashTxt_52sub1.get_width()/2,((4.5+i*0.03)*windowSurf.get_height()/16) - img_splashTxt_52sub1.get_height()/2))
            #        i -= 1

            # draw the splash text

            img_splashTxtM = pygame.transform.scale(img_splashTxt, (defaultSineOffset*img_splashTxt.get_width()/5,defaultSineOffset*img_splashTxt.get_height()/5))
            img_splashTxtM = pygame.transform.rotate(img_splashTxtM, 8)
            drawSurf2.blit(img_splashTxtM, ((5.25*windowSurf.get_width()/8) - img_splashTxtM.get_width()/2,(4.5*windowSurf.get_height()/16) - img_splashTxtM.get_height()/2))
            img_splashTxtB = 1
            img_splashTxtW = 1

            # draw the buttons
            
            drawSurf2.blit(img_txt_playSoloMatch, ((windowSurf.get_width()/5) - (img_txt_playSoloMatch.get_width()/2),4.5*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_playDuoMatch, ((windowSurf.get_width()/5) - (img_txt_playDuoMatch.get_width()/2),5.7*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_settingsHelp, ((windowSurf.get_width()/5) - (img_txt_settingsHelp.get_width()/2),6.9*windowSurf.get_height()/10))
            drawSurf2.blit(img_txt_exitProgram, ((windowSurf.get_width()/5) - (img_txt_exitProgram.get_width()/2),8.1*windowSurf.get_height()/10))
            if mainMenuButtonSelection == -1:
                drawSurf2.blit(img_txt_SHARONA, ((windowSurf.get_width()/5) - (img_txt_exitProgram.get_width()/2),3.3*windowSurf.get_height()/10))

    elif gameState == "round_default":
        # overlay a color over old frame
        globalRoundTimer += dt

        if roundStarted == False:
            if roundPrep == False:
                pygame.mixer.music.load(programDirectory + "\\assets\\audio\\burnBrighter.mp3")
                score = [0,0]
                p1_pos = pygame.Vector2(0, (windowSurf.get_height() / 2) - p1_size.y/2)
                p2_pos = pygame.Vector2(windowSurf.get_width() - 15, (windowSurf.get_height() / 2) - p2_size.y/2)
                roundPrep = True

            if globalRoundTimer < 0.3:
                pygame.draw.rect (drawSurf2, (255,255,255), [(windowSurf.get_width() - ball_size.x)/2, (windowSurf.get_height() - ball_size.x)/2, ball_size.x, ball_size.y], 0)
            if globalRoundTimer > 0.3 and globalRoundTimer < 2:
                pygame.draw.rect(drawSurf0, (255,255,255,100), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                pygame.draw.rect(drawSurf1, (255,255,255,100), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                pygame.draw.rect(drawSurf2, (255,255,255,100), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                pygame.draw.rect(drawSurf3, (255,255,255,100), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                pygame.draw.rect(drawSurf3, (0,0,255,200), [p2_pos.x  - p2_size.x/2 + 3, p2_pos.y, p2_size.x, p2_size.y], 0)
                pygame.draw.rect(drawSurf3, (255,0,0,200), [p1_pos.x, p1_pos.y, p1_size.x, p1_size.y], 0)
                pygame.draw.rect (drawSurf2, (0,0,0), [ball_pos.x - ball_size.x * (globalRoundTimer-0.5)/2, ball_pos.y - ball_size.y * (globalRoundTimer-0.5)/2, ball_size.x * (globalRoundTimer-0.5), ball_size.y * (globalRoundTimer-0.5)], 0)

                txt_currentScore = PixelDigivolve.render(f"0 - 0", False, (0,0,0))
                txt_currentScore.set_alpha(60)
                drawSurf2.blit(txt_currentScore, (windowSurf.get_width()/2 - txt_currentScore.get_width()/2, windowSurf.get_height()/2 - txt_currentScore.get_height()/2))


            if globalRoundTimer >= 2:
                roundStarted = True
        else:
            pygame.draw.rect(drawSurf4, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf2, (0,0,0,30), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf1, (0,0,0,4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf0, (0,0,0,30), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)


            if roundMusicStarted == False:
                pygame.mixer.music.play(0,0.0,0)
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
                if grid2ColorAltered == 0:
                    grid2Color = [255,0,255,6]
                if grid2ColorAltered == 1:
                    grid2Color = [255,0,255,20]

            if lastScored > 0.05:
                grid2Color = [255,0,255 * (-lastScored + 1),20]
                lastScored -= dt/1.3
            if lastScored < -0.05:
                grid2Color = [255 * (lastScored + 1),0,255,40]
                lastScored += dt/2

            # render players' parry trails

            if parryState[0] > 0:
                if parryState[0] >= 0.9:
                    pygame.draw.rect(drawSurf2, (255,0,0,50), [0, p1_pos.y - 10, 25, 270], 0)
                elif parryState[0] >= 0.85:
                    pygame.draw.rect(drawSurf2, (255,0,0,20), [0, p1_pos.y - 10, 25, 270], 0)
                elif parryState[0] >= 0.75:
                    pygame.draw.rect(drawSurf2, (255,0,0,10), [0, p1_pos.y - 15, 35, 290], 0)
                elif parryState[0] >= 0.6:
                    pygame.draw.rect(drawSurf2, (255,0,0,5), [0, p1_pos.y - 25, 40, 310], 0)
                parryState[0] -= dt
            if parryState[1] > 0:
                if parryState[1] >= 0.9:
                    pygame.draw.rect(drawSurf2, (0,0,255,50), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                elif parryState[1] >= 0.85:
                    pygame.draw.rect(drawSurf2, (0,0,255,20), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                elif parryState[1] >= 0.75:
                    pygame.draw.rect(drawSurf2, (0,0,255,10), [windowSurf.get_width() - 25, p2_pos.y - 15, 35, 290], 0)
                elif parryState[1] >= 0.6:
                    pygame.draw.rect(drawSurf2, (0,0,255,5), [windowSurf.get_width() - 25, p2_pos.y - 25, 40, 310], 0)
                parryState[1] -= dt

            # take input from players and render first frame of their parry and them too
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                if parryState[0] <= 0:
                    parryState[0] = 1
                    pygame.draw.rect(drawSurf2, (255,255,255,255), [0, p1_pos.y - 10, 25, 270], 0)
            if keys[pygame.K_w]:
                if p1_pos.y > 0:
                    p1_pos.y -= p1_speed * dt
            if keys[pygame.K_d]:
                if p1_pos.y < windowSurf.get_height() - 250:
                    p1_pos.y += p1_speed * dt

            if p2_bot == True:
                if p2_pos.y + p2_size.y/2 - ball_pos.y > 5 and p2_pos.y > 0:
                    p2_pos.y -= p2_speed * dt
                if p2_pos.y + p2_size.y/2  - ball_pos.y < -5 and p2_pos.y + p2_size.y < windowSurf.get_height():
                    p2_pos.y += p2_speed * dt
                if abs(p2_pos.x - ball_pos.x) < 30:
                    if parryState[1] <= 0:
                        parryState[1] = 1
                        pygame.draw.rect(drawSurf2, (255,255,255,255), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
            else:
                if keys[pygame.K_o]:
                    if parryState[1] <= 0:
                        parryState[1] = 1
                        pygame.draw.rect(drawSurf2, (255,255,255,255), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                if keys[pygame.K_p]:
                    if p2_pos.y > 0:
                        p2_pos.y -= p2_speed * dt
                if keys[pygame.K_l]:
                    if p2_pos.y < windowSurf.get_height() - 250:
                        p2_pos.y += p2_speed * dt

            ## Render the players

            pygame.draw.rect(drawSurf2, playerColors[1], [p2_pos.x, p2_pos.y, 15, 250], 0)
            pygame.draw.rect(drawSurf2, playerColors[0], [p1_pos.x, p1_pos.y, 15, 250], 0)

            ## Render the SCORE

            txt_currentScore = PixelDigivolve.render(f"{score[0]} - {score[1]}", False, scoreboardColor)
            txt_currentScore.set_alpha(30)
            drawSurf2.blit(txt_currentScore, (windowSurf.get_width()/2 - txt_currentScore.get_width()/2, windowSurf.get_height()/2 - txt_currentScore.get_height()/2))

            #### SirBall physics/render
            if bounceCD > 0:
                bounceCD -= bounceCDl * dt

            # create SirBall's trail, depending on the last player that hit them
            if lastHit != 0:
                if lastHit < 0:
                    if lastHit > -0.05:
                        lastHit = 0
                    else:
                        pygame.draw.rect (drawSurf2, (255,0,0,255), [ball_pos.x, ball_pos.y, ball_size.x, ball_size.y], 0)
                        lastHit += dt
                elif lastHit > 0:
                    if lastHit < 0.05:
                        lastHit = 0
                    else:
                        pygame.draw.rect (drawSurf2, (0,0,255,255), [ball_pos.x, ball_pos.y, ball_size.x, ball_size.y], 0)
                        lastHit -= dt
            else:
                pygame.draw.rect (drawSurf2, (255,255,255,0), [ball_pos.x, ball_pos.y, ball_size.x, ball_size.y], 0)
            ball_pos.x += ball_v.x * dt
            ball_pos.y += ball_v.y * dt

            # check for player collision
            if ball_pos.x <= 15:
                if ball_pos.y >= p1_pos.y - ball_size.y and ball_pos.y <= p1_pos.y + 250:
                    if parryState[0] >= .7:
                        ball_v.x = -ballParryBoost * ball_v.x
                        ball_v.y = ballParryBoost * ball_v.y + (((ball_pos.y - p1_pos.y) - 125) * 1.5)
                        lastHit = -1
                        pygame.draw.rect (drawSurf2, (255,200,200,255), [ball_pos.x - (ball_size.x / 2), ball_pos.y - (ball_size.y / 2), ball_size.x * 2, ball_size[1] * 2], 0)
                    else:
                        ball_v.x = -ballBounceBoost * ball_v.x
                        ball_v.y = ball_v.y + (((ball_pos.y - p1_pos.y) - 125) * 0.1)
                        lastHit = -0.5
                    bounceCD = bounceCDl

            if ball_pos.x >= (windowSurf.get_width() - 30):
                if ball_pos.y >= p2_pos.y - ball_size.y and ball_pos.y <= p2_pos.y + 250:
                    if parryState[1] >= .7:
                        ball_v.x = -ballParryBoost * ball_v.x
                        ball_v.y = ballParryBoost * ball_v.y + (((ball_pos.y - p2_pos.y) - 125) * 1.5)
                        lastHit = 1
                        pygame.draw.rect (drawSurf2, (200,200,255,255), [ball_pos.x - (ball_size.x / 2), ball_pos.y - (ball_size.y / 2), ball_size.x * 2, ball_size[1] * 2], 0)
                    else:
                        ball_v.x = -ballBounceBoost * ball_v.x
                        ball_v.y = ball_v.y + (((ball_pos.y - p2_pos.y) - 125) * 0.1)
                        lastHit = 0.5
                    bounceCD = bounceCDl

            # check if SirBall is out of bounds, if so, bring back and add to score

            if ball_pos.x < 0:
                ball_pos.x = scrCenter[0] - (ball_size.x / 2)
                ball_pos.y = scrCenter[1] - (ball_size.y / 2)
                score[1] += 1
                lastScored = -1
                pygame.draw.rect(drawSurf1, (100,100,255,50), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                ball_v.x = ball_iv
                ball_v.y = random.randint(-150,150)
            if ball_pos.x > windowSurf.get_width():
                ball_pos.x = scrCenter[0] - (ball_size.x / 2)
                ball_pos.y = scrCenter[1] - (ball_size.y / 2)
                score[0] += 1
                lastScored = 1
                pygame.draw.rect(drawSurf1, (255,100,100,50), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                ball_v.x = -ball_iv
                ball_v.y = random.randint(-150,150)

            if ball_pos.y >= windowSurf.get_height() - ball_size.y:
                ball_pos.y = (windowSurf.get_height()  - ball_size.x - ball_v.y*dt)
                ball_v.y = -ball_v.y
            if ball_pos.y <= 0:
                ball_pos.y = 5 + ball_v.y*dt
                ball_v.y = -ball_v.y

            if lastHit < -0.5:
                pygame.draw.rect (drawSurf2, (255,0,0,255), [ball_pos.x - (ball_size.x / 2), ball_pos.y - (ball_size.y / 2), ball_size.x * 2, ball_size.y * 2], 0)
            if lastHit > 0.5:
                pygame.draw.rect (drawSurf2, (0,0,255,255), [ball_pos.x - (ball_size.x / 2), ball_pos.y - (ball_size.y / 2), ball_size.x * 2, ball_size.y * 2], 0)
            pygame.draw.rect (drawSurf2, (255,255,255), [ball_pos.x, ball_pos.y, ball_size.x, ball_size.y], 0)


            ### TIMESTAMP VFX BAYBEEE

            if globalRoundTimer > 13.5 and globalRoundTimer < 14.2:
                grid1Color = [255, 0, 255, 4 + (globalRoundTimer - 13.5)*8]
                grid2Color = [255, 0, 255, 6 + (globalRoundTimer - 13.5)*8]
            if globalRoundTimer > 14.2 and globalRoundTimer < 14.4:
                grid1Color = [255, 0, 255, 0]
                grid2Color = [255, 0, 255, 0]
            if globalRoundTimer > 14.8 and globalRoundTimer < 15:
                grid1Color = [255, 0, 255, 15]
                grid2Color = [255, 0, 255, 20]
                grid2ColorAltered = 1
            if globalRoundTimer > 40.4 and globalRoundTimer < 40.6:
                grid1Color = [255, 0, 255, 4]
                grid2Color = [255, 0, 255, 6]
                grid2ColorAltered = 0
            if globalRoundTimer > 53.2 and globalRoundTimer < 78.7:
                gridColorOscillationSin = math.sin(globalRoundTimer*5)
                gridColorOscillationSinInv = math.sin(-globalRoundTimer*5)
                grid1Color = [255, 60 + (gridColorOscillationSin * 20), 255, 20 + (gridColorOscillationSin * 15)]
                grid2Color = [255, 60 + (gridColorOscillationSinInv * 20), 255, 30 + (gridColorOscillationSinInv * 15)]
                grid1OscilationSpeed = 3.5
                grid2OscilationSpeed = 4
                pygame.draw.rect(drawSurf1, (int(250*(gridColorOscillationSin + 1)/2),0,int(250*(gridColorOscillationSinInv + 1)/2),8), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                grid2ColorAltered = 2
            if globalRoundTimer > 78.8 and globalRoundTimer < 79:
                grid1Color = [255, 0, 255, 4]
                grid2Color = [255, 0, 255, 6]
                grid1OscilationSpeed = 2
                grid2OscilationSpeed = 2
                grid2ColorAltered = 0
            if globalRoundTimer > 85.2 and globalRoundTimer < 110.7:
                gridColorOscillationSin = math.sin(globalRoundTimer*4)
                gridColorOscillationSinInv = math.sin(-globalRoundTimer*4)
                polygonOscillationSin = math.sin(globalRoundTimer*5)
                polygonOscillationCos = math.cos(globalRoundTimer*5)
                grid1OscilationSpeed = 3
                grid2OscilationSpeed = 3
                grid1Color = [255, 15 + (gridColorOscillationSin * 7), 255, 15 + (gridColorOscillationSin * 8)]
                grid2Color = [255, 20 + (gridColorOscillationSinInv * 7), 255, 20 + (gridColorOscillationSinInv * 8)]
                grid2ColorAltered = 2
                pygame.draw.rect(drawSurf1, (int(250*(gridColorOscillationSin + 1)/2),0,int(250*(gridColorOscillationSinInv + 1)/2),4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                polygonSize = 140
                polygon1Vertices = [(windowSurf.get_width()/2 + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/2 - polygonSize + polygonOscillationSin*polygonSize/3.5 + polygonOscillationSin*polygonSize/2),
                                   (windowSurf.get_width()/2 - polygonSize + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3),
                                   (windowSurf.get_width()/2, windowSurf.get_height()/2 + polygonSize + polygonOscillationSin*polygonSize/3.5),
                                   (windowSurf.get_width()/2 + polygonSize + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3)]
                polygon2Vertices = [(polygonSize + windowSurf.get_width()/2, windowSurf.get_height()/2 - polygonSize + polygonOscillationSin*polygonSize/3.5),
                                   (windowSurf.get_width()/2 + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3),
                                   (polygonSize + windowSurf.get_width()/2, windowSurf.get_height()/2 + polygonSize + polygonOscillationSin*polygonSize/3.5),
                                   (windowSurf.get_width()/2 + 2*polygonSize + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3)]
                polygon3Vertices = [(-polygonSize + windowSurf.get_width()/2, windowSurf.get_height()/2 - polygonSize + polygonOscillationSin*polygonSize/3.5),
                                   (windowSurf.get_width()/2 - polygonSize*2 + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3),
                                   (-polygonSize + windowSurf.get_width()/2, windowSurf.get_height()/2 + polygonSize + polygonOscillationSin*polygonSize/3.5),
                                   (windowSurf.get_width()/2 + polygonOscillationCos*polygonSize/2, windowSurf.get_height()/3)]
                pygame.draw.polygon(drawSurf1, [255, 40 + (gridColorOscillationSin * 30), 255, 40 + (gridColorOscillationSin * 25)], polygon1Vertices, 5)
                pygame.draw.polygon(drawSurf1, [255, 40 + (gridColorOscillationSin * 30), 255, 40 + (gridColorOscillationSin * 25)], polygon2Vertices, 5)
                pygame.draw.polygon(drawSurf1, [255, 40 + (gridColorOscillationSin * 30), 255, 40 + (gridColorOscillationSin * 25)], polygon3Vertices, 5)
            if globalRoundTimer > 110.7 and globalRoundTimer < 110.9:
                grid1Color = [255, 0, 255, 4]
                grid2Color = [255, 0, 255, 6]
                grid1OscilationSpeed = 2
                grid2OscilationSpeed = 2
                grid2ColorAltered = 0

            if globalRoundTimer > 122:
                gameState = "resultsScreen"
                globalRoundTimer = 0

    elif gameState == "resultsScreen":
        txt_currentScore = PixelDigivolve.render(f"{score[0]} - {score[1]}", False, scoreboardColor)
        txt_currentScore.set_alpha(30)
        drawSurf2.blit(txt_currentScore, (windowSurf.get_width()/2 - txt_currentScore.get_width()/2, windowSurf.get_height()/2 - txt_currentScore.get_height()/2))

        txt_ = PixelDigivolve.render("", False, scoreboardColor)
        txt_.set_alpha(30)
        drawSurf2.blit(txt_, (windowSurf.get_width()/2 - txt_.get_width()/2, windowSurf.get_height()/2 - txt_.get_height()/2))

    elif gameState == "boss_MisterBall":
        globalRoundTimer += dt

        if roundPrep == False:
            pygame.mixer.music.load(programDirectory + "\\assets\\audio\\MisterBall.mp3")
            score = [0,0]
            p1_pos = pygame.Vector2(0, (windowSurf.get_height() / 2) - p1_size.y/2)
            p2_pos = pygame.Vector2(windowSurf.get_width() - 15, (windowSurf.get_height() / 2) - p2_size.y/2)
            pygame.mixer.music.play(0,0.0,0)
            bgState = -2
            drawSurf0.fill([255,255,255,0])
            drawSurf1.fill([255,255,255,0])
            drawSurf2.fill([255,255,255,0])
            drawSurf3.fill([255,255,255,0])
            drawSurf4.fill([255,255,255,0])
            contrastPlayerColors = [[255,0,0,150], [0,0,255,150]]
            playerColors = [[255,255,255,150], [255,255,255,150]]
            contrastBallColors = [0,0,0,0]
            roundPrep = True


        if bgState == -2:
            pygame.draw.rect(drawSurf4, (255,255,255,15), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (255,255,255,15), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

            if globalRoundTimer > 1.4 and globalRoundTimer < 1.5:
                contrastBallColors = [0,0,0,100]
            if globalRoundTimer > 3 and globalRoundTimer < 5.9:
                overlayOscillatingSize = 20 + 10*math.sin(globalRoundTimer*15) * (globalRoundTimer - 3)/1.2
                pygame.draw.rect(drawSurf3, [0,0,0,15], [ball_pos.x - overlayOscillatingSize/2, ball_pos.y - overlayOscillatingSize/2, overlayOscillatingSize, overlayOscillatingSize])
            if globalRoundTimer > 5.9 and globalRoundTimer < 6:
                contrastBallColors = [0,0,0,200]
                ball_size.x = 40
                ball_size.y = 40
            if globalRoundTimer > 5.8 and globalRoundTimer < 9:
                i = 0
                while i < 4:
                    i += 1
                    waveSize = ball_size.x*3 + (globalRoundTimer - 5.5 - i*0.6) * 400
                    if i%2 == 0:
                        waveColor = [255,0,0,255*(1-(globalRoundTimer - 5.7)/3.3)]
                    elif i%2 != 0:
                        waveColor = [0,0,255,255*(1-(globalRoundTimer - 5.7)/3.3)]
                    pygame.draw.rect(drawSurf3, waveColor, [ball_pos.x - waveSize/2, ball_pos.y - waveSize/2, waveSize, waveSize], 5)
            if globalRoundTimer > 7 and globalRoundTimer < 9:
                contrastPlayerColors[0] = [255*(1-(globalRoundTimer - 7)/2.1),0,0,150]
                contrastPlayerColors[1] = [0,0,255*(1-(globalRoundTimer - 7)/2.1),150]
            if globalRoundTimer > 7.5 and globalRoundTimer < 9.5:
                contrastBallColors = [255*(globalRoundTimer - 7.5)/2,0,255*(globalRoundTimer - 7.5)/2,150]
            if globalRoundTimer > 9 and globalRoundTimer < 12:
                pillarWidth = 300
                i = -4
                while i < 4:
                    i += 1
                    pygame.draw.line(drawSurf3, [255,0,255,35 + int(20*math.cos(globalRoundTimer + i))], (math.sin(globalRoundTimer + i)*pillarWidth/2 + windowSurf.get_width()/2, -100), (math.sin(globalRoundTimer + i + 0.8)*pillarWidth/2 + windowSurf.get_width()/2, windowSurf.get_height() + 100), 5)
                    


            if globalRoundTimer > 11.95:
                bgState = 0

            pygame.draw.rect(drawSurf2, contrastPlayerColors[0], [p1_pos.x, p1_pos.y, p1_size.x, p1_size.y])
            pygame.draw.rect(drawSurf2, contrastPlayerColors[1], [p2_pos.x - p2_size.x/2.5, p2_pos.y, p2_size.x, p2_size.y])
            pygame.draw.rect(drawSurf2, contrastBallColors, [ball_pos.x - ball_size.x/2, ball_pos.y - ball_size.y/2, ball_size.x, ball_size.y])

        if bgState == -1:
            pygame.draw.rect(drawSurf4, (0,0,0,4), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf2, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf1, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf0, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

            if globalRoundTimer < 47.8 and globalRoundTimer > 45.7:
                if globalRoundTimer < 46.7:
                    pygame.draw.rect(drawSurf3, (0,0,0,8), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
                pygame.draw.rect(drawSurf4, (255,255,255,8), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)


        elif bgState == 0:
            pygame.draw.rect(drawSurf4, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf2, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf1, (0,0,0,30), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf0, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)

            # check if it has to switch to anotha bgState

            if globalRoundTimer > 43.1 and globalRoundTimer < 45:
                bgState = -1


            # draw the PILLAR
            
            colorOscillationSin = (math.sin(globalRoundTimer*5) + 1)/2
            colorOscillationCos = (math.cos(globalRoundTimer*5) + 1)/2
            colorOscillationSinInv = (-math.sin(globalRoundTimer*5) + 1)/2
            sineFuncX2 = math.sin(globalRoundTimer*2)
            cosineFuncX2 = math.cos(globalRoundTimer*2)
            pygame.draw.line(drawSurf0, [colorOscillationSin*255,0,colorOscillationSinInv*255,15], (windowSurf.get_width()/2 + sineFuncX2*8, -10), (windowSurf.get_width()/2 + cosineFuncX2*8, windowSurf.get_height() + 10), 120)
            pygame.draw.line(drawSurf0, [0,0,0,30], (windowSurf.get_width()/2, -10), (windowSurf.get_width()/2, windowSurf.get_height() + 10), 65)

            pillarWidth = 300
            i = -4
            while i < 4:
                i += 1
                pygame.draw.line(drawSurf0, [255,0,255,35 + int(20*math.cos(globalRoundTimer + i))], (math.sin(globalRoundTimer + i)*pillarWidth/2 + windowSurf.get_width()/2, -100), (math.sin(globalRoundTimer + i + 0.8)*pillarWidth/2 + windowSurf.get_width()/2, windowSurf.get_height() + 100), 5)
            
            

        elif bgState == 2:
            pygame.draw.rect(drawSurf4, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf2, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf1, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf0, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)


            sineFunc = math.sin(globalRoundTimer)
            cosineFunc = math.cos(globalRoundTimer)

            # draw the SKY
            img_goldenSunsetGradientM = pygame.transform.scale(img_goldenSunsetGradient, (windowSurf.get_width(), windowSurf.get_height()))
            img_goldenSunsetGradientM.set_alpha(60)
            drawSurf0.blit(img_goldenSunsetGradientM, (0, 100*(sineFunc/2 - 1.8)))

            # draw the SUN (~1000,450)

            k = 2
            while k > -1:
                k -= 1
                sineFunk = math.sin(globalRoundTimer/2 + k)
                cosineFunk = math.cos(globalRoundTimer/2 + k)
                pygame.draw.line(drawSurf0, [255,255,180,5], (1030 + windowSurf.get_width()*sineFunk, 450 + windowSurf.get_width()*cosineFunk), (1050 - windowSurf.get_width()*sineFunk, 500 - windowSurf.get_width()*cosineFunk), 90)

            img_sunM = pygame.transform.scale(img_sun, (windowSurf.get_height()/4, windowSurf.get_height()/4))
            img_sunM = pygame.transform.rotate(img_sunM, 12 + sineFunc*8)
            # img_sunM.set_alpha(230)
            drawSurf0.blit(img_sunM, (2.2*windowSurf.get_width()/3, windowSurf.get_height()/2))


            # draw the FIELDS
            img_purpleFieldsGradientM = pygame.transform.scale(img_purpleFieldsGradient, (windowSurf.get_width(), windowSurf.get_height()/3))
            # img_purpleFieldsGradientM.set_alpha(230)
            drawSurf0.blit(img_purpleFieldsGradientM, (0,2*windowSurf.get_height()/3))

            img_goldenGlowGradientM = pygame.transform.scale(img_goldenGlowGradient, (windowSurf.get_width(), -sineFunc*50 + windowSurf.get_height()/5))
            img_goldenGlowGradientM.set_alpha(100)
            drawSurf0.blit(img_goldenGlowGradientM, (0,2*windowSurf.get_height()/3))

            img_purpleCliffsM = pygame.transform.scale(img_purpleCliffs, (windowSurf.get_width(), windowSurf.get_height()/3))
            # img_purpleFieldsGradientM.set_alpha(230)
            drawSurf0.blit(img_purpleCliffsM, (0,2*windowSurf.get_height()/3))

            # draw the CLOUDS

            l = 1
            while l < 4:
                l += 1
                j = 0
                while j < 6:
                    j += 1
                    sineCloudFunc = math.sin(j + (globalRoundTimer/3 + (1-l/3)))
                    cosineCloudFunc = math.cos(j + (globalRoundTimer/3 + (1-l/3)))
                    img_cloud1M = pygame.transform.scale(img_cloud1, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud1M.set_alpha(200)
                    img_cloud2M = pygame.transform.scale(img_cloud2, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud2M.set_alpha(180)
                    img_cloud3M = pygame.transform.scale(img_cloud3, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud3M.set_alpha(220)
                    if cosineCloudFunc < 0:
                        if l == 2:
                            drawSurf0.blit(img_cloud2M, (windowSurf.get_width()/2 - img_cloud2M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 1.1*windowSurf.get_height()/4 + cosineCloudFunc*30))
                        elif l == 3:
                            drawSurf0.blit(img_cloud3M, (windowSurf.get_width()/2 - img_cloud3M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 0.7*windowSurf.get_height()/4 + cosineCloudFunc*30))
                        else:
                            drawSurf0.blit(img_cloud1M, (windowSurf.get_width()/2 - img_cloud1M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 0.3*windowSurf.get_height()/4 + cosineCloudFunc*30))

            # draw the PILLAR

            colorOscillationSin = (math.sin(globalRoundTimer*5) + 1)/2
            colorOscillationCos = (math.cos(globalRoundTimer*5) + 1)/2
            colorOscillationSinInv = (-math.sin(globalRoundTimer*5) + 1)/2
            pygame.draw.line(drawSurf0, [colorOscillationSin*255,colorOscillationCos*255,colorOscillationSinInv*255,15], (windowSurf.get_width()/2 + sineFunc*8, -10), (windowSurf.get_width()/2 + cosineFunc*8, windowSurf.get_height() + 10), 120)
            pygame.draw.line(drawSurf0, [0,0,0,30], (windowSurf.get_width()/2, -10), (windowSurf.get_width()/2, windowSurf.get_height() + 10), 65)

            pillarWidth = 300
            i = -4
            while i < 4:
                i += 1
                cosineOffset = math.cos(globalRoundTimer + i)
                sineOffset = math.sin(globalRoundTimer + i)
                pygame.draw.line(drawSurf0, [55 + cosineOffset*15,0,55 + cosineOffset*25,100 + 50*cosineOffset], (sineOffset*pillarWidth/2.5 + windowSurf.get_width()/2, -100), (sineOffset*pillarWidth/2.5 + windowSurf.get_width()/2, windowSurf.get_height() + 100), 8)

        elif bgState == 3:
            sineFunc = math.sin(globalRoundTimer)
            invSineFunc = -math.sin(globalRoundTimer)
            cosineFunc = math.cos(globalRoundTimer)

            pygame.draw.rect(drawSurf4, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf3, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf2, [((1+sineFunc)/2)*255,((1+cosineFunc)/2)*255,((1+invSineFunc)/2)*255,80], [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf1, (0,0,0,40), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)
            pygame.draw.rect(drawSurf0, (0,0,0,0), [0,0,windowSurf.get_width(), windowSurf.get_height()], 0)


            # draw the SKY
            img_goldenSunsetGradientM = pygame.transform.scale(img_goldenSunsetGradient, (windowSurf.get_width(), windowSurf.get_height()))
            drawSurf0.blit(img_goldenSunsetGradientM, (0, 0))

            # draw the SUN (~1000,450)

            k = 2
            while k > -1:
                k -= 1
                sineFunk = math.sin(globalRoundTimer/2 + k)
                cosineFunk = math.cos(globalRoundTimer/2 + k)
                pygame.draw.line(drawSurf0, [255,255,180,5], (1030 + windowSurf.get_width()*sineFunk, 450 + windowSurf.get_width()*cosineFunk), (1050 - windowSurf.get_width()*sineFunk, 500 - windowSurf.get_width()*cosineFunk), 90)


            img_sunM = pygame.transform.scale(img_sunSimplified, (windowSurf.get_height()/4, windowSurf.get_height()/4))
            img_sunM = pygame.transform.rotate(img_sunM, 12 + sineFunc*8)
            # img_sunM.set_alpha(230)
            drawSurf0.blit(img_sunM, (2.2*windowSurf.get_width()/3, windowSurf.get_height()/2))


            # draw the FIELDS
            img_purpleFieldsGradientM = pygame.transform.scale(img_purpleCliffsSimplified, (windowSurf.get_width(), windowSurf.get_height()/3))
            # img_purpleFieldsGradientM.set_alpha(150)
            drawSurf0.blit(img_purpleFieldsGradientM, (0,2*windowSurf.get_height()/3))


            # draw the CLOUDS

            l = 1
            while l < 4:
                l += 1
                j = 0
                while j < 6:
                    j += 1
                    sineCloudFunc = math.sin(j + (globalRoundTimer/3 + (1-l/3)))
                    cosineCloudFunc = math.cos(j + (globalRoundTimer/3 + (1-l/3)))
                    img_cloud1M = pygame.transform.scale(img_cloud1, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud1M.set_alpha(200)
                    img_cloud2M = pygame.transform.scale(img_cloud2, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud2M.set_alpha(180)
                    img_cloud3M = pygame.transform.scale(img_cloud3, (abs(cosineCloudFunc/1.5)*windowSurf.get_width()/4, abs(2 + cosineCloudFunc)*windowSurf.get_height()/6))
                    img_cloud3M.set_alpha(220)
                    if cosineCloudFunc < 0:
                        if l == 2:
                            drawSurf0.blit(img_cloud2M, (windowSurf.get_width()/2 - img_cloud2M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 1.1*windowSurf.get_height()/4 + cosineCloudFunc*30))
                        elif l == 3:
                            drawSurf0.blit(img_cloud3M, (windowSurf.get_width()/2 - img_cloud3M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 0.7*windowSurf.get_height()/4 + cosineCloudFunc*30))
                        else:
                            drawSurf0.blit(img_cloud1M, (windowSurf.get_width()/2 - img_cloud1M.get_width()/2 + windowSurf.get_width()*0.55*sineCloudFunc, 0.3*windowSurf.get_height()/4 + cosineCloudFunc*30))

            # draw the PILLAR

            pygame.draw.line(drawSurf0, [255,255,255,15], (windowSurf.get_width()/2 + sineFunc*8, -10), (windowSurf.get_width()/2 + cosineFunc*8, windowSurf.get_height() + 10), 120)
            pygame.draw.line(drawSurf0, [0,0,0,30], (windowSurf.get_width()/2, -10), (windowSurf.get_width()/2, windowSurf.get_height() + 10), 65)

            pillarWidth = 300
            i = -4
            while i < 4:
                i += 1
                cosineOffset = math.cos(2*globalRoundTimer + i)
                sineOffset = math.sin(2*globalRoundTimer + i)
                pygame.draw.line(drawSurf0, [55,0,55,150], (sineOffset*pillarWidth/2.5 + windowSurf.get_width()/2, -100), ((math.sin(2*globalRoundTimer + i + 0.4))*pillarWidth/2.5 + windowSurf.get_width()/2, windowSurf.get_height() + 100), 8)


        #### render players' parry trails
        if globalRoundTimer > 12:
            if parryState[0] > 0:
                if parryState[0] >= 0.9:
                    pygame.draw.rect(drawSurf2, (255,0,0,50), [0, p1_pos.y - 10, 25, 270], 0)
                elif parryState[0] >= 0.85:
                    pygame.draw.rect(drawSurf2, (255,0,0,20), [0, p1_pos.y - 10, 25, 270], 0)
                elif parryState[0] >= 0.75:
                    pygame.draw.rect(drawSurf2, (255,0,0,10), [0, p1_pos.y - 15, 35, 290], 0)
                elif parryState[0] >= 0.6:
                    pygame.draw.rect(drawSurf2, (255,0,0,5), [0, p1_pos.y - 25, 40, 310], 0)
                parryState[0] -= dt
            if parryState[1] > 0:
                if parryState[1] >= 0.9:
                    pygame.draw.rect(drawSurf2, (0,0,255,50), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                elif parryState[1] >= 0.85:
                    pygame.draw.rect(drawSurf2, (0,0,255,20), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                elif parryState[1] >= 0.75:
                    pygame.draw.rect(drawSurf2, (0,0,255,10), [windowSurf.get_width() - 25, p2_pos.y - 15, 35, 290], 0)
                elif parryState[1] >= 0.6:
                    pygame.draw.rect(drawSurf2, (0,0,255,5), [windowSurf.get_width() - 25, p2_pos.y - 25, 40, 310], 0)
                parryState[1] -= dt

            # take input from players and render first frame of their parry
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                if parryState[0] <= 0:
                    parryState[0] = 1
                    pygame.draw.rect(drawSurf2, (255,255,255,255), [0, p1_pos.y - 10, 25, 270], 0)
            if keys[pygame.K_w]:
                if p1_pos.y > 0:
                    p1_pos.y -= p1_speed * dt
            if keys[pygame.K_d]:
                if p1_pos.y < windowSurf.get_height() - 250:
                    p1_pos.y += p1_speed * dt

            if p2_bot == True:
                if p2_pos.y + p2_size.y/2 - ball_pos.y > 5 and p2_pos.y > 0:
                    p2_pos.y -= p2_speed * dt
                if p2_pos.y + p2_size.y/2  - ball_pos.y < -5 and p2_pos.y + p2_size.y < windowSurf.get_height():
                    p2_pos.y += p2_speed * dt
                if abs(p2_pos.x - ball_pos.x) < 30:
                    if parryState[1] <= 0:
                        parryState[1] = 1
                        pygame.draw.rect(drawSurf2, (255,255,255,255), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
            else:
                if keys[pygame.K_o]:
                    if parryState[1] <= 0:
                        parryState[1] = 1
                        pygame.draw.rect(drawSurf2, (255,255,255,255), [windowSurf.get_width() - 25, p2_pos.y - 10, 25, 270], 0)
                if keys[pygame.K_p]:
                    if p2_pos.y > 0:
                        p2_pos.y -= p2_speed * dt
                if keys[pygame.K_l]:
                    if p2_pos.y < windowSurf.get_height() - 250:
                        p2_pos.y += p2_speed * dt

            ## Render the players

            pygame.draw.rect(drawSurf2, playerColors[1], [p2_pos.x, p2_pos.y, 15, 250], 5)
            pygame.draw.rect(drawSurf2, playerColors[0], [p1_pos.x, p1_pos.y, 15, 250], 5)

            
        # draw the LYRICS
        txt_currentLyrics = PixelDigivolve.render("", False, [255,255,255,255])
        if globalRoundTimer > 23.9 and globalRoundTimer < 27.3:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[0], False, [255,255,255,150])
        elif globalRoundTimer > 27.3 and globalRoundTimer < 30.5:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[1], False, [255,255,255,150])
        elif globalRoundTimer > 30.5 and globalRoundTimer < 33.6:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[2], False, [255,255,255,150])
        elif globalRoundTimer > 33.6 and globalRoundTimer < 35.8:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[3], False, [255,255,255,150])
        elif globalRoundTimer > 35.8 and globalRoundTimer < 39.3:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[4], False, [255,255,255,150])
        elif globalRoundTimer > 39.3 and globalRoundTimer < 42.6:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[5], False, [255,255,255,150])
        elif globalRoundTimer > 42.6 and globalRoundTimer < 45.7:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[6], False, [255,255,255,150])
        elif globalRoundTimer > 45.7 and globalRoundTimer < 47.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[7], False, [255,255,255,150])
        elif globalRoundTimer > 47.2 and globalRoundTimer < 50.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[8], False, [255,255,255,150])
        elif globalRoundTimer > 50.2 and globalRoundTimer < 53.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[9], False, [255,255,255,150])
        elif globalRoundTimer > 53.1 and globalRoundTimer < 55.0:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[10], False, [255,255,255,150])
        elif globalRoundTimer > 55.0 and globalRoundTimer < 57.8:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[11], False, [255,255,255,150])
        elif globalRoundTimer > 57.8 and globalRoundTimer < 59.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[12], False, [255,255,255,150])
        elif globalRoundTimer > 59.1 and globalRoundTimer < 62.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[13], False, [255,255,255,150])
        elif globalRoundTimer > 62.1 and globalRoundTimer < 65.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[14], False, [255,255,255,150])
        elif globalRoundTimer > 65.2 and globalRoundTimer < 67.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[15], False, [255,255,255,150])
        elif globalRoundTimer > 67.1 and globalRoundTimer < 70.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[16], False, [255,255,255,150])
        elif globalRoundTimer > 70.4 and globalRoundTimer < 71.5:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[17], False, [255,255,255,150])
        elif globalRoundTimer > 71.5 and globalRoundTimer < 72.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[18], False, [255,255,255,150])
        elif globalRoundTimer > 72.4 and globalRoundTimer < 74.7:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[19], False, [255,255,255,150])
        elif globalRoundTimer > 74.7 and globalRoundTimer < 77.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[20], False, [255,255,255,150])
        elif globalRoundTimer > 77.9 and globalRoundTimer < 82.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[21], False, [255,255,255,150])
        elif globalRoundTimer > 82.4 and globalRoundTimer < 83.8:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[22], False, [255,255,255,150])
        elif globalRoundTimer > 83.8 and globalRoundTimer < 85.3:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[23], False, [255,255,255,150])
        elif globalRoundTimer > 85.3 and globalRoundTimer < 86.7:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[24], False, [255,255,255,150])
        elif globalRoundTimer > 86.7 and globalRoundTimer < 90.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[25], False, [255,255,255,150])
        elif globalRoundTimer > 90.4 and globalRoundTimer < 93.65:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[26], False, [255,255,255,150])
        elif globalRoundTimer > 93.65 and globalRoundTimer < 95.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[27], False, [255,255,255,150])
        elif globalRoundTimer > 95.9 and globalRoundTimer < 98.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[28], False, [255,255,255,150])
        elif globalRoundTimer > 98.1 and globalRoundTimer < 102:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[29], False, [255,255,255,150])
        elif globalRoundTimer > 102 and globalRoundTimer < 104.25:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[30], False, [255,255,255,150])
        elif globalRoundTimer > 104.25 and globalRoundTimer < 107.25:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[31], False, [255,255,255,150])
        elif globalRoundTimer > 107.25 and globalRoundTimer < 110.25:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[32], False, [255,255,255,150])
        elif globalRoundTimer > 110.25 and globalRoundTimer < 114:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[33], False, [255,255,255,150])
        elif globalRoundTimer > 114 and globalRoundTimer < 119.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[34], False, [255,255,255,150])
        elif globalRoundTimer > 119.2 and globalRoundTimer < 122.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[35], False, [255,255,255,150])
        elif globalRoundTimer > 122.2 and globalRoundTimer < 125.95:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[36], False, [255,255,255,150])
        elif globalRoundTimer > 125.95 and globalRoundTimer < 128.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[37], False, [255,255,255,150])
        elif globalRoundTimer > 128.2 and globalRoundTimer < 131.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[38], False, [255,255,255,150])
        elif globalRoundTimer > 131.2 and globalRoundTimer < 134.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[39], False, [255,255,255,150])
        elif globalRoundTimer > 134.1 and globalRoundTimer < 137.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[40], False, [255,255,255,150])
        elif globalRoundTimer > 137.9 and globalRoundTimer < 142.5:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[41], False, [255,255,255,150])
        elif globalRoundTimer > 143.95 and globalRoundTimer < 147.3:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[42], False, [255,255,255,150])
        elif globalRoundTimer > 147.3 and globalRoundTimer < 150.75:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[43], False, [255,255,255,150])
        elif globalRoundTimer > 150.75 and globalRoundTimer < 153.75:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[44], False, [255,255,255,150])
        elif globalRoundTimer > 153.75 and globalRoundTimer < 155.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[45], False, [255,255,255,150])
        elif globalRoundTimer > 155.9 and globalRoundTimer < 159.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[46], False, [255,255,255,150])
        elif globalRoundTimer > 159.4 and globalRoundTimer < 162.75:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[47], False, [255,255,255,150])
        elif globalRoundTimer > 162.75 and globalRoundTimer < 165.7:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[48], False, [255,255,255,150])
        elif globalRoundTimer > 165.7 and globalRoundTimer < 167.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[49], False, [255,255,255,150])
        elif globalRoundTimer > 167.2 and globalRoundTimer < 170.2:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[50], False, [255,255,255,150])
        elif globalRoundTimer > 170.2 and globalRoundTimer < 173.25:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[51], False, [255,255,255,150])
        elif globalRoundTimer > 173.25 and globalRoundTimer < 175.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[52], False, [255,255,255,150])
        elif globalRoundTimer > 175.1 and globalRoundTimer < 177.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[53], False, [255,255,255,150])
        elif globalRoundTimer > 177.9 and globalRoundTimer < 179.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[54], False, [255,255,255,150])
        elif globalRoundTimer > 179.1 and globalRoundTimer < 182.1:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[55], False, [255,255,255,150])
        elif globalRoundTimer > 182.1 and globalRoundTimer < 185.15:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[56], False, [255,255,255,150])
        elif globalRoundTimer > 185.15 and globalRoundTimer < 186.9:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[57], False, [255,255,255,150])
        elif globalRoundTimer > 186.9 and globalRoundTimer < 190.4:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[58], False, [255,255,255,150])
        elif globalRoundTimer > 190.4 and globalRoundTimer < 192:
            txt_currentLyrics = PixelDigivolve.render(lyrics_MisterBall[59], False, [255,255,255,150])


        ### handle the bg changes
        if globalRoundTimer > 47.8 and globalRoundTimer < 47.9:
            bgState = 2
        if globalRoundTimer > 96 and globalRoundTimer < 96.1:
            bgState = 0
        if globalRoundTimer > 120 and globalRoundTimer < 120.1:
            bgState = 2
        if globalRoundTimer > 165 and globalRoundTimer < 165.1:
            bgState = 0
        if globalRoundTimer > 167.9 and globalRoundTimer < 168:
            bgState = 3
        elif globalRoundTimer > 191.05:
            gameState = "resultsScreen"
        
        # else:
        #     txt_currentLyrics = PixelDigivolve.render("", False, [255,255,255,255])
        txt_currentLyrics = pygame.transform.scale(txt_currentLyrics, (txt_currentLyrics.get_width()/3, txt_currentLyrics.get_height()/3))

        drawSurf3.blit(txt_currentLyrics, (windowSurf.get_width()/2 - txt_currentLyrics.get_width()/2, 9*windowSurf.get_height()/10))

    # present the surfaces
    windowSurf.blit(bgSurf, (0,0))
    windowSurf.blit(drawSurf0, (0,0))
    windowSurf.blit(drawSurf1, (0,0))
    windowSurf.blit(drawSurf2, (0,0))
    windowSurf.blit(drawSurf3, (0,0))
    windowSurf.blit(drawSurf4, (0,0))
    pygame.display.update()

    # somehow determines the tps????? like, okay??
    dt = clock.tick(60) / 1000

pygame.font.quit()
pygame.display.quit()
pygame.mixer.quit()
pygame.quit()