from sm import SM

class turniket(SM):
    def __init__(self) -> None:
        self.startState = 'locked'

    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return ('unlocked', 'enter')
            else:
                return ('locked', 'pay')
        else:  # state == 'unlocked'
            if inp == 'turn':
                return ('locked', 'pay')
            else:
                return ('unlocked', 'enter')
a = turniket()
print(a.transduce(['turn','coin','turn', 'coin'])
