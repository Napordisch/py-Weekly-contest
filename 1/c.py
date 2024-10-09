year = int(input())

def isleap(y):
    if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        return True
    else:
        return False

if isleap(year):
    print(True)

else:
    print(False, end = " ")
    a_year = year
    b_year = year
    a_is_leap, b_is_leap = isleap(a_year), isleap(b_year)
    while not (a_is_leap or b_is_leap): 
        a_year -= a_year % 4
        b_year += (4 - (b_year % 4))
        a_is_leap, b_is_leap = isleap(a_year), isleap(b_year)
    
    if not isleap(a_year):
        print(b_year)
    elif not isleap(b_year):
        print(a_year)
    
    elif b_year - year < year - a_year:
        print(b_year)
    elif b_year - year > year - a_year:
        print(a_year)
