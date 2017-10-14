
a = '   lubie czekolade   '
print(a.count('l'))
print(a)
print(a.strip())
print(a.replace('lubie', 'nielubie'))
print(a.swapcase())


a = 'olka'
b = a[:]
#first
c = b.replace('k','g',1)
print(c)

#second
k_idx = b.find('k')
c = b
print(c[0:(k_idx)] + 'g' + c[(k_idx+1):])

#thrind'
c = b.split('k')
print(c[0] + 'g' + c[1])

#forth
#c = b.split('k')

#print(str.join(c, 'g'))
