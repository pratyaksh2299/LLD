# Low-Level Design (LLD) Examples

This repository contains implementations of fundamental design principles and patterns in Python, focusing on Low-Level Design (LLD) concepts. LLD emphasizes creating flexible, maintainable, and scalable software through proper abstraction, encapsulation, and design patterns.

## SOLID Principles

The SOLID principles are five design principles intended to make software designs more understandable, flexible, and maintainable.

### 1. Single Responsibility Principle (SRP)
- **File**: [Single_Responsiblity_Principle.py](Single_Responsiblity_Principle.py)
- **Description**: A class should have only one reason to change, meaning it should have only one job or responsibility.

### 2. Open-Closed Principle (OCP)
- **File**: [Open_Close_Principle.py](Open_Close_Principle.py)
- **Description**: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

### 3. Liskov Substitution Principle (LSP)
- **File**: [LIiskov_Substitution_Principal.py](LIiskov_Substitution_Principal.py)
- **Description**: Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.

### 4. Interface Segregation Principle (ISP)
- **File**: [Intergface_Segregation_principle.py](Intergface_Segregation_principle.py)
- **Description**: No client should be forced to depend on methods it does not use. Interfaces should be client-specific.

### 5. Dependency Inversion Principle (DIP)
- **File**: [Dependancy_Inversion_Principle.py](Dependancy_Inversion_Principle.py)
- **Description**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

## Design Patterns

Design patterns are reusable solutions to common problems in software design.

### Creational Patterns

#### Factory Design Pattern
- **Directory**: [Factory_Design_Pattern/](Factory_Design_Pattern/)
- **Files**:
  - [Simple_Factory.py](Factory_Design_Pattern/Simple_Factory.py): Simple Factory pattern implementation.
  - [Factory.py](Factory_Design_Pattern/Factory.py): Factory Method pattern.
  - [Abstrasct_Factory.py](Factory_Design_Pattern/Abstrasct_Factory.py): Abstract Factory pattern.
- **Description**: Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### Behavioral Patterns

#### Observer Design Pattern
- **File**: [Observer_Design_pattern.py](Observer_Design_pattern.py)
- **Description**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

#### Strategy Design Pattern
- **File**: [Strategy_Design_Pattern.py](Strategy_Design_Pattern.py)
- **Description**: Enables selecting an algorithm's behavior at runtime. Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

## Sample Application: Tomato App

A practical example demonstrating the application of design principles in a food delivery system.

- **Directory**: [Tomato_app/](Tomato_app/)
- **Components**:
  - **Models**:
    - [cart.py](Tomato_app/models/cart.py): Shopping cart model.
    - [MenuItem.py](Tomato_app/models/MenuItem.py): Menu item model.
    - [Restraurent.py](Tomato_app/models/Restraurent.py): Restaurant model.
  - **Managers**:
    - [RestrurentManger.py](Tomato_app/Managers/RestrurentManger.py): Restaurant management logic.

## Document Editor

- **File**: [Document_Editor.py](Document_Editor.py)
- **Description**: An example implementation of a document editor, possibly demonstrating various design patterns in action.

## How to Run

These are Python implementations. To run any of the files:

```bash
python <filename>.py
```

For example:
```bash
python Single_Responsiblity_Principle.py
```

Note: Some files may require additional setup or may be demonstration classes without a main execution block. Check the file contents for specific usage instructions.

## Contributing

Feel free to contribute by adding more design pattern implementations or improving existing ones. Ensure code follows Python best practices and includes appropriate comments.

## License

This project is for educational purposes. Use at your own discretion.