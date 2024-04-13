# Jason Torres
def encode(password):
    ans = []
    ting = ""
    for i in range(len(password)):
        ans.append((int(password[i])+3)%10)
    for i in range(len(password)):
        ting += str(ans[i])
    return(ting)

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")
    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!\n")
    elif option == "2":
        print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
    elif option == "3":
        break