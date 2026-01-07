import string 

from Sec_pass_HIBP import check_hibp 

from Sec_pass_generate import generate_secure

#___Funktioner______________________________________________________________________________________________________

def password_requirements(password):
    #Kontrollerar att lösenordet består av minst 12 tecken
    length = len(password) >= 12
    #Kontrollerar att lösenordet innehåller en siffra 
    digit = False 
    for x in password:
        if x.isdigit():
            digit = True 
            break
    #Kontrollerar att lösenordet har en stor bokstav       
    upper = False 
    for x in password:
        if x.isupper():
            upper = True
            break
    #Kontrollerar att lösenordet har ett specialtecken
    special = False
    for x in password:
        if x in string.punctuation:
            special = True
            break
    #Kontrollerar om lösenordet uppfyller alla variablernas krav
    if length and digit and upper and special:
        print("\n\033[32mLösenordet uppfyller kraven ✓\033[0m")
    else:
        print("\n\033[31mLÖSENORDET UPPFYLLER INTE KRAVEN:\033[0m")
        if not length:
            print("\n- Det bör vara minst 12 tecken")
        if not digit:
            print("\n- Det bör vara minst en siffra")
        if not upper:
            print("\n- Det bör vara minst en STOR bokstav")
        if not special:
            print("\n- Det bör vara minst ett specialtecken")


    
#___Körning av funktioner i loop_____________________________________________________________________________

meny_namn = ["Kontrollera ditt nuvarande lösenord","Kolla om ditt lösenord är läckt","Generera ett säkert lösenord", "Avsluta"]

print("\033[═════════════════════════════════════════\033")
print("\t\033[1;36mSECURE PASSWORD CHECKER\033[0m")
print("\033[═════════════════════════════════════════\033")

while True:
    print("\n\033[90m-----------------\033[1;36mMENY\033[0m\033[90m------------------\033[0m")
    for i, namn in enumerate(meny_namn):
        print(f"\033[1;36m{i}: {namn}\033[0m")

    # Läs menyval och hantera felaktig input
    try:
        meny_val = int(input("\nGör ett av följande val (0-3): "))
    except ValueError:
        print("\n\033[31mNu blev det tokigt.\033[0m\n\033[1;36mFörsök igen med en siffra mellan (0-3)\033[0m")
        continue

    if meny_val == 0:
        password = input("\nSkriv lösenordet du vill kontrollera: ")
        password_requirements(password)
    elif meny_val == 1:
        password = input("\nSkriv lösenordet du vill kontrollera: ")
        check_hibp(password)
    elif meny_val == 2:
        safe_pass = generate_secure()
        print(f"\n\033[1;36mHär är ditt nya säkra lösenord:\033[0m\n{safe_pass}")
    elif meny_val == 3:
        print("\nAvslutar programmet.")
        break
    else:
        print("\n\033[1;36mVälj ett alternativ mellan 0-3.\033[0m")