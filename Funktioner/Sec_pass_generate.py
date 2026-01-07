import string 
import secrets
    
#___Funktioner_____________________________________________________________________________________________________________________________________________

def generate_secure(length=16):
    #Importerar variabler från modulen string
    small_letters = string.ascii_lowercase
    big_letters = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    #Placeras i en gemensam variabel
    all_variables = small_letters + big_letters + digits + special 

    #Skapar en lista och använder modulen secrets för att generera säkert randomiserade tecken
    new_pass = [secrets.choice(small_letters),secrets.choice(big_letters),secrets.choice(digits),secrets.choice(special)]

    #Så länge nya lösenordet är mindre än kravet på längd, fyll på med flera tecken från alla tidigare variabler. Blanda alla tecken
    while len(new_pass) < length:
        new_pass.append(secrets.choice(all_variables))
        secrets.SystemRandom().shuffle(new_pass)
    #Tar alla slumpade tecken och gör det till en sträng
    return "".join(new_pass)

        