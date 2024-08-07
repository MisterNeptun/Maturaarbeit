class Immobilie():
    def __init__(self, pos, farbe, startwert, haeuserpreise, preisliste, x, y):
        self.position = pos
        self.farbe = farbe
        self.startwert = startwert
        self.besitzer = ""
        self.haeuserpreise = haeuserpreise
        self.haeuser = 0
        self.preise = preisliste
        self.wert = self.preise[0]
        self.x = x
        self.y = y
        self.wahrscheinlichkeit=0

    def bauen(self, spieler,verkaufteimmobilien):
        if self.bauenueberpruefen(spieler, verkaufteimmobilien) == True :
            if self.haeuser < 5 and spieler.geld - self.haeuserpreise > 0:
                spieler.geld = spieler.geld - self.haeuserpreise
                self.haeuser = self.haeuser + 1
                self.wert = int(self.preise[self.haeuser])

    def abbauen(self, spieler):
        if self.abbauenueberpruefen(spieler)==True:
            if self.haeuser > 0:
                spieler.geld = spieler.geld + 0.5 * self.haeuserpreise
                self.haeuser = self.haeuser - 1
                self.wert = int(self.preise[self.haeuser])

    def bauenueberpruefen(self, spieler, verkaufteimmobilien):
        häuser=0
        hotels=0
        for i in range(len(verkaufteimmobilien)):
            if verkaufteimmobilien[i].haeuser<5:
                häuser=häuser+verkaufteimmobilien[i].haeuser
        for i in range(len(verkaufteimmobilien)):
            if verkaufteimmobilien[i].haeuser==5:
                hotels=hotels+1
        if (häuser<32 and self.haeuser<4) or (self.haeuser==4 and hotels<12):
            if self.farbe == "eins":
                if len(spieler.eins) == 2:
                    for i in range(len(spieler.eins)):
                        if spieler.eins[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "zwei":
                if len(spieler.zwei) == 3:
                    for i in range(len(spieler.zwei)):
                        if spieler.zwei[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "drei":
                if len(spieler.drei) == 3:
                    for i in range(len(spieler.drei)):
                        if spieler.drei[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "vier":
                if len(spieler.vier) == 3:
                    for i in range(len(spieler.vier)):
                        if spieler.vier[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "fuenf":
                if len(spieler.fuenf) == 3:
                    for i in range(len(spieler.fuenf)):
                        if spieler.fuenf[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "sechs":
                if len(spieler.sechs) == 3:
                    for i in range(len(spieler.sechs)):
                        if spieler.sechs[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "sieben":
                if len(spieler.sieben) == 3:
                    for i in range(len(spieler.sieben)):
                        if spieler.sieben[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            elif self.farbe == "acht":
                if len(spieler.acht) == 2:
                    for i in range(len(spieler.acht)):
                        if spieler.acht[i].haeuser < self.haeuser:
                            return False

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def abbauenueberpruefen(self, spieler):
        if self.farbe == "eins":
            for i in range(len(spieler.eins)):
                if spieler.eins[i].haeuser > self.haeuser:
                    return False
            return True

        elif self.farbe == "zwei":
            for i in range(len(spieler.zwei)):
                if spieler.zwei[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "drei":
            for i in range(len(spieler.drei)):
                if spieler.drei[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "vier":
            for i in range(len(spieler.vier)):
                if spieler.vier[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "fuenf":
            for i in range(len(spieler.fuenf)):
                if spieler.fuenf[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "sechs":
            for i in range(len(spieler.sechs)):
                if spieler.sechs[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "sieben":
            for i in range(len(spieler.sieben)):
                if spieler.sieben[i].haeuser > self.haeuser:
                    return False
            return True
        elif self.farbe == "acht":
            for i in range(len(spieler.acht)):
                if spieler.acht[i].haeuser > self.haeuser:
                    return False
            return True
        else:
            return False
