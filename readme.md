```markdown
# CR2 to JPG Converter

The "CR2 to JPG Converter" is a Python tkinter application that simplifies the process of converting Canon CR2 image files to JPG format. This user-friendly app provides an intuitive interface for easy conversion of multiple files while allowing you to choose both the source and destination directories.

## Prerequisites

Before using the app, ensure that you have the necessary Python libraries installed. You can install them by running:

```bash
pip install -r requirements.txt
```

## Getting Started

1. **Clone the Repository:** Start by cloning this repository to your local machine or download the source code as a ZIP file and extract it.

2. **Install Dependencies:** Navigate to the project directory and install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

3. **Launch the App:** Run the following command to start the app:

```bash
python cr2_to_jpg_converter.py
```

## Using the App

1. **Select Input Directory:**
   - Click the "Select" button next to "Input Directory" to choose the folder containing your CR2 files.

2. **Select Output Directory:**
   - Click the "Select" button next to "Output Directory" to specify where the converted JPG files will be saved.

3. **Convert:**
   - After selecting both input and output directories, click the "Convert" button to initiate the conversion process. The app will convert all CR2 files in the input directory to JPG format and display the progress.

4. **Progress Bar:**
   - A progress bar shows the conversion progress, allowing you to monitor the status of the conversion.

5. **Status Messages:**
   - The app provides status messages for each file conversion, indicating whether the conversion was successful or if there were any errors.

## Notes

- This is a basic example, and you can expand upon it to add more features and error handling.
- The app runs in a separate thread to prevent freezing the GUI during batch conversions.
- Ensure you have the necessary permissions to read from the input directory and write to the output directory.
