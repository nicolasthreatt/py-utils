'''
Mediator
    - Manages communcations among objects
	- Loose coupling
	- Better maintainabiliy
'''

import sys


class Player(object):
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def getName(self):
        return self._name

    def send(self, msg):
        pass

    def receive(self, msg):
        pass


class ConcretePlayer(Player):
    def __init__(self, mediator, name):
        super().__init__(mediator, name)

    def send(self, msg):
        print("Message '" + msg + "' sent by Player " + str(self._name))
        self._mediator.distribute(self, msg)

    def receive(self, msg):
        print("Message '" + msg + "' received by Player " + str(self._name))


class Mediator:
    def add(self, Player):
        pass

    def distribute(self, sender, msg):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self._player = list()

    def add(self, player):
        self._player.append(player)

    def distribute(self, sender, msg):
        for player in self._player:
            if player.getName() != sender.getName():
                player.receive(msg)


def main():
    mediator = ConcreteMediator()

    p1 = ConcretePlayer(mediator, 'Lebron James')
    p2 = ConcretePlayer(mediator, 'Michael Jordan')

    mediator.add(p1)
    mediator.add(p2)

    p1.send("I'm The Goat Now")


if __name__ == "__main__":
    main()
