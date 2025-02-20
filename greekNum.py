import math
ones = "αβγδεϛζηθ"
tens = "ικλμνξοπϙ"
hundreds = "ρστυφχψωϡ"
char = [ones, tens, hundreds, ones]

def convert(x, base=False):
    index = 0

    period = 0
    order = 0

    size = max(math.ceil(math.log10(x)), 1)
    if not base:
        print('Size of number:',size)
    s = ""
    while x > 0:
        c = x % 10
        x //= 10
        if c != 0:
            s += char[index%4][c-1]
            if index%4 == 3:
                s+="`"
        if index%8 == 3:
            s += '}'
        if index%8 == 7:
            if s[-1] == '}':
                s = s[:-1]
            else:
                s += '{M'
            period+=1
            if len(s) > 0 and (s[-1] not in '(['):
                s+=('('+convert(period,True)+')')[::-1]
            if period >= 100000000:
                order+=1
                s+=('['+convert(order,True)+']')[::-1]
                period = 0
        print(s, base)
        index += 1
        if not base and index % 100 == 0:
            print("%.2f" %(100.0*index/size) + '%')
    
        
    if s[-1] == '}':
        s = s[:-1]
    if s[-1] != '(' and not base:
        period+=1
        s+=('('+convert(period,True)+')')[::-1]
        if period >= 100000000:
            order+=1
            s+=('['+convert(order,True)+']')[::-1]
    if s[-1] != '[' and not base:
        order+=1
        s+=('['+convert(order,True)+']')[::-1]
    return s[::-1]

def write(num, filename):
    f = open(filename+'.MD', 'w', encoding='utf-8')
    f.write('$')
    f.write(num.replace('M', 'M^'))
    f.write('$')
    f.close()

handprime = 20988936657440586486151264256610222593863921
write(convert(handprime), 'handprime')
computeTime = 200000000
write(convert(computeTime), 'computeTime')
largeFactor = 340282366939463463374607431768211457
write(convert(largeFactor), 'largeFactor')
#Mersenne = 2**136279841 - 1
#write(convert(Mersenne), 'Mersenne')
