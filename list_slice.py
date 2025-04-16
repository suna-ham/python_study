
# 예제1) spell = ['h','a','n','d','i','c','r','a','f','t']인 경우 아래 문제들의 결과를 예상해 보고 직접 확인해 보자
spell = ['h','a','n','d','i','c','r','a','f','t']
print(spell[1:5]) 
print(spell[:])
print(spell[:4])
print(spell[5:])
print(spell[:2] + spell[9:])

#### 문제1) 
spell_re = ['r','e']
spell_server = ['s','e','r','v','e','r']

# (1) 두개의 list를 사용하여 'reserve'의 스펠링으로 구성된 list_spell_reserve를 만들어 보자
# (2) (1)의 수행 결과를 바탕으로 'observe'로 변경해 보자
spell_server[:5]


list_spell_reserve = spell_re + spell_server[:5]
print(list_spell_reserve)

list_spell_reserve2 = list_spell_reserve[0:1] =['o', 'b']

print(list_spell_reserve2 + spell_server[:5])

