# Дан список интов , повторяющихся элементов в списке нет . 
# Нужно преобразовать это множество в строку , сворачивая соседние по числовому ряду числа в диапазоны . Примеры :
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

# numbersArr = [1,4,5,2,3,9,8,11,0]
# sortedArr = sorted(numbersArr)

# result = ""

# i = 0
# while i < len(sortedArr):   
#     start = sortedArr[i]
#     counter = 0

#     for j in range (i, len(sortedArr)):
#         if (j + 1 < len(sortedArr) and sortedArr[j] + 1 == sortedArr[j+1]):
#             counter = counter + 1
#         else:
#             break        

#     if (counter == 0):
#         result = result + str(start) + ','
#         i = i + 1
#     else:
#         result = result + str(start) + '-' + str(start + counter) + ','
#         i = i + counter + 1

# print(numbersArr)
# print(result.removesuffix(','))



# Дана строка ( возможно , пустая ), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида :
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку , если на вход пришла невалидная строка. 
# Пояснения : Если символ встречается 1 раз , он остается без изменений ;
#  Если символ повторяется более 1 раза , к нему добавляется количество повторений

def compress(text):
    # итоговая строка
    result = ""
    count = 1  

    for i in range (len(text)):
        if (i + 1 < len(text) and text[i] == text[i + 1]):
            count = count + 1    
        elif(i + 1 == len(text)):
            if(count == 1 and text[i] == text[i - 1]):
                result = result + text[i - 1] + 2
            elif(count == 1 and text[i] != text[i - 1]):
                result = result + text[i]
            else:
                count = count + 1    
                result = result + text[i - 1] + str(count)
        else:
            if(count == 1):
                result = result + text[i]
            else:
                result = result + text[i] + str(count)
            count = 1
            
    print(result)

import re
text = input("Введите строку (разрешены только символы A-Z): ")

if re.search(r'[^A-Z]', text):
     print("Вы ввели неверные символы, разрешены только большие латинские буквы A-Z")
else:
    compress(text)
