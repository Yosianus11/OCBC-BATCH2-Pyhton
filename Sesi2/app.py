if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('inner_condition 1')

    if 100 < 20:

        print('End of Outer Condition')
print('After outer  Condition')

x = 13
if x >= 10 and x <= 15:
    print(x)


sunny = False
if x >= 10 and x <= 15 and not sunny:
    print(x)

if x < 50:
    print('(First Suite)')
    print('x is small')
else:
    print('(Second Suite)')
    print('x is large')


hargaBuku = 20000
hargaMajalah = 5000
uang = 7000

if uang > hargaBuku:
    print('Beli buku')
elif uang > hargaMajalah:
    print('Beli Majalah')
else:
    print("Uang Tidak Cukup")


name = 'Yosianus'
if name == 'Antonio':
    print('Hello Antonio')
if name == 'Yosianus':
    print('Hello Yosianus')


total_purchase = 1000

if 'foo' in ['foo', 'bar', 'baz']:
    print('Yes Foo'); print('alla');
    

raining = False
print("let's go to the", 'beach' if not raining else 'library')


#Looping =================================================================================

n = 5 
while n > 0 :
    n -=1 
    print(n)
print("\n================================")
n = 5
while n > 0:    
    n -= 1    
    if n == 2:        
        break # Break Statement    
    print(n)
print('Loop ended.')

a = ['foo', 'bar']
while len(a):    
    print(a.pop(0))    
    b = ['baz', 'qux']    
    while len(b):        
        print('>', b.pop(0))
        
d = {'foo': 1, 'bar':2, 'baz':3}
for k, v in d.items():
    print(k,':', v)
