numbers = input().split()

command = input().split()
new_list = []
odd = []
even = []
while not command[0] == "END":
    com,to, do = command[0:3]
    if com == "add":
        com,to, do = command[0:3]
        intigers = command[3:]

        if do == "start":
            intigers.reverse()
            intigers = "".join(intigers)
            for intg in intigers:
                numbers.insert(0, intg)
            # numbers.insert(0, intigers)
        if do == "end":
            intigers = "".join(intigers)
            for intg in intigers:
                numbers.append(intg)

    elif com == "remove":
        value = command[3]
        if to == "lower":
            del numbers[:int(value)]
        elif to == "greater":
            del numbers[int(value)::]
    elif com == "replace":
        value = int(to)
        replacemant = int(do)
        if len(numbers) < value:
            numbers[value],numbers[replacemant] = numbers[replacemant], numbers[value]
        else:
            continue
    elif com == "remove at index":
        index = int(command[3])
        if len(numbers) < index:
            numbers.remove(numbers[index])
        else:
            continue
    if com == "find":
        if com[1] == "even":
            even.append(com[1])
        elif com[1] == "odd":
            odd.append(com[1])

    command = input().split()
print(" ".join(even))
print(" ".join(odd))
print(", ".join(numbers))






