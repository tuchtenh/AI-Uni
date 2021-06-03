import numpy as np
import time
import random


class my_random_bot:
    def __init__(self, spieler_farbe):
        self.farbe = spieler_farbe
        self.pos_felder = None
        self.cur_choice = None
        self.timeout = False

    def set_next_stone(self):
        pos_zeilen = [(idr, idz) for idr, row in enumerate(self.pos_felder) for idz, zelle in enumerate(row) if zelle == "pos_f"]
        self.cur_choice = random.choice(pos_zeilen)
        #self.cur_choice = pos_zeilen[0]     # Bei jedem Bot zuerst irgendein Wert setzen, falls Timeout abgelaufen, wird dieser Wert genommen
        """
        Wählen Sie für den Random-Bot zufällig ein Element aus pos_zeilen und übergeben Sie diesen Wert dem Attribut self.cur_choice
        """




