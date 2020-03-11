# UJIAN MODUL 1 GABRIELLA

# SOAL NOMOR 1

def Hashtag(string):
    if string:
        string = "#"+string
        string = string.split()
        
        temp = []
        for i in string:
            temp.append(i.capitalize())
        
        #printing as hashtag
        result = ""
        for i in temp:
            result += i
        
        #len < 140
        print(len(result))
        if len(result) <= 140:
            return result
        return False
        
    else:
        return False

print(Hashtag(" Hello there how are you doing"))
print(Hashtag("  Hello  World  "))
print(Hashtag(""))
print(Hashtag("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))



# SOAL NOMOR 2

def create_phone_number(number):
    return f"({number[0]}{number[1]}{number[2]}) {number[3]}{number[4]}{number[5]}-{number[6]}{number[7]}{number[8]}{number[9]}"

print(create_phone_number([1,2,3,4,5,6,7,8,9,0])) #"(123) 456-7890"



# SOAL NOMOR 3

def bubbleSort(list) :
    for i in range(len(list), 0, -1) :
        for j in range(0,i-1) :
            if (list[j] > list[j + 1]) :
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def sort_odd_even(num):
    odds = []
    evens = []
    for i in num:
        if i%2 == 0:
            evens.append(i)
            evens = bubbleSort(evens)[::-1]
            # for j in range(len(evens)):
            #     num[i] = evens[j]
        else:
            odds.append(i)
            odds = bubbleSort(odds)
            # for k in range(len(odds)):
            #     num[i] = odds[k]

    # for j in range(len(num)): # 0,1,2,3,4,5
    #     if num[j]%2 == 0:
    #         num[0] = evens[0]
    #     else:
    #         num[0] = odds[0]

    num[0] = odds[0]
    num[1] = odds[1]
    num[2] = evens[0]
    num[3] = evens[1]
    num[4] = odds[2]
    num[5] = evens[2]

    # print(odds)
    # print(evens)
    # print(num)
    return num

print(sort_odd_even([5,3,2,8,1,4])) # [1,3,8,4,5,2]
# sort_odd_even([0])
# sort_odd_even([])



# SOAL NOMOR 4

def hollowTriangle(height):
    z = ""
    for i in range(height):     # rows = height     i = 0,1,2
        for j in range(height):    # width  j = 0,1,2
            if j <= (height+i+1) and j >= (height-i-1):
                z += "#"
            else:
                z += "_"
        for j in range(height):
            if j > 0:
                if j < height and j > height:
                    z += "#"
                else:
                    z += "_"
        z += "\n"
    return z

print(hollowTriangle(1))
print(hollowTriangle(2))
print(hollowTriangle(3))
print(hollowTriangle(4))
print(hollowTriangle(5))
print(hollowTriangle(6))