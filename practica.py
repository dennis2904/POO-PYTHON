x   = 6

print(x)

x = 43
x = x + 1
print(x)

width = 15
height = 12.0
print(height/3)

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()

n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
    
    
    
    smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


for n in "banana":
    print(n)
    
fruit = "banana"
x = fruit[1]

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
        
        d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)
    
    import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)