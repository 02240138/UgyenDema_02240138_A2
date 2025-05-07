
class PokemonOrganizer:
    def __init__(self):
        self.MAX_ENTRIES = 1025
        self.PAGE_SIZE = 64  # 8 rows x 8 columns
        self.collected = {}
        
    def _get_storage_position(self, pokedex_num):
        """Calculate storage location for new card"""
        if pokedex_num < 1 or pokedex_num > self.MAX_ENTRIES:
            raise ValueError("Invalid Pokedex ID")
            
        existing = len(self.collected)
        page = (existing // self.PAGE_SIZE) + 1
        slot = existing % self.PAGE_SIZE
        row = (slot // 8) + 1
        col = (slot % 8) + 1
        return page, row, col
        
    def add_pokemon(self):
        try:
            num = int(input("\nEnter Pokedex number (1-1025): "))
            if num in self.collected:
                print("This card is already in your collection")
                return
                
            page, row, col = self._get_storage_position(num)
            self.collected[num] = (page, row, col)
            print(f"\nAdded Pokedex #{num}")
            print(f"Storage Location: Page {page}, Row {row}, Column {col}")
            
        except ValueError:
            print("Please enter a valid number between 1-1025")
            
    def show_collection(self):
        if not self.collected:
            print("\nYour collection is empty")
            return
            
        print("\nPokemon Collection:")
        for idx, (num, (page, row, col)) in enumerate(sorted(self.collected.items()), 1):
            print(f"{idx}. #{num}: Page {page}, Row {row}, Col {col}")
            
        completion = (len(self.collected) / self.MAX_ENTRIES) * 100
        print(f"\nCollection Progress: {len(self.collected)}/{self.MAX_ENTRIES}")
        print(f"Completion: {completion:.2f}%")
        
    def reset_collection(self):
        confirm = input("\nType 'DELETE ALL' to confirm: ").upper()
        if confirm == 'DELETE ALL':
            self.collected.clear()
            print("Collection reset successfully")
        else:
            print("Reset cancelled")

def manage_pokemon():
    organizer = PokemonOrganizer()
    while True:
        print("\n==== Pokemon Organizer ====")
        print("1. Add New Pokemon")
        print("2. View Collection")
        print("3. Reset Collection")
        print("4. Exit to Main")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            organizer.add_pokemon()
        elif choice == '2':
            organizer.show_collection()
        elif choice == '3':
            organizer.reset_collection()
        elif choice == '4':
            print("Returning to main menu...")
            break
        else:
            print("Invalid selection")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    manage_pokemon()