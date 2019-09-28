from positions import Positions

class Worker:
    def __init__(self, fullName, position, gender, payment):
        self.fullName = fullName
        self.position = position
        self.gender = gender
        self.payment = payment

    def workerToString(self):
        print('Name: ', self.fullName)
        print('Position: ', Positions(self.position).name)
        if self.position == -1:
            print('Payment: ', f'{-0.0001}')
        else:
            print('Payment: ', f'{(self.position * self.position * self.position * self.position * self.position * self.position)+0.3}$')

    def changePosition(self,x):
        self.position += x

janKowalski = Worker("Janusz Kowalski",12, "Homo Sapiens", 0.1)
janKowalski.workerToString()