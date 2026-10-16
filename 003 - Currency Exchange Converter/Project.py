# Conversion rates dictionary
conversion_rates = {
    ("EGP", "USD"): 0.032,  #Key1
    ("USD", "EGP"): 31.25,  #Key2
    ("EGP", "Dirham"): 0.12, #key3
    ("Dirham", "EGP"): 8.33, #key4
    ("USD", "Dirham"): 3.67, #key5
    ("Dirham", "USD"): 0.27, #key6
}

history = []   #To store the conversion history.

def convert_currency(amount, from_currency, to_currency, rates): #Used function to convert curencies
    key = (from_currency, to_currency)
    if key in rates:
        return amount * rates[key]
    else:
        return None  

def show_history(history): #this function is used to display the previous function :)
    if not history:
        print("No conversion history available.")
    else:
        print("Conversion History:")
        for record in history:
            print(f"{record[0]} {record[1]} → {record[2]:.2f} {record[3]}") 


def main():
    print("Welcome to the Currency Converter!")
    print("Available currencies: EGP, USD, Dirham")
    
    while True:
        print("Menu:")
        print("1. Convert Currency")
        print("2. View Conversion History")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            from_currency = input("Enter the currency you want to convert from (EGP, USD, Dirham): ").strip()
            to_currency = input("Enter the currency you want to convert to (EGP, USD, Dirham): ").strip()
            amount = input("Enter the amount to convert: ").strip()
            
            if from_currency not in ["EGP", "USD", "Dirham"] or to_currency not in ["EGP", "USD", "Dirham"]:
                print("Invalid currency choice. Please try again.")
                continue
            if not amount.isdigit():
                print("Invalid amount. Please enter a positive number.")
                continue
            
            amount = float(amount)
            
            converted_amount = convert_currency(amount, from_currency, to_currency, conversion_rates)
            if converted_amount is not None:
                print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                history.append((amount, from_currency, converted_amount, to_currency))
            else:
                print("Conversion not possible with the given currencies.")
        
        elif choice == "2":
            show_history(history)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

main()
