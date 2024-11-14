words = []
same = []
for i in range(10):
    word = input(f"Enter a word {i + 1}: ")
    words.append(word)
    
while True:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("Invalid. Enter a number.")
        
sameword = [word for word in words if len(word) >= number]
for item in sameword:
    if len(item) >= number:
        same.append(item)
print(f"letters has a length atleast", number, ":", sameword)                                                                    