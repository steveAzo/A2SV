def boyGirl(s):
    s = set(s)

    if len(s) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
s = input()
boyGirl(s)