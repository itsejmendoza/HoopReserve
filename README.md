<div align="center">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/HoopReserve.png" alt="HoopReserve Logo" width="290" height="260">

  <h1>HoopReserve</h1>

  <h3>🏀 "Your game, your time, your court!" 🏀 <br>
  A community basketball court reservation system. Made to play, built to be fair..</h3>

   <p><b>IT 2104</b><br>
  <a href="https://github.com/itsejmendoza">Mendoza, Elthon-Jhon M.</a></p>

   
  <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

<details>
  <summary><strong>Table of Contents</strong></summary>
  
  1. [Project Overview](#project-overview)  
  2. [Application of Python Concepts](#application-of-python-concepts)  
  3. [Integration with SDG](#integration-with-sdg)  
  4. [Running the Program](#running-the-program)
  5. [Gratitude Statement](#gratitude-statementa)
</details>

---

### Project Overview 🔍
**HoopReserve** makes reserving local basketball courts easy and fair. By allowing users to book court time in advance, it helps prevent conflicts over who gets to play, ensuring everyone has an equal opportunity. The simple booking process lets players plan their games without hassle, so they can focus on enjoying the sport. It's not just about convenience—it's about building a respectful, connected community where everyone has a fair chance to use the court.

 <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

### Application of Python Concepts 🐍
The  Basketball Court Reservation System effectively illustrates core Object-Oriented Programming (OOP) principles. Below is an explanation of how these principles were applied:

- **Classes and Objects (OOP Basics)** 🗂️

    -	Classes are used to represent the main entities in the system: `User`, `Reservation`, and `ReservationManager.`
    - Each class has attributes (such as `name`,` contact`, `start_time`, `end_time`) and methods (such as `__init__`, `create_reservation`, `update_reservation`) that define its behavior.
    -	The ReservationManager class manages the interactions between User and Reservation objects, keeping track of existing reservations and providing user-facing methods for registration and reservation handling


- **Properties and Encapsulation** 🩹
    
    -	The `User` and `Reservation` classes use private attributes (e.g., `self._name`, `self._contact`) to store data.
    -	Properties (`@property`) are used to allow controlled access to these private attributes. For example, the `name`, `contact`, and `address` properties in the `User` class provide read-only access to the attributes.
    -	This ensures that users cannot directly modify attributes like `self._name` from outside the class, thus protecting the integrity of the data.


- **Class Methods and Instance Methods** 📄
  
    - Instance Methods (e.g., `__init__`, `update_reservation`) define behavior that operates on individual instances of the class.
    -	Class Methods (e.g., `from_dict`) operate on the class itself, not on an individual instance. They are used to create instances from external data (like a dictionary), which is useful for serialization or deserialization tasks.

    
- **List and Data Management** 🗄️
  
    -	Lists are used to manage multiple reservations. The `ReservationManager` class uses a list (`self._reservations`) to store all reservations created during the session.
    -	You use loops and conditional statements to manage and check reservation availability, allowing the system to handle multiple reservations efficiently.
      

- **File Handling and JSON Serialization**
  
    - File I/O is used to save reservations to a JSON file. The method `save_reservation_to_json` reads from a file and writes data in JSON format, allowing you to persist data across sessions.
    - JSON Serialization: The `to_dict()` method in both `User` and `Reservation` classes converts objects to dictionaries, making it easy to store and retrieve them in a JSON format.
      

- **Input/Output and Interaction**
  
    -	User Input: The system relies on user input to gather information for registration and reservations (e.g., `input()`).
    -	Print Statements: The code uses `print()` to interact with the user, showing status messages, reservation details, and receipts.
      

- **Conditionals and Loops**
  
    -	If-Else Statements: The code uses `if-else` to check whether a reservation exists, validate user input, and check for availability (e.g., in `is_date_available` and `create_reservation`).
    -	While Loop: The main program runs in an infinite loop (`while True`), allowing the user to interact with the system until they choose to exit by inputting 7.


- **Exception Handling**
  
    -	Try-Except Blocks: The code handles errors using `try-except` to manage potential issues like file not being found or invalid JSON format. This ensures the program doesn’t crash and can recover gracefully.


- **String Formatting**
  
    -	The `__str__` method in both` User` and `Reservation` classes uses f-string formatting to create user-friendly output.
 

- **Static Variables**

    -	The `Reservation` class uses a static variable `_counter` to keep track of the reservation ID. Each new reservation gets a unique ID by incrementing this counter.

    
<hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>
 
### Integration with SDG 🌏 
<div align="center">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/SDG%20Goal%2011.png" alt="SDG Goal 11" width="900">
</div>

**Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities**  
  HoopReserve aligns perfectly with Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities. By offering a fair and respectful system for reserving basketball courts, it promotes inclusivity, prevents conflicts, and ensures everyone has equal access to community spaces. Beyond fairness, structured bookings allow for better maintenance planning, keeping courts clean, safe, and enjoyable for all. This isn’t just about convenience—it’s about fostering respect, connection, and sustainability in urban communities. HoopReserve helps create vibrant, well-managed spaces where everyone can come together and play.
 

 <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>


### Running the Program 👩‍💻

To run the HoopReserve system, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/itsejmendoza/HoopReserve.git
2. Navigate to the project repository:
   ```bash
   cd HoopReserve

3. Run the program:
   ```bash
   python main.py


### Instructions for Running the HoopReserve Basketball Court Reservation System  💻 

This guide provides step-by-step instructions for using the HoopReserve Basketball Court Reservation System, which allows users to register, create, update, and manage reservations for a basketball court.
- **Starting the Program** 
   -	Run the program in a Python environment.
   -	Upon starting, you will see a welcome message and a main menu with the following options:
   -	Enter the number corresponding to the action you want to perform.

<div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Starting%20the%20Program.jpg" alt="Starting the Program" width="370" height="170">
</div>
       

- **Registering a User** 
   -  Choose option 1 from the main menu.
   -  You will be prompted to enter:
   -  The entered details will be saved, and a confirmation message will appear.

 
 <div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Ragister%20a%20User.jpg" alt="Register a User" width="370" height="200">
</div>
 
  
- **Creating a Reservation** 
   - 	Choose option 2 to create a new reservation.
   -	Enter the following details:
   -	Your reservation will be created and saved, with details displayed for confirmation.

<div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Creating%20a%20Reservation.jpg" alt="Creating a Reservation" width="480" height="270">
</div>


- **Updating a Reservation** 
   - 	Choose option 3 to modify an existing reservation.
   -  You will be prompted to enter new details. Press Enter to keep existing values:
   -  The updated reservation details will be saved.

 <div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Updating%20a%20Reservation.jpg" alt="Updating a Reservation" width="490" height="270">
</div>

- **Canceling a Reservation** 
   -	Choose option 4 to cancel an existing reservation.
   -	You will be asked to confirm the cancellation. Type yes to confirm, or no to cancel the operation.

 <div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Canceling%20a%20Reservation.jpg" alt="Canceling a Reservation" width="370" height="200">
</div>

- **Printing a Receipt** 
   -	Choose option 5 to print a receipt for your reservation.
   -	The receipt will display your details, reservation date, start time, and end time, 
formatted as follows:

<div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Printing%20a%20Receipt.jpg" alt="Printing a Receipt" width="370" height="400">
</div>

- **Confirming a Reservation** 
   -	Choose option 6 to save the reservation to a JSON file.
   -	A confirmation message will be shown, and the reservation will be stored in the reservation.json file.

 <div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Confirming%20a%20Reservation.jpg" alt="Confirming a Reservation" width="370" height="200">
</div>

- **Exiting the Program** 
   -	To exit, select option 7.
   -	A farewell message will appear, and the program will terminate.

<div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Exiting%20the%20Program.jpg" alt="Exiting the Program" width="370" height="200">
</div> 
     
   -  These steps provide an easy-to-follow guide for managing your basketball court reservations using the HoopReserve system.

<hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

## Gratitude Statement 🫡

`I want to thank God for the guidance, my family for their love, my friends for their support, and my professor, Ms. Fatima Marie P. Agdon, for her guidance and wisdom. Thank you all for being part of this project journey.`
