import requests

battles = [
    "4369",
]


def load_battle_info(battle_id):
    url = "https://battleofthebits.org/api/v1/battle/load/{}/".format(battle_id)
    json_data = requests.get(url).json()
    title = json_data['title']
    entry_count = int(json_data['entry_count'])
    battle_type = int(json_data['type'])
    return title, entry_count, battle_type


def create_entry_array(entry_array, url):
    json_data = requests.get(url).json()
    for entry in json_data:
        entry_array.append(entry['score'])
    return entry_array


def get_battle_entries(battle_id):
    title, entry_count, battle_type = load_battle_info(battle_id)
    if battle_type == 3:
        title = "OHB: " + title
    else:
        title = "Major: " + title
    entry_array = []
    if entry_count > 250:
        entry_array = create_entry_array(entry_array, "https://battleofthebits.org/api/v1/entry/list/0/250?filters=battle_id~{}".format(battle_id))
        entry_array = create_entry_array(entry_array, "https://battleofthebits.org/api/v1/entry/list/1/250?filters=battle_id~{}".format(battle_id))
        return title, entry_array
    else:
        entry_array = create_entry_array(entry_array, "https://battleofthebits.org/api/v1/entry/list/0/250?filters=battle_id~{}".format(battle_id))
        return title, entry_array

def calc_average(score_array):
    score = 0.0
    for entry_score in score_array:
        score = score + float(entry_score)
    score_average = score / len(score_array)
    return round(score_average, 3)

try:
    full_score_array = []
    for battle_id in battles:
        title, score_array = get_battle_entries(battle_id)
        full_score_array += score_array
        score_average = calc_average(score_array)
        print(title+"\n"+str(len(score_array))+" Entries"+"\n"+"Average Score: "+str(score_average)+"\n")
    full_score_average = calc_average(full_score_array)
    print("All Battles" + "\n" + str(len(full_score_array)) + " Entries" + "\n" + "Average Score: " + str(full_score_average))
except:
    print("Not a valid battle id.")

