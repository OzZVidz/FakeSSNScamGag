#This asks the user for their first name.
fname = str(input("What is your first name? "))
lname = str(input("What is your last name? "))

#This gives the user one line of output, then adds two lines to the bottom.
print("Your name is " + fname + " " + lname + ". Cool!\n~~~")

#This asks the user how they are feeling today, and asks if I can have their SSN.
feeling = input("So, how are you doing today? ")
print ("Wow! Glad to know you're feeling " + feeling + " today. Now, next question!\n~~~")
yesno = input ("This is kind of a longshot, but can you tell me your SSN? (This is a \"yes\" or \"no\" answer) ")

#This sets the user's response to yesno, and sets multiple outcome variables.
response = yesno
no = str(("no"))
No = str(("No"))
NO = str(("NO"))
nO = str(("nO"))
yes = str(("yes"))
YES = str(("YES"))
Yes = str(("Yes"))
yEs = str(("yEs"))
yeS = str(("yeS"))
YEs = str(("YEs"))
yES = str(("yES"))
YeS = str(("YeS"))

#These below match different responses.
if response == no:
    print("Wow," + fname + ", you're mean. At least you responded with a normal no.")

elif response == No:
    print("Wow, " + fname + ", you're mean. At least you capatalized the first \"N\" in No.")

elif response == NO:
    print("Wow," + fname + ", you're mean. You also seem very mad because you used all caps in the word \"NO\"")

elif response == nO:
    print("Wow, " + fname + ", you're mean. Also, are you weird or something? Why did you write \"No\" like \"nO?\"")

elif response == yes:
    print("Wow, " + fname + ", you're generous. You know what, just because you spelled \"yes\" correctly and sanely without crazy caps, I'll let you keep it today.")

elif response == YES:
    print("Wow, " + fname + ", you're generous. You also seem kind of happy too because you inputted \"YES\" Please input below.")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

elif response == Yes:
    print("Wow, " + fname + ", you're generous. You know what, just because you spelled \"Yes\" correctly and sanely without crazy caps, I'll let you keep it today.")

elif response == yEs:
    print("Wow, " + fname + ", you're generous. Please input below, because you're weird and spelled yes as \"yEs\"")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

elif response == yeS:
    print("Wow, " + fname + ", you're generous. Please input below, because you're weird and spelled yes as \"yeS\"")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

elif response == YEs:
    print("Wow, " + fname + ", you're generous. Please input below, because you're weird and spelled yes as \"YEs\"")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

elif response == yES:
    print("Wow, " + fname + ", you're generous. Please input below, because you're weird and spelled yes as \"yES\"")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

elif response == YeS:
    print("Wow, " + fname + ", you're generous. Please input below, because you're weird and spelled yes as  \"YeS\"")
    ssn = input("Okay, what is your social security number? ")
    print("Thanks for your Social Security number, which is allegedly " + ssn + ". Have a nice day.")

else:
    print("Invalid response, are you dumb?\n\n(If you're confused why you got this, it's because you didn't answer with a \"Yes\" or a \"No\")\n\n(You're gonna have to rerun the script now, but try answering with random caps if you want.. ;)")

#End of script message, regardless of response.
print("~~~\n\nThanks for using my first script ever created!\n(By the way, no I did not take your Social Security Number. This script is completely harmless.) \nIf you did actually input your real Social Security Number, please, don't do that again. People could create credit cards with your name!\n\nCreated October 7, 2020 by Osaym Omar. Updated May 22, 2021")