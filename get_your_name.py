class NewMe:

   def __init__(self, name):
       self.name = name
       self.number = []

   def average(self):
       return sum(self.number) / len(self.number)


avr_num = NewMe('Valeri')
print (avr_num.name)
avr_num.number.append(12)
avr_num.number.append(55)
print(avr_num.average())
