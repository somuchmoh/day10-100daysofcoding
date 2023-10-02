#Functions
def something():
    print("something")
    #Do something

#Function with inputs
def something_else(parameter):
    print(parameter)
    #Do something with parameter

#Functions with outputs
def my_function():
    result = 3 * 2
    return result 
#output is now 6

#Function with input and output
def format_name(f_name, l_name):
    """It's going to take the first and last name and format it."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
#Return function will store the variables 


formated_string = format_name("mOhANa", "madhurakavi")
#Return is captured inside formated_string and printed below
print(formated_string)

