import random
with open('hand.txt', 'r', encoding='utf-8') as a:
    text = a.read()
words = text.split()
random_index = random.randint(0, len(words) - 1)
slovo = words[random_index]
d = len(slovo)
print('ЭТО ИГРА ВИСЕЛЬЦА. У ТЕБЯ 6 ПОПЫТОК. ДАВАЙКА НАЧНЁМ!')
#print(slovo)
nul = ['_'] * d
print(''.join(nul))
p = 0
nep = []
ug = []
while p <= 6:
    l = input()
    if l not in slovo:
        p = p + 1
        nep.append(l)
    if l in slovo:
        ug.append(l)
        for i in range(len(slovo)):
            if slovo[i] in ug:
                nul[i] = slovo[i]
    if '_' not in nul:
        print ('НУУ ЭТО ПОБЕДА ПОЛУЧАЕТСЯ!')
        print('ВОТ ПРАВИЛЬНОЕ СЛОВО:',slovo)
        print('ТВОИ ПРАВИЛЬНЫЕ БУКВЫ:', ''.join(ug))
        print('ТВОИ НЕПРАВИЛЬНЫЕ БУКВЫ:', ''.join(nep))
        break
    if p == 0:
        print('\n')
        print(''.join(nul))
        print('\n')
        print('ПОКА БЕЗОШИБОЧНАЯ ПОШЛА')
        print('ВСЕ ТВОИ БУКВЫ:',''.join(nep+ug))
    if p == 1:
        print('\n')
        print(''.join(nul))
        print('\n')
        print('_______/|\_')
        print('ПЕРВАЯ РАЗМИНОЧНАЯ')
        print('ВСЕ ТВОИ БУКВЫ:', ''.join(nep+ug))
    if p == 2:
        print('\n')
        print(''.join(nul))
        print('\n')
        print('        | \n '
              '       | \n'
              '        | \n'
              '        | \n'
              '_______/|\_')
        print('БЫВАЕТ')
        print('ВСЕ ТВОИ БУКВЫ:', ''.join(nep + ug))
    if p == 3:
        print('\n')
        print(''.join(nul))
        print('   +----+ \n '
              '       | \n '
              '       | \n'
              '        | \n'
              '        | \n'
              '_______/|\_')
        print('ЖИВЁМ ЖИВЁМ')
        print('ВСЕ ТВОИ БУКВЫ:', ''.join(nep + ug))
    if p == 4:
        print(''.join(nul))
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '        | \n'
              '        | \n'
              '_______/|\_')
        print('ОСТАЛОСЬ НЕМНОГО...!')
        print('ВСЕ ТВОИ БУКВЫ:', ''.join(nep + ug))
    if p == 5:
        print(''.join(nul))
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '  /|\   | \n'
              '        | \n'
              '_______/|\_')
        print('ПОСЛЕДНИЙ ШАНС.....')
        print('ВСЕ ТВОИ БУКВЫ:', ''.join(nep + ug))
    if p == 6:
        print('\n')
        print(''.join(nul))
        print('   +----+ \n '
              '  |    | \n '
              '  o    | \n'
              '  /|\   | \n'
              '  / \   | \n'
              '_______/|\_')
        print('GGWP   ТЫ ПРОИГРАЛ')
        print('ПРАВИЛЬНОЕ СЛОВО:',slovo)
        print('ТВОИ ПРАВИЛЬНЫЕ БУКВЫ:',''.join(ug))
        print('ТВОИ НЕПРАВИЛЬНЫЕ БУКВЫ:',''.join(nep))
        break

