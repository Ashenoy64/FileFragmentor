# File Fragmentor

File Fragmentor is a Python tool that allows you to fragment large files into smaller chunks, making it easier to store and manage them, especially when dealing with cloud services that have restrictions on file size. Additionally, the tool provides a user-friendly tkinter-based UI to interactively fragment and merge files.

## Features

- Fragment large files into smaller chunks for easy storage and management.
- Merge fragmented files back into the original file.

## How to Use

### Prerequisites

- Python installed on your system.

### Installation

1. Clone the project from GitHub:

   ```bash
   git clone https://github.com/Ashenoy64/FileFragmentor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FileFragmentor
   ```

### Fragmenting and Merging via Command Line

1. Import the `FileFragmentor` class from `fragmentor.py` into your Python script.

2. Instantiate the `FileFragmentor` class.

3. To fragment a file, call the `fragment` method and pass the `File_path` argument along with the desired fragment size (default is 20 MB).

   ```python
   from fragmentor import FileFragmentor

   # Instantiate the class
   Object = FileFragmentor()

   # Fragment the file
   Object.fragment(File_path="path/to/your/file", size=20)
   ```

   This will create a folder containing fragments of the original file, with each fragment being of the specified size (in MB).

4. To merge the fragmented files back into the original file, call the `merge` method and provide the directory path where the fragments are located.

   ```python
   # Merge the fragments
   Object.merge(dirPath="path/to/your/fragment/folder")
   ```

   The fragmented files will be merged back into the original file.

### Using the Tkinter UI

1. Run the Python app to access the tkinter-based UI.

   ```bash
   python app.py
   ```

2. In the UI, enter the fragment size (in MB) and the file path you want to fragment.

3. Click the "Fragment" button to fragment the file. The fragmented files will be saved in a folder.

4. To merge the fragmented files back into the original file, enter the directory path where the fragments are located.

5. Click the "Merge" button to merge the fragmented files back into the original file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Note

File Fragmentor is a useful tool when dealing with large files and cloud storage limitations. Feel free to use it and make adjustments to suit your specific needs. If you have any questions or feedback, please don't hesitate to reach out. Happy fragmenting! 📁📦