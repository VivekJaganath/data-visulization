from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import math

#Reading slice150.raw and reshaping
#refrence: https://stackoverflow.com/questions/17479296/read-in-raw-binary-image-in-python
Data = np.fromfile("C:\\Users\\Vivek\\Downloads\\slice150.raw",dtype='int16',sep="")
Data = Data.reshape([512,512])
#A) Proflie Line - plotting datavalues ranging between 0 to 255
#refrence - Chapter 3 slide 51
PL = []
for i in range(len(Data)):
    if i == 255:
        PL = Data[i]
plt.title('Profile Line through line 256')
plt.xlabel('Position on x-axis')
plt.ylabel('Data values')
plt.plot(PL)
plt.show()

#B) Finding Mean and variance value:
#refrence - https://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html
#reference - https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html#numpy.mean

print("The mean value of the dataset is: ", np.mean(Data))
print("The variance value of the dataset is: ", np.var(Data))

#C) Plotting histogram to find absolute occurrence of data value
#refrence - https://stackoverflow.com/questions/10741346/numpy-most-efficient-frequency-counts-for-unique-values-in-an-array
unique,count = np.unique(Data,return_counts=True)
width = .5
plt.title('Histogram of absolute occurrence')
plt.xlabel('Data values')
plt.ylabel('absolute occurrence')
plt.bar(unique,count, width, color = "tomato")
plt.show()

#D) Rescaling values to range between 0 and 255 using a linear transformation.
#refrence - Using linear transformation formula from chapter 3 slide 35
#T(r) = ((r-rmin)/(rmax-rmin)*smax
rmax = Data[0,0]
rmin = Data[0,0]
for items in Data:
    for item in items:
        if item > rmax:
            rmax = item
        elif item < rmin:
            rmin = item
smax = 255
x = len(Data)
l = np.zeros((x,x))
for i in range(0,len(Data)):
    for j in range(0,len(Data[i])):
        l[i][j] = int((((Data[i][j]) - rmin))/(rmax - rmin)*smax)
plt.title('Linear Transformation of Data')
plt.imshow(l, cmap=cm.gray)
plt.show()

#E) Rescaling values to range between 0 and 255 using a non-linear transformation.
#reference - Using non-linear transformation formula from chapter 3 slide 13
#T(r) = log2((r+1)^c)
x = len(Data)
nl = np.zeros((x,x))
c = 23.1
for i in range(0,x):
    for j in range(0,len(Data[i])):
            y = Data[i][j] + 1
            z = y ** c
            nl[i][j] = math.log(z, 2) 
plt.title('Non-Linear Transformation of data values')
plt.imshow(nl, cmap=cm.gray)
plt.show()

#F)  11x11 boxcar smoothing filter on  data set
#refrence - Chapter 3, page 56-60
#kernel/boxcar = 11*11
kernel = np.zeros((11,11)) #boxcar filer
result = np.zeros((512,512)) #resultant matrix after smoothing
for i in range(0,len(Data)):
    if ((len(Data) - i) >= (len(kernel))): # limiting rows to the size of the kernal
        for j in range(0,len(Data[i])):
            if ((len(Data[i]) - j) >= (len(kernel))): # limiting coloumns to the size of the kernal
                sum = 0
                for row in range(i, i + 11): #  11 rows for boxcar
                    for col in range(j, j + 11):#   11 columns for boxcar
                        sum = sum + Data[row][col] #summing of data in rows and coloumns
                result[i][j] = (sum/11) #taking average and append
plt.title('BoxCar Smoothing Filter on the dataset')
plt.imshow(result, cmap=cm.gray)
plt.show()

#G)  11x11 median filter on data set.
#refrence - Chapter 3, page 61-65
#reference - https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
#reference - https://kite.com/python/answers/how-to-sort-a-list-of-numbers-without-built-in-sort(),-min(),-max()-in-python
#kernel/median = 11*11
def sort(templist):
    unsorted_list = templist
    sorted_list = []
    while unsorted_list:
        minimum = unsorted_list[0]
        for item in unsorted_list:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)
    return sorted_list

def median(templist):
    n_num = templist
    n = len(n_num)
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n // 2]
        median2 = n_num[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = n_num[n // 2]
    return median

kernel = np.zeros((11, 11))
mf = np.zeros((512, 512))
for i in range(0, len(Data)):
    if ((len(Data) - i) >= (len(kernel))):
        for j in range(0, len(Data[i])):
            if ((len(Data[i]) - j) >= (len(kernel))):
                templist = []
                sortedlist = []
                for row in range(i, i + 11):
                    for col in range(j, j + 11):
                        templist.append(Data[row][col])
                        sortedlist = sort(templist)
                mf[i][j] = median(sortedlist)
plt.title('Median Filter on the dataset')
plt.imshow(mf, cmap=cm.gray)
plt.show()