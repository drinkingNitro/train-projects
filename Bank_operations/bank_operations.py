
import sys

file = sys.stdin.read().splitlines()


def Deposit(name, summ):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] += summ


def Withdraw(name, summ):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] -= summ


def Income(percent):
    for account in accounts:
        if accounts[account] > 0:
            indexed = accounts[account] * (1 + percent / 100)
            accounts[account] = int(indexed)


def Transfer(name, name2, summ):
    if name not in accounts:
        accounts[name] = 0
    if name2 not in accounts:
        accounts[name2] = 0
    accounts[name] -= summ
    accounts[name2] += summ


def Balance(name):
    if name not in accounts:
        print('ERROR')
    else:
        print(accounts[name])


accounts = {}
for command in file:
    command = command.split()
    operation = command[0]

    if operation == 'DEPOSIT':
        Deposit(command[1], int(command[2]))
    elif operation == 'WITHDRAW':
        Withdraw(command[1], int(command[2]))
    elif operation == 'INCOME':
        Income(int(command[1]))
    elif operation == 'TRANSFER':
        Transfer(command[1], command[2], int(command[3]))
    elif operation == 'BALANCE':
        Balance(command[1])
