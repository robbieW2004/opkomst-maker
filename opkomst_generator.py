import json

def load_existing_data(filename):
    try:
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []
    return existing_data

def create_activity():
    category = input("Enter the category of the activity: ")
    name = input("Enter the name of the activity: ")
    time = input("Enter the time it takes for the activity (in minuten): ")
    description = input("Enter a description of the activity: ")

    activity = {
        "category": category,
        "name": name,
        "time": time,
        "description": description
    }

    return activity

def update_or_add_activity(existing_data, new_activity):
    for existing_activity in existing_data:
        if existing_activity["category"] == new_activity["category"]:
            existing_activity["activities"].append({
                "name": new_activity["name"],
                "time": new_activity["time"],
                "description": new_activity["description"]
            })
            return

    # If the category doesn't exist, add a new category
    existing_data.append({
        "category": new_activity["category"],
        "activities": [{
            "name": new_activity["name"],
            "time": new_activity["time"],
            "description": new_activity["description"]
        }]
    })

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f"Activity details saved to {filename}.")

def main():
    filename = "pathtojson\\activities.json"
    existing_data = load_existing_data(filename)

    while True:
        activity = create_activity()
        update_or_add_activity(existing_data, activity)

        another_activity = input("Do you want to add another activity? (yes/no): ")
        if another_activity.lower() != 'yes':
            break

    save_to_json(existing_data, filename)

if __name__ == "__main__":
    main()
