from Stale import imgPath
import pygame
import random


class Karta:
    def __init__(self, picture_path, moc_bojowa=0):
        self.image = pygame.image.load(imgPath + picture_path)
        self.smaller_image = pygame.transform.scale(self.image, [100, 144])
        self.moc_bojowa = moc_bojowa


class PustaKartaHand(Karta):
    def __init__(self):
        super().__init__("PustaKarta.png")


class PustaKartaEquipment(Karta):
    def __init__(self):
        super().__init__("PustaKartaEkwipunku.png")


class PustaKartaPotwora(Karta):
    def __init__(self):
        super().__init__("PustaKartaPotwora.png")

class PustaKartaNagrody(Karta):
    def __init__(self):
        super().__init__("reward.png")

class MiejsceKart(pygame.sprite.Sprite):
    def __init__(self, picture_path, pozycja, index):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect[0] = pozycja[0]
        self.rect[1] = pozycja[1]
        self.index = index


class Potwor(Karta):
    def __init__(self, picture_path, moc_bojowa):
        super().__init__(picture_path, moc_bojowa)


class Rasa(Karta):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Klasa(Karta):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Przedmioty(Karta):
    def __init__(self, picture_path, moc_bojowa):
        super().__init__(picture_path, moc_bojowa)


class Bron1h1(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Bron1h2(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Bron2h(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=3):
        super().__init__(picture_path, moc_bojowa)


class Buty(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Zbroja(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Helm(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Talizman(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class Chowaniec(Przedmioty):
    def __init__(self, picture_path, moc_bojowa=1):
        super().__init__(picture_path, moc_bojowa)


class WszystkieKarty:
    def __init__(self):
        self.Karty = [Demon, Elf, Krasnolud, Mag, Lowca, Wojownik, Miecz, LekkiTopor,
                      Rozdzka, Tarcza, Sztylet, Palantir, Topor, Luk, Kostor, TalizmanWojownika,
                      TalizmanLowcy, TalizmanMaga, Warg, Wilk, Smok, ZbrojaPlytowa, ZbrojaSkorzana, MagicznaSzata,
                      HelmPlytowy, HelmSkorzany, MagicznaCzapka, Sandaly, ButyPlytowe, ButySkorzane]
        self.Uzyte = []

        self.Potwory = [Monster11, Monster12, Monster13, Monster21, Monster22, Monster23, Monster31, Monster32,
                        Monster33, Monster41, Monster42, Monster43, Monster51, Monster52, Monster53, Monster61,
                        Monster62, Monster63, Monster71, Monster72, Monster73, Monster81, Monster82, Monster83,
                        Monster91, Monster92, Monster93, Monster01, Monster02, Monster03]

    def losuj(self, x):
        wylosowane = random.sample(list(filter(lambda karta: karta not in self.Uzyte, self.Karty)), x)
        self.Uzyte += wylosowane
        return wylosowane

    def monster(self, x, dane):
        dane.ismonster = True
        return self.Potwory[random.randrange(0, 3)+(3*(x-1))]


Demon = Rasa("Demon.jpg")
Elf = Rasa("Elf.jpg")
Krasnolud = Rasa("Krasnolud.jpg")

Mag = Klasa("Mag.jpg")
Lowca = Klasa("Lucznik.jpg")
Wojownik = Klasa("Wojownik.jpg")

Miecz = Bron1h1("Miecz.jpg")
LekkiTopor = Bron1h1("LekkiTopor.jpg")
Rozdzka = Bron1h1("Rozdzka.jpg")

Tarcza = Bron1h2("Tarcza.png")
Sztylet = Bron1h2("Sztylet.jpg")
Palantir = Bron1h2("Palantir.jpg")

Topor = Bron2h("Topor.jpg", 3)
Luk = Bron2h("Luk.jpg", 3)
Kostor = Bron2h("Kostor.jpg", 3)

TalizmanWojownika = Talizman("TalizmanWoj.jpg")
TalizmanLowcy = Talizman("TalizmanLowca.jpg")
TalizmanMaga = Talizman("TalizmanMag.jpg")

Warg = Chowaniec("Warg.jpg")
Wilk = Chowaniec("Wilk.jpg")
Smok = Chowaniec("Smok.jpg")

ZbrojaPlytowa = Zbroja("Plytowazbroja.jpg")
ZbrojaSkorzana = Zbroja("Skorzanazbroja.jpg")
MagicznaSzata = Zbroja("Magicznaszata.jpg")

ButyPlytowe = Buty("Plytowebuty.jpg")
ButySkorzane = Buty("Skorzanebuty.jpg")
Sandaly = Buty("Sandaly.jpg")

HelmPlytowy = Helm("Plytowyhelm.jpg")
HelmSkorzany = Helm("Skorzanyhelm.jpg")
MagicznaCzapka = Helm("Czarodziejhelm.jpg")

sloty_eq = [HelmSkorzany, TalizmanLowcy, LekkiTopor, ZbrojaSkorzana,
            Sztylet, ButySkorzane, Wilk, Elf, Lowca]

Monster11 = Potwor("Monster11.jpg", 3)
Monster12 = Potwor("Monster12.jpg", 3)
Monster13 = Potwor("Monster13.jpg", 3)

Monster21 = Potwor("Monster21.jpg", 5)
Monster22 = Potwor("Monster22.jpg", 5)
Monster23 = Potwor("Monster23.jpg", 5)

Monster31 = Potwor("Monster31.jpg", 7)
Monster32 = Potwor("Monster32.jpg", 7)
Monster33 = Potwor("Monster33.jpg", 7)

Monster41 = Potwor("Monster41.jpg", 8)
Monster42 = Potwor("Monster42.jpg", 8)
Monster43 = Potwor("Monster43.jpg", 8)

Monster51 = Potwor("Monster51.jpg", 10)
Monster52 = Potwor("Monster52.jpg", 10)
Monster53 = Potwor("Monster53.jpg", 10)

Monster61 = Potwor("Monster51.jpg", 12)
Monster62 = Potwor("Monster62.jpg", 12)
Monster63 = Potwor("Monster63.jpg", 12)

Monster71 = Potwor("Monster51.jpg", 14)
Monster72 = Potwor("Monster52.jpg", 14)
Monster73 = Potwor("Monster53.jpg", 14)

Monster81 = Potwor("Monster51.jpg", 16)
Monster82 = Potwor("Monster52.jpg", 16)
Monster83 = Potwor("Monster53.jpg", 16)

Monster91 = Potwor("Monster51.jpg", 18)
Monster92 = Potwor("Monster52.jpg", 18)
Monster93 = Potwor("Monster53.jpg", 18)

Monster01 = Potwor("Monsterboss.jpg", 20)
Monster02 = Potwor("Monsterboss.jpg", 20)
Monster03 = Potwor("Monsterboss.jpg", 20)


wszystkieKarty = WszystkieKarty()
