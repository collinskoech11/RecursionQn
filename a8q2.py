Year = [2001,2002,2003,2004,2005,2006,2007,2008]
Population = [100,150,200,250,300,350,400,450]  

import matplotlib.pyplot as plt

initial_population =  int(input("Iinitial pupolation \n"))
n = int(input("No of years \n"))
r = float(input("Growth rate in that year \n"))
K = int(input("Maximum population the environment can support \n"))
current_population = 0
lst = []
count = 0




def rucursive():
    for count in range (0,n):
        for i in range(0,n):
            current_population = ((initial_population * r) + initial_population)
            lst.append(curent_population)
        count + 1
    else:
        return 0



print(lst)

plt.plot(Year, Population)
plt.title('Population Growth Rate ')
plt.xlabel('Year')
plt.ylabel('Population THat Year')
plt.show()


print("Span No of years :" , n , "\n")
print("Population Growth Rate :" , r , "\n")
print("Max Population :" , K , "\n")