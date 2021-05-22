# EKUB: Qoldiq
def gcd(a, b):
    if a == 0 :
        return b      
    return gcd(b%a, a)

if __name__ == '__main__':
    print(gcd(168,64))