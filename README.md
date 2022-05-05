# Movie-Ticket-Management

Implement a simple movie ticket vending machine. The movie theater that will use the machine has only one movie and one show time each day. Every morning, the theater manager will turn on the ticket machine, and it will ask him for the name of the movie and the ticket price that day. It will also ask how many seats are in the theater (so it won't sell too many tickets). When a customer walks up to the ticket machine, he will see the name of the movie, the time, and the ticket price displayed. There is a slot to insert money, a keypad of buttons to enter a number into the "Number of Tickets" field, and a "Buy" button. Printed tickets come out of a slot at the bottom of the machine. Above the ticket slot is a message display (for error messages like "Please enter more money or request fewer tickets" or "SOLD OUT!"). An additional display shows the customer's balance inside the machine. Finally, there is a "Return Change" button so the customer can get his unspent money back.

# Project Requirements
* Hardware Interfaces:
1. Hard Disk: The database connectivity requires a hardware configuration that is on-line. This makes it necessary to have a fast database system running on high rpm hard disk permitting complete data redundancy and back-up systems to support the primary goal of reliability.
2. The system must interface with the standard output devise, keyboard and mouse to interact with this software.

* Software Interfaces:
1. PyCharm

* Product Function:
1. Setting movie name, time and rate by the Manager.
2. Calculating the amount of money using number of tickets entered by customer.
3. Returning the balance amount on the basis of total amount and amount entered by user.
4. Creating a file, containing movie name, show time, rate of ticket, customer name, number of tickets bought, total amount to be paid and amount donated, after studding down the machine.

* Modules Used:
1. PySimpleGUI
2. Pandas

* Language Used:
1. Python

# Diagrams related to project
* Dataflow Diagram
<img width="929" alt="Data Flow Diagram" src="https://user-images.githubusercontent.com/58062535/166870014-4f1d657b-4a22-4da6-b2d6-dc69e4eefeec.png">

* Use Case Diagram
<img width="487" alt="Use Case Diagram" src="https://user-images.githubusercontent.com/58062535/166870078-da536cbf-376d-4e7f-86a2-66350c455dbe.png">

* Class Diagram
<img width="308" alt="Class Diagram" src="https://user-images.githubusercontent.com/58062535/166870112-ec89fccb-370b-4df2-b712-f2652313e781.png">

# Things learnt from the project

* Making diagram using case tools.
* Connecting small functions and making a larger code so that the code becomes clearer and more understandable.
* Making dialog box with buttons and data that are entered by user and later storing it, using PySimpleGUI.
* Making a file in python using pandas and converting it into excel file.
