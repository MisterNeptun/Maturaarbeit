from strategie_1 import Strategie_1
from strategie_2 import Strategie_2
from strategie_3 import Strategie_3
from strategie_4 import Strategie_4
from strategie_5 import Strategie_5
from spiel_final import spiel_f

sieger=0
strategien_1=[]
strategien_2=[]
auswertung=[0,0,0,0,0]

strategien_1.append(Strategie_1)
strategien_1.append(Strategie_2)
strategien_1.append(Strategie_3)
strategien_1.append(Strategie_4)
strategien_1.append(Strategie_5)
strategien_2.append(Strategie_1)
strategien_2.append(Strategie_2)
strategien_2.append(Strategie_3)
strategien_2.append(Strategie_4)
strategien_2.append(Strategie_5)

for i in range(len(strategien_1)):

    for j in range(len(strategien_2)):
        print(auswertung)
        for t in range(1000):
            player1=strategien_1[i]()
            player2=strategien_2[j]()
            if i==j:
                pass
            else:
                sieger=spiel_f(player1,player2)
                if sieger == 1:
                    auswertung[i] = auswertung[i] + 1
                else:
                    auswertung[j] = auswertung[j] + 1

            player2 = strategien_1[j]()
            player1 = strategien_2[i]()
            if i == j:
                pass
            else:
                sieger = spiel_f(player1, player2)
                if sieger == 2:
                    auswertung[i] = auswertung[i] + 1
                else:
                    auswertung[j] = auswertung[j] + 1