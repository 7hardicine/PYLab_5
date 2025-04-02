import numpy as np

#arr = np.array([[1,2,3,4,5,6],[9,8,7,6,5,4]]) #Лучший случай
#arr = np.array([[17, 13, 6, 15, 13, 2],[7, 4, 11, 2, 12, 4]]) #Худший случай дефектная партия
#arr = np.array([[13, 13, 6, 15, 13, 2],[7, 4, 11, 2, 12, 4]]) #Когда целых больше дефектная партия
#arr = np.array([[17, 13, 6, 15, 13, 2],[7, 11, 11, 2, 12, 4]]) #Когда целых меньше дефектная партия
arr = np.array([[10, 5, 20, 6, 10, 5, 11],[11, 2, 5, 7, 3, 4, 8]]) #Целая но не идеальная

PV = 15
PD = 10
size = len(arr[0])
defective = 0
def_weight_summ = 0

for i in range(size):
    if arr[0][i] > PV or arr[1][i] > PD:
        defective += 1
        def_weight_summ += arr[0][i]

if defective > 0:
    def_weight_avg = def_weight_summ / defective
    print("Средний вес дефектных деталей:", def_weight_avg)
    percent = defective/size
    if percent > 0.3:
        print("Партия бракованная!!")
    if percent > 0.5:
        print("Бракованных деталей больше, чем целых")
    elif percent == 0.5:
        print("Бракованных и целых деталей одинаковое количество")
    else:
        print("Бракованных деталей меньше, чем целых")
else:
    print("Нет бракованных делатей!!")
