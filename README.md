Here’s a **README** file template for your **GitHub** repository, where you can showcase your **Todo List App** and **Vehicle Management System** projects:

---

# Object-Oriented Programming (OOP) Projects in Python 🚀

This repository contains two mini projects built using **Object-Oriented Programming (OOP)** concepts in Python. These projects helped me understand core OOP principles such as **classes**, **objects**, **inheritance**, **polymorphism**, and **abstraction**. Below are the details of the two projects:

---

## 1. Todo List App 📝

A command-line **Todo List app** that allows users to manage tasks effectively. The app lets you:

* **Add** tasks to the list
* **Remove** tasks from the list
* **View** the tasks
* **Mark** tasks as **completed**

### Structure:

* **Task Class**: Represents an individual task with the attributes **task name** and **status** (pending/completed).
* **TodoList Class**: Manages the list of tasks and allows adding, removing, viewing, and updating task statuses.

### Key Concepts:

* **Abstraction**: The `mark_completed()` method hides unnecessary details and updates the status of tasks.
* **Encapsulation**: Task details and task statuses are protected and managed within methods.
* **Magic Methods**: The `__str__` method makes task outputs cleaner and easier to read.

---

## 2. Vehicle Management System 🚗🏍️🚚

In this project, I built an abstract base class `Vehicle` with subclasses like **Car**, **Bike**, and **Truck**. The app showcases the following features:

* **Service**: Each vehicle can be serviced, and its service status is tracked.
* **Drive**: Each vehicle implements a different `drive()` method based on the vehicle type.

### Structure:

* **Vehicle Class** (Abstract Base Class): Contains common attributes like **brand**, **model**, and **service status**.
* **Car, Bike, Truck Classes**: Each vehicle implements the `drive()` method differently, showcasing **inheritance** and **polymorphism**.

### Key Concepts:

* **Abstraction**: Hiding unnecessary details while allowing users to interact with vehicle objects (e.g., servicing a vehicle).
* **Inheritance**: All vehicles inherit from the `Vehicle` class and implement the `drive()` method in their own way.
* **Polymorphism**: Different vehicles perform the same action (`drive()`), but the behavior varies based on the class type.
* **Encapsulation**: Vehicle attributes like **brand**, **model**, and **service status** are hidden within the class and updated using methods.

---

## Getting Started

### Prerequisites:

* Python 3.x installed on your machine
* No additional dependencies are required for these projects.

### How to Run:

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/repository-name.git
   ```

2. Navigate to the project directory.

   ```bash
   cd repository-name
   ```

3. Run the Python files to see the app in action.

   ```bash
   python todo_list_app.py
   python vehicle_management_system.py
   ```

---

## Next Steps 🔥

* **Todo List App**: Add new features like **due dates**, **task priorities**, and **persistence (saving tasks to a file)**.
* **Vehicle Management System**: Enhance vehicle functionalities and include more vehicle types or additional actions.
