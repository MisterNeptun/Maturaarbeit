def spiel_rw_1(player1,player2):
        import copy

        import M


        from M import A
        from M import wahrscheinlichkeiten
        from immobilie import Immobilie
        from werke import Werke
        from bahnen import Bahnen
        wahrschwinlichkeit1 = []
        wahrschwinlichkeit2 = []

        x = 0
        nochnichtgekaufteimmobilien = []
        verkaufteimobilien = []

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
        alleimmobilien = copy.deepcopy(nochnichtgekaufteimmobilien)
        alleimmobilien.sort(key=lambda x: x.position, reverse=False)

        karten1zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                16]  # wenn alle Karten im Spiel aufgebraucht sind ist das die Liste die man zum auffüllen nehmen kann
        karten2zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        karten1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        karten2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        for i in range(10000):
            wahrschwinlichkeit1 = M.wahrscheinlichkeiten(player1.wert2, player2.position, M.A)
            for i in range(len(alleimmobilien)):
                alleimmobilien[i].wahrscheinlichkeit = wahrschwinlichkeit1[alleimmobilien[i].position]
            player1.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,
                         nochnichtgekaufteimmobilien)

            player1.gekauft.sort(key=lambda x: x.wahrscheinlichkeit, reverse=True)
            for i in range(len(player1.gekauft)):
                if player1.gekauft[i].wahrscheinlichkeit > player1.wert1:
                    player1.gekauft[i].bauen(player1, verkaufteimobilien)

            # print(player1.geld, player2.geld)
            if player1.geld < 0:
                while True:
                    player1.gekauft.sort(key=lambda x: x.wahrscheinlichkeit, reverse=False)
                    x = 0
                    for i in range(len(player1.gekauft)):
                        x = x + player1.gekauft[i].haeuser
                        player1.gekauft[i].abbauen(player1)
                        if player1.geld >= 0:
                            break
                    if player1.geld >= 0:
                        break

                    if x == 0:
                        # print(len(player1.gekauft), player1.wert1, len(player2.gekauft), player2.wert1)
                        # print(player1.geld, player2.geld)
                        return 2


            player2.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,
                         nochnichtgekaufteimmobilien)
            if player2.random_funktion == True:

                for i in range(len(player2.gekauft)):
                    player2.gekauft[i].bauen(player2, verkaufteimobilien)
                    if player2.random_funktion == True:
                        break

            # print(player1.geld, player2.geld)
            if player2.geld < 0:
                while True:

                    x = 0
                    for i in range(len(player2.gekauft)):
                        x = x + player2.gekauft[i].haeuser
                        player2.gekauft[i].abbauen(player2)
                        if player2.geld >= 0:
                            break
                    if player2.geld >= 0:
                        break

                    if x == 0:
                        # print(len(player1.gekauft), player1.wert1, len(player2.gekauft), player2.wert1)
                        # print(player1.geld, player2.geld)
                        return 1
            # print(player1.geld, player2.geld)
        if player1.geld > player2.geld:
            return 1
        else:
            return 2

def spiel_rw_2(player1,player2):
        import copy

        import M


        from M import A
        from M import wahrscheinlichkeiten
        from immobilie import Immobilie
        from werke import Werke
        from bahnen import Bahnen
        wahrschwinlichkeit1 = []
        wahrschwinlichkeit2 = []

        x = 0
        nochnichtgekaufteimmobilien = []
        verkaufteimobilien = []

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
        alleimmobilien = copy.deepcopy(nochnichtgekaufteimmobilien)
        alleimmobilien.sort(key=lambda x: x.position, reverse=False)

        karten1zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                16]  # wenn alle Karten im Spiel aufgebraucht sind ist das die Liste die man zum auffüllen nehmen kann
        karten2zumauffuellen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        karten1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        karten2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        for i in range(10000):
            player1.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,
                         nochnichtgekaufteimmobilien)
            if player1.random_funktion == True:
                for i in range(len(player1.gekauft)):
                    player1.gekauft[i].bauen(player1, verkaufteimobilien)
                    if player2.random_funktion == True:
                        break

            # print(player1.geld, player2.geld)
            if player1.geld < 0:
                while True:
                    x = 0
                    for i in range(len(player1.gekauft)):
                        x = x + player1.gekauft[i].haeuser
                        player1.gekauft[i].abbauen(player1)
                        if player1.geld >= 0:
                            break
                    if player1.geld >= 0:
                        break

                    if x == 0:
                        # print(len(player1.gekauft), player1.wert1, len(player2.gekauft), player2.wert1)
                        # print(player1.geld, player2.geld)
                        return 2

            wahrschwinlichkeit2 = M.wahrscheinlichkeiten(player2.wert2, player1.position, M.A)
            for i in range(len(alleimmobilien)):
                alleimmobilien[i].wahrscheinlichkeit = wahrschwinlichkeit2[alleimmobilien[i].position]
            player2.wurf(verkaufteimobilien, karten1, karten2, karten1zumauffuellen, karten2zumauffuellen,
                         nochnichtgekaufteimmobilien)

            player2.gekauft.sort(key=lambda x: x.wahrscheinlichkeit, reverse=True)
            for i in range(len(player2.gekauft)):
                if player2.gekauft[i].wahrscheinlichkeit > player2.wert1:
                    player2.gekauft[i].bauen(player2, verkaufteimobilien)

            # print(player1.geld, player2.geld)
            if player2.geld < 0:
                while True:
                    player2.gekauft.sort(key=lambda x: x.wahrscheinlichkeit, reverse=False)
                    x = 0
                    for i in range(len(player2.gekauft)):
                        x = x + player2.gekauft[i].haeuser
                        player2.gekauft[i].abbauen(player2)
                        if player2.geld >= 0:
                            break
                    if player2.geld >= 0:
                        break

                    if x == 0:
                        # print(len(player1.gekauft), player1.wert1, len(player2.gekauft), player2.wert1)
                        # print(player1.geld, player2.geld)
                        return 1
            # print(player1.geld, player2.geld)
        if player1.geld > player2.geld:
            return 1
        else:
            return 2


