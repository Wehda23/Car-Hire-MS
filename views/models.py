

# Interface of a table class
class Table:
    name: str
    fields: list


class CustomersTable(Table):
    name: str = 'customers'
    fields: list = [
        "customer_id INT AUTO_INCREMENT PRIMARY KEY",
        "name VARCHAR(255) NOT NULL",
        "email VARCHAR(255) UNIQUE NOT NULL",
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    ]

class VehiclesTable(Table):
    name: str = 'vehicles'
    fields: list = [
        "vehicle_id INT AUTO_INCREMENT PRIMARY KEY",
        "car_type ENUM('Small Car', 'Family Car', 'Van') NOT NULL"
    ]
    
class BookingsTable(Table):
    name: str = 'bookings'
    fields: list = [
        "booking_id INT AUTO_INCREMENT PRIMARY KEY",
        "customer_id INT NOT NULL",
        "vehicle_id INT NOT NULL",
        "hire_date DATE NOT NULL",
        "return_date DATE NOT NULL",
        "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)",
        "FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)"
    ]