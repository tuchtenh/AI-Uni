import numpy as np
import time


class my_bot:
    def __init__(self, spieler_farbe, simple_Bot):
        self.spieler_farbe = spieler_farbe
        if self.spieler_farbe == "black":
            self.gegner_farbe = "white"
        else:
            self.gegner_farbe = "black"
        self.spielfeld = None
        self.pos_felder = None
        self.cur_choice = None
        self.timeout = False
        self.simple_Bot = simple_Bot
        self.weight = [[100,-10,11,6,6,11,-10,100],
                       [-10,-20,1,2,2,1,-20,-10],
                       [10,1,5,4,4,5,1,10],
                       [6,2,4,2,2,4,2,6],
                       [6,2,4,2,2,4,2,6],
                       [10,1,5,4,4,5,1,10],
                       [-10,-20,1,2,2,1,-20,-10],
                       [100,-10,11,6,6,11,-10,100]]


    def check_rules(self, neuer_stein, spieler, check_only=True):
        """
        :param neuer_stein: Tupel von der Form (x,y) mit x und y im Intervall [0,7]. Wobei x der Spalte
                            und y der Zeile entspricht. Beispiel: self.spielfeld[y][x]
                            Zum aktualisieren des Spielfeldes genügt es, wenn sie das Array self.spielfeld aktualisieren, das
                            heißt, Sie müssen nicht die Methode update_spielfeld aufrufen.
        :param spieler: Entspricht dem aktuellen Spieler 0 steht für "black" 1 für "white"
        :param check_only: optinaler Parameter.
                            Wenn der Zug zulässig ist und check_only=False, dann soll self.spielfeld
                            aktualisiert werden. check_only=True, dann wird self.spielfeld nicht aktualisiert
        :return: True, wenn neuer_stein für spieler ein zulässiger Zug ist, Flase sonst
        """
        idx, idy = neuer_stein
        akt_farbe = "black" if spieler == 0 else "white"
        gegner_farbe = "black" if ((spieler + 1) % 2) == 0 else "white"

        # print("\nidy, idx =", idy, idx)
        # print("self.spielfeld[idy][idx] =", self.spielfeld[idy][idx])

        if not self.spielfeld[idy][idx] == "empty":
            return False
        else:
            possible_directions = []  # von (-1,-1) bis (1,1)
            for row in np.arange(max(idy - 1, 0), min(idy + 2, 8), 1):
                for zelle in np.arange(max(idx - 1, 0), min(idx + 2, 8), 1):
                    if not (row == idy and zelle == idx) and self.spielfeld[row][zelle] == gegner_farbe:
                        # print("(row-idy, zelle-idx) =", (row-idy, zelle-idx))
                        possible_directions.append((row - idy, zelle - idx))
            if len(possible_directions) > 0:
                richtiger_zug = False
                for elem in possible_directions:
                    schluss_stein_gefunden = False
                    temp_spielfeld = self.spielfeld.copy()
                    y_direction = idy + elem[0]
                    x_direction = idx + elem[1]
                    while y_direction in range(8) and x_direction in range(8) and not schluss_stein_gefunden:
                        if self.spielfeld[y_direction][x_direction] == gegner_farbe:
                            temp_spielfeld[y_direction][x_direction] = akt_farbe
                        elif self.spielfeld[y_direction][x_direction] == akt_farbe:
                            schluss_stein_gefunden = True
                            richtiger_zug = True
                            if not check_only:
                                self.spielfeld = temp_spielfeld.copy()
                        elif self.spielfeld[y_direction][x_direction] == "empty":
                            break

                        y_direction += elem[0]
                        x_direction += elem[1]
                if richtiger_zug:
                    return temp_spielfeld.copy()
            return False

    def set_next_stone(self):
        pos_zeilen = [(idr, idz) for idr, row in enumerate(self.pos_felder) for idz, zelle in enumerate(row) if zelle == "pos_f"]

        try:
            pos_count = len(pos_zeilen)
            #print("pos_count: ", pos_count)
            max_points = -5000
            best_index = 0
            for i in range(pos_count):
                points = 0
                farbe = 0 if self.spieler_farbe == "black" else 1
                if self.check_rules(pos_zeilen[i], farbe, check_only = True) == False:
                    continue
                temp_feld = self.check_rules(pos_zeilen[i], farbe, check_only = True)
                points = self.count_points(temp_feld,self.spieler_farbe)
                if points > max_points:
                    max_points = points
                    best_index = i
                
            #print("try") 
            #print("best_index: ", best_index)
            #print("max_points: ", max_points)
            self.cur_choice = pos_zeilen[best_index]   
        except:
            #print("execpt")
            self.cur_choice = pos_zeilen[0]  # Bei jedem Bot zuerst irgendein Wert setzen, falls Timeout abgelaufen, wird dieser Wert genommen
        


    def count_points(self, feld, farbe):
        points = 0
        my_farbe = farbe
        enemy_farbe = "black" if my_farbe == "white" else "white"
        for row in range(8):
            for zelle in range(8):
                if feld[row][zelle] == my_farbe:
                    points += self.weight[row][zelle]
                elif feld[row][zelle] == enemy_farbe:
                    points -= self.weight[row][zelle]
        return points
        



