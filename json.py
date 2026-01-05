import json
import os

DATABASE_FILE = "family_data.json"

class DanUwa:
    def __init__(self, suna, shekaru, matsayi):
        self.suna = suna
        self.shekaru = shekaru
        self.matsayi = matsayi

    def to_dict(self):
        return {"suna": self.suna, "shekaru": self.shekaru, "matsayi": self.matsayi}

    def yi_bayani(self):
        print(f"👤 SUNA: {self.suna} | SHEKARU: {self.shekaru} | MATSAYI: {self.matsayi}")

# --- Functions ---

def load_data():
    iyali_objects = []
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as file:
                data = json.load(file)
                for item in data:
                    mutum = DanUwa(item['suna'], item['shekaru'], item['matsayi'])
                    iyali_objects.append(mutum)
        except:
            pass
    return iyali_objects

def save_data(iyali_list):
    data_to_save = [mutum.to_dict() for mutum in iyali_list]
    with open(DATABASE_FILE, "w") as file:
        json.dump(data_to_save, file, indent=4)
    print("💾 An yi Saving canje-canje!")

# --- Sabbin Functions (Search & Delete) ---

def nemo_mutum(iyali_list, sunan_da_ake_nema):
    """Yana bincika list don ganin ko akwai sunan"""
    for mutum in iyali_list:
        # Muna amfani da .lower() don kar 'Musa' da 'musa' su ba da matsala
        if mutum.suna.lower() == sunan_da_ake_nema.lower():
            return mutum
    return None

def cire_mutum(iyali_list, sunan_da_ake_so_cire):
    mutum = nemo_mutum(iyali_list, sunan_da_ake_so_cire)
    if mutum:
        iyali_list.remove(mutum)
        save_data(iyali_list) # Save nan take bayan gogewa
        print(f"✅ An goge {mutum.suna} daga tsarin iyali.")
    else:
        print(f"❌ Ba a sami mai suna '{sunan_da_ake_so_cire}' ba.")

def main():
    iyali = load_data() # Dauko bayanai da zarar an fara

    while True:
        print("\n=== TSARIN IYALI (CRUD SYSTEM) ===")
        print("1. Kara Mutum (Add)")
        print("2. Duba Kowa (View All)")
        print("3. Nemo Mutum (Search)")
        print("4. Goge Mutum (Delete)")
        print("5. Fita (Exit)")
        
        zabi = input("\nMe kake so kayi? (1-5): ")

        if zabi == '1':
            s = input("Suna: ")
            sh = input("Shekaru: ")
            m = input("Matsayi: ")
            iyali.append(DanUwa(s, sh, m))
            save_data(iyali)
            print("An kara lafiya.")

        elif zabi == '2':
            print(f"\n--- Jimilla: Mutum {len(iyali)} ---")
            for mutum in iyali:
                mutum.yi_bayani()

        elif zabi == '3':
            sunan = input("Wane suna kake nema?: ")
            mutum = nemo_mutum(iyali, sunan)
            if mutum:
                print("\nE, an same shi/ta:")
                mutum.yi_bayani()
            else:
                print("Babu wannan sunan a ciki.")

        elif zabi == '4':
            sunan = input("Wa kake so a goge?: ")
            tabbatarwa = input(f"Ka tabbata kana so ka goge {sunan}? (y/n): ")
            if tabbatarwa.lower() == 'y':
                cire_mutum(iyali, sunan)
            else:
                print("An fasa gogewa.")

        elif zabi == '5':
            print("Sai anjima...")
            break
        else:
            print("Zabi ba daidai ba.")

if __name__ == "__main__":
    main()
