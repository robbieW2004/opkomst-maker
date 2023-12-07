import json
import random

def load_existing_data(filename):
    try:
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return existing_data

def select_categories(existing_data):
    if not existing_data:
        return None

    categories = [activity["category"] for activity in existing_data]
    print("Select categories (comma-separated):")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        choices = input("Enter the counts of activities for each category (e.g., 2,1,3): ").split(',')
        choices = [int(choice.strip()) for choice in choices]
        selected_counts = choices
        selected_categories = [categories[i] for i in range(len(categories)) if selected_counts[i] > 0]
        
        if selected_categories:
            return selected_categories, selected_counts
        else:
            print("Invalid choices. Please enter valid counts.")
            return select_categories(existing_data)
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return select_categories(existing_data)

def select_random_activities(existing_data, selected_categories, selected_counts):
    if not existing_data:
        return None

    selected_activities = []

    for category, count in zip(selected_categories, selected_counts):
        category_data = next((data for data in existing_data if data["category"] == category), None)
        if category_data:
            activities = category_data.get("activities", [])
            if activities:
                # Shuffle the activities to ensure randomness
                random.shuffle(activities)
                # Select the specified count of activities from the category
                selected_activities.extend(activities[:count])

    if selected_activities:
        return selected_activities
    else:
        print("No activities found in the selected categories.")
        return None

def main():
    filename = r"pathtojson\activities.json"
    existing_data = load_existing_data(filename)

    if existing_data:
        selected_categories, selected_counts = select_categories(existing_data)

        if selected_categories:
            random_activities = select_random_activities(existing_data, selected_categories, selected_counts)

            if random_activities:
                print("\nRandomly selected activities:")
                for activity in random_activities:
                    category = activity.get('category', 'N/A')  # Handle missing 'category' key
                    print(f"\nCategory: {category}")
                    print(f"Name: {activity.get('name', 'N/A')}")
                    print(f"Time: {activity.get('time', 'N/A')}")
                    print(f"Description: {activity.get('description', 'N/A')}")
            else:
                print("No activities found in the selected categories.")
    else:
        print("Exiting program.")

if __name__ == "__main__":
    main()
