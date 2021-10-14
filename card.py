class Card:
    def __init__(self, name, image):
        self.name = name
        self.image = image


class Weapon(Card):
    dagger = Card("Dagger", "dagger.png")
    candleStick = Card("Candle Stick", "candlestick.png")
    revolver = Card("Revolver", "revolver.png")
    rope = Card("Rope", "rope.png")
    leadPipe = Card("Lead Pipe", "leadPipe.png")
    wrench = Card("Wrench", "wrench.png")
    weapons = {"Dagger": dagger, "Candle Stick": candleStick, "Revolver": revolver, "Rope": rope,
               "Lead Pipe": leadPipe, "Wrench": wrench}


class Room(Card):
    diningRoom = Card("Dining Room", "diningRoom.png")
    study = Card("Study", "study.png")
    hall = Card("Hall", "hall.png")
    library = Card("Library", "library.png")
    billiardRoom = Card("Billiard Room", "billardRoom.png")
    conservatory = Card("Conservartory", "conservatory.png")
    ballRoom = Card("Ballroom", "ballRoom.png")
    kitchen = Card("Kitchen", "kitchen.png")
    lounge = Card("Lounge", "lounge.png")
    rooms = {"Dining Room": diningRoom, "Study": study, "Hall": hall, "Library": library, "Billiard Room": billiardRoom,
             "Conservatory": conservatory, "Ballroom": ballRoom, "Kitchen": kitchen, "Lounge": lounge}


class Character(Card):
    scarlet = Card("Miss Scarlet", "scarlet.png")
    mustard = Card("Col Mustard", "mustard.png")
    white = Card("Mrs White", "white.png")
    plum = Card("Prof Plum", "plum.png")
    green = Card("Rev Green", "green.png")
    peacock = Card("Mrs Peacock", "peacock.png")
    characters = {"Miss Scarlet": scarlet, "Col Mustard": mustard, "Mrs White": white, "Prof Plum": plum,
                  "Rev Green": green, "Mrs Peacock": peacock}
