title = "G re en  Lant  ern C  orp"

counter = 0

while counter < len(title):
    if (counter % 2) == 0 and title[counter] != ' ':
        print(title[counter])
    counter += 1

# %2 means, as long as counter is divisible by 2 // loop through and print ever other character
# counter needs to be part of the while loop, not the if statement
# counter += means, add 1 every count

# this means, that if there are no blank spaces, then COUNT EM