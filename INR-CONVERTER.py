def currency_converter():
    # Conversion rates as of April 2026 (Approximate)
    # 1 INR equals:
    USD_RATE = 0.012    # US Dollar
    EUR_RATE = 0.011    # Euro
    JPY_RATE = 1.82     # Japanese Yen
    RUB_RATE = 1.10     # Russian Ruble
    ZAR_RATE = 0.22     # South African Rand

    print("--- Manual Currency Converter (INR Base) ---")
    
    try:
        inr_amount = float(input("Enter amount in INR: "))
        
        if inr_amount < 0:
            print("Please enter a positive amount.")
            return

        print(f"\nConversions for {inr_amount} INR:")
        print("-" * 35)
        
        # Calculations
        print(f"US Dollars (USD):    {inr_amount * USD_RATE:>10.2f}")
        print(f"Euros (EUR):         {inr_amount * EUR_RATE:>10.2f}")
        print(f"Japanese Yen (JPY):  {inr_amount * JPY_RATE:>10.2f}")
        print(f"Russian Rubles (RUB):{inr_amount * RUB_RATE:>10.2f}")
        print(f"S. African Rand (ZAR):{inr_amount * ZAR_RATE:>10.2f}")
        print("-" * 35)

    except ValueError:
        print("Invalid Input! Please enter a numerical value.")

if __name__ == "__main__":
    currency_converter()
    