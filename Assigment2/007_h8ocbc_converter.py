print("=================== Suhu Converter =====================")
print("===================   Pilih Menu   =====================")
print("1. Dari Celcius   |titik didih 100                      |")
print("2. Dari Kelvin    |titik didih 373.15                   |")
print("3. Dari Farenheit |titik didih 212                      |")
print("========================================================")
menu = int(input("Chose Menu:"))


def celKel(cel, sat):
    '''This prints a passed string into this function'''
    if sat == 1:
        # celcius to Kelvin
        return cel + 273.15
    elif sat == 2:
        # Kelvin to celcius
        return cel - 273.15
    else:
        return 'satuan salah'


def toFarenheit(suhu, sat):
    if sat == 1:
        return f"{((suhu*9)/5)+32} F"
    elif sat == 2:
        return f"{((celKel(suhu,2)*9)/5)+32} F"


def fromFarenheit(suhu, sat):
    if sat == 1:
        return f"{(5/9)*(suhu-32)} C"
    elif sat == 2:
        return f"{celKel((5/9)*(suhu-32),1)} K"


if menu == 1:
    print("Dari Celcius ke :")
    print("1. Ke Kelvin                                           |")
    print("2. Ke Farenheit                                        |")
    print("3. Semua                                               |")
    print("========================================================")
    submenu = int(input("Chose submenu:"))
    if submenu == 1:
        suhu = float(input("Masukan Suhu :"))
        print(f"Celcius ke Kelvin : {celKel(suhu,1)} K")
    elif submenu == 2:
        suhu = float(input("Masukan Suhu :"))
        print(f"Celcius ke Farenheit : {toFarenheit(suhu,1)}")
    elif submenu == 3:
        suhu = float(input("Masukan Suhu :"))
        print(f"Celcius ke Kelvin    : {celKel(suhu,1)} K")
        print(f"Celcius ke Farenheit : {toFarenheit(suhu,1)}")

elif menu == 2:
    print("Dari Kelvin ke :")
    print("1. Ke Celcius                                          |")
    print("2. Ke Farenheit                                        |")
    print("3. Semua                                               |")
    print("========================================================")
    submenu = int(input("Chose submenu:"))
    
    if submenu == 1:
        suhu = float(input("Masukan Suhu :"))
        print(f"Kelvin ke Celcius : {celKel(suhu,2)} C")
    elif submenu == 2:
        suhu = float(input("Masukan Suhu :"))
        print(f"Kelvin ke Farenheit : {toFarenheit(suhu,2)}")
    elif submenu == 3:
        suhu = float(input("Masukan Suhu :"))
        print(f"Kelvin ke Celcius   : {celKel(suhu,2)} C")
        print(f"Kelvin ke Farenheit : {toFarenheit(suhu,2)}")

elif menu == 3:
    print("Dari Farenheit ke :")
    print("1. Ke Celcius                                          |")
    print("2. Ke Kelvin                                           |")
    print("3. Semua                                               |")
    print("========================================================")
    submenu = int(input("Chose submenu:"))
    
    if submenu == 1:
        suhu = float(input("Masukan Suhu :"))
        print(f"Farenheit ke Celcius : {fromFarenheit(suhu,1)}")
    elif submenu == 2:
        suhu = float(input("Masukan Suhu :"))
        print(f"Farenheit ke Kelvin : {fromFarenheit(suhu,2)}")
    elif submenu == 3:
        suhu = float(input("Masukan Suhu :"))
        print(f"Farenheit ke Celcius : {fromFarenheit(suhu,1)}")
        print(f"Farenheit ke Kelvin  : {fromFarenheit(suhu,2)}")
else:
    print("Please Input 1-3")
