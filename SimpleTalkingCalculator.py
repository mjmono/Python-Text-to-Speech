# De Dios, Mark Joshua

import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

engine.say("Enter 1st number: ")
engine.runAndWait()
num1 = int(input("Enter 1st number: "))

engine.say("Enter 2nd number: ")
engine.runAndWait()
num2 = int(input("Enter 2nd number: "))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quo = num1 / num2

print("\nSum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Quotient:", quo)
engine.say("sum, " + str(sum))
engine.say("difference, " + str(diff))
engine.say("product, " + str(prod))
engine.say("quotient, " + str(quo))
engine.runAndWait()




