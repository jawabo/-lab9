# Jason Torres
def encode(password):
    ans = []
    ting = ""
    for i in range(len(password)):
        ans.append((int(password[i])+3)%10)
    for i in range(len(password)):
        ting += str(ans[i])
    return(ting)
    
def decode(encoded_password):
        after = []
        for i in range (0,len(encoded_password)):
            num = int(encoded_password[i])
            if num >=3:
                after.append(num)
            else:
                if num == 0:
                    new_num = 10
                    after.append(new_num)
                elif num == 1:
                    new_num = 11
                    after.append(new_num)
                elif num == 2:
                    new_num = 12
                    after.append(new_num)
        updated = [str(x-3) for x in after]
        revert = "" 
        return revert.join(x for x in updated)


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
