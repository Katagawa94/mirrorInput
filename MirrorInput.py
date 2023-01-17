'''
AUTOR: KEVIN EMUNDS - Kleines Projekt zum Kennenlernen

AUFGABE:
„Es soll eine Konsolen-Applikation erstellt werden (d.h. ohne Benutzeroberfläche), 
die eine maximal 4-stellige Zahl vom Benutzer einfordert und diese wie eine digitale Uhr darstellt, d.h. mit Strichen. 
Ist die Zahl nicht 4-stellig, soll sie mit führenden Nullen aufgefüllt werden. Beim Knopfdruck der x-Taste soll die Zahl an der x-Achse gespiegelt werden. 
Beim Knopfdruck auf die y-Taste an der y-Achse“
Schön wäre es, wenn das fertige Programm auf einem Windowsrechner ausgeführt werden kann (.net Framework).
Sie können auch Pseudocode schreiben, dann können wir es lesen. Bitte die Arbeitsweise dokumentieren, der Weg ist dabei das Ziel.
Das Programm wird natürlich nicht produktiv eingesetzt. Die Aufgabe dient ausschließlich dazu, herauszufinden, wie Sie an die Lösung herangehen.
Hier eine kleine Zeichnung, wie das Ganze an der x-Achse aussehen soll. Die Eingabe beträgt 234, die Ausgabe ist keine Uhrzeit, sondern wie eine digitale Uhr mit Strichen, an der roten x-Achse gespiegelt.“
'''
import time
# Im Folgenden Programm wird in den Kommentaren hauptsächlich, wie in der Aufgabe verlangt, der Denkprozess dokumentiert.
# Zunächst kann man die Aufgabe in drei Teile gliedern: Input, Verarbeitung und Ausgabe.

# Für den Input müssen wir zunächst eine Funktion schreiben, die den Input des Benutzers abfragt und prüft, ob er gültig ist.

def readUserInput():
    userInput =''
    while not validateNumberInput(userInput):
        userInput = input("Enter a number with up to 4 digits: ") # Abfrage des Inputs
        if not validateNumberInput(userInput):
            print("Invalid input. Please try again.") # Fehlermeldung, falls der Input ungültig ist
    return userInput

# Die Validierung des Inputs wird in der Funktion validateNumberInput() durchgeführt. - lieber viele Funktionen, die sich um eine Aufgabe kümmern, als eine große Funktion, die alles macht.

def validateNumberInput(userInput):
    if userInput.isdigit() and len(userInput) <= 4:
        return True
    else:
        return False

# Der Input muss zusätzlich zum validieren noch eventuell modifiziert werden falls dieser weniger als 4 Stellen hat. 

def modicfyInput(userInput):
    if len(userInput) < 4:
        userInput = userInput.zfill(4) 
    return userInput

'''
Nun Müssen wir uns eine Darstellungs Art der Zahlen und der gespiegelten Zahlen überlegen.
Eventuell brauchen wir uns nichtmal um die Spiegelung kümmern, da wir die ASCII Reihen der Zahlen einfach nur umdrehen können, 
könnte aber sein, dass das schlecht aussieht. - Wir werden es sehen.

Lösungsidee:
Die Zahlen werden in einem Array gespeichert, in dem jeder Index eine Zeile der Zahl darstellt.
Es wird extra eine Form gewählt, die sich gut für die Darstellung der Zahlen - auch der umgedrehten - eignet.

Beispiel:
aus 
     ────
         │  
         │
     ────
         │
         │    
     ────

wird [ ' ──── ', '     │', '     │', ' ──── ', '     │', '     │', ' ──── ' ]

wir erkennen Muster - der Querstrich sieht immer gleich aus, die senkrechten Striche / Doppelstriche sind immer an den gleichen Stellen.
Daher schreit das danach als Konstante verwendet zu werden. 
'''

QUERSTRICH = ' ──── '
SEITENSTRICHRECHTS = '     │'
SEITENSTRICHLINKS =  '│     '
SEITENSTRICHDOPPELT= '|    │'
LEER = '      '


LENGTH=7 # Die einheitliche Länge der Arrays, die die Zahlen darstellen
SPACE = '  ' # Der Abstand zwischen den Zahlen
EINS=[LEER,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,LEER,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,LEER]
ZWEI=[QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,QUERSTRICH,SEITENSTRICHLINKS,SEITENSTRICHLINKS,QUERSTRICH]
DREI=[QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,QUERSTRICH]
VIER=[LEER,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,LEER]
FÜNF=[QUERSTRICH,SEITENSTRICHLINKS,SEITENSTRICHLINKS,QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,QUERSTRICH]
SECHS=[QUERSTRICH,SEITENSTRICHLINKS,SEITENSTRICHLINKS,QUERSTRICH,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH]
SIEBEN=[QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,LEER,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,LEER]
ACHT=[QUERSTRICH,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH]
NEUN=[QUERSTRICH,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH,SEITENSTRICHRECHTS,SEITENSTRICHRECHTS,QUERSTRICH]
NULL=[QUERSTRICH,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,LEER,SEITENSTRICHDOPPELT,SEITENSTRICHDOPPELT,QUERSTRICH]

# Nun müssen wir unsere Ausgabe generieren. Bei dieser besteht die erste Zeile - der erste String aus dem Array - aus den zusammengesetzten ersten Zeilen der eigentlichen Zahlen.

def generateOutput(userInput):
    output = []
    for i in range(LENGTH):
        output.append('')
        for num in userInput:
            match num:
                case '1':
                    output[i] += (EINS[i])+SPACE
                case '2':
                    output[i] += (ZWEI[i])+SPACE
                case '3':
                    output[i] += (DREI[i])+SPACE
                case '4':
                    output[i] += (VIER[i])+SPACE
                case '5':
                    output[i] += (FÜNF[i])+SPACE
                case '6':
                    output[i] += (SECHS[i])+SPACE
                case '7':
                    output[i] += (SIEBEN[i])+SPACE
                case '8':
                    output[i] += (ACHT[i])+SPACE
                case '9':
                    output[i] += (NEUN[i])+SPACE
                case '0':
                    output[i] += (NULL[i])+SPACE
    return output

# Eine Funktion, zum simplen ausgeben des Outputs.

def printOutput(output):
    for i in range(LENGTH):
        print(output[i])

# Eine Funktion, die die Achsen Eingabe des Users registriert und validiert.

def readUserInputMirror():
    userInput = ''
    while not validateAxisInput(userInput):
        if userInput != '':
            print ('Invalid Input. Please try again.')
        userInput = input('Please pick a mirror axis ("X"/"Y") or terminate the programm ("EXIT"): ').lower()
    return userInput

# Die Funktion, die zum validieren verwendet wird. 

def validateAxisInput(userInput):
    if userInput == 'x' or userInput == 'y' or userInput == 'exit':
        return True
    else:
        return False

# Das eigentliche Kernstück der Applikation. Hier wird der Output gespiegelt. 

def mirrorOutput(output, userInput):
    if userInput == 'x':
        output = mirrorX(output)
    elif userInput == 'y':
        output = mirrorY(output)
    return output

def mirrorX(output):
    output = output[::-1]
    return output

def mirrorY(output):
    for i in range(LENGTH):
        output[i] = output[i][::-1]
    return output

# Eine Persönliche Note zum Abschluss. :)

def  printGoodBye():
    goodBye="\
      _____                 _ ____             _  \n \
     / ____|               | |  _ \           | | \n \
    | |  __  ___   ___   __| | |_) |_   _  ___| | \n \
    | | |_ |/ _ \ / _ \ / _` |  _ <| | | |/ _ \ | \n \
    | |__| | (_) | (_) | (_| | |_) | |_| |  __/_| \n \
    \_____|\___/ \___/ \__,_|____/ \__, |\___(_)  \n \
                                    __/ |         \n \
                                    |___/        "
    print(goodBye)

# Eine main-Funktion, in ihr setzten wir die Puzzlestücke zusammen.

def main():

    userInput = readUserInput()
    userInput = modicfyInput(userInput)
    output = generateOutput(userInput)
    printOutput(output)

    userInput = readUserInputMirror()
    while userInput != 'exit':
        output = mirrorOutput(output, userInput)
        printOutput(output)
        userInput = readUserInputMirror()

    time.sleep(1.0)
    print('\n \n Thank you for using my application. Have a nice day! :) ')
    time.sleep(1.0)
    printGoodBye()
    time.sleep(3.0)

main()