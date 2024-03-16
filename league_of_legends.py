from donnees import champions_list
import random

def get_from_role(role):
    role_champion_list = []
    for c in champions_list['champion']:
        if role in c['roles']:
            role_champion_list.append(c)
    return { role:role_champion_list }


def get_random_champion(role):
    if role == 'all':
        return random.choice(champions_list['champion'])
    else:
        dict = get_from_role(role)
        return random.choice(dict[role])