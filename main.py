import sys
import pygame
from Rysowanie import Rysuj
from Stale import Screen_width, Screen_height
from Gra import DaneGry
from Karty import wszystkieKarty


#                                                  GENERAL SETUP

pygame.init()
pygame.display.set_caption("Python RPG")
clock = pygame.time.Clock()
clock.tick(60)
pygame.mouse.set_visible(False)


Ekran = ["MainMenu", "EkranGry", "EkranKoncowy"]
ekran = Ekran[0]

rysuj = Rysuj()
#                                                   MAIN LOOP
kolor = (0, 0, 0)
kolor2 = (0, 0, 0)
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ekran == "MainMenu" and \
                    Screen_width / 2 - 193 <= pygame.mouse.get_pos()[0] <= Screen_width / 2 + 205 and \
                    215 <= pygame.mouse.get_pos()[1] <= 315:
                Dane = DaneGry()
                ekran = Ekran[1]
            if(ekran == "MainMenu" or ekran == "EkranKoncowy" or ekran == "ekranPrzegranej") and Screen_width / 2 - 193\
                    <= pygame.mouse.get_pos()[0] <= Screen_width / 2 + 205 and 415 <= pygame.mouse.get_pos()[1] <= 515:
                pygame.quit()
                sys.exit()
            if ekran == "EkranGry" and Screen_width - 194 <= pygame.mouse.get_pos()[0] <= Screen_width - 34 and \
                    Screen_height / 3 + 15 <= pygame.mouse.get_pos()[1] <= Screen_height / 3 + 95\
                    and not Dane.ismonster:
                Dane.runda += 1
                Dane.monster = wszystkieKarty.monster(Dane.runda, Dane)
            if ekran == "EkranGry" and 415 <= pygame.mouse.get_pos()[0] <= 775:
                for x in range(2):
                    if Dane.isreward[x]:
                        pos_x, pos_y = pygame.mouse.get_pos()
                        index = int((pos_x-415)/185)
                        if x*185+415 <= pos_x <= x*185+549 and 345 <= pos_y <= 395:
                            Dane.sellnagroda(index)
                        if x * 185 + 415 <= pos_x <= x * 185 + 549 and 405 <= pos_y <= 455:
                            Dane.doeq(index)
            if ekran == "EkranGry" and Screen_width-400 <= pygame.mouse.get_pos()[0] <= Screen_width-375 and\
                    630 <= pygame.mouse.get_pos()[1] <= 655:
                Dane.lvlup()
            if ekran == "EkranGry":
                x, y = pygame.mouse.get_pos()
                if 175 <= x <= 400 and 405 <= y <= 455 and Dane.ismonster:
                    Dane.walcz()
            if ekran == "EkranGry":
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 1025 and 610 <= y <= 863:
                    if int((x-50)/200) == int((x-25)/200):
                        Dane.index = int((x-50)/200)
                        Dane.popmenu = 1
                p = 50 + Dane.index * 200
                if p <= pygame.mouse.get_pos()[0] <= p+175:
                    if 490 <= pygame.mouse.get_pos()[1] <= 540:
                        Dane.equip()
                    if 550 <= pygame.mouse.get_pos()[1] <= 600:
                        Dane.sell()

        if ekran == "MainMenu" and Screen_width / 2 - 193 <= pygame.mouse.get_pos()[0] <= Screen_width / 2 + 205 and \
                215 <= pygame.mouse.get_pos()[1] <= 315:
            kolor = (100, 100, 100)
        else:
            kolor = (128, 128, 128)
        if (ekran == "MainMenu" or ekran == "EkranKoncowy" or ekran == "EkranPrzegranej")\
                and Screen_width / 2 - 193 <= pygame.mouse.get_pos()[0] <= Screen_width / 2 + 205 and \
                415 <= pygame.mouse.get_pos()[1] <= 515:
            kolor2 = (100, 100, 100)
        else:
            kolor2 = (128, 128, 128)

    if ekran == "MainMenu":
        rysuj.rysujmenu(kolor, kolor2)

    if ekran == "EkranGry":
        rysuj.rysujgre(Dane)
        Dane.liczmoc()
        if Dane.win:
            ekran = "EkranKoncowy"
        if Dane.lose:
            ekran = "EkranPrzegranej"
    if ekran == "EkranKoncowy":
        rysuj.rysujekrankoncowy(kolor2)
    if ekran == "EkranPrzegranej":
        rysuj.rysujekranprzegranej(kolor2)
