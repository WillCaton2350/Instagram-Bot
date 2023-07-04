words = {
        1:"I",
        2:"Don't",
        3:"Share",
        4:"Private",
        5:"Information",
        6:"with",
        7:"the",
        8:"opposition",
}
MaxValue = 10
counter = 0

while MaxValue:
    counter += 1
    print("While Count: ",counter)
    if counter == 10:
        break

print()


for i in words:
    counter += 1
    print(counter,"Text: ",words[i])
    if counter == 20:
        break

