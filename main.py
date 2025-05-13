from database import init_db
from models import Parcel, DeliveryAgent

init_db()
parcel_obj = Parcel()
agent_obj = DeliveryAgent()

def menu():
    while True:
        print("\n=== Parcel Delivery Tracker ===")
        print("1. Add Delivery Agent")
        print("2. Add New Parcel")
        print("3. Update Parcel Status")
        print("4. Track Parcel")
        print("5. View Parcel History")
        print("6. View All Parcels")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter agent name: ")
            agent_obj.add_agent(name)

        elif choice == "2":
            sender = input("Sender name: ")
            receiver = input("Receiver name: ")
            address = input("Delivery address: ")
            agents = agent_obj.list_agents()
            for a in agents:
                print(f"{a[0]} - {a[1]}")
            agent_id = int(input("Enter delivery agent ID: "))
            parcel_obj.add_parcel(sender, receiver, address, agent_id)

        elif choice == "3":
            parcel_id = int(input("Enter parcel ID: "))
            new_status = input("Enter new status (Pending/In Transit/Delivered): ")
            parcel_obj.update_status(parcel_id, new_status)

        elif choice == "4":
            parcel_id = int(input("Enter parcel ID: "))
            parcel = parcel_obj.track_parcel(parcel_id)
            print(parcel)

        elif choice == "5":
            parcel_id = int(input("Enter parcel ID: "))
            logs = parcel_obj.show_logs(parcel_id)
            for log in logs:
                print(f"Status: {log[0]}, Time: {log[1]}")

        elif choice == "6":
            parcels = parcel_obj.list_all_parcels()
            for p in parcels:
                print(p)

        elif choice == "7":
            print("Thanks for your using our parcel tarcker")
            break

        else:
            print("Invalid choice ❌")

if __name__ == "__main__":
    menu()
