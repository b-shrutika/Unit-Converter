import numpy as np
def length():
    frm = input("From(km ↔ miles,meters ↔ feet,cm ↔ inches): ").lower()
    to = input("To: ").lower()
    value = np.array(list(map(float, input("Enter value(leave the space between two consecutive values): ").split())))
    if frm == 'km' and to=='miles':
     print(value * 0.621371)
    elif frm == 'miles' and to=='km':
     print(value / 0.621371)
    elif frm == 'meters' and to=='feet':
     print(value * 3.28084)
    elif frm == 'feet' and to=='meters':
     print(value / 3.28084)
    elif frm == 'cm' and to=='inches':
     print(value * 0.393701)
    elif frm == 'inches' and to=='cm':
     print(value / 0.393701)
    else:
     print("Enter valid unit conversion!!")

def weight():
   frm = input("From(kg ↔ pounds,g ↔ ounces): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float, input("Enter value(leave the space between two consecutive values): ").split())))
   if frm == 'kg' and to=='pounds':
     print(value * 2.20462)
   elif frm == 'pounds' and to=='kg':
     print(value / 2.20462)
   elif frm == 'g' and to=='ounces':
     print(value * 0.035274)
   elif frm == 'ounces' and to=='g':
     print(value / 0.035274)
   else:
      print("Enter valid unit conversion!!")

def temperature():
   frm = input("From(celsius ↔ fahrenheit, kelvin ↔ celsius): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float, input("Enter value(leave the space between two consecutive values): ").split())))
   if frm == 'celsius' and to=='fahrenheit':
     print((value * 9/5) + 32)
   elif frm == 'fahrenheit' and to=='celsius':
     print((value - 32) * 5/9)
   elif frm == 'celsius' and to=='kelvin':
     print(value + 273.15)
   elif frm == 'kelvin' and to=='celsius':
     print(value - 273.15)
   else:
      print("Enter valid unit conversion!!")

def time():
   frm = input("From(hours ↔ minutes ↔ seconds,days ↔ weeks,days ↔ years): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'hours' and to=='minutes':
     print(value * 60)
   elif frm == 'minutes' and to=='seconds':
     print(value * 60)
   elif frm == 'days' and to=='weeks':
     print(value / 7)
   elif frm == 'days' and to=='years':
     print(value / 365)
   else:
      print("Enter valid unit conversion!!")

def area():
   frm = input("From(sq meters ↔ sq feet, acres ↔ hectares): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'sq meters' and to=='sq feet':
     print(value * 10.7639)
   elif frm == 'sq feet' and to=='sq meters':
     print(value / 10.7639)
   elif frm == 'acres' and to=='hectares':
     print(value * 0.404686)
   elif frm == 'hectares' and to=='acres':
     print(value / 0.404686)
   else:
      print("Enter valid unit conversion!!")
    
def volume():
   frm = input("From(liters ↔ milliliters,liters ↔ gallons,liters ↔ cups): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'liters' and to=='milliliters':
     print(value * 1000)
   elif frm == 'liters' and to=='gallons':
     print(value * 0.264172)
   elif frm == 'liters' and to=='cups':
     print(value * 4.22675)
   elif frm == 'cups' and to=='liters':
     print(value / 4.22675)
   elif frm == 'gallons' and to=='liters':
     print(value / 0.264172)
   else:
      print("Enter valid unit conversion!!")

def currency():
   frm = input("From(USD ↔ INR,JPY ↔ EUR): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'usd' and to=='inr':
     print(value * 83.10)
   elif frm == 'inr' and to=='usd':
     print(value / 83.10)
   elif frm == 'jpy' and to=='eur':
     print(value * 163.45)
   elif frm == 'eur' and to=='jpy':
     print(value / 163.45)
   else:
      print("Enter valid unit conversion!!")

def data():
   frm = input("From(KB ↔ MB,MB ↔ GB,GBs ↔ TB): ")
   to = input("To: ")
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'KB' and to=='MB':
     print(value / 1024)
   elif frm == 'MB' and to=='GB':
     print(value / 1024)
   elif frm == 'GB' and to=='TB':
     print(value / 1024)
   elif frm == 'MB' and to=='KB':
     print(value * 1024)
   elif frm == 'GB' and to=='MB':
     print(value * 1024)
   else:
      print("Enter valid unit conversion!!")
      
def speed(): 
   frm = input("From(mps ↔ kmph,mps ↔ mph,kmph ↔ mph): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'mps' and to=='kmph':
     print(value * 3.6)
   elif frm == 'kmph' and to=='mps':
     print(value / 3.6)
   elif frm == 'mps' and to=='mph':
     print(value * 2.23694)
   elif frm == 'mph' and to=='mps':
     print(value / 2.23694)
   elif frm == 'kmph' and to=='mph':
     print(value * 0.621371)
   elif frm == 'mph' and to=='kmph':
     print(value / 0.621371)
   else:
      print("Enter valid unit conversion!!")

def fuel_efficiency(): 
   frm = input("From(mpg(miles per gallon) ↔ kmpl(kilometers per liter),kmpL(kilometers per liter) ↔ L/100km(liter per 100km)): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'mpg' and to=='kmpl':
     print(value * 0.425144)
   elif frm == 'kmpl' and to=='mpg':
     print(value / 0.425144)
   elif frm == 'kmpl' and to=='l/100km':
     print(100 / value)
   elif frm == 'l/100km' and to=='kmpl':
     print(100 / value)
   else:
      print("Enter valid unit conversion!!")
def frequency(): 
   frm = input("From(Hz ↔ kHz,Hz ↔ MHz, Hz ↔ GHz, kHz ↔ MHz, MHz ↔ GHz, kHz ↔ GHz)): ").lower()
   to = input("To: ").lower()
   value = np.array(list(map(float,input("Enter value(leave the space between two consecutive values):").split())))
   if frm == 'hz' and to=='khz':
    print(value / 1000)
   elif frm == 'khz' and to=='hz':
     print(value * 1000)
   elif frm == 'hz' and to=='mhz':
     print(value / 1000000)
   elif frm == 'mhz' and to=='hz':
     print(value * 1000000)
   elif frm == 'hz' and to=='ghz':
     print(value / 1000000000)
   elif frm == 'ghz' and to=='hz':
     print(value * 1000000000)
   elif frm == 'khz' and to=='mhz':
     print(value / 1000)
   elif frm == 'mhz' and to=='khz':
     print(value * 1000)
   elif frm == 'mhz' and to=='ghz':
     print(value / 1000)
   elif frm == 'ghz' and to=='mhz':
     print(value * 1000)
   elif frm == 'khz' and to=='ghz':
     print(value / 1000000)
   elif frm == 'ghz' and to=='khz':
     print(value * 1000000)
   else:
      print("Enter valid unit conversion!!")

def main():
    choices = ['Length','Weight','Temperature','Time','Area','Volume','Currency','Data','Speed','Fuel Efficiency','Frequency','Exit']
    while True:
        for i,item in enumerate(choices):
            print(f"{i+1}. {item}")
        choice = int(input("Enter unit number to convert: "))
        if choice == 1:
            length()
        elif choice == 2:
            weight()
        elif choice == 3:
            temperature()
        elif choice == 4:
            time()
        elif choice == 5:
            area()
        elif choice == 6:
            volume()
        elif choice == 7:
            currency()
        elif choice == 8:
            data()
        elif choice == 9:
            speed()
        elif choice == 10:
            fuel_efficiency()
        elif choice == 11:
            frequency()
        elif choice == 12:
            print("Thank you!!")
            break
        else:
            print("Invalid input!!")

main()