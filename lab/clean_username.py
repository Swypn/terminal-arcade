with open("users.txt") as usersNames:
    for name in usersNames:
        cleanName = name.strip()
        cleanName = cleanName.title()
        cleanName = cleanName.replace(" ", "-")

        for letter in cleanName:
            if letter == "@":
                cleanName = cleanName.split("@")[0]
                break
            elif letter == ".":
                cleanName = cleanName.split(".")[0]
                break
            
        print(cleanName)



