import time

from spieler import Spieler
from immobilie import Immobilie
from werke import Werke
from bahnen import Bahnen
import sys, pygame
from spieler_mensch import Mensch
from strategie_2 import Strategie_2

pygame.init()

pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

grund = pygame.image.load("image/Spielfeld_Monopoly.png")
grund = pygame.transform.smoothscale(grund, (900, 1260))

nochnichtgekaufteimmobilien = []
verkaufteimobilien = []

player1 = Mensch()
player2 = Strategie_2()

font = pygame.font.SysFont(None, 35)
text1 = font.render("Spieler1 Vermögen:", True, "Black")
text2 = font.render("Spieler2 Vermögen:", True, "Black")
text1_1 = font.render(str(player2.geld), True, "Black")
text2_1 = font.render(str(player2.geld), True, "Black")
text3 = font.render("",True,"white")


chur = Immobilie(1, "eins", 1200, 1000, [40, 200, 600, 1800, 3200, 5000], 997, 880)
schaffhausen = Immobilie(3, "eins", 1200, 1000, [80, 400, 1200, 3600, 6400, 9000], 852, 880)

aarau = Immobilie(6, "zwei", 2000, 1000, [120, 600, 1800, 5400, 8000, 11000], 640, 880)
neuenburg = Immobilie(8, "zwei", 2000, 1000, [120, 600, 1800, 5400, 8000, 11000], 500, 880)
thun = Immobilie(9, "zwei", 2400, 1200, [160, 800, 2000, 6000, 9000, 12000], 430, 880)

basel_vorstadt = Immobilie(11, "drei", 2800, 2000, [200, 1000, 3000, 9000, 12500, 15000], 320, 730)
solothurn = Immobilie(13, "drei", 2800, 2000, [200, 1000, 3000, 9000, 12500, 15000], 320, 585)
lugano = Immobilie(14, "drei", 3200, 2000, [240, 1200, 3600, 10000, 14000, 18000], 320, 515)

biel = Immobilie(16, "vier", 3600, 2000, [280, 1400, 4000, 11000, 15000, 19000], 320, 375)
freiburg = Immobilie(18, "vier", 3600, 2000, [280, 1400, 4000, 11000, 15000, 19000], 320, 232)
lachauxdefonds = Immobilie(19, "vier", 4000, 2000, [320, 1600, 4400, 12000, 16000, 20000], 320, 160)

winterthur = Immobilie(21, "fuenf", 4400, 3000, [360, 1800, 5000, 14000, 17500, 21000], 430, 50)
stgallen = Immobilie(23, "fuenf", 4400, 3000, [360, 1800, 5000, 14000, 17500, 21000], 575, 50)
bern_bundesplatz = Immobilie(24, "fuenf", 4800, 3000, [400, 2000, 6000, 15000, 18000, 22000], 645, 50)

luzern = Immobilie(26, "sechs", 5200, 3000, [440, 2200, 6600, 16000, 19500, 23000], 788, 50)
zuerich_rennweg = Immobilie(27, "sechs", 5200, 3000, [440, 2200, 6600, 16000, 19500, 23000], 858, 50)
lausanne_ruedebourge = Immobilie(29, "sechs", 5600, 3000, [440, 2040, 7200, 17000, 20500, 24000], 1000, 50)

basel_Freiestrasse = Immobilie(31, "sieben", 6000, 4000, [520, 2600, 7800, 18000, 22000, 25000], 1150, 155)
genf = Immobilie(32, "sieben", 6000, 4000, [520, 2600, 7800, 18000, 22000, 25000], 1150, 225)
bern_spitalgasse = Immobilie(34, "sieben", 6400, 4000, [560, 3000, 9000, 20000, 24000, 28000], 1150, 365)

lausanne_place = Immobilie(37, "acht", 7000, 4000, [700, 3500, 10000, 22000, 26000, 30000], 1150, 580)
zuerich_paradeplatz = Immobilie(39, "acht", 8000, 4000, [1000, 4000, 12000, 28000, 34000, 40000], 1150, 725)

nochnichtgekaufteimmobilien.append(chur)
nochnichtgekaufteimmobilien.append(schaffhausen)
nochnichtgekaufteimmobilien.append(aarau)
nochnichtgekaufteimmobilien.append(neuenburg)
nochnichtgekaufteimmobilien.append(thun)
nochnichtgekaufteimmobilien.append(basel_vorstadt)
nochnichtgekaufteimmobilien.append(solothurn)
nochnichtgekaufteimmobilien.append(lugano)
nochnichtgekaufteimmobilien.append(biel)
nochnichtgekaufteimmobilien.append(freiburg)
nochnichtgekaufteimmobilien.append(lachauxdefonds)
nochnichtgekaufteimmobilien.append(winterthur)
nochnichtgekaufteimmobilien.append(stgallen)
nochnichtgekaufteimmobilien.append(bern_bundesplatz)
nochnichtgekaufteimmobilien.append(luzern)
nochnichtgekaufteimmobilien.append(zuerich_rennweg)
nochnichtgekaufteimmobilien.append(lausanne_ruedebourge)
nochnichtgekaufteimmobilien.append(basel_Freiestrasse)
nochnichtgekaufteimmobilien.append(genf)
nochnichtgekaufteimmobilien.append(bern_spitalgasse)
nochnichtgekaufteimmobilien.append(lausanne_place)
nochnichtgekaufteimmobilien.append(zuerich_paradeplatz)

elektrowerk = Werke(12, "werk", 3000, 320, 655)
wasserwerk = Werke(28, "werk", 3000, 927, 50)

privatbahn = Bahnen(5, "bahn", 4000, 710, 880)
bergbahn = Bahnen(15, "bahn", 4000, 320, 445)
ueberlandbahn = Bahnen(25, "bahn", 4000, 715, 50)
schwebebahn = Bahnen(35, "bahn", 4000, 1150, 435)

nochnichtgekaufteimmobilien.append(elektrowerk)
nochnichtgekaufteimmobilien.append(wasserwerk)
nochnichtgekaufteimmobilien.append(privatbahn)
nochnichtgekaufteimmobilien.append(bergbahn)
nochnichtgekaufteimmobilien.append(ueberlandbahn)
nochnichtgekaufteimmobilien.append(schwebebahn)

karten1zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # wenn alle Karten im Spiel aufgebraucht sind ist das die Liste die man zum auffüllen nehmen kann
karten2zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
karten1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
karten2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
gameon=False

def draw():
    text1_1 = font.render(str(player1.geld), True, "Black")
    text2_1 = font.render(str(player2.geld), True, "Black")
    screen.fill((255, 255, 255))
    screen.blit(grund, (300, -150))
    screen.blit(text1, (20, 30))
    screen.blit(text2, (1200, 30))
    screen.blit(text1_1, (20, 70))
    screen.blit(text2_1, (1200, 70))
    pygame.draw.circle(screen, "red", [player1.posx, player1.posy], 20)
    pygame.draw.circle(screen, "blue", [player2.posx, player2.posy], 15)
    for i in range(len(player1.gekauft)):
        if 11 > player1.gekauft[i].position > 0 or 30 > player1.gekauft[i].position > 20:
            pygame.draw.rect(screen, "red", [player1.gekauft[i].x, player1.gekauft[i].y, 74, 30])
            if player1.gekauft[i].haeuser > 0:
                text3 = font.render(str(player1.gekauft[i].haeuser), True, "white")
                screen.blit(text3, (player1.gekauft[i].x + 30, player1.gekauft[i].y + 10))
        elif 20 > player1.gekauft[i].position > 10 or 40 > player1.gekauft[i].position > 30:
            pygame.draw.rect(screen, "red", [player1.gekauft[i].x, player1.gekauft[i].y, 30, 74])
            if player1.gekauft[i].haeuser > 0:
                text3 = font.render(str(player1.gekauft[i].haeuser), True, "white")
                screen.blit(text3, (player1.gekauft[i].x + 10, player1.gekauft[i].y + 30))
    for i in range(len(player2.gekauft)):
        if 11 > player2.gekauft[i].position > 0 or 30 > player2.gekauft[i].position > 20:
            pygame.draw.rect(screen, "blue", [player2.gekauft[i].x, player2.gekauft[i].y, 74, 30])
            if player2.gekauft[i].haeuser > 0:
                text3 = font.render(str(player2.gekauft[i].haeuser), True, "white")
                screen.blit(text3, (player2.gekauft[i].x + 30, player2.gekauft[i].y + 10))
        elif 20 > player2.gekauft[i].position > 10 or 40 > player2.gekauft[i].position > 30:
            pygame.draw.rect(screen, "blue", [player2.gekauft[i].x, player2.gekauft[i].y, 30, 74])
            if player2.gekauft[i].haeuser > 0:
                text3 = font.render(str(player2.gekauft[i].haeuser), True, "white")
                screen.blit(text3, (player2.gekauft[i].x + 10, player2.gekauft[i].y + 30))
    pygame.display.flip()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameon=True

    if gameon==True:
        """""

        draw()
        time.sleep(1)

        player1.wurf_grafisch(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen, nochnichtgekaufteimmobilien, draw)
        draw()
        time.sleep(1)
        draw()
        time.sleep(1)
        for i in range(len(player1.gekauft)):
            player1.gekauft[i].bauen(player1,verkaufteimobilien)
        draw()
        if player1.geld < 0:
            while True:
                for i in range(len(player1.gekauft)):
                    player1.gekauft[i].abbauen(player1)
                    draw()
                    if player1.geld >= 0:
                        break
                if player1.geld >= 0:
                    break

        """""
        player1.wurf_grafisch(verkaufteimobilien,karten1,karten2,karten1zumauffuellen,karten2zumauffuellen,nochnichtgekaufteimmobilien,draw)
        draw()
        while True:
            draw()
            eingabe=input("aktion  bauen:b abbauen:a beenden:s")
            if eingabe == "b":
                pos=int(input("POS"))
                for i in range(len(player1.gekauft)):
                    if pos==player1.gekauft[i].position:
                        player1.gekauft[i].bauen(player1,verkaufteimobilien)
            if eingabe == "a":
                pos=int(input("POS"))
                for i in range(len(player1.gekauft)):
                    if pos==player1.gekauft[i].position:
                        player1.gekauft[i].abbauen(player1)
            if eingabe=="s":
                if player1.geld<0:
                    pygame.quit()
                else:
                    break


        time.sleep(1)
        print("xxxxxxxxxxxx")
        player2.wurf_grafisch(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen, nochnichtgekaufteimmobilien, draw)
        draw()
        time.sleep(1)
        """""
        for i in range(len(player2.gekauft)):
            player2.gekauft[i].bauen(player2,verkaufteimobilien)
        if player2.geld < 0:
            while True:
                for i in range(len(player2.gekauft)):
                    player2.gekauft[i].abbauen(player2)
                    draw()
                    if player2.geld >= 0:
                        break
                if player2.geld >= 0:
                    break
        """
        if player2.wert2 * 10000 > player2.geld:
            player2.gekauft.sort(key=lambda x: x.startwert, reverse=player2.wert3)
            for i in range(len(player2.gekauft)):
                player2.gekauft[i].bauen(player2,verkaufteimobilien)
                draw()
                if player2.wert2 * 10000 < player2.geld:
                    break

        #print(player1.geld, player2.geld)
        if player2.geld<0:
            while True:
                player2.gekauft.sort(key=lambda x: x.startwert, reverse= not player2.wert3)
                x=0
                for i in range(len(player2.gekauft)):
                    x = x + player2.gekauft[i].haeuser
                    player2.gekauft[i].abbauen(player2)
                    draw()
                    if player2.geld >= 0:
                        break
                if player2.geld >= 0:
                    break





        draw()
    else:
        draw()



