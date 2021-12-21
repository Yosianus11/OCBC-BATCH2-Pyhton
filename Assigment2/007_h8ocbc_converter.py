# tampilan menu untuk memilih inputan awal
print("=================== Suhu Converter =====================")
print("===================   Pilih Menu   =====================")
print("1. Dari Celcius   |titik didih 100                      |")
print("2. Dari Kelvin    |titik didih 373.15                   |")
print("3. Dari Farenheit |titik didih 212                      |")
print("========================================================")
# mengambil nilai inputan berupa number (int)
menu = int(input("Chose Menu:"))


def celKel(cel, sat):
    '''Function to convert celcius to kelvin and kelvin to celcius'''
    # Condition 1 is celcius 2 is kelvin
    if sat == 1:
        # celcius to Kelvin
        return cel + 273.15
    elif sat == 2:
        # Kelvin to celcius
        return cel - 273.15
    else:
        return 'satuan salah'


def toFarenheit(suhu, sat):
    '''Function to convert from celcius or kelvin to farenheit'''
    # Condition 1 is celcius 2 is kelvin
    if sat == 1:
        # rumus convert celcius to farenheit
        return f"{((suhu*9)/5)+32} F"
    elif sat == 2:
         # rumus convert kelvin to farenheit convert to celcius first with first function
        return f"{((celKel(suhu,2)*9)/5)+32} F"


def fromFarenheit(suhu, sat):
    '''Function to convert from farenheit to celcius or kelvin'''
    # Condition 1 is celcius 2 is kelvin
    if sat == 1:
        # rumus convert from farenheit to celcius
        return f"{(5/9)*(suhu-32)} C"
    elif sat == 2:
        # rumus convert from farenheit to kelvin with convert to celcius first
        return f"{celKel((5/9)*(suhu-32),1)} K"

# menu with input celcius code 1
if menu == 1:
    print("Dari Celcius ke :")
    print("1. Ke Kelvin                                           |")
    print("2. Ke Farenheit                                        |")
    print("3. Semua                                               |")
    print("========================================================")
    # input submenu with number(int)
    submenu = int(input("Chose submenu:"))
    if submenu == 1:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to kelvin 
        print(f"Celcius ke Kelvin : {celKel(suhu,1)} K")
    elif submenu == 2:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to farenheit
        print(f"Celcius ke Farenheit : {toFarenheit(suhu,1)}")
    elif submenu == 3:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with 2 function to kelvin & to farenheit
        print(f"Celcius ke Kelvin    : {celKel(suhu,1)} K")
        print(f"Celcius ke Farenheit : {toFarenheit(suhu,1)}")

# menu with input kelvin code 3
elif menu == 2:
    print("Dari Kelvin ke :")
    print("1. Ke Celcius                                          |")
    print("2. Ke Farenheit                                        |")
    print("3. Semua                                               |")
    print("========================================================")
    # input submenu with number(int)
    submenu = int(input("Chose submenu:"))
    
    if submenu == 1:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to celcius
        print(f"Kelvin ke Celcius : {celKel(suhu,2)} C")
    elif submenu == 2:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to farenheit
        print(f"Kelvin ke Farenheit : {toFarenheit(suhu,2)}")
    elif submenu == 3:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with 2 function to celcius & to farenheit
        print(f"Kelvin ke Celcius   : {celKel(suhu,2)} C")
        print(f"Kelvin ke Farenheit : {toFarenheit(suhu,2)}")

# menu with input farenheit code 3
elif menu == 3:
    print("Dari Farenheit ke :")
    print("1. Ke Celcius                                          |")
    print("2. Ke Kelvin                                           |")
    print("3. Semua                                               |")
    print("========================================================")
    # input submenu with number(int)
    submenu = int(input("Chose submenu:"))
    
    if submenu == 1:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to celcius 
        print(f"Farenheit ke Celcius : {fromFarenheit(suhu,1)}")
    elif submenu == 2:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with function to kelvin 
        print(f"Farenheit ke Kelvin : {fromFarenheit(suhu,2)}")
    elif submenu == 3:
        # input suhu with number(float)
        suhu = float(input("Masukan Suhu :"))
        # convert input with 2 function to celcius & to kelvin
        print(f"Farenheit ke Celcius : {fromFarenheit(suhu,1)}")
        print(f"Farenheit ke Kelvin  : {fromFarenheit(suhu,2)}")
else:
    print("Please Input 1-3")
