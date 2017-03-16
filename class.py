class Person(object):
    def __int__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return  self.first_name
    def __cmp__(self, other):
        return cmp((self.family_name, self.first_name), (other.family_name, other.first_name))
    def __str__(self):
        return  "It is" + (self.first_name, self.family_name)
    def say(self, toPer, something):
        return self.first_name + ' ' + self.family_name + " says to " + toPer.first_name + ' "' + something + '"'
    def sing(self, toPer, something):
        return self.say(toPer, something + ' la la lan')

p1 = Person()
p2 = Person()
p1.family_name = 'Crazy'
p1.first_name = 'Lazy'
p2.family_name = 'Just'
p2.first_name = 'Doit'

print p1.sing(p2, 'Nothing is nothing')

class MITperson(object):
    idNumber = 0
    def __int__(self, familyName, firstName):
        Person.__int__(self, familyName, firstName))
        self.id =