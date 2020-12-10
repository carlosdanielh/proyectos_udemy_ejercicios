# class Vehicle:
#     color = 'white'

#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity  

#     def get_data(self):
#         return f'Vehicle Name: {self.name} capacity: {self.capacity} Mileage: '
#         f'{self.mileage}'

#     def Arrancando(self):
#         print('arrancando fuertemente....')

#     def seating_capacity(self, capacity):
#         return f'The seating capacity of a {self.name} is {capacity} passengers'

#     def fare(self):
#         return self.capacity * 100


# class Bus(Vehicle):

#     def set_data(self):
#         pass

#     def seating_capacity(self, capacity):
#         return super().seating_capacity(capacity)
    
#     def fare(self):
#         return self.capacity * 100 + self.capacity * 10

    

# class Car(Vehicle):
#     pass


# bus = Bus('autobus', 10, 50)
# car = Car('fastfury', 20, 40)
# print(bus.get_data())
# bus.name = 'hola'
# print(bus.get_data())
# bus.Arrancando()

# print(bus.seating_capacity(6000))
# print(bus.color)
# print(car.color)
# print(bus.fare())
# print(type(bus))
# print(type(car))

class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id = identifier
        self.comment = comment
        self.seq = self._clean(seq)


    def _clean(self, seq):
        """
        remove newline from the string representing the sequence
        :param seq: the string to clean
        :return: the string without '\n'
        :rtype: string
        """
        return seq.replace('\n')


    def gc_percent(self):
        """
        :return: the gc ratio
        :rtype: float
        """
        seq = self.seq.upper()
        return float(seq.count('G') + seq.count('C')) / len(seq)




dna1 = Sequence('gi214', 'the first sequence', 'tcgcgcaacgtcgcctacatctcaagattca')
dna2 = Sequence('gi3421', 'the second sequence', 'gagcatgagcggaattctgcatagcgcaagaatgcggc')

print(dna1)
print(dna2)