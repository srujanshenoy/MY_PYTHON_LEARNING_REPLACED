color = 5
print('red') if color < 5 else print('blue')

grade = 'idiot'

match grade:
    case 'a': print('Very good')
    case 'b': print('Good')
    case 'c': print('Needs improvement')
    case 'd': print('Bad')
    case 'f': print('FAILURE')
    case __: print('Grade not recognized')

if grade == 'a': print('Very good!')
if grade == 'b': print('Good!')
if grade == 'c': print('Needs improvement!')
if grade == 'd': print('Bad')
if grade == 'f': print('FAILURE')
if grade == __: print('Grade not recognized!')



