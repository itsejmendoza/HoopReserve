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
    - Classes serve as blueprints for creating objects, encapsulating both data and behavior. The project uses several classes to represent real-world entities in the system.
    - User Class: Encapsulates user information (`name`, `contact`, `address`) and provides methods to interact with this data, including `to_dict` for converting it into a simple format like a dictionary.
    - Reservation Class: Represents a reservation with attributes like `id`, `user_name`, `start_time`, `end_time`, and `date`. Methods such as update and `to_dict` allow for dynamic updates and easy conversion to a dictionary format.
    - ReservationManager Class: Handles the reservation process, managing user registration, reservation creation, and system interactions..

- **Encapsulation** 🩹
    - Encapsulation restricts direct access to object data, exposing only necessary methods for interaction.
    - In this project, private attributes (e.g., `_name`, `_contact`, `_id`) are used, with public getter methods (`@property`) providing controlled access.
    - For example, the Reservation class has methods like `update` to change its details without directly accessing private data.

- **Polymorphism** 📄
    - Polymorphism allows objects to redefine inherited behaviors.
    - The `__str__` method is overridden in both the `User` and `Reservation` classes to provide meaningful string representations of objects. This ensures that printed objects display human-readable information fit for their respective class.

- **Abstraction** 🗄️
    - Abstraction hides complex logic while exposing only the necessary interfaces for interaction.
    - The `ReservationManager` class abstracts the reservation system's operations, presenting users with intuitive methods (`register_user`, `create_reservation`, `save_reservation_to_json`) without exposing the underlying implementation details, such as file handling or object serialization.  
    
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
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Creating%20a%20Reservation.jpg" alt="Creating a Reservation" width="370" height="200">
</div>


- **Updating a Reservation** 
   - 	Choose option 3 to modify an existing reservation.
   -  You will be prompted to enter new details. Press Enter to keep existing values:
   -  The updated reservation details will be saved.

 <div align="right side">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Updating%20a%20Reservation.jpg" alt="Updating a Reservation" width="370" height="200">
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
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/Printing%20a%20Receipt.jpg" alt="Printing a Receipt" width="370" height="200">
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
