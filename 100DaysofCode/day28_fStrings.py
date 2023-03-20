#string formatting (introduced in python version 3.6)
letter="Hey my name is {} and I am from {}"
name = "Harry"
country = "India"
print(letter.format(name,country)) #altering may result in wrong results
letter="Hey my name is {1} and I am from {0}"
print(letter.format(country,name)) #(0,1)

##fString
print(f"Hey my name is {name} and I am from {country}")
#as it is
print(f"Hey my name is {{name}} and I am from {{country}}")

#old way of string formatting
txt="For only {price:.2f} dollars!"
print(txt.format(price = 843.87387479))

#fstring
price=898.843977398
print(f"For only {price:.2f} dollars")

print(type(f"{2*34}"))