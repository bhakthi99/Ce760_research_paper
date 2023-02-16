
k= 2.315*(10**(-6))

import math
e= math.e

U=0.025
Sd=2.0834*(10**(-3))

#initial value of c 
c=2100

C=[c]
actual_values=[25.72, 24.34,24.10,23.99, 22.80]

xs=[1500,1370,940,633,330,30]

for i in range(5):

   x = xs[i]-xs[i+1]

   v = e**(-(k*x)/U)
   print("v",v)

   c=c*v + (Sd/k)*(1-v)
   
   C.append(c)

   print("P"+str(i+1), c, x)

import matplotlib.pyplot as plt

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(20)


plt.plot(xs[1:], C[1:], color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=5, label="predicted")
plt.plot(xs[1:], actual_values, color='blue', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=5, label="actual")

# setting x and y axis range
plt.xlim(1500,0)

# naming the x axis
plt.xlabel(' x in m  ')
# naming the y axis
plt.ylabel('C')
  
# giving a title to my graph
plt.title('Plot')
  
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

C1=list(c1 for c1 in C)
print(C1)
plt.plot(xs[1:], C1[1:], color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=5, label="predicted")
# setting x and y axis range
plt.xlim(1500,0)

# naming the x axis
plt.xlabel(' x in m  ')
# naming the y axis
plt.ylabel(' COD (mg/L)')
  
# giving a title to my graph
plt.title('Plot')
  
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

plt.plot(xs[1:], actual_values, color='blue', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=5, label="actual")
# setting x and y axis range
plt.xlim(1500,0)

# naming the x axis
plt.xlabel(' x in m  ')
# naming the y axis
plt.ylabel(' COD (mg/L)')
  
# giving a title to my graph
plt.title('Plot')
  
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

