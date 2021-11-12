import random


def find_eat(cords):
    min_len = -1
    num = -1
    for i in range(len(eat)):
        local_len = (cords[0] - eat[i][0])**2 + (cords[1] - eat[i][1])**2
        if local_len < min_len or min_len < 0:
            min_len = local_len
            num = i
    return num


def find_i_person_by_id(id, persons):
    for i in range(len(persons)):
        if persons[i]["id"] == id:
            return i


def move(cords, point):
    go_x = point[0] - cords[0]
    if go_x > 1:
        go_x = 1
    elif go_x < -1:
        go_x = -1
    go_y = point[1] - cords[1]
    if go_y > 1:
        go_y = 1
    elif go_y < -1:
        go_y = -1
    return go_x, go_y


eat_count = 1000
persons_good_count = 100

eat = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(eat_count)]  # x, y
persons_good = [{"point": [], "cords": [random.randint(0, 100), random.randint(0, 100)], "energy": 100, "id": i}
                for i in range(persons_good_count)]

while persons_good:
    i_del = []
    for person_good_i in range(len(persons_good)):
        person_good = persons_good[person_good_i]

        if person_good["energy"] <= 0:
            i_del.append(person_good["id"])

        index = find_eat(person_good["cords"])
        if index > -1:
            person_good["point"] = eat[index]
        else:
            person_good["point"] = []

        if person_good["point"]:
            if person_good["energy"] >= 5:
                move_x, move_y = move(person_good["cords"], person_good["point"])
                person_good["cords"][0] = person_good["cords"][0] + move_x
                person_good["cords"][1] = person_good["cords"][1] + move_y
                person_good["energy"] -= 5
            if person_good["point"] == person_good["cords"]:
                person_good["energy"] = 100
                del eat[find_eat(person_good["point"])]
                person_good["point"] = []

        person_good["energy"] -= 2
        print(person_good)

    print(i_del)
    for i in i_del:
        del persons_good[find_i_person_by_id(i, persons_good)]