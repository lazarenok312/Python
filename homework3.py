print("Обычный калькулятор запущен")
print("+ для сложения \n- для вычитания\n* для умножения\n/ для деления\n")
def calculate():
   operation = input('Введите операцию которую хотите выполнить: ')
   
   number_1 = int(input("Введите первое число: "))
   number_2 = int(input("Введите второе число: "))

   if operation == '+':
       print('{} + {} = '.format(number_1, number_2))
       print(number_1 + number_2)

   elif operation == '-':
       print('{} - {} = '.format(number_1, number_2))
       print(number_1 - number_2)

   elif operation == '*':
       print('{} * {} = '.format(number_1, number_2))
       print(number_1 * number_2)

   elif operation == '/':
       print('{} / {} = '.format(number_1, number_2))
       print(number_1 / number_2)

   else:
       print('Вы ввели неправильный оператор')

calculate()
while True:
		comand = input("Хотите продолжить?(Да/Нет): ")
		if comand == 'Да':
			calculate()
			continue
		if comand == 'Нет':
			print("Выходим из проиложения")
			break
else:
		print("Не верная команда")