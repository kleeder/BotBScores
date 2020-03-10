import requests

battle_id = "4394"


def load_battle_info(battle_id):
    url = "https://battleofthebits.org/api/v1/battle/load/{}/".format(battle_id)
    json_data = requests.get(url).json()
    title = json_data['title']
    entry_count = int(json_data['entry_count'])
    battle_type = int(json_data['type'])
    return title, entry_count, battle_type


def check_user(entry_id):
    url = "https://battleofthebits.org/api/v1/entry/load/{}".format(entry_id)
    json_data = requests.get(url).json()
    return str(json_data['botbr']['id'])


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


try:
    title, score_array = get_battle_entries(battle_id)
    score = 0.0
    for entry_score in score_array:
        score = score + float(entry_score)
    score_average = score/len(score_array)
    score_average = round(score_average, 3)
    print(title+"\n"+str(len(score_array))+" Entries"+"\n"+"Average Score: "+str(score_average))
except:
    print("Not a valid battle id.")

