for i in range(45, 210):
    if i == 100:
        continue
    print(i)
    if i == 205:
        break



while True:
    userAnswer = int(input("what is the product of 7 * 24 ?"))
    if userAnswer == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
