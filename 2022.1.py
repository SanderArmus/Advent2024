f = open('advent/2022.1.txt', 'r')
lines=[line.strip() for line in f.readlines()]
res=0
list=[]
for line in lines:
    if line=="":
        
        elf = 0
    else:
        elf+=int(line)
    print (elf)
