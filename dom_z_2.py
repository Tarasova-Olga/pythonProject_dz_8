#  2. Напишите функцию, которая проверяет: является ли слово палиндромом.

word = input('Введите слово: ')
word_reverse = word[::-1]

if word == word_reverse:
    print('Слово является полиндромом.')
else:
    print('Не полиндром.')