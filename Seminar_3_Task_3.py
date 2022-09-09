# В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить 
# количество в ней символов и слов.

fname=input('файл:')
f=open(fname,'w')
while True:
    s=input()
    if s=="": 
        break
    f.write(s+"\n")
f.close()

finp = open('file.txt', 'r')
count = 0
for line in finp:
    count += 1
    print(len(line))
    print(len(line.split()))

print(f'количество строк в файле: {count}')
finp.close()