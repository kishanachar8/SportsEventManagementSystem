from time import sleep
import os
import stdiomask
import getpass
import sys


# Main Method
def main():
    login()


# Admin Login
def login():
    print(f'\n\n\n\n\n\t\t\t\t\t==============================')
    print(f'\t\t\t\t\tSPORTS EVENT MANAGEMENT SYSTEM')
    print(f'\t\t\t\t\t==============================')
    print(f'\t\t\t\t\t\t      LOGIN')
    print(f'\t\t\t\t\t------------------------------')
    pwd = stdiomask.getpass(f'\t\t\t\t\tPassword : ', '*')
    print(f'\t\t\t\t\t------------------------------')
    sleep(1)
    if pwd == 'admin':
        clear()
        print(f'\n\n\n\n\n\n\n\n\n\n')
        print(f'\t\t\t\t\tWelcome Back !')
        sleep(2)
        clear()
        loading()
    else:
        clear()
        print(f'\n\n\n\n\n\n\n\n\n\n')
        print(f'\t\t\t\t\tSorry! Wrong password\n')
        input(f'\t\t\t\t\tPress ENTER to RETRY')
        clear()
        login()


# To Clear Screen
def clear():
    _ = os.system('cls')


# Loading Bar ...
def loading():
    progress = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
    for p in progress:
        clear()
        print(f'\n\n\n\n\n\n\n\n\n\n\n\n')
        print(f'\t\t\t\t\t {p}% Loading ... Please wait...')
        sleep(1)
    clear()
    welcome()


def welcome():
    wlcm = "\n\n\n\n\n\t\t\tW E L C O M E   T 0\n\n\t\t\t\t S P O R T S\n\n\t\t\t\t\tE V E N T\n\n\t\t\t\t\t\tM A N A G E M E N T\n\n\t\t\t\t\t\t\tS Y S T E M"

    for char in wlcm:
        sleep(0.06)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(2)
    clear()
    menu()


def menu():
    print(f'=====================================')
    print(f'>>             MENU                <<')
    print(f'=====================================')
    print(f'1: Add New Player Record')
    print(f'2: Show All Players Record')
    print(f'3: Delete the Player')
    print(f'4: Search Player/Players')
    print(f'5: Count the No. of Player (Game wise)')
    print(f'6: Total No. of Player\'s Record')
    print(f'7: Clear all Player\'s Record')
    print(f'8: Exit')
    print(f'=====================================')

    ch = int(input(f'Enter your choice : '))

    if (ch == 1):
        clear()
        addPlayer()
        menu()
    elif (ch == 2):
        clear()
        showPlayers()
        menu()
    elif (ch == 3):
        clear()
        deletePlayer()
        menu()
    elif (ch == 4):
        clear()
        searchPlayers()
        menu()
    elif (ch == 5):
        clear()
        countPlayersGames()
        menu()
    elif (ch == 6):
        clear()
        countTotal()
        menu()
    elif (ch == 7):
        clear()
        clearRecords()
        menu()
    elif (ch == 8):
        clear()
        exitProgrm()
    else:
        clear()
        print('<!> Invalid Choice :')
        menu()


# 1: Add a new Player Record
def addPlayer():
    print(f'=======================')
    print(f'ADD NEW PLAYER RECORD')
    print(f'=======================')

   # label: newID
    pid = str(input('Enter Player ID : '))

    f = open("db.txt", "r")
    flag = 0
    index = 0

    # Check for Player already exist
    for line in f:
        index += 1
        if 'P' + pid in line:
            flag = 1
            break
    if flag != 0:
        print(f'\nPlayer Already Exist')
        sleep(2)
        clear()
        addPlayer()
    f.close()

    age = int(input('Enter Player Age (Number) : '))
    fname = str(input('Enter Player First Name : '))
    lname = str(input('Enter Player Last Name : '))
    city = str(input('Enter Player Address (City Only) : '))
    phoneno = int(input('Enter Player Phone Number (Number) :'))
    pfname = str(input('Enter Player Parent First Name : '))
    plname = str(input('Enter Player Parent Last Name : '))

    # Select Game type
    print(f'Please Select Game Type :')
    print(f'1. Cricket')
    print(f'2. Basketball')
    print(f'3. TableTennis')
    print(f'4. Volleyball')
    print(f'5. Hockey')
    print(f'6. Taekwondo')
    print(f'7. Badminton')
    print(f'8. Other')
    ch = int(input('Enter your Choice (Number) :'))

    # Check for Player Game Type Choice
    if(ch == 1):
        game = 'Cricket'
    elif(ch == 2):
        game = 'Basketball'
    elif(ch == 3):
        game = 'TableTennis'
    elif(ch == 4):
        game = 'Volleyball'
    elif (ch == 5):
        game = 'Hockey'
    elif (ch == 6):
        game = 'Taekwondo'
    elif(ch == 7):
        game = 'Badminton'
    else:
        game = 'Other'

    cfname = str(input('Enter Player Coach First Name : '))
    clname = str(input('Enter Player Coach Last Name : '))
    dormno = str(input('Enter Player Dorm Number : '))
    bedno = str(input('Enter Player Bed Number :'))

    try:
        f = open("db.txt", 'a')
        f.writelines(
            f'P{pid}\t{age}\t{fname}\t{lname}\t{city}\t{phoneno}\t{pfname}\t{plname}\t{game}\t{cfname}\t{clname}\tD{dormno}\tB{bedno}\n')
        f.close()
    except:
        print(f'<!> Player Record Not Created !')
    finally:
        clear()
        print(f'<*> Player Record Created !')
    menu()


# 2: Show all Players Record
def showPlayers():
    print(f'=========================')
    print(f'   ALL PLAYERS RECORDS   ')
    print(f'=========================')

    try:
        f = open("db.txt")
        data = f.readlines()
        if data == []:
            print(f'<!> No Records Available')
        else:
            for d in data:
                print(d)
            print(f'<*> Records Successfully Retrived')
        f.close()
    except:
        print(f'<!> No Records Available')

    print(f'=========================')


# 3: Delete the Player
def deletePlayer():
    print(f'=======================')
    print(f'     DELETE PLAYER     ')
    print(f'=======================')
    print(f'1. Delete Player By ID')
    print(f'2. Delete Player By Name')
    print(f'3. Main Menu')
    print(f'=======================')
    ch = int(input('Enter Your Choice : '))

    if(ch == 1):
        s = str(input('Enter Player ID : '))
        deletePlayerData('P'+s)
        clear()
        print(f'<*> Player is Removed !')
        deletePlayer()
    elif (ch == 2):
        s = str(input('Enter Player Name : '))
        deletePlayerData(s)
        clear()
        print(f'<*> Player is Removed !')
        deletePlayer()
    else:
        clear()
        menu()


def deletePlayerData(s):
    # bad_words = [s]
    # with open('db.txt') as oldfile, open('db.txt', 'w') as newfile:
    #     for line in oldfile:
    #         if not any(bad_word in line for bad_word in bad_words):
    #             newfile.write(line)

    old_file = open("db.txt")
    lines = old_file.readlines()
    old_file.close()

    new_file = open("db.txt", "w")
    for line in lines:
        if s not in line:
            new_file.write(line)
    new_file.close()

    print(f'<*> Player is Removed !')


# 4: Search Players
def searchPlayers():
    print(f'=====================================')
    print(f'         SEARCH PLAYER MENU          ')
    print(f'=====================================')
    print(f'1: Search Player using Player Name')
    print(f'2: Search Player using Player Id')
    print(f'3: Search Player using Dorm No.')
    print(f'4: Search Player using Bed No.')
    print(f'5: Search Players using Parents Name')
    print(f'6: Search Players in a specific Game')
    print(f'7. Main Menu')

    ch = int(input('Enter Your Choice : '))

    if(ch == 1):
        s = str(input('Enter Player Name : '))
        showPlayerData(s)
        searchPlayers()
    elif(ch == 2):
        s = str(input('Enter Player ID : '))
        showPlayerData('P'+s)
        searchPlayers()
    elif(ch == 3):
        s = str(input('Enter Player Dorm Number : '))
        showPlayerData('D'+s)
        searchPlayers()
    elif(ch == 4):
        s = str(input('Enter Player Bed Number : '))
        showPlayerData('B'+s)
        searchPlayers()
    elif(ch == 5):
        s = str(input('Enter Player Parent Name : '))
        showPlayerData(s)
        searchPlayers()
    elif(ch == 6):
        s = str(input('Enter Specific Game Type : '))
        showPlayerData(s)
        searchPlayers()
    else:
        clear()
        menu()


# Show Player by Query
def showPlayerData(s):
    try:
        f = open("db.txt")
        data = f.readlines()
        if data == []:
            print(f'<!> No Records Available')
        else:
            for lines in data:
                if s in lines:
                    print(lines)
                # for line in lines:
                #     print(line)
        f.close()
    except:
        print(f'<!> No Records Available')


# 5: Count the No. of Player in all Games
def countPlayersGames():
    print(f'=====================================')
    print(f'       NUMBER OF PLAYERS BY GAME     ')
    print(f'=====================================')

    try:
        Cricket = 0
        Basketball = 0
        TableTennis = 0
        Volleyball = 0
        Hockey = 0
        Taekwondo = 0
        Badminton = 0
        Other = 0
        with open("db.txt") as f:
            contents = f.read()
            Cricket = contents.count("Cricket")
            Basketball = contents.count("Basketball")
            TableTennis = contents.count("TableTennis")
            Volleyball = contents.count("Volleyball")
            Hockey = contents.count("Hockey")
            Taekwondo = contents.count("Taekwondo")
            Badminton = contents.count("Badminton")
            Other = contents.count("Other")
        f.close()
    except:
        print(f'<!> No Records Available')

    print(f'>> Cricket Players : {Cricket}')
    print(f'>> Basketball Players : {Basketball}')
    print(f'>> TableTennis Players : {TableTennis}')
    print(f'>> Volleyball Players : {Volleyball}')
    print(f'>> Hockey Players : {Hockey}')
    print(f'>> Taekwondo Players : {Taekwondo}')
    print(f'>> Badminton Players : {Badminton}')
    print(f'>> Other Players : {Other}')
    print(f'=====================================')


# 6: Count the Total No. of Player\'s Record
def countTotal():
    print(f'=====================================')
    print(f'        TOTAL NUMBER OF PLAYERS      ')
    print(f'=====================================')

    file = open("db.txt")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print(f'>> Total No. of Players is : {line_count}')
    print(f'=====================================')


# 7: Clear the complete database of Player\'s Record
def clearRecords():
    print(f'======================================================')
    print(f'|   Are you sure you want to Delete Records ? (Y/N)  |')
    print(f'======================================================')

    ch = str(input('Enter your choice : '))

    if (ch == 'Y'):
        open('db.txt', 'w').close()
        clear()
        print(f'<*> All records Deleted !')
    elif(ch == 'N'):
        clear()
        menu()
    else:
        clear()
        print(f'<!> Invalid Choice')
        clearRecords()


# 8: Exit from Program
def exitProgrm():
    print(f'\n\n\n\n\n\n\n\n\n\n\n\t\t\tThank you !.. Window will be exit automatically... Please wait...!')
    sleep(2)
    sys.exit()


# Program Entry Point
if __name__ == '__main__':
    main()
