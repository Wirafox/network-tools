import os
from datetime import datetime
import platform

def main():
    #sprawdza jaki to jest system operacyjny 
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    with open("hosty.txt", "r") as file_in, open("wynik.txt", "w") as file_out:
        for val in file_in:
            ip = val.strip()
            if not ip:
                continue
            #wykonuje ping w systemie pojedyńczy na windows -n
            status = os.system(f"ping {parameter} 1 {ip} > /dev/null 2>&1")
            #sprawdza czy ping wrócił
            komunikat = "OK" if status == 0 else "Brak odpowiedzi"
            #zapisuje do pliku adres ip wraz z wynikiem 
            file_out.write(f"{datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} {ip} - {komunikat}\n")
            #pokazuje ze program dziala spoko przy duzych liczbach 
            print(f"Test: {ip} --> {komunikat}")

if __name__ == "__main__":
    main()