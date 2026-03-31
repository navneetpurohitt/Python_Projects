import random

# Simple_RPG_Game.py


# Base class for characters
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self, target):
        damage = random.randint(1, self.attack)
        target.take_damage(damage)
        return damage

    def __str__(self):
        return f"{self.name}: HP={self.hp}, Attack={self.attack}"


# Warrior subclass
class Warrior(Character):
    def __init__(self, name, hp, attack, armor):
        super().__init__(name, hp, attack)
        self.armor = armor

    def take_damage(self, damage):
        reduced_damage = max(damage - self.armor, 0)
        super().take_damage(reduced_damage)

    def __str__(self):
        return f"{self.name} (Warrior): HP={self.hp}, Attack={self.attack}, Armor={self.armor}"


# Mage subclass
class Mage(Character):
    def __init__(self, name, hp, attack, mana):
        super().__init__(name, hp, attack)
        self.mana = mana

    def cast_spell(self, target):
        if self.mana >= 10:
            self.mana -= 10
            spell_damage = self.attack + 5
            target.take_damage(spell_damage)
            return spell_damage
        else:
            return 0

    def __str__(self):
        return f"{self.name} (Mage): HP={self.hp}, Attack={self.attack}, Mana={self.mana}"


# Enemy class
class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)

    def __str__(self):
        return f"{self.name} (Enemy): HP={self.hp}, Attack={self.attack}"


# Inventory class
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        return f"Inventory: {', '.join(self.items) if self.items else 'Empty'}"


# Example gameplay
if __name__ == "__main__":
    # Create characters
    warrior = Warrior("Aragorn", 100, 15, 5)
    mage = Mage("Gandalf", 80, 12, 50)
    enemy = Enemy("Orc", 50, 10)

    # Create inventory
    inventory = Inventory()
    inventory.add_item("Health Potion")
    inventory.add_item("Mana Potion")

    # Display initial states
    print(warrior)
    print(mage)
    print(enemy)
    print(inventory)

    # Simulate battle
    print("\nBattle begins!")
    while enemy.is_alive() and (warrior.is_alive() or mage.is_alive()):
        # Warrior attacks
        damage = warrior.deal_damage(enemy)
        print(f"{warrior.name} attacks {enemy.name} for {damage} damage.")
        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            break

        # Mage casts spell
        spell_damage = mage.cast_spell(enemy)
        if spell_damage > 0:
            print(f"{mage.name} casts a spell on {enemy.name} for {spell_damage} damage.")
        else:
            print(f"{mage.name} tries to cast a spell but lacks mana.")

        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            break

        # Enemy attacks
        target = warrior if warrior.is_alive() else mage
        damage = enemy.deal_damage(target)
        print(f"{enemy.name} attacks {target.name} for {damage} damage.")

    # Display final states
    print("\nFinal states:")
    print(warrior)
    print(mage)
    print(enemy)
    print(inventory)