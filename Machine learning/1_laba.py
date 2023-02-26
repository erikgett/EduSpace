def disemvowel(string_):
    voids = ['e','y','u','i','o','a']
    for char in voids:
        string_ = string_.replace(char, '').replace(char.upper(), '')
    return string_

print(disemvowel(string_ ='i< IU>D SuG.dyO g.j r*$Eiu%!uJU'): ')