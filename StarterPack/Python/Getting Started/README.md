## Getting Started with Python

Starting with Python is easy and straightforward. Follow these steps to set up Python and run your first program:

### 1. **Install Python**

**Windows:**
1. Download the Python installer from the [official Python website](https://www.python.org/downloads/).
2. Run the installer. **Important**: Check the box that says "Add Python to PATH" before clicking "Install Now."
3. Follow the on-screen instructions to complete the installation.

**macOS:**
1. Python is often pre-installed on macOS. You can check this by opening Terminal and typing:
   ```bash
   python3 --version
   ```
   If it’s not installed, you can download and install Python from the [official Python website](https://www.python.org/downloads/) or use Homebrew:
   ```bash
   brew install python
   ```

**Linux:**
1. Open Terminal.
2. Install Python using your package manager. For example, on Ubuntu, run:
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

### 2. **Verify Python Installation**

To check if Python is installed correctly, open your terminal or command prompt and type:
   ```bash
   python --version
   ```
   or for Python 3:
   ```bash
   python3 --version
   ```
   You should see the Python version number displayed.

### 3. **Open the Python Interpreter**

You can run Python directly from your terminal or command prompt. Type:
   ```bash
   python
   ```
   or for Python 3:
   ```bash
   python3
   ```
   This will start the Python interpreter, and you will see a prompt that looks like this:
   ```python
   >>>
   ```

### 4. **Write Your First Python Program**

In the Python interpreter, type the following command to print "Hello, World!" to the screen:
   ```python
   print("Hello, World!")
   ```
   Press `Enter`. You should see:
   ```python
   Hello, World!
   ```

### 5. **Exit the Python Interpreter**

To exit the Python interpreter, type:
   ```python
   exit()
   ```
   and press `Enter`, or use the shortcut `Ctrl + D` (on Linux/macOS) or `Ctrl + Z` followed by `Enter` (on Windows).

---

### Known Issues and Troubleshooting

#### **1. Python Not Recognized as a Command**
- **Issue**: Terminal or command prompt says Python is not recognized.
  - **Solution**: Make sure Python is added to your system’s PATH. If you missed this step during installation, you might need to reinstall Python and ensure the "Add Python to PATH" option is selected.

#### **2. Incorrect Python Version**
- **Issue**: Command `python` or `python3` doesn’t show the expected version.
  - **Solution**: Ensure you are using the correct command. On some systems, `python` might refer to Python 2.x, and `python3` to Python 3.x. Use `python3` if you need to work with Python 3.

#### **3. Error Running `print("Hello, World!")`**
- **Issue**: SyntaxError or other errors when running `print("Hello, World!")`.
  - **Solution**: Ensure you are typing the command correctly and that you are in the Python interpreter (`>>>` prompt). Check for any typos or syntax errors.

#### **4. Issues with Installation**
- **Issue**: Installation errors or problems with running Python.
  - **Solution**: Refer to the [Python documentation](https://docs.python.org/3/using/index.html) or visit the Python [community forums](https://www.python.org/community/forums/) for support. Ensure you are downloading Python from the official website.
