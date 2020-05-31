import enemy as Enemy
import player as Player
import random
import time

name = input("\nWelcome to the Monster Attack Game. Your Name: > ")

def start_game():

    while True:
        sp_attack = input("\nYour Turn. Type S, for special attack or N for normal attack  >>> ").lower()
        if sp_attack == 's':
            gamer_sp_attack = special_attack()

            if gamer_sp_attack == True:
                gamer.health += 15
                big_e.health -= 15
                print(f":) Successfully launced Special attack. Your health has been upgraded with 15%. you have {gamer.health} health now")
                print(f"Monster health is now {big_e.health}")
            else:
                gamer.health -= 15
                print(
                    f":( You failed to launch special attack 15% of your health has been deducted. Your health has deducted by 15%.\nYour health is now >>> {gamer.health}")
        elif sp_attack == 'n':
            gamer_attack(name, p_damage[random.randint(0, 1)])
        else:
            print('entry not recognised!!!')
        break


    if big_e.health < 0:
        print (f"Hurray {name}. You have won.")
        return False
    enemy_attack(name, big_damage[random.randint(0, 2)])

    if gamer.health < 0:
        print(f"Tough luck {name}. You have lost to the Monster.")
        return False
    time.sleep(2)
    return True


#health, damage_to_opponent, special_damage_to_opponent):
name = "Gamer"
#small_e = Enemy.Enemy(25, 7, 12)
big_e = Enemy.Enemy(100, 15, 20)

#name, health, damage_to_opponent, special_damage_to_opponent):
gamer = Player.Player(name, 100 , 10, 15)

p_damage = [0, 10]
#small_damage = [0, 7, 12]
big_damage = [0, 12, 18]


def gamer_attack(name, damage):
    if damage == 0:
        print(f"{name}!, you failed to attack on your turn")
        return (f"{name}!, failed to attack")
    elif damage == 10:
        big_e.health -= gamer.damage_to_opponent
        print(f"Normal attack applied to enemy. Remaining enemy's health >>> {big_e.health}")
        return 10


def enemy_attack(name, damage):
    if damage == 0:
        print(f"Monster, failed to attack")
        return (f"Monster, failed to attack")
    elif damage == 12:
        gamer.health -= big_e.damage_to_opponent
        print(
            f"Normal attack applied to {name}. Your remaining health is >>> {gamer.health}")
        return 12
    else:
        big_e.health += big_e.special_damage_to_opponent
        gamer.health -= big_e.special_damage_to_opponent
        print(f"\nOuchh!! {name}. Monster applied a special damage on you.\nYour health is now >>> {gamer.health}\nMonster health is now >>> {big_e.health}")
        return 18

def special_attack():
    if random.randint(1, 5) == 5:
        return True


while True:
    if start_game() == False:
        time.sleep(2)
        break
