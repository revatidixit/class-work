# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None.
#x = [1,2,3,4,5]

''' def chop(x):
  
  del x[0]
  del x[-1:]
  print (x)
  return None
  
print (chop(x)) '''

# Then write a function called middle that takes a list 
# and returns a new list that contains all but the first and last elements.

''' x = [1,2,3,4,5]
def middle(x):
    x.pop(0)
    x.pop(len(x)-1)
    return x

print(middle(x)) '''


''' user_data = input("Which file? ")

fhand = open(user_data, 'r')

count = 0

for line in fhand:

    words = line.split()

    # print 'Debug:', words

    if len(words) == 0 : 
        continue

    if words[0] != 'From' : 
        continue

    print (words[2]) '''

#Exercise 2: Figure out which line of the above program is still not properly guarded. 
# See if you can construct a text file which causes the program to fail 
# and then modify the program so that the line is properly guarded 
# and test it to make sure it handles your new text file.
''' user_data = input ("Which file? ")

fhand = open(user_data, 'r')

count = 0

for line in fhand:

    words = line.split()

    # print 'Debug:', words

    if len(words) == 0 or len(words) < 3: 
        continue

    if words[0] != 'From' : 
        continue

    print (words[2]) '''
# Exercise 3: Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the and logical operator with a single if statement
''' fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or words[0] != 'From': 
        continue
    print (words[2]) '''

''' user_data = input("Which file? ")

fhand = open(user_data, 'r')

count = 0

for line in fhand:

    words = line.split()

    # print 'Debug:', words

    if (len(words) == 0 or len(words) < 3) or words[0] != 'From' : 
        continue

    print (words[2]) '''

# Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt 
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

''' fname = input("Enter file: ")
lines = [line.strip('\n') for line in open(fname, 'r')]
word_list = []
for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_list:
            pass
        else:
            word_list.append(word)
print (sorted(word_list)) '''

# Exercise 5: Write a program to read through the mail box data and 
# when you find line that starts with “From”, you will split the line into words using the split function. 
# We are interested in who sent the message, which is the second word on the From line.
''' fname = input("Enter a file name: ")

lines = [line.strip("\n") for line in open(fname, 'r')
         if line.startswith("From") and not line.startswith("From:")]
count = 0
for line in lines:

    words = line.split()

    print (words[1])

    count += 1

print("There were",count, "lines in the file with From: as the first word") '''

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and 
# prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
# Write the program to store the numbers the user enters in a list and use the max() and min() 
# functions to compute the maximum and minimum numbers after the loop completes.

''' def FindMinMax():
    user_responses = []
    while True:
        try:
            user_input = input("Enter a number: ")
            user_input = int(user_input)
        except:
            break
        user_responses.append(user_input)
    print ("Maximum: ", max(user_responses))
    print ("Minimum: ", min(user_responses))

FindMinMax() '''

#Exercise 1: [wordlist2] Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.

''' lines = [word.strip('\n') for word in open('words.txt', 'r')]
wordDict = {}
for line in lines:
    words = line.split()
    for word in words:
        wordDict[word] = None

print ("would" in wordDict)

print ("fortune" in wordDict)

print ("daily" in wordDict)

print ("Seattle" in wordDict) '''

#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running 
# count of each of the days of the week. At the end of the program print out the contents of your dictionary 
# (order does not matter). 

''' fname = 'mbox-short.txt'
lines = [line.strip('\n') for line in open(fname, 'r')
         if line.startswith("From ")]
dateDict = {}
for line in lines:
    words = line.split()
    dateDict[words[2]] = dateDict.get(words[2], 0) + 1
print (dateDict) '''

# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
# to count how many messages have come from each email address, and print the dictionary
''' fname = 'mbox-short.txt'
lines = [line.strip('\n') for line in open(fname, 'r')
         if line.startswith("From ")]
NumberOfMessages = {}
for line in lines:
    words = line.split()
    NumberOfMessages[words[1]] = NumberOfMessages.get(words[1], 0) + 1
print (NumberOfMessages) '''

# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
#After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Section [maximumloop]) 
# to find who has the most messages and print how many messages the person has.

''' fname = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(fname, 'r')
         if line.startswith("From ")]
NumberOfMessages = {}
for line in lines:
    words = line.split()
    NumberOfMessages[words[1]] = NumberOfMessages.get(words[1], 0) + 1
most = 0
MaxMessages = None
for person in NumberOfMessages:
    if NumberOfMessages[person] > most:
        most = NumberOfMessages[person]
        MaxMessages = person
print (MaxMessages, NumberOfMessages[MaxMessages]) '''

# Exercise 5: This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

''' fname = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(fname, 'r')
         if line.startswith("From ")]
NumberOfMessages = {}
for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    NumberOfMessages[domain] = NumberOfMessages.get(domain, 0) + 1
print (NumberOfMessages) '''

# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary. 
# After all the data has been read, print the person with the most commits by creating 
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print 
# out the person who has the most commits.

''' fname = input("Enter a file name: ")
lineList = [line.strip("\n") for line in open(fname, 'r')
             if line.startswith("From ")]
emailDict = {}
for line in lineList:
    email = line.split()[1]
    emailDict[email] = emailDict.get(email, 0) + 1
tupleList = []
for email in emailDict:
    tupleList.append((emailDict[email], email))
MaxMessages = sorted(tupleList, reverse=True)[0]
print (MaxMessages[1], MaxMessages[0]) '''

# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string 
# into parts using the colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.
''' fname = input("Enter a file name: ")
lineList = [line.strip("\n") for line in open(fname, 'r')
             if line.startswith("From ")]
hourHistogram = {}
tupleList = []
for line in lineList:
    time = line.split()[5]
    hour = time.split(":")[0]
    hourHistogram[hour] = hourHistogram.get(hour, 0) + 1
for key in hourHistogram:
    tupleList.append((key, hourHistogram[key]))
sortedTuplelist = sorted(tupleList)
for item in sortedTuplelist:
    print(item[0], item[1]) '''

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages.

fname = input("Which book? ")
book = open(fname, 'r')
def prepare_text(raw_book):
    ''' Take file handler as input. Chop off the project Gutenberg header
    and footer. Remove non-alpha characters. Convert all letters to
    lowercase and finally return the entire book as a singe string '''
    startMarker = "*** START OF THIS"
    endMarker = "*** END OF THIS"
    processText = False
    bookLines = []
    allLetters = ''
    for line in raw_book:
        # see the start marker, switch flag to begin processing
        if line.startswith(startMarker) and processText is False:
            processText = True
        # see the end marker, switch flag to end processing
        if line.startswith(endMarker) and processText is True:
            processText = False
        if processText is True:
            line = ''.join([char for char in line if char.isalpha()])
            line = line.lower()
            bookLines.append(line)
    allLetters = allLetters.join(bookLines)
    return allLetters
condensedBooks = prepare_text(book)
letterHistogram = {}
for letter in condensedBooks:
    letterHistogram[letter] = letterHistogram.get(letter, 0) + 1
resultLists = []
for key in letterHistogram:
    resultLists.append((letterHistogram[key], key))
print ("Letter frequency:", fname)
for pair in sorted(resultLists, reverse=True):
    print (pair[1], pair[0])
