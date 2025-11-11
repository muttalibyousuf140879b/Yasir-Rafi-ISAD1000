from pricing import calculate_cost
from storage import load_services

def main():
    services = load_services("services.csv")
    subscriptions = {}

    while True:
        print("\nWelcome to ICSC – ISE Cloud Services Calculator")
        print("Add subscription for:")
        for idx, service in enumerate(services.keys(), start=1):
            print(f"{idx}) {service}")
        print("s) List subscriptions")
        print("$) Display cost breakdown")
        print("q) Quit")

        choice = input("> ").strip().lower()

        if choice == "q":
            print("Thank you for using ICSC!")
            break
        elif choice == "s":
            if subscriptions:
                print("You have subscriptions for:")
                for name, amount in subscriptions.items():
                    print(f"{name}: {amount} {services[name]['unit']}(s)")
            else:
                print("No subscriptions yet.")
        elif choice == "$":
            total = 0
            if not subscriptions:
                print("No subscriptions yet.")
                continue
            print("Your current cost breakdown is:")
            for name, amount in subscriptions.items():
                data = services[name]
                cost = calculate_cost(name, amount, data["tiers"], data["costs"])
                print(f"{name}: {amount} @ ${data['costs'][0]} = ${cost}")
                total += cost
            print(f"TOTAL: ${round(total,2)}")
        else:
            try:
                index = int(choice) - 1
                service_name = list(services.keys())[index]
            except (ValueError, IndexError):
                print("Invalid option.")
                continue

            data = services[service_name]
            print(f"You chose {service_name}, which has the following cost structure:")
            for i in range(len(data["tiers"])):
                start = data["tiers"][i]
                end = data["tiers"][i + 1] if i + 1 < len(data["tiers"]) else "+"
                print(f"{start}-{end}: ${data['costs'][i]} per {data['unit']}")
            print(f"Current amount: {subscriptions.get(service_name, 0)} {data['unit']}(s)")
            try:
                new_amount = float(input(f"Enter new {data['unit']} amount: "))
                subscriptions[service_name] = new_amount
            except ValueError:
                print("Invalid number entered.")
