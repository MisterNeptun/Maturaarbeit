from spiel_3 import spiel_3
from spieler_3 import Spieler_3
werte1=[0,0.2,0.4,0.6,0.8,1]
werte2=[0,0.2,0.4,0.6,0.8,1]
werte3=[True,False]

auswertung=[[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
wiederholungen=0
for i1_1 in range(len(werte1)):
    for i1_2 in range(len(werte2)):
        for i1_3 in range(len(werte3)):
                    wiederholungen=0
                    for i2_1 in range(len(werte1)):
                        for i2_2 in range(len(werte2)):
                            for i2_3 in range(len(werte3)):
                                        for t in range(5):

                                            player1 = Spieler_3(werte1[i1_1], werte2[i1_2],werte3[i1_3])
                                            player2=Spieler_3(werte1[i2_1], werte2[i2_2],werte3[i2_3])
                                            if i1_1 == i2_1 and i1_2 == i2_2 and i1_3==i2_3:
                                                pass
                                            else:
                                                sieger=spiel_3(player1,player2)
                                                wiederholungen = wiederholungen + 1
                                                if sieger==1:
                                                    auswertung[i1_1][i1_2][i1_3]=auswertung[i1_1][i1_2][i1_3]+1
                                                else:
                                                    auswertung[i2_1][i2_2][i2_3] = auswertung[i2_1][i2_2][i2_3] + 1

                                            player2 = Spieler_3(werte1[i1_1], werte2[i1_2],werte3[i1_3])
                                            player1 = Spieler_3(werte1[i2_1], werte2[i2_2],werte3[i2_3])
                                            if i1_1 == i2_1 and i1_2 == i2_2 and i1_3==i2_3:
                                                pass
                                            else:
                                                sieger = spiel_3(player1, player2)
                                                wiederholungen = wiederholungen + 1
                                                if sieger == 2:
                                                    auswertung[i1_1][i1_2][i1_3] = auswertung[i1_1][i1_2][i1_3] + 1
                                                else:
                                                    auswertung[i2_1][i2_2][i2_3] = auswertung[i2_1][i2_2][i2_3] + 1
                                            print(auswertung, wiederholungen)
print(auswertung, wiederholungen)
