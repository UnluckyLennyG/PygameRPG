import time
from Karty import *
from Stale import ekwipunek
from Gracz import Player


class DaneGry:
    def __init__(self):
        self.start = time.time()
        self.hand = []
        self.hand_sprite = pygame.sprite.Group()
        self.equipment = []
        self.equipment_sprite = pygame.sprite.Group()
        self.potwory_slot = []
        self.nagrody_sprite = pygame.sprite.Group()
        self.runda = 1
        self.win = False
        self.lose = False
        self.popmenu = 0
        self.index = 50
        self.minuty = 0
        self.ismonster = False
        self.isreward = [False, False]
        self.monster = wszystkieKarty.monster(self.runda, self)
        self.pustakartahand = PustaKartaHand()
        self.pustakartanagrody = PustaKartaNagrody()
        self.nagrody = [self.pustakartanagrody, self.pustakartanagrody]
        self.pustakartapotwora = PustaKartaPotwora()
        self.pustakartaequipment = PustaKartaEquipment()
        for x in range(9):
            self.equipment.append(self.pustakartaequipment)
        self.hand = wszystkieKarty.losuj(5)
        for x in range(len(self.hand)):
            self.hand_sprite.add(MiejsceKart(imgPath + "PustaKarta.png", [50 + x * 200, 610], x))
        for x in range(len(self.equipment)):
            self.equipment_sprite.add(MiejsceKart(imgPath + "PustaKartaEkwipunku.png", ekwipunek[x], x))
        self.nagrody_sprite.add(MiejsceKart(imgPath + "PustaKarta.png", [175 + 240, 75], 0))
        self.nagrody_sprite.add(MiejsceKart(imgPath + "PustaKarta.png", [175 + 240+185, 75], 1))
        setmaga = [MagicznaCzapka, TalizmanMaga, Rozdzka, MagicznaSzata, Palantir, Sandaly, Smok, Demon, Mag]
        setmagaend = [MagicznaCzapka, TalizmanMaga, Kostor, MagicznaSzata, self.pustakartaequipment,
                      Sandaly, Smok, Demon, Mag]
        setlowca = [HelmSkorzany, TalizmanLowcy, Miecz, ZbrojaSkorzana, Sztylet, ButySkorzane, Wilk, Elf, Lowca]
        setlowcaend = [HelmSkorzany, TalizmanLowcy, Luk, ZbrojaSkorzana, self.pustakartaequipment,
                       ButySkorzane, Wilk, Elf, Lowca]
        setwojownik = [HelmPlytowy, TalizmanWojownika, LekkiTopor, ZbrojaPlytowa, Tarcza, ButyPlytowe, Warg,
                       Krasnolud, Wojownik]
        setwojownikend = [HelmPlytowy, TalizmanWojownika, Topor, ZbrojaPlytowa, self.pustakartaequipment,
                          ButyPlytowe, Warg, Krasnolud, Wojownik]
        self.setlist = [setlowca, setlowcaend, setwojownik, setwojownikend, setmaga, setmagaend]

    def czasgry(self):
        sekundy = int(time.time() - self.start)
        if sekundy >= 59:
            self.minuty += 1
            self.start += 59
        return "Czas gry: {:02d}:{:02d}".format(self.minuty, sekundy)

    @staticmethod
    def lvlup():
        if Player.gold >= 1000:
            Player.poziom += 1
            Player.gold -= 1000

    def walcz(self):
        if self.monster.moc_bojowa < Player.moc_bojowa:
            Player.poziom += 1
            self.ismonster = False
            self.monster = self.pustakartapotwora
            self.nagrody = wszystkieKarty.losuj(2)
            self.isreward = [True, True]
            if self.runda == 10:
                self.win = True
        else:
            self.lose = True

    def sell(self):
        if self.hand[self.index] != self.pustakartahand:
            Player.gold += 350
            wszystkieKarty.Uzyte.remove(self.hand[self.index])
            self.hand[self.index] = self.pustakartahand
        self.popmenu = 0

    def sellnagroda(self, index):
        Player.gold += 350
        wszystkieKarty.Uzyte.remove(self.nagrody[index])
        self.nagrody[index] = self.pustakartanagrody
        self.isreward[index] = False

    def doeq(self, index):
        wolne_sloty = [x for x in range(len(self.hand)) if self.hand[x] == self.pustakartahand]
        if len(wolne_sloty) > 0:
            self.hand[wolne_sloty[0]] = self.nagrody[index]
            self.nagrody[index] = self.pustakartanagrody
            self.isreward[index] = False

    def equip(self):
        for x in range(len(self.equipment)):
            if isinstance(self.hand[self.index], type(sloty_eq[x])) \
                    and not isinstance(self.hand[self.index], type(Sztylet)) \
                    and not isinstance(self.hand[self.index], type(Miecz)):
                if self.equipment[x] == self.pustakartaequipment:
                    bufor = self.pustakartahand
                else:
                    bufor = self.equipment[x]
                self.equipment[x] = self.hand[self.index]
                self.hand[self.index] = bufor
                break
            #                                       SEKCJA BRONI
            elif isinstance(self.hand[self.index], type(Miecz)):
                if self.equipment[2] == self.pustakartaequipment:
                    self.equipment[2] = self.hand[self.index]
                    self.hand[self.index] = self.pustakartahand
                else:
                    bufor = self.equipment[2]
                    self.equipment[2] = self.hand[self.index]
                    self.hand[self.index] = bufor
                break
            elif isinstance(self.hand[self.index], type(Sztylet)):
                if isinstance(self.equipment[2], type(Luk)):
                    self.equipment[4] = self.hand[self.index]
                    self.hand[self.index] = self.equipment[2]
                    self.equipment[2] = self.pustakartaequipment
                else:
                    if self.equipment[4] == self.pustakartaequipment:
                        self.equipment[4] = self.hand[self.index]
                        self.hand[self.index] = self.pustakartahand
                    else:
                        bufor = self.equipment[4]
                        self.equipment[4] = self.hand[self.index]
                        self.hand[self.index] = bufor
                break
            elif isinstance(self.hand[self.index], type(Luk)):
                if self.equipment[2] == self.pustakartaequipment:
                    self.equipment[2] = self.hand[self.index]
                    self.hand[self.index] = self.pustakartahand
                else:
                    bufor = self.equipment[2]
                    self.equipment[2] = self.hand[self.index]
                    self.hand[self.index] = bufor
                if self.equipment[4] != self.pustakartaequipment:
                    bufor = self.equipment[4]
                    self.equipment[4] = self.pustakartaequipment
                    wolne_sloty = [x for x in range(len(self.hand)) if self.hand[x] == self.pustakartahand]
                    if len(wolne_sloty) > 0:
                        self.hand[wolne_sloty[0]] = bufor
                    else:
                        Player.gold += 350
                        wszystkieKarty.Uzyte.remove(bufor)
                break
        self.popmenu = 0

    def liczmoc(self):
        bonusy = 0
        moc_ekwipunku = 0
        for x in range(len(self.equipment)):
            if self.equipment[x] != self.pustakartaequipment:
                moc_ekwipunku += self.equipment[x].moc_bojowa
        if (self.equipment[7] == Elf and self.equipment[8] == Lowca) \
                or (self.equipment[7] == Krasnolud and self.equipment[8] == Wojownik) \
                or (self.equipment[7] == Demon and self.equipment[8] == Mag):
            bonusy += 1
        for x in range(6):
            if self.equipment == self.setlist[x]:
                moc_ekwipunku += 4
        Player.moc_bojowa = Player.poziom + moc_ekwipunku + bonusy
