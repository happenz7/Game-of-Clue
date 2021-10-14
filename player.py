from random import *
from src.card import *


class Player:

    def __init__(self, charac, real):
        """
        Class initialiser
        :param charac: Selected character
        :param boolean real: True if the character is human
        """
        self.cards = []
        self.character = charac
        self.name = charac.name
        self.real = real

    @staticmethod
    def rollDice():
        """
        Rolls the dice
        :return: a tuple containing the value of each die.
        """
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return dice1, dice2

    def checkNextPlayer(self, cards, players):
        """
        Finds the first card in the suggested card list that another player is holding.
        If no player has the card, None is returned
        :param cards: List of cards suggested
        :param players: List of players in the game
        :return: Card or None
        """
        for i, p in enumerate(players):  # Outermost loop is for finding position of current player in self.players
            if p == self:
                for j in range(1, len(players)):  # Check next player
                    if i + j > len(players) - 1: # If we go too far, loop back around
                        j = -i

                    for card in players[i + j].cards:
                        print("check card " + card.name)
                        if card in cards:
                            return card  # Will only return first card found

                    print("Check next player")
                return None  # We have checked all players, so break out of the outermost loop


class HumanPlayer(Player):
    def __init__(self, charac):
        super().__init__(charac, True)
        pass

    def suggestion(self, roomcard, weaponcard, charactercard, players):
        """
        Human player suggestion method.
        Takes input of three cards, compiles into the correct list order and checks other players
        in the game for matching cards
        :param roomcard: Suggested room
        :param weaponcard: Suggested weapon
        :param charactercard: Suggested character
        :param players: List of players in the game
        :return: Card or None
        """
        cards = [roomcard, weaponcard, charactercard]
        return self.checkNextPlayer(cards, players)  # Check if a player in the game has any of the cards suggested


    def accusation(self, roomcard, weaponcard, charactercard, envelope):
        """
        Human player accusation method
        Takes input of three cards, compiles into the correct list order and directly compares it with
        the given murder cards envelope.
        :param roomcard: Accused room
        :param weaponcard: Accused weapon
        :param charactercard: Accused character
        :param envelope: Game murder envelop (in format [room, weapon, card])
        :return: True if the accusation is correct, else False.
        """
        cards = [roomcard, weaponcard, charactercard]
        return cards == envelope

    def showCard(self, suggestedCardsHuman, chosenCard):  # showing someone else your card
        """
        Show another player, who has made a suggestion, a card of your choice (if that
        card is one that has been suggested)
        :param suggestedCardsHuman: the cards suggested by the current player
        :param chosenCard: the card chosen to be shown to the suggesting player
        :return: The players chosen card, or 0 if the player did not have a relevant card
        """

        cardsToChooseHuman = []
        for card in suggestedCardsHuman:
            if card in self.cards:
                cardsToChooseHuman.append(card)
        # Update UI with cards that can be chosen by the player
        if len(cardsToChooseHuman) > 0:
            # return UI.getChosenCard()
            print("Chosen card")
        else:
            return 0  # Player does not have any cards, signal game to ask next p


class aiPlayer(Player):
    def __init__(self, charac):
        Player.__init__(self, charac, False)


    def suggestion(self, players):
        """
        Ai player suggestion method
        Randomly picks a weapon and character card, uses current room.
        :param players: List of player in the game
        :return: shownCard the card shown the ai player
        """
        weapon = choice(list(Weapon.weapons.values()))
        room = self.curRoom
        char = choice(list(Character.characters.values()))

        suggestedCards = [weapon, room, char]

        shownCard = self.checkNextPlayer(suggestedCards, players)  # retrieve a shown card (if player is shown)
        if shownCard != 0:  # if there is a shown card, mark notebook
            self.notebook.mark(shownCard)

        return shownCard


    def accusation(self, envelope):
        """
        Ai player accusation method
        Randomly picks a weapon, room and character to accuse
        :param envelope: Game murder envelop (in format [room, weapon, card])
        :return: True if the accusation is correct, else False
        """
        # Randomly pick cards and use them for accusation
        weapon = choice(list(Weapon.weapons.values()))
        room = choice(list(Room.rooms.values()))
        char = choice(list(Character.characters.values()))

        return [room, weapon, char] == envelope


    def showCards(self, suggestedCards):
        """
        :param suggestedCards: List of another player's suggested cards
        :return: The players chosen card, or 0 if the player did not
                 have a relevant card
        """
        cardsToChoose = []  # List of cards available for the player to choose from
        for card in suggestedCards:
            if card in self.cards:
                cardsToChoose.append(card)  # if a player has a card that has been suggested, add to list
        if len(cardsToChoose) > 0:
            return choice(cardsToChoose) # pick a card at random to show
        else:
            return 0  # Player does not have any cards, signal game to ask next player
