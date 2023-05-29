from sympy.logic.boolalg import truth_table
from sympy import symbols, Not, Or, And, simplify_logic, Implies, satisfiable
from itertools import product

def implies_entails(p, q, r):
    table = list(product([False, True], repeat=3))
    for row in table:
        p_val, q_val, r_val = row
        if (p_val and not q_val) != ((p >> q).subs([(p, p_val), (q, q_val)]) and
                                     ((p & r) >> q).subs([(p, p_val), (q, q_val), (r, r_val)])):
            return False
    return True

print("\n Zad 1")
p, q = symbols('p q')
KB = Or(And(p, q), And(p, Not(q)))
alpha2 = And(True, True)

table_kb = list(truth_table(KB, [p, q]))
table_alpha2 = list(truth_table(alpha2, [p, q]))

is_safe = table_kb.count(True) >= table_alpha2.count(True)
print("KB |= α2? ", is_safe)

print("\n Zad 2")
p, q = symbols('p q')
s1 = Not(Or(p, And(Not(p), q)))
s2 = And(Not(p), Not(q))

simp_s1 = simplify_logic(s1)
simp_s2 = simplify_logic(s2)

is_equivalent = simp_s1 == simp_s2
print("Czy zdania są logicznie równoważne? ", is_equivalent)

print("\n Zad 3")
p, q, r = symbols('p q r')

s3 = (p >> q) >> (Not(p) >> Not(q))
s4 = (p >> q) >> ((p & r) >> q)

is_satisfiable1 = satisfiable(s3)
is_satisfiable2 = satisfiable(s4)

print("Czy zdanie (i) jest spełnialne? ", is_satisfiable1)
print("Czy zdanie (ii) jest spełnialne? ", is_satisfiable2)

print("\n Zad 4")
p, q, r = symbols('p q r')



entails = implies_entails(p, q, r)
print("(p ⇒ q) |= ((p ∧ r) ⇒ q)? ", entails)

print("\n Zad 5")
cnf = simplify_logic(s3, form='cnf')
dnf = simplify_logic(s3, form='dnf')
print("CNF : ", cnf)
print("DNF: ", dnf)