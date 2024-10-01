from spiel_4 import spiel_4
from spieler_4 import Spieler_4
werte1=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]
werte2=[1,2,3,4,5,6,7,8,9,10]




auswertung=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
wiederholungen=0
for i1_1 in range(len(werte1)):
    for i1_2 in range(len(werte2)):

                    wiederholungen=0
                    for i2_1 in range(len(werte1)):
                        for i2_2 in range(len(werte2)):

                                        for t in range(5):

                                            player1 = Spieler_4(werte1[i1_1], werte2[i1_2])
                                            player2=Spieler_4(werte1[i2_1], werte2[i2_2])
                                            if i1_1 == i2_1 and i1_2 == i2_2:
                                                pass
                                            else:
                                                sieger=spiel_4(player1,player2)
                                                wiederholungen = wiederholungen + 1
                                                if sieger==1:
                                                    auswertung[i1_1][i1_2]=auswertung[i1_1][i1_2]+1
                                                else:
                                                    auswertung[i2_1][i2_2] = auswertung[i2_1][i2_2] + 1

                                            player2 = Spieler_4(werte1[i1_1], werte2[i1_2])
                                            player1 = Spieler_4(werte1[i2_1], werte2[i2_2])
                                            if i1_1 == i2_1 and i1_2 == i2_2 :
                                                pass
                                            else:
                                                sieger = spiel_4(player1, player2)
                                                wiederholungen = wiederholungen + 1
                                                if sieger == 2:
                                                    auswertung[i1_1][i1_2] = auswertung[i1_1][i1_2] + 1
                                                else:
                                                    auswertung[i2_1][i2_2] = auswertung[i2_1][i2_2] + 1
                                            print(auswertung, wiederholungen)
print(auswertung, wiederholungen)
