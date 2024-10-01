from spiel_random_geld import spiel_r_g1, spiel_r_g2
from spieler_random import Spieler_r
from strategie_1 import Strategie_1
from strategie_2 import Strategie_2
from strategie_3 import Strategie_3
from strategie_4 import Strategie_4
from strategie_5 import Strategie_5
from strategie_6 import Strategie_6
from strategie_7 import Strategie_7
from strategie_8 import Strategie_8
from strategie_9 import Strategie_9
from strategie_10 import Strategie_10
from spiel_random_wahrscheinlichkeiten import spiel_rw_1, spiel_rw_2

strategien_g=[]
strategien_w=[]
strategien_g.append(Strategie_1)
strategien_g.append(Strategie_2)
strategien_g.append(Strategie_3)
strategien_g.append(Strategie_4)
strategien_g.append(Strategie_5)
strategien_w.append(Strategie_6)
strategien_w.append(Strategie_7)
strategien_w.append(Strategie_8)
strategien_w.append(Strategie_9)
strategien_w.append(Strategie_10)

g_a=[0,0,0,0,0]

w_a=[0,0,0,0,0]


for i in range(len(strategien_g)):
    for t in range(100):
        print(g_a,w_a)
        player1 = strategien_g[i]()
        player2 = Spieler_r()
        sieger = spiel_r_g1(player1, player2)
        if sieger == 1:
            g_a[i] = g_a[i] + 1
        else:
            pass

        player1 = Spieler_r()
        player2 = strategien_g[i]()
        sieger = spiel_r_g2(player1, player2)
        if sieger == 1:
            pass
        else:
            g_a[i] = g_a[i] + 1

for i in range(len(strategien_w)):
    for t in range(100):
        print(g_a, w_a)
        player1 = strategien_w[i]()
        player2 = Spieler_r()
        sieger = spiel_rw_1(player1, player2)
        if sieger == 1:
            w_a[i] = w_a[i] + 1
        else:
            pass

        player1 = Spieler_r()
        player2 = strategien_w[i]()
        sieger = spiel_rw_2(player1, player2)
        if sieger == 1:
            pass
        else:
            w_a[i] = w_a[i] + 1


#[180, 184, 168, 183, 177] [13, 25, 20, 15, 15]