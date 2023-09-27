import os

parent_folder = '/media/cameron/76E8-CACF'  # Replace this with the path to your parent folder

# Define a function to recursively count items in a folder and its subfolders
def count_items_in_folder(folder):
    count = 0
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path) or os.path.isdir(item_path):
            if os.path.isdir(item_path):
                count += count_items_in_folder(item_path)
            count += 1

    # Get the name of the current folder (relative to the parent folder)
    folder_name = os.path.relpath(folder, parent_folder)
    
    # Print the count for the current folder
    if count < 50:
        print(f'{folder_name}: {count}')

    return count

count_items_in_folder(parent_folder)
