class Remote():
    pass

class Player: #Encapsulation
    def moveRigt(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

# Objects.

remote1 = Remote()
player1 = Player()
if(remote1.isLeftPressed()):
    player1.moveLeft()   #Abstraction 