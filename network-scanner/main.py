import ipaddress
import platform
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def ip_check(ip):
    #sprawdza jaki to jest system operacyjny 
    parametr1 = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    parametr2 = "> nul" if platform.system().lower() == "windows" else "> /dev/null 2>&1"
    status = os.system(f"ping {parametr1} -w 500 {ip} {parametr2}")
    dane = f"[{datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')}] {ip}"
    if status == 0:
        wynik = f"{dane} - OK"
        return wynik
    else:
        wynik = f"{dane} - Brak odpowiedzi"
        return wynik

def main(): 
    user_input = input("Sieć [Enter dla 192.168.1.0/24]: ")

    #sprawdza czy adres nie jest pusty zadładam ze bedzie poprwany i nie bedzie literowki :)
    adres_sieci = user_input if user_input else "192.168.1.0/24"
    #tworzy wszystkie adresy ip w sieci
    try:
        siec = ipaddress.ip_network(adres_sieci)
        hosty = list(siec.hosts())
    except ValueError:
        print("Błąd formatu adresu sieci!!!")
        return 

    start_time = datetime.now()
    print(f"Skanowanie sieci {adres_sieci}")

    with ThreadPoolExecutor(max_workers=10) as wykonawca:
        wyniki = list(wykonawca.map(ip_check, hosty))
    
    with open("wyniki.txt", "w") as file_out:
        for val in wyniki:
            file_out.write(f"{val}\n")
    
    end_time = datetime.now()
    print(f"Skanowanie sieci {adres_sieci} zakończone. W czasie: {end_time-start_time}")
    
if __name__ == "__main__":
    main()
