
name_p= input("Введите имя игрока: ")
player= {
    "name": name_p,
    "health": 100,
    "damage": 50,
    "armor": 1.2
}

name_e= input("Введите имя врага: ")
enemy= {
    "name": name_e,
    "health": 50,
    "damage": 30,
    "armor": 1.2
}

def get_damage(damage, armor):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit["damage"],target["armor"])
    target["health"] -= damage


attack(player,enemy)

attack(enemy,player)

print(player)
print(enemy)