"""
HANDIN 9 ()
This handin is done by (study ids and names of up to three students):
    202004972 <Lucas Bagge>
Reflection upon solution:
    <
    I denne opgave har vi skulle generaliserer et maximum flow problem.
    Jeg kommenter min kode løbende om hvad jeg har gjort og hvilke tanker.
    Opgave a og b skal ses i forlængelse af hinanden. Det betyder at jeg ikke
    genskrive eller laver funktioner af hvad jeg laver i a, men man skal kører
    a for at løse b. 
    >
"""
# Indlæs moduler
import numpy as np
np.set_printoptions(suppress=True)
from scipy.optimize import linprog

# a) 

## Opgave beskrivelse
edges = [('A', 'C', 4),
         ('A', 'B', 3),
         ('C', 'E', 1),
         ('C', 'D', 1),
         ('B', 'E', 3),
         ('B', 'D', 1),
         ('E', 'D', 3),
         ('E', 'F', 1),
         ('D', 'F', 5)]
source = 'A'
sink = 'F'

# Splitter vores data op.
edge_from, edge_to, capacity = zip(*edges)

# Kombiner vores from and to for at finde de unikke værdier i mit loop.
edge_to_combined_edge_from = edge_to + edge_from
# Den unikke liste gemmer jeg her:
unique = []
for char in edge_to_combined_edge_from[::]:
    if char not in unique:
        unique.append(char)
unique.sort()
# Den sorteret liste gemmer jeg i uq.
uq = unique

# Jeg vil gerne bruge uq som et opslagsværk. Det gør jeg ved at lave en dict.
uq_dict = {f:i for i, f in enumerate(uq)}

# Senerer i koden vil jeg gerne slette nogle rækker. Det gøres med udgangspunkt
# i hvad man har definerede som sin source og sunk. 
source_sink = [source, sink] 

# Hvad der skal slettes oversættes jeg til rækker nummer i min dict.
delete_items_array = [uq_dict[i] for i in source_sink if i in uq_dict]

# Jeg laver min conservation som er hvor flowet skal opbevares.
conservation = np.zeros([len(uq), len(capacity)])

# Baseret på from og to så fylder jeg conservation med enten 1 hvor det betyder
# her går vi til og -1 fra hvor vi forlader edge.
for edge, (f,t) in enumerate(zip(edge_from, edge_to)):
  conservation[uq_dict[f]][edge] = 1.0 
  conservation[uq_dict[t]][edge] = -1.0 

# Nu hvor conservation er fyldt ud vil jeg slette de to rækker som ikke er 
# nødvendig. 
conservation_reduced = np.delete(conservation, delete_items_array ,axis = 0)

# Samme nummer gør jeg gor min sink.
sink_placeholder = np.zeros([len(capacity)])

# Erstatter nuller med 1 hvor det angiver hvilke edge der går til source.
for edge, to in enumerate(edge_to):
  if sink == to:
    sink_placeholder[edge] = 1.0

# Nu er tingene klar til at gå ind i linprog.
res_a = linprog(-sink_placeholder,
              A_eq = conservation_reduced, 
              b_eq = np.zeros(conservation_reduced.shape[0]),
              A_ub = np.eye(np.array(capacity).size),
              b_ub = np.array(capacity))
print(f'Får samme resultat som i forlæsning: \n: {res_a}')

## b)

edges_b = [('A', 'C', 4, 1),
         ('A', 'B', 3, 1),
         ('C', 'E', 1, 1),
         ('C', 'D', 1, 1),
         ('B', 'E', 3, 1),
         ('B', 'D', 1, 1),
         ('E', 'D', 3, 0),
         ('E', 'F', 1, 1),
         ('D', 'F', 5, 2),
        ]

source = 'A'
sink = 'F'
flow = 4

# Jeg vil kun beholde cost, hvor jeg antager man benytter sig af samme edges,
# source og sink som i opgave a. 
_, _, _, cost_b = zip(*edges_b)

# benytter mig af samme conservation som i a og sink palce holder, men
# reshaper data så det macher at vi har en ny række.
new = np.append(conservation_reduced, \
                sink_placeholder.reshape(conservation_reduced.shape[1],1))

# PÅ den mest elegante måde jeg kunne finde på reshaper jeg mit date.
new_reshape = new.reshape(conservation_reduced.shape[0] + 1,  \
                       conservation_reduced.shape[1])

res_b = linprog(np.array(cost_b), # laver cost om til en array
              A_eq = new_reshape, 
              # laver min b_eq ved at lave en nul matrice og erstatte den sidste
              # værdi med flow.
              b_eq = np.append(np.zeros(conservation_reduced.shape[0]), flow),
              A_ub = np.eye(np.array(capacity).size),
              b_ub = np.array(capacity))
print(f'Fra mit resultat får jeg de totale omkostninger til 15: \n {res_b}')

