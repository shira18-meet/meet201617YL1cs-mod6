#Module 6, Part 5: Practice with dictionaries here


my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###
num=my_phonebook["Statue of Liberty"]
###
#Print the variable, num
###
print(num)
###
#Change the value of the Ghostbusters' phone number to 2125559876
###
my_phonebook["Ghostbusters"]=2125559876
#Here's an empty dictionary
my_phonebook={}

###
#Add 5 values to it like this
#your_phonebook['key']=value
###
my_phonebook["MY_NAME"]="Shira"
my_phonebook["MY_STREET"]="Carmel"
my_phonebook["MY_HOUSE_NUM"]=26
my_phonebook["MY_DAD'S_NAME"]="Wladimir"
my_phonebook["MY_MOM'S_NAME"]="Rina"

###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys
the_keys=my_phonebook.keys()
#Loop over this sequence with a for loop
#using syntax like

#for key in sequence_of_keys :
#    #Do stuff

#Use the loop to print to the shell the key and value
#of every element in the dictionary
###
for i in the_keys:
    print(my_phonebook[i])
