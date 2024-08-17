'''temperature calculator from Celsius to Fahrenheit'''

def fahrenheit(temperature):
    return 5*(temperature-32)/9

temperature=int(input("the temperature is :"))
c=fahrenheit(temperature)
print(c)
