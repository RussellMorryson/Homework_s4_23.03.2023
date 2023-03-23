"""*****Напишите функцию , которая будет возвращать 
переданное в качестве параметра n число словами

Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь"""

def from_1_to_10 (num):
    array = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    text = ''
    text += array[num]
    return array[num]

def from_10_to_20 (num):
    array = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
                   'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать']
    text = ''
    text += array[num]
    return text
    
def from_21_to_100 (num):
    array = ['', '', 'двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ',
                    'семьдесят ', 'восемьдесят ', 'девяносто ']
    text = ''
    d_10 = int(num / 10)
    d_1 = int(num % 10)
    
    text += array[d_10]
    text += from_1_to_10(d_1)
    return text
        
def from_101_to_1000 (num):
    array = ['', 'сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ',
                    'семьсот ', 'восемьсот ', 'девятьсот ']
    text = ''
    d_100 = int(num/100)
    num = int(num%100)
    text += array[d_100]
    text += main_constructor(num)
    return text

def from_1001_to_10000(num):
    array = ['0', 'одна тысяча ', 'две тысячи ']
    text = ''
    if num < 3000:
        d_1000 = int(num / 1000)
        text += array[d_1000]
        num = int(num % 1000)
        text += main_constructor(num)
    elif num < 5000:
        d_1000 = int(num / 1000)
        text += from_1_to_10(d_1000) + ' тысячи '
        num = int(num % 1000)
        text += main_constructor(num)
    else:
        d_1000 = int(num / 1000)
        text += from_1_to_10(d_1000) + ' тысяч '
        num = int(num % 1000)
        text += main_constructor(num)
    return text
    

def main_constructor(num):
    txt =''
    if num < 10:
        txt = from_1_to_10(num)
    elif num < 21:
        txt = from_10_to_20(num)
    elif num < 100:
        txt = from_21_to_100(num) 
    elif num < 1000:
        txt = from_101_to_1000(num)
    elif num < 10000:
        txt = from_1001_to_10000(num)
    # elif num < 10000:
    #     txt = from_1001_to_10000(num)
        
              
    return txt

# =============================================
    # Основной блок программы #
# =============================================
number = int(input("Введите число: "))
words = main_constructor(number)
print(words)

