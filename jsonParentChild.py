import json

def add_child(parent, child_name):
    child = {"name": child_name, "children": []}
    parent["children"].append(child)
    return child

def main():
    # Load existing JSON data from file
    filename = "tree.json"
    try:
        with open(filename, 'r') as json_file:
            tree_data = json.load(json_file)
    except FileNotFoundError:
        tree_data = {"name": "Root", "children": []}

    # Interactive process to add nodes
    current_node = tree_data
    while True:
        print(f"\nCurrent Node: {current_node['name']}")
        print("1. Add Child Node")
        print("2. Move to Parent Node")
        print("3. Print JSON")
        print("4. Save and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            child_name = input("Enter the name for the child node: ")
            add_child(current_node, child_name)
            print(f"Child node '{child_name}' added.")
        elif choice == "2":
            if current_node != tree_data:
                # Move to the parent node if not already at the root
                current_node = tree_data
                print("Moved to the parent node.")
            else:
                print("Already at the root node.")
        elif choice == "3":
            print(json.dumps(tree_data, indent=2))
        elif choice == "4":
            with open(filename, 'w') as json_file:
                json.dump(tree_data, json_file, indent=2)
            print("Tree data saved to 'tree.json'. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
