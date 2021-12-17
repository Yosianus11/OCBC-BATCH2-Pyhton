name = "Yosianus"
age =23
has_laptop = True

print(name,age,has_laptop)

a = 10
b = 20
print(a + b)
print(a + b - 5)

a = 4
b = 3
print("tambah :",a + b)
print("Kurang :",a - b)
print("Kali :",a * b)
print(a / b) #division
print(a // b) #integer division
print(a % b)
print(a**b) #power/ pangkat

s = 'foo'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4)
#Case Conversion
print(s.capitalize())
print(s.lower())
print(s.swapcase())

i= 20
j=10
print('Umur : {} {}'.format(i, j))
print('Umur : {nilai_i} {nilai_j}'.format(nilai_j = j, nilai_i =i))
print(f'Umur : {i} {j}')
print(f"Umur : {i} {j}")


#Slicing
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:5]
# a[m:n] --> return from index m to n, but exclude n
# 2 3 4
 
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#kosong di depan
a[:5]
a[0:5]
#0 1 2 3 4
#a b c d e
 
#kosong di belakang
a[3:]
a[3:7] 
# --> length of a = 7
# 3 4 5 6
# d e f g


t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])

MLB_team = {    'Colorado': 'Rockies',    'Boston': 'Red Sox',    'Minnesota': 'Twins',}
print(MLB_team['Minnesota'])

person = {}
person['fname'] = 'Yosianus'
person['lname'] = 'Antonio'
person['age'] = 23
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])

for key , value in MLB_team.items():
    print(key, value)