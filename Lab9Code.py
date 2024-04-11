# Jason Torres
def encode(password):
    ans = []
    ting = ""
    for i in range(len(password)):
        ans.append((int(password[i])+3)%10)
    for i in range(len(password)):
        ting += str(ans[i])
    print(ting)

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")
    if option == "1":
        password = input("Please enter your password to encode: ")
        encode(password)
    elif option == "2":
        pass #replace for decode
    elif option == "3":
        break