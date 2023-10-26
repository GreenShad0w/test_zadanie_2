def bubble_sort_chisel(masiv):  #Сортировка массива чисел по убыванию
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(masiv) - 1):
            if masiv[i] < masiv[i + 1]:
                masiv[i], masiv[i + 1] = masiv[i + 1], masiv[i]
                swapped = True
                
def bubble_sort_slov(masiv_slov):  #Сортировка массива слов по алфавиту
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(masiv_slov) - 1):
            if masiv_slov[i] > masiv_slov[i + 1]:
                masiv_slov[i], masiv_slov[i + 1] = masiv_slov[i + 1], masiv_slov[i]
                swapped = True

def last_sort_slov(arr_slov, arr_osn, count_1, count_2): 

    if arr_osn[count_2] == arr_slov[count_1]:
        arr_osn.pop(count_2)                             #Удаляем копию слова из основного массив
        arr_osn.insert(0, arr_slov[count_1])             #Добавляем это же слово в основной массив в начало 

def last_sort_chisel(arr_chisel, arr_osn1, count_1_1, count_2_2):
    
    if arr_osn1[count_2_2] == arr_chisel[count_1_1]: 
        arr_osn1.pop(count_2_2)                          #Удаляем копию числа из основного массива 
        arr_osn1.append(arr_chisel[count_1_1])           #Добавляем это же число в основной массив в конец 
    


def sort():
    stroka = input("Введите строку - ") 
    arr = stroka.split()                                 #Преобразуем строку в массив
    arr_slova = [0] * len(arr)                           #Создаём новый массив для слов из строки и заполняем его нулями по длине основного массива
    arr_chisla = [0] * len(arr)                          #То же самое, но уже массив для чисел
    count = 0
    for i in range(len(arr)):
        if arr[i].isdigit():                             #Проверяем i-ый элемент основного массива является ли он числом
            arr_chisla[count] = arr[i]                   #Добавляем найденое число в массив чисел
            count += 1
    del arr_chisla[count:len(arr)]                       #Удаляем лишние нули из массива чисел
    count = 0
    for i in range(len(arr)): 
        if arr[i].isdigit() == False:                    #Проверяем i-ый элемент основного массива, что он не является числом
            arr_slova[count] = arr[i]                    #Добавляем найденое слово в массив слов
            count += 1
    del arr_slova[count:len(arr)]                        #Удаляем лишние нули из массива слов
    bubble_sort_slov(arr_slova)                          #Сортируем массив слов по алфавиту
    bubble_sort_chisel(arr_chisla)                       #Сортируем массив чисел по убыванию
    count = 1
    for i in range(len(arr_slova)):
        for k in range(len(arr)):
            last_sort_slov(arr_slova, arr, i, k)         #Добавляем слова в основной массив, удаляя копию вставленного слова
        for k in range(len(arr)):
            last_sort_chisel(arr_chisla, arr, i, k)      #Добавляем число в основной массив, удаляя копию вставленного числа
        print(count,' шаг: ', ' '.join(arr))
        count += 1
    return sort()
sort()