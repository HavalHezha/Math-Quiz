print("""
········································································
: ___  ___      ________      ___      ___  ________      ___          :
:|\  \|\  \    |\   __  \    |\  \    /  /||\   __  \    |\  \         :
:\ \  \\\  \   \ \  \|\  \   \ \  \  /  / /\ \  \|\  \   \ \  \        :
: \ \   __  \   \ \   __  \   \ \  \/  / /  \ \   __  \   \ \  \       :
:  \ \  \ \  \   \ \  \ \  \   \ \    / /    \ \  \ \  \   \ \  \____  :
:   \ \__\ \__\   \ \__\ \__\   \ \__/ /      \ \__\ \__\   \ \_______\:
: ___\|___\|__| _______|\|__| ________/     ___\|___\|__| ____________|:
:|\  \|\  \    |\  ___ \     |\_____  \    |\  \|\  \    |\   __  \    :
:\ \  \\\  \   \ \   __/|     \|___/  /|   \ \  \\\  \   \ \  \|\  \   :
: \ \   __  \   \ \  \_|/__       /  / /    \ \   __  \   \ \   __  \  :
:  \ \  \ \  \   \ \  \_|\ \     /  /_/__    \ \  \ \  \   \ \  \ \  \ :
:   \ \__\ \__\   \ \_______\   |\________\   \ \__\ \__\   \ \__\ \__\:
:    \|__|\|__|    \|_______|    \|_______|    \|__|\|__|    \|__|\|__|:
········································································
""")
print("welcome To my Math quiz")

i = 0
# Nawe Aw kasay daxl abe
name = input("what is your name?  ")


# Prsyar la amada bun
redy = input("okay " + name + " are you reedy to play")

#danane marj ka agar amadabu shtek bkat agar na barnamaka dabxa
if redy.lower() != "yes":
    quit()

print("let is do this \n")

# prsyarakan
# { i += 1 } awa wata bo zane har prsyarak darachayak zyad bkat
corex = input("1- what is 2+2 = ")

if corex == "1":
    i += 1
    print("Correct")
else:
    print("incorrect")

corex2 = input("1- what is 2x4 = ")
if corex2 == "8":
    i += 1
    print("Correct")
else:
    print("incorrect")

corex3 = input("1- what is 2x2 = ")
if corex3 == "4":
    i += 1
    print("Correct")
else:
    print("incorrect")
corex4 = input("1- what is 2x8 = ")
if corex4 == "16":
    i += 1
    print("Correct")
else:
    print("incorrect")

# Agar darachakat la 2 w zyatr bu wa yaksan bu ba 2 awa bruata bashe dwatr agar na barnamaka dabxat
if i >= 2:
    print("next stage")
else:
    quit()


print(i)
