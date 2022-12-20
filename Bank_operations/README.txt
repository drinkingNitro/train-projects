В программе реализованы функции, имитирующие банковскую деятельность:
- Зачисление средств /DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет счета, то счет создается.

- Снятие средств /WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет счета, то счет создается.

- Запрос остатка по счету /BALANCE name - узнать остаток средств на счету клиента name.

- Перевод средств другому клиенту /TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у
какого-либо клиента нет счета, то ему создается счет.

- Нвчисление процентов на остаток /INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета.

Примеры:

Тест 1
Входные данные:
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

Вывод программы:
105
-50
ERROR



Тест 2
Входные данные:
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov

Вывод программы:
ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179



Тест 3
Входные данные:
BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b

Вывод программы:
ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771