print "This program converts the tempurature between celsius, kelvin, and\
fahrenheit scales,enter the temperature followed by the first letter of the\
scale, e.g. 32c for 32 celsius"

#user enters input
temperature = raw_input(">") 

#sets the letter at the end of the string as the variable entered_scale
entered_scale = temperature [-1]

print entered_scale

if entered_scale == "c":  
    new_scale = temperature.replace("c", "") #rips the letter off 
    celsius = int(new_scale)                ## and converts string to interger
    fahrenheit = celsius * 1.8 + 32    #logic
    print "Fahrenheit = ", fahrenheit #prints answer to user
    kelvin = celsius + 273.15 
    print "Kelvin = ", kelvin

elif entered_scale == "f":
    new_scale = temperature.replace("f", "")
    fahrenheit = int(new_scale)
    celsius = (fahrenheit - 32) / 1.8
    print "Celsius = ", celsius
    kelvin = (fahrenheit + 459.67) * 0.55555556
    print "Kelvin = ", kelvin

elif entered_scale == "k":
    new_scale = temperature.replace("k", "")
    kelvin = int(new_scale)
    fahrenheit = kelvin * 0.55555556 - 459.67
    print "Fahrenheit = ", fahrenheit
    celsius = kelvin - 273.15
    print "Celsius= ", celsius
