from funcs import *

T1 = intinput("Number 1, Ten's place: ")
U1 = intinput("Number 1, One's place: ")
T2 = intinput("Number 2, Ten's place: ")
U2 = intinput("Number 2, One's place: ")

L = T1 * T2 
C = T2 * U1 + T1 * U2
R = U1 * U2

print(f"""
  {T1}{U1}
x {T2}{U2}
=============================================
Left   = T1 x T2           = {T1} x {T2}               = {L}
Center = T2 x U1 + T1 x U2 = {T2} x {U1} + {T1} x {U2} = {C}
Right  = U1 x U2           = {U1} x {U2}               = {R}
                
                {L} - {C} - {R} (Balancing)
              = {int(f"{T1}{U1}") * int(f"{T2}{U2}")}
""")