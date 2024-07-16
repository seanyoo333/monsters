# only lowercase and one space, 0 < = N < = 100
# a,e,i,o,u -> pa,pe,pi,po,pu

kemija_coded = input()
'''kepemipijapa
kemija
zepelepenapa papapripikapa
zelena paprika'''

i = 0
result =''

while i < len(kemija_coded):
    result = result + kemija_coded[i]

    if kemija_coded[i] in 'aeiou':
       i = i + 3
    else:
       i = i + 1

print(result)