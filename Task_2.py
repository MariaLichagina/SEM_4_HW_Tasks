# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом 
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего 
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым 
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import  randint

total_num_bushes = int(input("Введите количество кустов на грядке (3 или более): "))

blueberry_bed = []
for i in range(1,total_num_bushes+1):
    blueberry_bed.append(randint(100, 1000))
print(blueberry_bed)

num_bush = int(input("Введите номер куста: "))

running = True

while running:
    if num_bush-1 in range(len(blueberry_bed)):
        print(f'Кол-во ягод на этом кусте: {blueberry_bed[num_bush-1]}')
        running = False
    else:
        print(f'Введите номер куста в пределах {total_num_bushes}, начиная с 1!')
        num_bush = int(input("Введите номер куста: "))
        
sum_berries = 0

if num_bush not in range(len(blueberry_bed)):
    sum_berries = blueberry_bed[num_bush-1] + blueberry_bed[0] + blueberry_bed[num_bush-2]

elif num_bush-2 not in range(len(blueberry_bed)):
    sum_berries = blueberry_bed[num_bush-1] + blueberry_bed[0] + blueberry_bed[1]

else:
    sum_berries = blueberry_bed[num_bush-1] + blueberry_bed[num_bush] + blueberry_bed[num_bush-2]

print(f'Всего ягод на этом кусте и двух соседних: {sum_berries}.')






