'''
Create a class Person to represent a person with a name, year of birth, year of death 
(None if the person is still alive),
 and with references to two other Person objects representing the father and mother of the person. 
 The class should define the following three methods:

A constructor Person(name, mother, father, born, died) where all arguments have default value None.
__str__ returning the string "name born-died".
ancestor() returns a tupple (name-string, recursive-father-ancestor, recursive-mother-ancestor)
 (see example below).
Create a second class AnnotatedPerson that is a subclass of Person, that allows each person to be 
annotated with a note, 
that can be given as an argument to the constructor, and will be part of the string returned 
by __str__, i.e. redefine the methods __init__ and __str__. 
The method ancestor should be inheritated from Person and not be redefined in AnnotatedPerson. 
Try to avoid repeating code from the super class, instead call the methods in the super class.

Using the two classes you should be able to create the following objects:

louise_af_HK = Person("Louise of Hessen-Kassel", None, None, 1817, 1898)
christian_9 = Person("Christian 9.", None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson("Louise of Sweden-Norway", None, None, 1851, 1926, "born Princess of
 Sweden and Norway")
frederik_8 = Person("Frederik 8.", louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person("Christian 10.", louise_af_SN, frederik_8, 1870, 1947)
ingrid = AnnotatedPerson("Ingrid of Sweden", None, None, 1910, 2000, "Queen of Denmark 1947-1970")
frederik_9 = Person("Fredrik 9.", None, christian_10, 1899, 1972)
margrethe_ii = AnnotatedPerson("Margrethe II", ingrid, frederik_9, 1940, note="Queen of Denmark")
Calling margrethe_ii.ancestors() should return something like:

('Margrethe II 1940- [Queen of Denmark]', ('Fredrik 9. 1899-1972', ('Christian 10. 1870-1947', 
('Frederik 8. 1870-1947', ('Christian 9. 1818-1906', '-', '-'),
 ('Louise of Hessen-Kassel 1817-1898', '-', '-')), ('Louise of Sweden-Norway 1851-1926 
 [born Princess af Sweden and Norway]', '-', '-')), '-'), 
 ('Ingrid of Sweden 1910-2000 [Queen of Denmark 1947-1970]', '-', '-'))

Applying the tree printing program of Exercise 9.2 to this output would print something like the below.

--Margrethe II 1940- [Queen of Denmark]
  |--Fredrik 9. 1899-1972
  |  |--Christian 10. 1870-1947
  |  |  |--Frederik 8. 1870-1947
  |  |  |  |--Christian 9. 1818-1906
  |  |  |  |  |---
  |  |  |  |  |---
  |  |  |  |--Louise of Hessen-Kassel 1817-1898
  |  |  |  |  |---
  |  |  |  |  |---
  |  |  |--Louise of Sweden-Norway 1851-1926 [born Princess of Sweden and Norway]
  |  |  |  |---
  |  |  |  |---
  |  |---
  |--Ingrid of Sweden 1910-2000 [Queen of Denmark 1947-1970]
  |  |---
  |  |---
'''

class Person:
  
  def __init__(self, name = None, mother = None, father = None, born = None, died = None):
    self.name = name
    self.mother = mother
    self.father = father
    self.born = born
    self.died = died

  def __str__(self):
    return "<%s, %s, %s>" % (self.name, self.born, self.died)

def ancestor(self, name = None, FatherAncestor = None, MotherAncestor = None):
  
  result = FatherAncestor.get('name', tuple())
  if result:
    return result
  
  acestors_tuple = MotherAncestor.get('name', tuple())
  result = tuple(acestors_tuple)
  for ance in acestors_tuple:
    # rekursiv step
    result |= ancestor(ance, FatherAncestor, MotherAncestor)

  FatherAncestor[name], MotherAncestor[name] = result

  return result

  
    
  



