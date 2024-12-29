# InfoText Manager
https://github.com/Kittensx/create_infotext

## Overview
The **InfoText Manager** project simplifies the process of managing text files for images in a specified folder. It creates `.txt` files for images that lack them and updates existing `.txt` files with user-defined metadata. The script uses a configuration-driven approach with support for YAML configuration files and virtual environments for dependency management.

---

## Features
- Automatically scans a folder for image files (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`) and generates `.txt` files if missing.
- Updates `.txt` files with a user-provided list of values.
- Reads settings such as folder path and user list from a YAML configuration file.
- Supports command-line arguments for custom configurations.
- Virtual environment management for isolated dependency installation.

---

## Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`:
  - `pyyaml`

---

## Installation

### 1. Set Up the Virtual Environment
Run the `install_infotext.py` script to create a virtual environment and install dependencies:

```bash
python install_infotext.py
```

### 2. Dependencies
Dependencies are listed in `requirements.txt` and include:

```text
pyyaml
```

---

## Configuration

### Configuration File (`infotext_config.yaml`)
The script uses a YAML configuration file to define settings such as the folder to process and the user list for metadata.

#### Example Configuration
```yaml
folder_path: 'D:\\software_projects\\infotext\\test_folder\\beach'
user_list: beach, sunset
```

- **`folder_path`**: The folder containing images to scan.
- **`user_list`**: A comma-separated list of metadata values to update in the `.txt` files.

---

## Usage

### Command-line Arguments
Run the `infotext.py` script with the following options:

```bash
python infotext.py --config infotext_config.yaml
```

- **`--config`**: Path to the YAML configuration file (default: `infotext_config.yaml`).
- **`--folder`**: Specify the folder to scan for images (overrides `folder_path` in the config file).
- **`--user_list`**: Provide a comma-separated list of metadata values (overrides `user_list` in the config file).

#### Example
```bash
python infotext.py --folder "D:\\images" --user_list "sunrise, ocean, waves"
```

---

## Workflow

### 1. Scanning for Images
The script identifies images with the following extensions:
- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

For each image without a `.txt` file, it creates one with the same name as the image.

### 2. Updating `.txt` Files
All `.txt` files in the specified folder are updated with the user-defined metadata list, written as a comma-separated string.

---

## File Structure

- **`infotext.py`**: Main script for scanning and updating text files.
- **`infotext_config.yaml`**: YAML file for configuration settings.
- **`requirements.txt`**: Lists Python dependencies.
- **`install_infotext.py`**: Script for setting up the virtual environment and installing dependencies.

---

## Development

### Extending Functionality
You can extend the functionality by:
- Adding support for additional file types.
- Customizing the format of `.txt` file content.

### Debugging
Enable debug prints by modifying the `scan_folder_for_images` and `process` methods in `infotext.py`.

---

## Troubleshooting

### Common Issues
1. **No `.txt` files are created**:
   - Ensure the folder contains valid image files.
   - Verify `folder_path` is correct in `infotext_config.yaml` or passed via `--folder`.

2. **Missing dependencies**:
   - Run `pip install -r requirements.txt` in the virtual environment.

---

## License
This project is licensed under the MIT License.

---

## Contribution
Contributions are welcome! Please submit pull requests or raise issues on GitHub.

