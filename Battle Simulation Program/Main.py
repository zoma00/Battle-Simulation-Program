from Enemy import *
from Zombie import *
from Ogre import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('-------------------')

        e1.special_attack()
        e2.special_attack()
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
        print('------------')
        if e1.health_points > 0:
            print(f'{e1.get_type_of_enemy()} wins!')
        else:
            print(f'{e2.get_type_of_enemy()} wins!')


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie, ogre)


"""
The operator `-=` in Python is a shorthand for subtracting a value from a variable and then assigning the result back to that variable. 

### Explanation:
In the expression:
```python
e1.health_points -= e2.attack_damage
```
This means:
1. **Retrieve the current value** of `e1.health_points`.
2. **Subtract the value** of `e2.attack_damage` from it.
3. **Store the result** back into `e1.health_points`.

### Example:
If `e1.health_points` is initially `50` and `e2.attack_damage` is `10`, after executing the line:
- The operation would compute `50 - 10`, resulting in `40`.
- `e1.health_points` would then be updated to `40`.

### Summary:
The `-=` operator simplifies the syntax for updating variables by combining subtraction and assignment into 
a single operation, making the code cleaner and easier to read.
"""