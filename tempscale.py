print("This program converts the tempurature between celsius, kelvin, and\
fahrenheit scales,enter the temperature followed by the first letter of the\
scale, e.g. 32c for 32 celsius")

#user enters input
temperature = input(">") 

#sets the letter at the end of the string as the variable entered_scale
scale = (temperature[-1])
digit_length = (len(temperature) - 1)
digits = int(temperature[0:digit_length])
print(digits) 

if scale == "c":  
    fahrenheit = digits * 1.8 + 32    #logic
    kelvin = digits + 273.15 
    celsius = digits
    
elif scale == "f":
    celsius = (digits - 32) / 1.8
    kelvin = (digits + 459.67) * 0.55555556
    fahrenheit = digits
    
elif scale == "k":
    fahrenheit = digits / 0.55555556 - 459.67
    celsius = digits - 273.15
    kelvin = digits

print("Your Temperature In Celsius Is", celsius)
print("Your Temperature In Fahrenehit Is", fahrenheit)
print("Your Temperature In Kelvin Is", kelvin)
