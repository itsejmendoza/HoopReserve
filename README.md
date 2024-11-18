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
  - I created the `User` and `Reservation` classes to represent individual users and their reservations.
  - For managing these processes, I implemented the `ReservationManager` class to handle actions like user registration, reservation creation, updating, cancellation, and receipt generation.
  - The `BasketballCourtReservationSystem` class serves as the main controller, integrating user registration, reservation management, and overall system navigation.

 
- **Encapsulation** 🩹
  -	It refers to combining data and the functions that manipulate that data into a single unit or class, while limiting direct access to certain parts of the object’s components.
  -	In the `User` and `Reservation` classes, I encapsulated the attributes (e.g., `name`, `contact`, `date`) and their corresponding methods. These methods control how the data is accessed and updated, preventing direct manipulation of object attributes.



 - **Polymorphism**  📑
     - `update Method:` The `update` method in the `Reservation` class demonstrates polymorphism. It allows users to update any combination of `start_time`, `end_time`, and `date` independently of one another.

- **Abstraction**  🗄️  
     - ReservationManager as an Abstraction Layer: The `ReservationManager` class abstracts the complexities of managing users and reservations. It provides an easy-to-use interface for the user to interact with the system without having to worry about the underlying implementation.
     - User-Friendly Interface: The `ReservationManager` class simplifies interactions with the reservation system. For example, the method `create_reservation` hides the complexity of creating a reservation from the user:
 
### Integration with SDG 🌍
<div align="center">
  <img src="https://github.com/yshlae/ResQnect/blob/main/images/SDG%20Goal%2011.png" alt="SDG Goal 11" width="1000">
</div>

**Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities** HoopReserve can effectively align with Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities. SDG 11 focuses on creating inclusive, safe, resilient, and sustainable urban environments, and this system promotes inclusivity and fairness in community spaces. By enabling a clear and respectful way for individuals to reserve court time, the system helps avoid conflicts, promotes equitable access, and supports a harmonious environment where all community members have a fair opportunity to use the facilities.
Additionally, this reservation system encourages efficient resource management. With structured booking, court maintenance can be better planned, ensuring a clean and well-maintained space for users. This improves the sustainability of community resources and creates a safer, more enjoyable environment for everyone. By fostering respect and organization, the system supports a more inclusive and connected community, where recreational areas are thoughtfully and sustainably managed.


This system contributes to SDG 11 in three key areas. First, it aids in **preparation** by allowing communities to track and store essential resources such as food, water, and medical supplies, ensuring quick mobilization when disaster strikes. The system's ability to maintain an updated inventory of resources helps communities be better prepared for emergencies. Second, during the **response and recovery** phases, it facilitates the assignment of tasks and the management of volunteers, ensuring that resources are deployed efficiently and volunteers can be quickly assigned to critical areas. Task tracking and real-time response monitoring ensure timely intervention in disaster-affected regions. Lastly, the system contributes to resilience building by allowing communities to track response times, resource usage, and volunteer deployment. This data helps communities improve their disaster response strategies over time.

 <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>


 
