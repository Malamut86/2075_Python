class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        self.lists.update({equipment.serial_number:[equipment.title, self]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,инвентарный № - '+ str(equipment.serial_number))


    def give_to_depot(self, equipment, other):
        self.give_lists.update({equipment.serial_number: [equipment.title,other]})
        print('Передано оборудование:' + '' + equipment.title + ' ,инвентарный № - ' + str(equipment.serial_number))
        other.take_to_depot(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number):
        Office_equipment.__init__(self,title, serial_number)


    def __str__(self):
        return  'Модель:'+Office_equipment.__str__(self)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number):
        Office_equipment.__init__(self,title, serial_number)


    def __str__(self):
        return  'Модель:'+Office_equipment.__str__(self)

class Copier(Office_equipment):
    def __init__(self, title,serial_number):
        Office_equipment.__init__(self, title, serial_number)


    def __str__(self):
        return  'Модель:'+Office_equipment.__str__(self)



store1 = Depot('ТСО')
store2 = Depot('ОСиСТ')
a = Printer('HP',10001)
b = Scanner('Dell',100005)
c = Copier('Epson',1000006)
d = Printer('HP',10002)
e = Printer('HP',10003)
f = Printer('HP',10004)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


store1.take_to_depot(a)
store1.take_to_depot(d)
store1.take_to_depot(e)
store1.take_to_depot(f)
store2.take_to_depot(b)
store2.take_to_depot(c)

store1.list_equipments()
store2.list_equipments()