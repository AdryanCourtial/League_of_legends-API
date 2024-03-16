from donnees import champions_list

new_list = {
    'champion': [

    ]
}

for c in champions_list['champion']:
    c["id"] = c["id"] - 1
    new_list["champion"].append(c)
    print(c)