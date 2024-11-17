<div align="center">
  <img src="https://github.com/itsejmendoza/HoopReserve/blob/main/images/HoopReserve.png" alt="ResQnect Logo" width="290" height="260">

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

</details>

---

### Project Overview 🕵🏻
**HoopReserve** makes reserving local basketball courts easy and fair. By allowing users to book court time in advance, it helps prevent conflicts over who gets to play, ensuring everyone has an equal opportunity. The simple booking process lets players plan their games without hassle, so they can focus on enjoying the sport. It's not just about convenience—it's about building a respectful, connected community where everyone has a fair shot at the court.

### Application of Python Concepts 🐉
In building this Basketball Court Reservation System, key Python concepts were used to make it easy and functional. Here's how they were applied:

- **Classes and Objects (OOP Basics)** 📕
  -  `User Class: ` Represents a user who wants to make a reservation. The `User` class encapsulates personal details such as `name`, `contact`, and `address`.
  -	`Reservation Class:` Represents a reservation with properties like `start_time`, `end_time`, `date`, and a unique `id`. Each reservation is an object of this class. 
  - `ReservationManager Class:` Manages the reservation process. It handles user registration, reservation creation, updates, cancellation, and receipt generation.
 
- **Encapsulation** 🩹
   - `Private Attributes:` The `User` and `Reservation` classes use private attributes ( `_name`, `_contact`, `_start_time`) to store sensitive data. Access to these attributes is provided via getter methods (`@property`).
   - `Control over Data Access:` For example, in the `Reservation class`, you can control how the reservation’s start time, end time, and date are modified through the `update` method.

 - **Polymorphism**  📑
     - `update Method:` The `update` method in the `Reservation` class demonstrates polymorphism. It allows users to update any combination of `start_time`, `end_time`, and `date` independently of one another.

- **Abstraction**  🗄️  
     - ReservationManager as an Abstraction Layer: The `ReservationManager` class abstracts the complexities of managing users and reservations. It provides an easy-to-use interface for the user to interact with the system without having to worry about the underlying implementation.
     - User-Friendly Interface: The `ReservationManager` class simplifies interactions with the reservation system. For example, the method `create_reservation` hides the complexity of creating a reservation from the user:  


 
