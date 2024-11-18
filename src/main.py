import json

class User:
    def __init__(self, name, contact, address):
        self._name = name
        self._contact = contact
        self._address = address

    def __str__(self):
        return f"Name: {self._name}, Contact: {self._contact}, Address: {self._address}"

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact

    @property
    def address(self):
        return self._address

    def to_dict(self):
        return {
            "name": self._name,
            "contact": self._contact,
            "address": self._address
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['contact'], data['address'])


class Reservation:
    _counter = 1

    def __init__(self, user_name, start_time, end_time, date):
        self._id = f"R{Reservation._counter}"
        Reservation._counter += 1
        self._user_name = user_name
        self._start_time = start_time
        self._end_time = end_time
        self._date = date

    @property
    def id(self):
        return self._id

    @property
    def user_name(self):
        return self._user_name

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def date(self):
        return self._date

    def update(self, start_time=None, end_time=None, date=None):
        if start_time:
            self._start_time = start_time
        if end_time:
            self._end_time = end_time
        if date:
            self._date = date

    def __str__(self):
        return f"Reservation ID: {self._id}, Name: {self._user_name}, Date: {self._date}, " \
               f"Start Time: {self._start_time}, End Time: {self._end_time}"

    def to_dict(self):
        return {
            "id": self._id,
            "user_name": self._user_name,
            "start_time": self._start_time,
            "end_time": self._end_time,
            "date": self._date
        }

    @classmethod
    def from_dict(cls, data):
        reservation = cls(data['user_name'], data['start_time'], data['end_time'], data['date'])
        reservation._id = data['id']
        return reservation


class ReservationManager:
    def __init__(self):
        self._user = None
        self._reservation = None

    def register_user(self):
        print("Let's register you for the basketball court reservation.")
        name = input("Enter your full name: ")
        contact = input("Enter your contact number: ")
        address = input("Enter your address: ")
        self._user = User(name, contact, address)
        print(f"\nWelcome, {self._user.name}! You've been registered.")

    def create_reservation(self):
        if not self._user:
            print("You need to register first!")
            return
        print("Let's create a reservation.")
        date = input("Enter reservation date (yyyy-mm-dd): ")
        start_time = input("Enter start time (HH:mm): ")
        end_time = input("Enter end time (HH:mm): ")
        self._reservation = Reservation(self._user.name, start_time, end_time, date)
        print(f"\nYour reservation has been created: {self._reservation}")

    def update_reservation(self):
        if not self._reservation:
            print("No reservation to update.")
            return
        print("Update your reservation.")
        start_time = input("Enter new start time (or press Enter to keep the same): ")
        end_time = input("Enter new end time (or press Enter to keep the same): ")
        date = input("Enter new date (or press Enter to keep the same): ")
        self._reservation.update(start_time or None, end_time or None, date or None)
        print(f"Your reservation has been updated: {self._reservation}")

    def cancel_reservation(self):
        if not self._reservation:
            print("No reservation to cancel.")
            return
        choice = input("Are you sure you want to cancel your reservation? (yes/no): ")
        if choice.lower() == 'yes':
            self._reservation = None
            print("Your reservation has been canceled.")
        else:
            print("Cancellation aborted.")

    def print_receipt(self):
        if not self._reservation:
            print("No reservation found to print a receipt.")
            return
        print("--------------------------------------------")
        print("------------Reservation Receipt------------")
        print("--------------------------------------------")
        print("Paharang West Basketball Court\n")
        print(f"Full Name: {self._user.name}")
        print(f"Contact Number: {self._user.contact}")
        print(f"Address: {self._user.address}")
        print(f"Date: {self._reservation.date}")
        print(f"Start Time: {self._reservation.start_time}")
        print(f"End Time: {self._reservation.end_time}")
        print("\nTHANK YOU FOR YOUR RESERVATION AND ENJOY!")
        print("-------------------------------------------")
        print("PAHARANG WEST BASKETBALL COURT")
        print("09764978219")
        print("pwbcc@gmail.com")
        print("-------------------------------------------")

    def save_reservation_to_json(self, filename="reservation.json"):
        if not self._reservation:
            print("No reservation to save.")
            return
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"reservations": []}
        
        data["reservations"].append({
            "user": self._user.to_dict(),
            "reservation": self._reservation.to_dict()
        })

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Reservation confirmed and saved to {filename}.")

    def start(self):
        while True:
            print("\nWelcome to the Basketball Court Reservation System!\n")
            print("Please choose an option:")
            print("Press 1 if you want to register.")
            print("Press 2 if you want to create a reservation.")
            print("Press 3 if you want to update a reservation.")
            print("Press 4 if you want to cancel a reservation.")
            print("Press 5 if you want to print a receipt.")
            print("Press 6 if you want to Confirm Reservation.")
            print("Press 7 if you want to exit.")
            
            choice = input("Your choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.create_reservation()
            elif choice == "3":
                self.update_reservation()
            elif choice == "4":
                self.cancel_reservation()
            elif choice == "5":
                self.print_receipt()
            elif choice == "6":
                self.save_reservation_to_json()
            elif choice == "7":
                print("Thank you for using the reservation system! Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    manager = ReservationManager()
    manager.start()
