# car_rental_system

Master of Software Engineering Assignment_1 — Car Rental System Project

## Project_description

This project is Command Line Interface based Car Rental System developed using python. it is designed to help users easily search, book, and manage rental cars through a simple text-based menu. The project also includes a car recommendation feature that suggests suitable cars based on user prefrences collected through a few simple questions. This helps users choose the right car according to their needs.

## Features(User side)

1. Search cars by Filters (users can search cars based on price range,fuel type or car category).
2. Save Favourite Cars (users can mark cars as favourite and view them later for quick bookings).
3. Booking Reminder (the system notifies users about upcoming booking start and return dates).
4. Rental Duration Calculator (users can check the total rental cost based on the number of rental days before confirming the booking).
5. View Car Availability Calendar (users can see whichdates a car is available or already booked). 
6. Booking Status Tracking (users can track the current status of their booking like Pending,Confirmed,Active,Completed).
7. Cancel Booking with Reason (users can cancel a booking by providing a reason, which is saved for admin review).
8. Rate and Review Cars (after returning a car, users can rate and give feedback about car).
9. Download Booking Recipt (users can download or view a booking summary and payment recipt).
10. wallet Balance (users can maintain a wallet balance and use it for faster payments).

## Features(Admins)

1.Dashboard Summary (admins can view a summary of total users,cars,booking, and earnings).
2.View Cancellation Reasons (admins can analyze user cancellation reasons to improve services). 
3.Approve or Rejection Bookings (admins can approve or reject bookings based on availability or policies).
4.Manage Car Availability (admins can mark cars as available under maintenance or unavailable).
5.User Activity Monitoring (admins can monitor booking and payment activity of users).
6.Review User Feedback (admins can view user ratings and reviews to improve car quality).
7.Data Backup Management (admins can back up restore system data to prevent data loss).

## Technologies Used

- Python 3.x
- SQLite

## Installation / Setup

- git clone https://github.com/nancy/car_rental_system.git
- cd car-rental-system
- pip install -r requirements.txt
- python main.py

## Usage

- Run python main.py
- Follow the menu prompts to
- Browse cars
- Rent a car
- Return a car
- View rental history
- Admin users can log in with predefined credentials to manage cars and bookings
