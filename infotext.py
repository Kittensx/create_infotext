import os
import argparse
import yaml


class InfoTextManager:
    def __init__(self, config_path="infotext_config.yaml"):
        self.config = {}
        self.IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        if config_path:
            self.load_config(config_path)
    def scan_folder_for_images(self, folder_path):
        """
        Scans the given folder for image files and creates corresponding text files if they don't exist.
        """
        for file_name in os.listdir(folder_path):
            print(f"Scanning folder: {folder_path}")
            if os.path.splitext(file_name)[1].lower() in self.IMAGE_EXTENSIONS:
                base_name = os.path.splitext(file_name)[0]
                text_file_path = os.path.join(folder_path, base_name + '.txt')

                if not os.path.exists(text_file_path):
                    print(f"Creating text file for: {file_name}")
                    with open(text_file_path, 'w') as text_file:
                        text_file.write(base_name + '\n')  # Writes the base name of the image into the .txt file
    def load_config(self, config_path):
        """Loads the configuration from a YAML file."""
        with open(config_path, 'r') as config_file:
            self.config = yaml.safe_load(config_file)

    def process(self, folder_path=None, user_list=None):
        """
        Executes the main processing flow: scan folder and update text files.
        Folder path and user list can come from the config or parameters.
        """
        folder_path = folder_path or self.config.get('folder_path', '.')
        user_list = user_list or self.config.get('user_list', [])

        if isinstance(user_list, str):
            user_list = [item.strip() for item in user_list.split(',')]

        self.scan_folder_for_images(folder_path)
        self.update_text_files_with_list(folder_path, user_list)
        
    def update_text_files_with_list(self, folder_path, user_list=None):
        """
        Updates all text files in the folder with the values from the user-defined list.
        Writes the entire list as a comma-separated string.
        """
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                text_file_path = os.path.join(folder_path, file_name)
                print(f"Updating {file_name} with list values.")
                
                with open(text_file_path, 'w') as text_file:
                    # Write the list as a comma-separated string on the first line
                    text_file.write(','.join(user_list) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage infotext files for images.")

    parser.add_argument('--config', help="Path to the configuration YAML file.")
    parser.add_argument('--folder', help="Folder to scan for images.")
    parser.add_argument('--user_list', help="Comma-separated list of values to add to text files.")

    args = parser.parse_args()

    manager = InfoTextManager(config_path=args.config) if args.config else InfoTextManager()

    folder_path = args.folder
    user_list = args.user_list

    if user_list:
        user_list = [item.strip() for item in user_list.split(',')]

    manager.process(folder_path=folder_path, user_list=user_list)
