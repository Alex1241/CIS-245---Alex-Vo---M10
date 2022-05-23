import os

#This is the main function
def enterInfo():
    inName = input('Please enter the file name.')
    Filename = inName+'.txt'
    directory = input('Please enter the directory of choice.')


    print('Please enter your name')
    name = str(input())
    print('Please enter your address')
    address = str(input())
    print('Please enter your phone number.')
    phone = str(input())

    with open(Filename, 'w') as handle:
        handle.write(name+', ' + address + ', ' + phone)
        handle.close()

    sumList = (f'{name}, {address} , {phone}')
    print('You entered:',sumList)

    #This reads the saved file information
    with open(Filename, 'r') as handle:
        print('Now opening and reading FROM the file...')
        data = handle.readlines()
        print('Displaying Information...')
        print(data)
        handle.close()

enterInfo()