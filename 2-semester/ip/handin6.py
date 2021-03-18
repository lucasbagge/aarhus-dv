"""
HANDIN 5 (eight queens puzzle)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <
    I denne uges aflvering har vi arbejder med klasser og hiarkier, hvor vi har skulle lave en Person
    der tager forskellige data attributter og AnnotatedPerson som gør man kan skrive en note til Person klassen.
    Det svære ved denne opgave har egentlig været at komme ind i tanke gangen med hvorfor man kalder self og hvad
    __init__ gør.
    Jeg ender næsten ud med det samme som Gerth får, men der er en forskel i at hans note er lukket med [], mens
    min ikke er det. Det kunne jeg godt tænke mig at få et råd om.
    >
"""

class Person:
  
  def __init__(self, name = None, mother = None, father = None, born = None, died = None):
    self.name = name
    self.mother = mother
    self.father = father
    self.born = born
    self.died = died
    
  def __str__(self):
    if self.died == None:
      died = "-"
    else:
      died = self.died
    return "<%s, %s, %s>" % (self.name, self.born, died)
 
  def ancestor(self):
    if self.mother == None:
      m_ancestor = "-"
    else:
      m_ancestor = self.mother.ancestor()
    if self.father == None:
      f_ancestor = "-"
    else:
      f_ancestor = self.father.ancestor()
    return str(self), f_ancestor, m_ancestor

class AnnotatedPerson(Person):

  def __init__(self, name = None, mother = None, father = None, born = None, died = None, note = None):
    self.note = note
    Person.__init__(self, name, mother, father, born, died) 
    
  def __str__(self):
    if self.note == None:
      pass
    else:
      note = self.note
    return "<%s>" % Person.__str__(self) + note
      
 

louise_af_HK = Person("Louise of Hessen-Kassel", None, None, 1817, 1898)
christian_9 = Person("Christian 9.", None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson("Louise of Sweden-Norway", None, None, 1851, 1926, "born Princess of Sweden and Norway")
frederik_8 = Person("Frederik 8.", louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person("Christian 10.", louise_af_SN, frederik_8, 1870, 1947)
ingrid = AnnotatedPerson("Ingrid of Sweden", None, None, 1910, 2000, "Queen of Denmark 1947-1970")
frederik_9 = Person("Fredrik 9.", None, christian_10, 1899, 1972)
margrethe_ii = AnnotatedPerson("Margrethe II", ingrid, frederik_9, 1940, note="Queen of Denmark")

def print_tree(tree):
    stack = [(tree,0)]
    while len(stack) > 0:
        subtree, depth = stack.pop()
        name, *children = subtree
        print("  |"*depth, "--", name, sep="")
        for child in children[::-1]:
            stack.append((child, depth + 1))

print_tree(margrethe_ii.ancestor())            

'''
print_tree(margrethe_ii.ancestor())            
--<<Margrethe II, 1940, ->>Queen of Denmark
  |--<Fredrik 9., 1899, 1972>
  |  |--<Christian 10., 1870, 1947>
  |  |  |--<Frederik 8., 1870, 1947>
  |  |  |  |--<Christian 9., 1818, 1906>
  |  |  |  |  |---
  |  |  |  |  |---
  |  |  |  |--<Louise of Hessen-Kassel, 1817, 1898>
  |  |  |  |  |---
  |  |  |  |  |---
  |  |  |--<<Louise of Sweden-Norway, 1851, 1926>>born Princess of Sweden and Norway
  |  |  |  |---
  |  |  |  |---
  |  |---
  |--<<Ingrid of Sweden, 1910, 2000>>Queen of Denmark 1947-1970
  |  |---
  |  |---
'''


'''
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