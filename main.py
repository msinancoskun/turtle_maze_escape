from manager import *

def turtle_backwards(turtle):
    rt(turtle, 90)
    rt(turtle, 90)

def can_go_right(turtle):
    #This function checks, if the turtle is able to go right.
    rt(turtle, 90)
    if is_facing_wall(turtle):
        lt(turtle, 90)
        return False
    else:
        lt(turtle, 90)
        return True


def escape_from_column(turtle, max_treasure_count, total_treasure_count):
    treasure_count = total_treasure_count
    if is_over_treasure(turtle):
        pick_treasure(turtle)
        treasure_count += 1
        if treasure_count == max_treasure_count:
            return treasure_count
    lt(turtle, 90)
    while not is_facing_wall(turtle):   # Turtle moves up until facing wall
        fd(turtle, 30)
        if is_over_treasure(turtle):
            pick_treasure(turtle)
            treasure_count += 1
            if treasure_count == max_treasure_count:
                return treasure_count
    turtle_backwards(turtle)            # When faced a wall, turns back
    while not is_facing_wall(turtle):
        fd(turtle, 30)
        if is_over_treasure(turtle):
            pick_treasure(turtle)
            treasure_count += 1
            if treasure_count == max_treasure_count:
                return treasure_count
    turtle_backwards(turtle)
    while not is_facing_wall(turtle):
        if can_go_right(turtle):
            rt(turtle, 90)
            fd(turtle, 30)
            fd(turtle, 30)
            break
        else:
            fd(turtle, 30)
    else:
        if can_go_right(turtle):
            rt(turtle, 90)
            fd(turtle, 30)
            fd(turtle, 30)

    return treasure_count


def q1(turtle):
    escape_from_column(turtle, 0, 0)


def q2(turtle, no_of_columns):
    for i in range(no_of_columns):
        escape_from_column(turtle, 0, 0)



def q3(turtle, max_treasure_count):
    collected_treasure = escape_from_column(turtle, max_treasure_count, 0)
    return collected_treasure

def q4(turtle, max_treasure_count, no_of_columns):
    collected_total_treasure = 0
    for i in range(no_of_columns):
        collected_total_treasure_by_column = escape_from_column(turtle, max_treasure_count, collected_total_treasure)
        collected_total_treasure += 1
    collected_total_treasure += collected_total_treasure_by_column - 1
    return collected_total_treasure

manager = WorldManager()
is_facing_wall = manager.is_facing_wall
is_over_treasure = manager.is_over_treasure
pick_treasure = manager.pick_treasure

if __name__ == '__main__':

    print(40 * "*" + " Welcome " + 40 * "*" + "\n")
    delay = 0.4

    while True:
        world = TurtleWorld()
        world.geometry("600x400")
        for i in range(1, 5):
            print(i, "-", "Question", i)
        print(0, "-", "Exit")
        choice = int(input("Choose Question Number: "))
        if choice == 1:
            manager.read_world("maze1.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q1(bob)
            wait_for_user()
        elif choice == 2:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            manager.read_world("maze2.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q2(bob, no_of_columns)
            wait_for_user()
        elif choice == 3:
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze3.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            print("# of treasures collected: " + str(q3(bob, max_treasure_count)))
            wait_for_user()
        elif choice == 4:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze4.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            print("# of treasures collected:" + str(
                q4(bob, max_treasure_count, no_of_columns)))
            wait_for_user()
        elif choice == 0:
            exit()
