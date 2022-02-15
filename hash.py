key = "ala"

def hf(key):

    hash = [str(bin(ord(x)<<1)[2:]) for x in key]

    return "".join(hash)


def hf1(key):

    index = 1

    for x in key:

        index = (index << 6) + (index << 16) + ord(x) - index

    return index%(len(key)*64)

print(hf("ala"))

print(hf1("ola"))

print(hf("ola kowalska"))

print(hf1("ala kowalska"))

print(hf1("hasło nie do odgadnięcia!!"))

print(hf("9f!!^^*(()panda44;;tak"))

print(hf1("9f!!^^*(()panda44;;tak"))
