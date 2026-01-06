
import hashlib
import requests

#___Funktioner_____________________________________________________________________________________________________________________________________________

def check_hibp(password):
    #Gör lösenordet till bytes med UTF-8.
    encoded_password = password.encode("utf-8")
    
    #Skapar SHA-1-hash av lösenordet.SHA-1 används enbart eftersom Have I Been Pwned API kräver det. För egen lösenordshantering bör starkare hashfunktioner som SHA-256 eller bcrypt användas
    hashed_password = hashlib.sha1(encoded_password)
    
    #Konvertera hash till hex-sträng.
    hex_password = hashed_password.hexdigest()
    
    #Gör alla bokstäver stora så det blir läsbart för databasen.
    hash_pwd = hex_password.upper()
    
    #Delar upp hashen i prefix och suffix för att inte skicka hela hashen till Have I been Pwned.
    prefix, suffix = hash_pwd[:5], hash_pwd[5:]

    #Skickar iväg förfågan om alla lösenord som börjar med prefixet till Have I been Pwned.
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    #Lagrar responsen i en try-except, om programmet inte får kontakt med servern efter 5 sekunder går den till except.
    try:
        response = requests.get(url, timeout=5)
        #Programmet får konakt med servern men inte med 200 som kod-status.
        if response.status_code != 200:
            print("\nKunde tyvärr inte kontrollera lösenordet.Försök igen senare!")
            return

        #Efter prefix respons, söker vi efter suffix match genom att loopa och läsa igenom textfilen, vid match printas Lösenord läckt samt hur många gånger i heltal.
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            count = int(count) 
            if hash_suffix == suffix:
                print(f"\n\033[31mLÖSENORDET LÄCKT {count} GÅNGER! VÄLJ ETT ANNAT LÖSENORD!\033[0m")
                return            
        #Ingen suffix-match.
        print("\n\033[32mLösenordet finns inte i kända dataläckor ✓\033[32m")
    #Ingen kontakt med servern.
    except requests.RequestException:
        print("\nKunde inte kontrollera lösenordet. Kolla din internetuppkoppling eller om sidan är nere.")
    

