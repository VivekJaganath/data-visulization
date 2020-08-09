import matplotlib.pyplot as plt
import numpy as np

#defining figure and size
fig, ax = plt.subplots(figsize=(10, 10))

#declating lists for values in the dataset starting position (x,y,z) and relative movement (u,v,w)
#since z and w are null ignoring them
X, Y, U, V, N, n1 = [],[],[],[],[],[]
x1, y1, u1, v1 = [], [], [], []

#Open the file and readlines
with open("field2.irreg.txt", "r") as f:
    rows = f.readlines()[6:] #ignoring the firts 6 values to get consistent plotting and to avoind indexing while itterating over elements
for line in rows:
    J = line.split(" ")
    X.append(float(J[0])) #filling the list with values from dataset
    Y.append(float(J[1]))
    U.append(float(J[3]))
    V.append(float(J[4]))

for i in range(len(U)):
    N.append(np.sqrt(U[i]**2)+(V[i]**2)) #calculating the length of vectors as discussed in the lectures

median = np.median(N)
min = np.min(N)
max = np.max(N)

#skipping and arranging data for better visulization
for i in range(len(N)):
    if i % 7 == 0 and N[i] >= median and N[i] < max:
        n1.append(N[i])
        x1.append(X[i])  # converting the list to numpy array to easily work on even larger datasets
        y1.append(Y[i])
        u1.append(U[i])
        v1.append(V[i])
for i in range(len(N)):
    if i % 7 == 0 and N[i] >= min and N[i] < median:
        n1.append(N[i])
        x1.append(X[i])
        y1.append(Y[i])
        u1.append(U[i])
        v1.append(V[i])
#Plotting the values
#refrence 1: https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.15-Quiver-and-Stream-Plots/
#reference 2: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.colorbar.html
#reference 3: https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html
plt.quiver(x1, y1, u1, v1, n1, cmap='cividis',scale=6, pivot="mid")
ax.set_title('Direction of Water in Tunnel')
ax.set_aspect('equal')
cbx = plt.colorbar()
plt.axis([0, 1, 0, 1])
cbx.set_ticks([0,0.5,1])
cbx.set_ticklabels(['Low', 'Medium', 'High'])
cbx.set_label('Velocity of water in tunnel')
plt.tight_layout()
plt.show()