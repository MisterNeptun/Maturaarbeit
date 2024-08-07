from spiel import spiel
from Strategie_1.spieler_1 import Spieler_1
werte1=[0.2,0.4,0.6,0.8,1]
werte2=[0.2,0.4,0.6,0.8,1]
auswertung=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
siege=0
sieger=0
w=0
for i1_1 in range(len(werte1)):
    for i1_2 in range(len(werte2)):

        w=0
        for i2_1 in range(len(werte1)):
            for i2_2 in range(len(werte2)):
                for t in range(20):

                    player1 = Spieler_1(werte1[i1_1], werte2[i1_2])
                    player2=Spieler_1(werte1[i2_1], werte2[i2_2])
                    if i1_1==i2_1 and i1_2==i2_2:
                        pass
                    else:
                        sieger=spiel(player1,player2)
                        w = w + 1
                        if sieger==1:
                            auswertung[i1_1][i1_2]=auswertung[i1_1][i1_2]+1
                    player2 = Spieler_1(werte1[i1_1], werte2[i1_2])
                    player1 = Spieler_1(werte1[i2_1], werte2[i2_2])
                    if i1_1 == i2_1 and i1_2 == i2_2:
                        pass
                    else:
                        sieger = spiel(player1, player2)
                        w = w + 1
                        if sieger == 2:
                            auswertung[i1_1][i1_2] = auswertung[i1_1][i1_2] + 1
                    print(auswertung, w)
print(auswertung,w)
