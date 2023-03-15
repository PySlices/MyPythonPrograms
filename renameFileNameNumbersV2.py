#! python3
# renameFileNameNumbers.py

'''
"Finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in
a single folder and locates any gaps in the numbering (such as if there is a spam001.txt
and spam003.txt but no spam002.txt). The program renames all the later files to
close this gap." -Homework from Automate the Boring Things by Al Sweigart.
'''
#First filename that begins with prefix will start the counting so make sure it is 01 or 001...

from natsort import os_sorted
import os, re, shutil


#renames files
def numberfilefix(folder, prefix):
    # Create a regex search pattern that matches files with numbers and puts them in groups.
    numberPattern = re.compile(r"""
    ^(""" + re.escape(prefix) + """)           # starts with prefix variable
    (0*)?                           #any number of zeros. optional
    (\d*)                           # digits of any length
    (.*?)$                          # all text after the numbers
    """, re.VERBOSE) #allow whitespace and comments in code

    Comparelist = [] #stores numberparts to compare
    Inumber = 0
    lzerolist = []

    # Loop over the files in the working directory.
    for oldFilename in os_sorted(os.listdir(folder)): #sort folder files
        mo = numberPattern.search(oldFilename) #use search pattern

        # Skip files without numbers.
        if mo == None:
            continue

        # Get the different parts of the filename.
        beforePart = mo.group(1)
        zeroPart = mo.group(2)
        numberPart = mo.group(3)
        afterPart = mo.group(4)
        #print(numberPart + ' is numperpart')

        #store number of leading zeroes
        lzerolist.append(zeroPart)
        lzerolist.append(len(mo.group(2)))

        #check if the file's number is +1 the last file number
        Comparelist.append(numberPart)
        #print(Comparelist)

        if len(Comparelist) == 1: #skips the first file
            continue
        elif int(Comparelist[Inumber]) + 1 == int(numberPart): #checks if it is +1 the last file number
            Inumber += 1 #changes number to use for index
            #print(str(Inumber) + ' is Inumber')

            #currect numbers, now check leading zeroes
            if len(mo.group(2)) != lzerolist[1]:
                zeroPart = lzerolist[0]

                # Form the new file name.
                newFilename = beforePart + zeroPart + str(numberPart) + afterPart

                # Get the full, absolute file paths.
                absWorkingDir = os.path.abspath(folder)
                oldFilename = os.path.join(absWorkingDir, oldFilename)
                newFilename = os.path.join(absWorkingDir, newFilename)

                # Rename the files.
                print(f'Renaming "{oldFilename}" to "{newFilename}"...')
                shutil.move(oldFilename, newFilename)   # uncomment after testing


            continue
        else: #
            numberPart = str(int(Comparelist[Inumber]) + 1)
            #print(str(numberPart) + ' is altered numberpart ')
            zeroPart = lzerolist[0]
            Comparelist[Inumber + 1] = numberPart
            Inumber += 1

            # Form the new file name.
            newFilename = beforePart + zeroPart + str(numberPart) + afterPart

            # Get the full, absolute file paths.
            absWorkingDir = os.path.abspath(folder)
            oldFilename = os.path.join(absWorkingDir, oldFilename)
            newFilename = os.path.join(absWorkingDir, newFilename)

            # Rename the files.
            print(f'Renaming "{oldFilename}" to "{newFilename}"...')
            shutil.move(oldFilename, newFilename)   # uncomment after testing



#test run that prints what files will be renamed. does not actually rename files.
def numberfilefixtest(folder, prefix):
    # Create a regex search pattern that matches files with numbers and puts them in groups.
    numberPattern = re.compile(r"""
    ^(""" + re.escape(prefix) + """)           # starts with prefix variable
    (0*)?                           #any number of zeros. optional
    (\d*)                           # digits of any length
    (.*?)$                          # all text after the numbers
    """, re.VERBOSE) #allow whitespace and comments in code

    Comparelist = [] #stores numberparts to compare
    Inumber = 0
    lzerolist = []

    # Loop over the files in the working directory.
    for oldFilename in os_sorted(os.listdir(folder)): #sort folder files
        mo = numberPattern.search(oldFilename) #use search pattern

        # Skip files without numbers.
        if mo == None:
            continue

        # Get the different parts of the filename.
        beforePart = mo.group(1)
        zeroPart = mo.group(2)
        numberPart = mo.group(3)
        afterPart = mo.group(4)
        #print(numberPart + ' is numperpart')

        #store number of leading zeroes
        lzerolist.append(zeroPart)
        lzerolist.append(len(mo.group(2)))

        #check if the file's number is +1 the last file number
        Comparelist.append(numberPart)
        #print(Comparelist)

        if len(Comparelist) == 1: #skips the first file
            continue
        elif int(Comparelist[Inumber]) + 1 == int(numberPart): #checks if it is +1 the last file number
            Inumber += 1 #changes number to use for index
            #print(str(Inumber) + ' is Inumber')

            #currect numbers, now check leading zeroes
            if len(mo.group(2)) != lzerolist[1]:
                zeroPart = lzerolist[0]

                # Form the new file name.
                newFilename = beforePart + zeroPart + str(numberPart) + afterPart

                # Get the full, absolute file paths.
                absWorkingDir = os.path.abspath(folder)
                oldFilename = os.path.join(absWorkingDir, oldFilename)
                newFilename = os.path.join(absWorkingDir, newFilename)

                # Rename the files.
                print(f'Renaming "{oldFilename}" to "{newFilename}"...')
                #shutil.move(oldFilename, newFilename)   # uncomment after testing

            continue
        else: #
            numberPart = str(int(Comparelist[Inumber]) + 1)
            #print(str(numberPart) + ' is altered numberpart ')
            zeroPart = lzerolist[0]
            Comparelist[Inumber + 1] = numberPart
            Inumber += 1

            # Form the new file name.
            newFilename = beforePart + zeroPart + str(numberPart) + afterPart

            # Get the full, absolute file paths.
            absWorkingDir = os.path.abspath(folder)
            oldFilename = os.path.join(absWorkingDir, oldFilename)
            newFilename = os.path.join(absWorkingDir, newFilename)

            # Rename the files.
            print(f'Renaming "{oldFilename}" to "{newFilename}"...')
            #shutil.move(oldFilename, newFilename)   # uncomment after testing



#user interface

print("Welcome to the \'Organize your file name\'s numbers tool\'")
print('Please make sure your first file (that we will alter) in an alphanumerically sorted list is the lowest number you want and has the amount of leading zeroes you want. \nEx. myfile001')
while True:
    print('Enter the full folder path for the files you would like to organize \nEx. C:\\Users\\OWNER\\mu_code\\myTestFolder')
    userpath = input()
    print('Enter the file name prefix for all the files you would like to organize. \nEx. myFile for myFile001.txt')
    prefix = input()
    print('Would you like to run a test first, or just organize them? (testrun or organize)')
    userchoice = input()
    print('You chose to ' + userchoice + ' the filepath: ' + userpath + ' and the prefix: ' + prefix)
    print('Is this correct? (yes or no)')
    confirm = input()
    if confirm == 'no':
        continue
    elif confirm == 'yes':
        if userchoice == 'testrun':
            numberfilefixtest(userpath, prefix)
        elif userchoice == 'organize':
            numberfilefixtest(userpath, prefix)
        else:
            print('Unknown input.')

#numberfilefixtest('C:\\Users\\OWNER\\mu_code\\myTestFolder', 'spam')
