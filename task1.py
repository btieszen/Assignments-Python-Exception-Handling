# Exceptional Weather Forecast
#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.
while True:
    try:    
        temp = float(input("What is the temperature in degrees Fahrenheit: "))
    except ValueError:
        print(f"Please enter a  number")
    else:
        celcius = ((temp) - 32) * 5/9
        print(f"{temp} degrees Fahrenheit is {celcius} degrees Celsius.")
    finally:
        print("Thank you for using our weather sysytem")
    
    
        
    
    
        
    



