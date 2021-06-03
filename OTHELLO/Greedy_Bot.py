import numpy as np
import random as rn
import time




class my_greedy_bot:
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
        self.temp_field = None
        self.weight =  [[120, -20, 20, 5, 5, 20, -20, 120],
                        [-20, -40, -5, -5, -5, -5, -40, -20],
                        [20, -5, 15, 3, 3, 15, -5, 20],
                        [5, -5, 3, 3, 3, 3, -5, 5],
                        [5, -5, 3, 3, 3, 3, -5, 5],
                        [20, -5, 15, 3, 3, 15, -5, 20],
                        [-20, -40, -5, -5, -5, -5, -40, -20],
                        [120, -20, 20, 5, 5, 20, -20, 120]]


    def check_rules(self, neuer_stein, spieler, check_only=False):
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
                    self.temp_field = self.spielfeld.copy()
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
                            else:
                                self.temp_field = temp_spielfeld.copy()
                        elif self.spielfeld[y_direction][x_direction] == "empty":
                            break

                        y_direction += elem[0]
                        x_direction += elem[1]
                if richtiger_zug:
                    return True
            return False

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


    def set_next_stone(self):
        pos_zeilen = [(idr, idz) for idr, row in enumerate(self.pos_felder) for idz, zelle in enumerate(row) if zelle == "pos_f"]
        farbe = 0 if self.spieler_farbe == "black" else 1
        pos_count = len(pos_zeilen)
        max_count = 0
        best_index = rn.randint(0,pos_count - 1)
        if self.simple_Bot:
            for i in range(pos_count):
                self.check_rules(pos_zeilen[i], farbe, check_only=True)
                count_stones = np.sum((self.temp_field == self.spieler_farbe))
                if count_stones > max_count:
                    max_count = count_stones
                    best_index = i

        else:
            try:
                pos_count = len(pos_zeilen)
                max_points = -5000
                for i in range(pos_count):
                    farbe = 0 if self.spieler_farbe == "black" else 1
                    if self.check_rules(pos_zeilen[i], farbe, check_only=True) == False:
                        continue
                    self.check_rules(pos_zeilen[i], farbe, check_only=True)
                    points = self.count_points(self.temp_field, self.spieler_farbe)
                    if points > max_points:
                        max_points = points
                        best_index = i

                self.cur_choice = pos_zeilen[best_index]
            except:
                self.cur_choice = rn.choice(pos_zeilen)  # Bei jedem Bot zuerst irgendein Wert setzen, falls Timeout abgelaufen, wird dieser Wert genommen

            """
            for i in range(pos_count):
                total = 0
                self.check_rules(pos_zeilen[i], farbe, check_only=True)
                count_stones = np.sum((self.temp_field == self.spieler_farbe))
                it = np.nditer(self.temp_field, flags = ['multi_index'])
                for tile in it:
                    idx, idy = it.multi_index
                    if tile == self.spieler_farbe:
                        total += self.weight[idx][idy]
                    elif tile == self.gegner_farbe:
                        total -= self.weight[idx][idy]
                count_points = (total/2) * count_stones
                if count_points > max_points:
                        max_points = count_points
                        best_index = i
            """


        self.cur_choice = pos_zeilen[best_index]



     # Bei jedem Bot zuerst irgendein Wert setzen, falls Timeout abgelaufen, wird dieser Wert genommen




        """
        Für den Greedy-Bot wählen Sie jene Position, sodass mit dem Zug die meisten Steine zu ihren eigenen Steinen werden (also umgedreht werden).
        Mit Hilfe des Attributs simple_Bot können Sie zwei Schwierigkeitsgrade definieren, z.B. naive (wie zuvor beschrieben) oder mit Gewichtsmatrix
        als Heuristik. Beachten Sie, dass hier auch das Spielfeld zuvor übergeben wird. Damit haben Sie bzw Ihr Bot die volle Spiel-Information.
        """




