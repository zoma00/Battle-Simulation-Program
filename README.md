# **Battle Simulation Program**

## **Overview**

The Battle Simulation Program is a Python-based project that showcases the use of **object-oriented programming (OOP)** concepts, particularly focusing on **polymorphism**. This simulation involves different enemy types engaging in a battle, with each enemy having unique behaviours and abilities. The flexibility of the code structure allows for easy addition of new enemy types, highlighting the power of polymorphism in OOP.

## **Project Structure**

The project is organized as follows:

```
/BattleSimulation
├── README.md
├── Enemy.py             # Base class for all enemy types
├── Ogre.py              # Derived class for Ogre enemy
├── Zombie.py            # Derived class for Zombie enemy
└── battle.py            # Main battle simulation logic
```

## **Installation**

1. **Clone the Repository**:
   
   ```bash
   git clone <repository_url>
   cd BattleSimulation
   ```

2. **Install Required Dependencies**:
   
install venv and install python version 3.7 or later versions.   
  

   *(If no dependencies are required, you can skip this step.)*

3. **Run the Battle Simulation**:
   
   Use the `Main.py` file to start the simulation:
   
   ```bash
   python Main.py
   ```

## **Usage**

The program is designed to simulate a battle between different enemy types, utilizing polymorphism to handle unique behaviours. Below is a brief guide to using the program:

1. **Creating Enemies**:
   - Instantiate the desired enemy types from the available classes like `Zombie` and `Ogre`.
   - You can also extend the base `Enemy` class to create new enemy types.

2. **Running a Battle**:
   - The `Main.py` file contains the logic to run a battle between two enemy instances.
   - The battle loop handles attacks and special abilities until one of the enemies wins.

3. **Extending the Program**:
   - To add a new enemy type, simply create a new class that inherits from `Enemy` and override the relevant methods.

## **Explanation of Concepts**

### **1. Polymorphism**

The core of this project is **polymorphism**, an OOP concept that allows objects to be treated as instances of their parent class. In this program:
- Different enemy types (`Zombie`, `Ogre`) inherit from a common base class, `Enemy`.
- Each enemy type can override methods such as `attack` and `special_attack` to introduce unique behaviours.
- The battle logic does not need to know the exact type of enemy; it relies on the common interface provided by the `Enemy` class.

### **2. Base and Derived Classes**

- **Base Class (`Enemy`)**:
  - Defines generic attributes like `health_points` and `attack_damage`.
  - Provides a standard interface for `attack` and `special_attack`.
  
- **Derived Classes**:
  - **`Ogre`** and **`Zombie`** extend the `Enemy` class.
  - Each subclass can override methods to implement unique behaviour (e.g., `Ogre` has a chance to increase attack damage, while `Zombie` can regenerate health).

### **3. Battle Logic**

- The `battle.py` file runs the battle between two enemies.
- Each round, enemies perform their actions (`talk`, `attack`, and `special_attack`).
- The program automatically determines which method to execute based on the enemy type, thanks to polymorphism.
- The battle ends when one enemy's health points drop to zero.

## **Examples**

### **Creating Enemies**

Here’s how you can create and initialize enemies:

```python
from Zombie import Zombie  *
from Ogre import Ogre *

# Creating enemy instances
zombie = Zombie(health_points=10, attack_damage=1)
ogre = Ogre(health_points=20, attack_damage=3)
```

### **Running a Battle**

To run a battle between the created enemies:

```python
from Enemy import *
from Zombie import *
from Ogre import *

# Running the battle simulation
battle(zombie, ogre)
```

### **Extending with a New Enemy Type**

To create a new enemy type, follow this pattern:

1. Create a new file, e.g., `Vampire.py`.
2. Define a new class that inherits from `Enemy`.
3. Override methods such as `talk`, `attack`, or `special_attack` to customize behaviour.

Example:

```python
from Enemy import Enemy

class Vampire(Enemy):
    def __init__(self, health_points=15, attack_damage=2):
        super().__init__(type_of_enemy='Vampire', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Vampire hisses menacingly.")

    def special_attack(self):
        # Custom behaviour for Vampire's special attack
        ...
```

## **Features**

- **Modular Code**: Easily extendable by adding new enemy types.
- **Battle Simulation**: Dynamic and chance-based battles create varied outcomes.
- **Object-Oriented Design**: Encapsulates enemy behaviours in separate classes, making the code clean and maintainable.

## **Future Enhancements**

- Add more enemy types with unique abilities.
- Implement a scoring system for each battle.
- Introduce more complex battle mechanics, like defensive moves or critical hits.
- Create a graphical interface for visualizing the battle.

## **Contributing**

If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request. Make sure to follow the coding style and provide tests for any new functionality.

## **License**

This project is licensed under the [MIT License](LICENSE).

Author: Hazem Elbatawy
Email: zoma0097@gmail.com

