whatever_str = input("Write whatever you want, please!\n")

if len(whatever_str) > 1:
    print(whatever_str[0] + whatever_str[1] + whatever_str[-2] + whatever_str[-1])
else:
    print("Empty string :(")
