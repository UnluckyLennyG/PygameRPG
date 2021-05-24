import pygame
from Stale import imgPath, Screen_height, Screen_width, kolor2, kolor, ekwipunek
from Gracz import Player


class Cursor(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Button:
    def __init__(self, image):
        self.image = pygame.image.load(imgPath+image)


buttonsell = Button("Buttonsprzedaj.jpg")
buttonequip = Button("Buttonzaloz.jpg")
buttonlvlup = Button("Buttonlvlup.png")
buttonfight = Button("ButtonWalcz.jpg")
buttontohand = Button("Buttontohand.jpg")


class Rysuj:
    def __init__(self):
        self.Screen = pygame.display.set_mode([Screen_width, Screen_height])
        self.cursor = Cursor(imgPath + "cursor.png")
        self.smallFont = pygame.font.SysFont('Corbell', 35)
        self.largeFont = pygame.font.SysFont('Corbell', 70)
        self.cursorGroup = pygame.sprite.GroupSingle(self.cursor)

    def rysujmenu(self, buttoncolor, button2color):
        self.Screen.fill(kolor)
        self.Screen.blit(self.largeFont.render('Python RPG', True, (0, 0, 0)), (650, 50))
        pygame.draw.rect(self.Screen, buttoncolor, [600, 200, 400, 100])
        pygame.draw.rect(self.Screen, button2color, [600, 400, 400, 100])
        self.Screen.blit(self.largeFont.render('Start gry', True, (0, 0, 0)), (700, 220))
        self.Screen.blit(self.largeFont.render('Zamknij gre', True, (0, 0, 0)), (660, 420))
        self.cursor.update()
        self.cursorGroup.draw(self.Screen)
        pygame.display.flip()

    def rysujgre(self, dane):
        self.Screen.fill(kolor)
        for x in range(len(dane.hand)):
            self.Screen.blit(dane.hand[x].image, [50 + x * 200, 610])
        for x in range(len(ekwipunek)):
            if dane.equipment[x] == dane.pustakartaequipment:
                self.Screen.blit(dane.equipment[x].image, ekwipunek[x])
            else:
                self.Screen.blit(dane.equipment[x].smaller_image, ekwipunek[x])

        if dane.popmenu == 1:
            p = 50 + dane.index * 200
            self.Screen.blit(buttonequip.image, [p, 490])
            self.Screen.blit(buttonsell.image, [p, 550])
        if 1 == 1:
            monster = dane.monster
            self.Screen.blit(monster.image, (175, 75))
        nastepna_runda = self.smallFont.render("Następna runda", True, (255, 255, 255))
        pygame.draw.rect(self.Screen, kolor2, [Screen_width - 205, Screen_height / 3, 200, 70])
        self.Screen.blit(nastepna_runda, (Screen_width - 200, Screen_height / 3 + 25))
        czas_gry = self.smallFont.render(dane.czasgry(), True, (255, 255, 255))
        numer_rundy = self.smallFont.render("runda: {}".format(dane.runda), True, (255, 255, 255))
        pygame.draw.rect(self.Screen, kolor2, (Screen_width - 150, 37, 150, 50))
        dane.nagrody_sprite.draw(self.Screen)
        self.Screen.blit(numer_rundy, (Screen_width - 120, 50))
        self.Screen.blit(czas_gry, (Screen_width - 186, 10))
        self.Screen.blit(self.smallFont.render("Moc bojowa: {}".format(Player.moc_bojowa), True, (255, 255, 255)),
                         (Screen_width-530, 680))
        self.Screen.blit(self.smallFont.render("Złoto: {:04d}".format(Player.gold), True, (255, 255, 255)),
                         (Screen_width - 530, 632))
        if Player.gold >= 1000:
            self.Screen.blit(buttonlvlup.image, [Screen_width-400, 630])
        for x in range(2):
            self.Screen.blit(dane.nagrody[x].image, (415 + x * 185, 75))
        for x in range(2):
            if dane.isreward[x]:
                self.Screen.blit(buttonsell.image, [x*185+175 + 240, 75+270])
                self.Screen.blit(buttontohand.image, [x*185+175 + 240, 75+270+60])
        self.Screen.blit(buttonfight.image, [175, 405])
        dane.hand_sprite.draw(self.Screen)
        dane.equipment_sprite.draw(self.Screen)
        dane.nagrody_sprite.draw(self.Screen)
        self.Screen.blit(dane.pustakartapotwora.image, (175, 75))
        self.cursor.update()
        self.cursorGroup.draw(self.Screen)
        pygame.display.flip()

    def rysujekrankoncowy(self, button2color):
        self.Screen.fill((128, 128, 128))
        self.Screen.blit(self.largeFont.render('Python RPG', True, (0, 0, 0)), (650, 50))
        pygame.draw.rect(self.Screen, kolor, [Screen_width / 2 - 200, 200, 400, 100])
        self.Screen.blit(self.largeFont.render('Gratuluję wygranej!', True, (0, 0, 0)), (Screen_width / 2 - 255, 220))
        pygame.draw.rect(self.Screen, button2color, [600, 400, 400, 100])
        self.Screen.blit(self.largeFont.render('Zamknij gre', True, (0, 0, 0)), (635, 420))
        self.cursorGroup.draw(self.Screen)
        self.cursorGroup.update()
        pygame.display.flip()

    def rysujekranprzegranej(self, button2color):
        self.Screen.fill((128, 128, 128))
        self.Screen.blit(self.largeFont.render('Python RPG', True, (0, 0, 0)), (650, 50))
        pygame.draw.rect(self.Screen, kolor, [Screen_width / 2 - 200, 200, 400, 100])
        self.Screen.blit(self.largeFont.render('Nie zawsze się wygrywa.', True, (0, 0, 0)), (500, 220))
        pygame.draw.rect(self.Screen, button2color, [600, 400, 400, 100])
        self.Screen.blit(self.largeFont.render('Zamknij gre', True, (0, 0, 0)), (645, 420))
        self.cursorGroup.draw(self.Screen)
        self.cursorGroup.update()
        pygame.display.flip()
