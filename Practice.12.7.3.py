per_cent = list({'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}.values())

money = int(input("Введите сумму вклада:"))

deposit = []
deposit.append(int(per_cent[0] * money / 100))
deposit.append(int(per_cent[1] * money / 100))
deposit.append(int(per_cent[2] * money / 100))
deposit.append(int(per_cent[-1] * money / 100))
print(deposit) #Функция вывода дохода с разных  годовых ставок оставлена для соответствия примеру к заданию, где выведены варианты дохода по сууме внесенных средств

print("Максимальная сумма, которую вы можете заработать -", max(deposit))
