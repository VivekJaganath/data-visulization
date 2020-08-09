from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import math


#reading data
def read(Data):
    n = len(Data)
    Datanew = np.zeros((n,n))
    for i in range(n-1 ,-1, -1):
        for j in range(0,len(Data[i])):
            rem = Data[i][j].strip('"')
            Datanew[i][j] = np.double(rem)
    y = 499
    n = len(Datanew)
    Data1 = np.zeros((n,n))
    for i in range(0,len(Datanew)):
        for j in range(0,len(Datanew[i])):
            Data1[i][j] = Datanew[y][j]
        y = y - 1
    return Data1

Data = np.loadtxt("C:\\Users\\Vivek\\Downloads\\orion\\orion\\i170b2h0_t0.txt", delimiter=",", dtype = str)
Data = Data.reshape([500,500])

#Printing Max, min and Variance
Data1 = read(Data)
print("Max: ", np.amax(Data1))
print("Min: ", np.amin(Data1))
print("Variance: ", np.var(Data1))
print("Mean: ", np.mean(Data1))

#Draw a profile line through the line with the maximum value of this 2D data set;
PL = []
max = np.amax(Data1)
b = np.where(Data1 == max)
rw = b[0]
for i in range(len(Data1)):
    if i == rw:
        PL = (Data1[i])
plt.title('profile line through the line with the maximum value')
plt.xlabel('Position on x-axis')
plt.ylabel('Data values')
plt.plot(PL)
plt.show()

#C) Plotting histogram to find absolute occurrence of data value
#refrence - https://stackoverflow.com/questions/10741346/numpy-most-efficient-frequency-counts-for-unique-values-in-an-array
unique,count = np.unique(Data1,return_counts=True)
plt.title('Histogram of absolute occurrence')
plt.xlabel('Data values')
plt.ylabel('absolute occurrence')
plt.plot(unique,count)
plt.show()

#d) Rescaling values to range between 0 and 255 using a non-linear transformation.
#reference - Using non-linear transformation formula from chapter 3 slide 13
#T(r) = log2((r+1)^c)
x = len(Data1)
nl = np.zeros((x,x))
c = 18.14
for i in range(0,x):
    for j in range(0,len(Data1[i])):
        y = Data1[i][j] + 1
        z = y ** c
        nl[i][j] = math.log(z, 2)

nmax = nl[0][0]
nmin = nl[0][0]
for items in Data1:
    for item in items:
        if item > nmax:
            nmax = item
        elif item < nmin:
            nmin = item
plt.title('Non-Linear Transformation of data values')
plt.imshow(nl, cmap=cm.gray)
v = np.linspace(0, 255, 15, endpoint=True)
plt.colorbar(label='New values ranging from max to min', ticks=v)
plt.show()

#e)Carry out a Histogram equalization on each of the four bands
#ref: Chapter 3 slide 40-45
#ref: https://www.tutorialspoint.com/python-program-to-find-cumulative-sum-of-a-list
#ref: https://www.geeksforgeeks.org/numpy-where-in-python/
#ref: https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/subplots_demo.html

def Cumulative(l):
   new = []
   cumsum = 0
   for element in l:
      cumsum += element
      new.append(cumsum)
   return new

def sum(l):
    total = 0
    for x in l:
        total += x
    return total

def index(unique, value):
    newu = np.array(unique).tolist()
    return newu.index(value)

def equilization(Data1):
    unique,count= np.unique(Data1, return_counts=True) #Calculating r and p values
    x= sum(count)
    pr = count / x #Calculating relative occurance
    cdf = Cumulative(pr)
    s = cdf * 255
    for i in range(len(Data1)):
        for j in range(len(Data1[i])):
            indx1 = index(unique, Data1[i][j])
            y = indx1
            Data1[i][j] = s[y]
    return Data1

Data = np.loadtxt("C:\\Users\\Vivek\\Downloads\\orion\\orion\\i170b1h0_t0.txt", delimiter=",", dtype = str)
Data = Data.reshape([500,500])
Data2 = read(Data)
HE1 = equilization(Data2)

HE2 = equilization(Data1)

Data = np.loadtxt("C:\\Users\\Vivek\\Downloads\\orion\\orion\\i170b3h0_t0.txt", delimiter=",", dtype = str)
Data = Data.reshape([500,500])
Data3 = read(Data)
HE3 = equilization(Data3)

Data = np.loadtxt("C:\\Users\\Vivek\\Downloads\\orion\\orion\\i170b4h0_t0.txt", delimiter=",", dtype = str)
Data = Data.reshape([500,500])
Data4 = read(Data)
HE4 = equilization(Data4)

f, axarr = plt.subplots(2,2)
axarr[0, 0].imshow(HE1, cmap='gray')
axarr[0, 0].set_title("i170b1h0_t0.txt")
axarr[0, 1].imshow(HE2, cmap='gray')
axarr[0, 1].set_title("i170b2h0_t0.txt")
axarr[1, 0].imshow(HE3, cmap='gray')
axarr[1, 0].set_title("i170b3h0_t0.txt")
axarr[1,1].imshow(HE4, cmap='gray')
axarr[1, 1].set_title("i170b4h0_t0.txt")
plt.show()

#f)Combine the histo-equalized data set to an RGB-image (b4=r, b3=g, b1=b).
#ref: https://www.w3resource.com/numpy/manipulation/dstack.php
#ref: https://stackoverflow.com/questions/18595488/combining-2d-arrays-to-3d-arrays
combine = np.dstack([HE4, HE3, HE1]).reshape((500, 500, 3))
plt.imshow(combine)
plt.title("RGB Image with datasets b4=r, b3=g, b1=b")
plt.show()