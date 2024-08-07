class Bahnen():
    def __init__(self, pos, farbe, startwert,x,y):
        self.position = pos
        self.farbe = farbe
        self.startwert = startwert
        self.besitzer = ""
        self.haeuser=0
        self.x = x
        self.y = y
        self.wert=0
        self.wahrscheinlichkeit = 0

    def bauenueberpruefen(self, spieler, verkaufteimmobilien):
        return False


    def bauen(self,spieler,verkaufteimobilien):
        pass

    def abbauen(self,spieler):
        pass

