name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for names in name:
    correct_name = names.split()[-1].capitalize()
    print(f'Привет, {correct_name}!')
