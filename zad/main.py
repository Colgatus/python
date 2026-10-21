def readData():
    file = open("dane.txt", "r", encoding="utf-8")
    data = file.readlines()
    file.close()

    for i in range(len(data)):
        data[i] = data[i].strip()

    return data

def showData(data):
    print("Zawartość pliku:")
    for element in data:
        print(element)

def sortData(data):
    data.sort()

    file = open("sort.txt", "w", encoding="utf-8")
    for element in data:
        file.write(element + "\n")
    file.close()

def menu():
    data = readData()

    while True:
        print("1. Wyświetl dane", "2. Posortuj dane", "3. Zakończ program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            showData(data)
        elif wybor == "2":
            sortData(data)
        elif wybor == "3":
            break
        
menu()
