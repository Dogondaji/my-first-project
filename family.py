# Project Name: Family Tree System
# Author: Abdulrahman Sanusi
# Description: Wannan program ne mai nuna bayanan yan uwa ta amfani da Python Class.

class DanUwa:
    def __init__(self, suna, shekaru, matsayi):
        self.suna = suna
        self.shekaru = shekaru
        self.matsayi = matsayi

    def yi_bayani(self):
        print(f"-> Sunana {self.suna}, ina da shekaru {self.shekaru}. Matsayina a gida shine: {self.matsayi}.")

# --- Babban Wajen Aiki (Main Execution) ---

def main():
    print("--- Barka da zuwa Tsarin Iyali na Abdulrahman ---")
    print("")

    # Muna kirkirar 'Objects' na yan uwa
    baba = DanUwa("Malam Sanusi", 55, "Mahaifi")
    mama = DanUwa("Hajiya Fatima", 48, "Mahaifiya")
    ni = DanUwa("Abdulrahman", 22, "Da (Student)")
    kanwa = DanUwa("Aisha", 16, "Kanwa")

    # Saka su a cikin List guda daya
    iyali = [baba, mama, ni, kanwa]

    # Yin Loop don fitar da bayanan kowa
    for mutum in iyali:
        mutum.yi_bayani()

if __name__ == "__main__":
    main()
