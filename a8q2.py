import matplotlib.pyplot as plt


initial_population =  int(input("Iitial pupolation"))
n = int(input("Year in qn"))
r = float(input("Growth rate in that year"))
K = int(input("Maximum population the environment can support"))

    
Year = [2001,2002,2003,2004,2006,2007,2008,2009]
Population = [100,150,200,250,300,350,400,450]  
plt.plot(Year, Population)
plt.title('Population Growth Rate ')
plt.xlabel('Year')
plt.ylabel('Population THat Year')
plt.show()