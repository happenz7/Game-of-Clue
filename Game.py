from src.player import *
from src.card import *
from random import randint, choice, shuffle


class Game:
    def __init__(self):
        self.curPlayer = None
        self.players = []
        self.murderCards = None

    def addPlayer(self, character):
        """
        Adds a player to the current game
        :param character: Character card the player is playing as
        """
        print("Adding player " + character.name)
        self.players.append(HumanPlayer(character))

    def sortCards(self):
        """
        Creates the murder envelope and deals the cards out to players in the game
        """
        # Creating list copies of the dictionaries from card class
        weapons = list(Weapon.weapons.values())
        rooms = list(Room.rooms.values())
        characters = list(Character.characters.values())

        p1 = choice(rooms)
        p2 = choice(weapons)
        p3 = choice(characters)

        self.murderCards = [p1, p2, p3]  # Randomly pick a card from each category and create the murder envelope

        # Remove the murder cards from rest of deck
        rooms.remove(p1)
        weapons.remove(p2)
        characters.remove(p3)

        # Combine all cards and shuffle the deck
        allCards = weapons + rooms + characters
        shuffle(allCards)

        p = 0
        while len(allCards) > 0:  # Deal all the cards out to players
            if p > len(self.players) - 1: # Reached end of list so loop back round
                p = 0
            else:
                self.players[p].cards.append(allCards.pop()) # Deal the top card
                p += 1

        print(len(allCards))  # Should always be 0, indicating all cards have been dealt


    def start(self):
        """
        Initialises the current player as the first player in the list
        """
        self.curPlayer = self.players[0]
        print(self.curPlayer.name)

    def nextPlayer(self):
        """
        Changes the current player to the next player
        """
        c = 0
        for i, p in enumerate(self.players):    # Find the place of the current player in the player list
            if p == self.curPlayer:
                c = i
                break

        if c + 1 > len(self.players) - 1: # Reached end of list so loop back round
            self.curPlayer = self.players[0]
        else:
            self.curPlayer = self.players[c + 1]

        print(self.curPlayer.name)

    def restart(self):
        """
        Resets all instance variables
        """
        self.curPlayer = None
        self.players = []
        self.murderCards = None

