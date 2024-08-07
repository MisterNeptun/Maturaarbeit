class Spieler_2():
    def __init__(self,wert1,wert2,wert3,wert4,wert5):
        self.position = 0
        self.geld = 30000
        self.pasch = 0
        self.gefängniskarten = 0
        self.posx = 1125
        self.posy = 860
        self.gekauft = []
        self.bahnen = []
        self.werke = []
        self.eins = []
        self.zwei = []
        self.drei = []
        self.vier = []
        self.fuenf = []
        self.sechs = []
        self.sieben = []
        self.acht = []
        self.gefängnis = False
        self.wert1=wert1
        self.wert2=wert2
        self.wert3=wert3
        self.wert4=wert4
        self.wert5=wert5



    def wurf(self, verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen, nochnichtgekaufteimobilien):
        import random
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a == b:
            self.pasch = self.pasch + 1
        if self.pasch == 3:
            self.pasch = 0
            self.position = 10
            self.gefängnis = True
        else:
            self.position = self.position + a + b
            if self.position > 39:
                self.position = self.position - 40
                if self.position == 0:
                    self.geld = self.geld + 8000
                else:
                    self.geld = self.geld + 4000
            if self.position == 7 or self.position == 22 or self.position == 36:
                self.chance(karten2, karten2zumauffuellen)
            if self.position == 2 or self.position == 17 or self.position == 33:
                self.kanzlei(karten1, karten1zumauffuellen)
            if self.position > 39:
                self.position = self.position - 40
                if self.position == 0:
                    self.geld = self.geld + 8000
                else:
                    self.geld = self.geld + 4000
            if self.position == 30:
                self.position = 10
                self.gefängnis = True
            if self.position == 4:
                self.geld = self.geld - 4000
            if self.position == 38:
                self.geld = self.geld - 2000
            self.bezahlen(verkaufteimobilien)
            self.kaufen(nochnichtgekaufteimobilien,verkaufteimobilien)
            if a == b and self.gefängnis == False:
                self.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,nochnichtgekaufteimobilien)
            else:
                self.pasch = 0
        if self.gefängnis == True:
            if self.gefängniskarten > 0:
                self.gefängniskarten = self.gefängniskarten - 1
            else:
                self.geld = self.geld - 1000
            self.gefängnis = False
        self.grafischeposition()

    def bezahlen(self, verkaufteimobilien):
        for i in range(len(verkaufteimobilien)):
            if self.position == verkaufteimobilien[i].position:
                if verkaufteimobilien[i].farbe == "bahn":
                    self.geld = self.geld - (500 * (2 ** (len(verkaufteimobilien[i].besitzer.bahnen) - 1)))
                    verkaufteimobilien[i].besitzer.geld = verkaufteimobilien[i].besitzer.geld + (500 * (2 ** (len(verkaufteimobilien[i].besitzer.bahnen)-1)))
                elif verkaufteimobilien[i].farbe == "werk":
                    import random
                    x = random.randint(1, 6) + random.randint(1, 6)
                    if len(verkaufteimobilien[i].besitzer.werke) == 1:
                        self.geld = self.geld - (40 * x)
                        verkaufteimobilien[i].besitzer.geld = verkaufteimobilien[i].besitzer.geld + (40 * x)
                    else:
                        self.geld = self.geld - (100 * x)
                        verkaufteimobilien[i].besitzer.geld = verkaufteimobilien[i].besitzer.geld + (100 * x)
                else:
                    self.geld = self.geld - verkaufteimobilien[i].wert
                    verkaufteimobilien[i].besitzer.geld = verkaufteimobilien[i].besitzer.geld + verkaufteimobilien[i].wert

    def kaufen(self, nochnichtgekauft, verkaufteimoblien):
        for i in range(len(nochnichtgekauft)):
            if (self.position == nochnichtgekauft[i].position and self.geld - nochnichtgekauft[i].startwert > 5000*self.wert1):
                nochnichtgekauft[i].besitzer = self
                self.gekauft.append(nochnichtgekauft[i])
                if nochnichtgekauft[i].farbe == "bahn":
                    self.bahnen.append(nochnichtgekauft[i])
                elif nochnichtgekauft[i].farbe == "werk":
                    self.werke.append(nochnichtgekauft[i])
                else:
                    if nochnichtgekauft[i].farbe == "eins":
                        self.eins.append(nochnichtgekauft[i])
                        if len(self.eins) == 2:
                            for x in range(len(self.eins)):
                                self.eins[x].preise[0] = self.eins[x].preise[0] * 2
                                self.eins[x].wert = self.eins[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "zwei":
                        self.zwei.append(nochnichtgekauft[i])
                        if len(self.zwei) == 3:
                            for x in range(len(self.zwei)):
                                self.zwei[x].preise[0] = self.zwei[x].preise[0] * 2
                                self.zwei[x].wert = self.zwei[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "drei":
                        self.drei.append(nochnichtgekauft[i])
                        if len(self.drei) == 3:
                            for x in range(len(self.drei)):
                                self.drei[x].preise[0] = self.drei[x].preise[0] * 2
                                self.drei[x].wert = self.drei[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "vier":
                        self.vier.append(nochnichtgekauft[i])
                        if len(self.vier) == 3:
                            for x in range(len(self.vier)):
                                self.vier[x].preise[0] = self.vier[x].preise[0] * 2
                                self.vier[x].wert = self.vier[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "fuenf":
                        self.fuenf.append(nochnichtgekauft[i])
                        if len(self.fuenf) == 3:
                            for x in range(len(self.fuenf)):
                                self.fuenf[x].preise[0] = self.fuenf[x].preise[0] * 2
                                self.fuenf[x].wert = self.fuenf[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "sechs":
                        self.sechs.append(nochnichtgekauft[i])
                        if len(self.sechs) == 3:
                            for x in range(len(self.sechs)):
                                self.sechs[x].preise[0] = self.sechs[x].preise[0] * 2
                                self.sechs[x].wert = self.sechs[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "sieben":
                        self.sieben.append(nochnichtgekauft[i])
                        if len(self.sieben) == 3:
                            for x in range(len(self.sieben)):
                                self.sieben[x].preise[0] = self.sieben[x].preise[0] * 2
                                self.sieben[x].wert = self.sieben[x].preise[0]
                    elif nochnichtgekauft[i].farbe == "acht":
                        self.acht.append(nochnichtgekauft[i])
                        if len(self.acht) == 2:
                            for x in range(len(self.acht)):
                                self.acht[x].preise[0] = self.acht[x].preise[0] * 2
                                self.acht[x].wert = self.acht[x].preise[0]
                self.geld = self.geld - nochnichtgekauft[i].startwert
                verkaufteimoblien.append(nochnichtgekauft[i])
                nochnichtgekauft.pop(i)
                break

    def kanzlei(self, karten1, karten1zumauffuellen):
        if len(karten1) == 0:
            import copy
            karten1 = copy.deepcopy(karten1zumauffuellen)
        import random
        x = random.randint(0, (len(karten1) - 1))
        if karten1[x] == 1:
            self.position = 40
        elif karten1[x] == 2:
            self.geld = self.geld + 500
        elif karten1[x] == 3:
            self.geld = self.geld - 2000
        elif karten1[x] == 4:
            self.geld = self.geld - 1000
        elif karten1[x] == 5:
            self.gefängniskarten = self.gefängniskarten + 1
        elif karten1[x] == 6:
            self.geld = self.geld + 4000
        elif karten1[x] == 7:
            self.geld = self.geld + 1000
        elif karten1[x] == 8:
            self.geld = self.geld + 2000
        elif karten1[x] == 9:
            self.geld = self.geld + 2000
        elif karten1[x] == 10:
            self.position = 1
        elif karten1[x] == 11:
            self.geld = self.geld - 200  # ...oder chance
        elif karten1[x] == 12:
            self.position = 10
            self.gefängnis = True
        elif karten1[x] == 13:
            self.geld = self.geld + 200
        elif karten1[x] == 14:
            self.geld = self.geld + -1000
        elif karten1[x] == 15:
            self.geld = self.geld + 400
        elif karten1[x] == 16:
            self.geld = self.geld + 200  # andere müssten noch Geld verlieren
        karten1.pop(x)

    def chance(self, karten2, karten2zumauffuellen):
        if len(karten2) == 0:
            import copy
            karten2 = copy.deepcopy(karten2zumauffuellen)

        import random
        x = random.randint(0, len(karten2) - 1)
        if karten2[x] == 1:
            self.position = 10
            self.gefängnis = True
        elif karten2[x] == 2:
            self.gefängniskarten = self.gefängniskarten + 1
        elif karten2[x] == 3:
            for i in range(len(self.gekauft)):
                if self.gekauft[i].haeuser < 5:
                    self.geld = self.geld - self.gekauft[i].haeuser * 500
                elif self.gekauft[i].haeuser == 5:
                    self.geld = self.geld - 2000
        elif karten2[x] == 4:
            if self.position > 11 and self.position < 40:
                self.geld = self.geld + 4000
            self.position = 11
        elif karten2[x] == 5:
            self.geld = self.geld - 300
        elif karten2[x] == 6:
            self.position = 40
        elif karten2[x] == 7:
            self.geld = self.geld + 3000
        elif karten2[x] == 8:
            if self.position > 15 and self.position < 40:
                self.geld = self.geld + 4000
            self.position = 15
        elif karten2[x] == 9:
            for i in range(len(self.gekauft)):
                if self.gekauft[i].haeuser < 5:
                    self.geld = self.geld - self.gekauft[i].haeuser * 800
                elif self.gekauft[i].haeuser == 5:
                    self.geld = self.geld - 2300
        elif karten2[x] == 10:
            self.geld = self.geld + 1000
        elif karten2[x] == 11:
            self.geld = self.geld - 3000
        elif karten2[x] == 12:
            self.position = 39
        elif karten2[x] == 13:
            self.geld = self.geld + 2000
        elif karten2[x] == 14:
            self.geld = self.geld - 40
        elif karten2[x] == 15:
            if self.position > 24 and self.position < 40:
                self.geld = self.geld + 4000
            self.position = 24
        elif karten2[x] == 16:
            self.position = self.position - 3
        karten2.pop(x)

    def grafischeposition(self):
        if 11 > self.position > -1:
            self.posy = 860
            self.posx = 1125 - ((self.position) * 76)
        if 21 > self.position > 10:
            self.posy = 860 - ((self.position - 10) * 76)
            self.posx = 365
        if 31 > self.position > 20:
            self.posy = 100
            self.posx = 365 + ((self.position - 20) * 76)
        if 40 > self.position > 30:
            self.posy = 100 + ((self.position - 30) * 76)
            self.posx = 1125


    def wurf_grafisch(self, verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen, nochnichtgekaufteimobilien,draw):
        import random
        import time
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a == b:
            self.pasch = self.pasch + 1
        if self.pasch == 3:
            self.pasch = 0
            self.position = 10
            self.gefängnis = True
        else:
            self.position = self.position + a + b
            if self.position > 39:
                self.position = self.position - 40
                if self.position == 0:
                    self.geld = self.geld + 8000
                else:
                    self.geld = self.geld + 4000
            if self.position == 7 or self.position == 22 or self.position == 36:
                self.grafischeposition()
                draw()
                time.sleep(0.5)
                self.chance(karten2, karten2zumauffuellen)
            if self.position == 2 or self.position == 17 or self.position == 33:
                self.grafischeposition()
                draw()
                time.sleep(0.5)
                self.kanzlei(karten1, karten1zumauffuellen)
            if self.position > 39:
                self.position = self.position - 40
                if self.position == 0:
                    self.geld = self.geld + 8000
                else:
                    self.geld = self.geld + 4000
            if self.position == 30:
                self.position = 10
                self.gefängnis = True
            if self.position == 4:
                self.geld = self.geld - 4000
            if self.position == 38:
                self.geld = self.geld - 2000
            self.bezahlen(verkaufteimobilien)
            self.kaufen(nochnichtgekaufteimobilien,verkaufteimobilien)
            if a == b and self.gefängnis == False:
                self.grafischeposition()
                draw()
                time.sleep(1)
                self.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,nochnichtgekaufteimobilien)
            else:
                self.pasch = 0
        if self.gefängnis == True:
            if self.gefängniskarten > 0:
                self.gefängniskarten = self.gefängniskarten - 1
            else:
                self.geld = self.geld - 1000
            self.gefängnis = False
        self.grafischeposition()
