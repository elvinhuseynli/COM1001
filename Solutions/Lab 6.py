class ListClass:

    def __init__(self, Items, name):
        self.Items = Items
        self.name = name
        self.Evennumbers = []
        self.Oddnumbers = []

    def printName(self):
        print("Name: " + self.name)

    def printOdds(self):
        strRepOfOdd = ''
        for odd_value in self.Items:
            if odd_value % 2 == 0:
                self.Evennumbers.append(odd_value)
            else:
                self.Oddnumbers.append(odd_value)
        for x in self.Oddnumbers[:-1]:
            strRepOfOdd = strRepOfOdd + str(x) + ' '
        print(strRepOfOdd + str(self.Oddnumbers[-1]))

    def printEvens(self):
        strRepOfEven = ''
        for y in self.Evennumbers[:-1]:
            strRepOfEven = strRepOfEven + str(y) + ' '
        print(strRepOfEven + str(self.Evennumbers[-1]))

    def getLength(self):
        return len(self.Items)

    def changeItem(self,oldValue,newValue):
        if oldValue in self.Items:
            z = self.Items.index(oldValue)
            self.Items[z] = newValue

    def addItem(self,item):
        if not item in self.Items:
            self.Items.append(item)

    def addItems(self,items):
        for added_items in items:
            if not added_items in self.Items:
                self.Items.append(added_items)

    def removeItem(self,item):
        if item in self.Items:
            self.Items.remove(item)

    def removeItems(self,items):
        for removed_items in items:
            if removed_items in self.Items:
                self.Items.remove(removed_items)

    def __str__(self):
        str_representation = ''
        for element in self.Items[:-1]:
            str_representation = str_representation + str(element) + ' '
        return '[' + str_representation + str(self.Items[-1]) + ']'

    def __lt__(self, other):
        sumOfSelf = 0
        sumOfOther = 0
        for sum_of_self in self.Items:
            sumOfSelf += sum_of_self
        for sum_of_other in other.Items:
            sumOfOther += sum_of_other
        return sumOfSelf < sumOfOther