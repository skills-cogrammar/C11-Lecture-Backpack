## Getting Started with Node.js

Node.js is a powerful JavaScript runtime built on Chrome's V8 JavaScript engine. Follow these steps to set up Node.js and run your first program:

### 1. **Install Node.js**

**Windows:**
1. Go to the [official Node.js website](https://nodejs.org/).
2. Download the Windows installer (choose the LTS version for stability).
3. Run the installer and follow the on-screen instructions. Make sure the option to add Node.js to your PATH is selected.
4. Complete the installation.

**macOS:**
1. You can install Node.js using the official installer from the [Node.js website](https://nodejs.org/) or through Homebrew.
   - **Using the installer**: Download the macOS installer and follow the instructions.
   - **Using Homebrew**: Open Terminal and run:
     ```bash
     brew install node
     ```

**Linux:**
1. Open Terminal.
2. Install Node.js using your package manager. For example, on Ubuntu, run:
   ```bash
   sudo apt-get update
   sudo apt-get install nodejs npm
   ```

### 2. **Verify Node.js Installation**

To check if Node.js is installed correctly, open your terminal or command prompt and type:
   ```bash
   node --version
   ```
   You should see the Node.js version number displayed.

### 3. **Open a Text Editor**

To write your Node.js code, you’ll need a text editor. You can use any text editor like Notepad, VSCode, Sublime Text, etc. For this guide, we'll use VSCode.

1. Open your text editor.
2. Create a new file and save it as `app.js`.

### 4. **Write Your First Node.js Program**

In your `app.js` file, type the following code to print "Hello, World!" to the terminal:

```javascript
console.log("Hello, World!");
```

Save the file.

### 5. **Run Your Node.js Program**

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved `app.js`. For example:
   ```bash
   cd path/to/your/directory
   ```
3. Run the program using Node.js by typing:
   ```bash
   node app.js
   ```
   You should see:
   ```bash
   Hello, World!
   ```

---

### Known Issues and Troubleshooting

#### **1. Node Not Recognized as a Command**
- **Issue**: Terminal or command prompt says Node is not recognized.
  - **Solution**: Ensure Node.js is added to your system’s PATH. If you missed this step during installation, you may need to reinstall Node.js and verify the PATH settings.

#### **2. Incorrect Node Version**
- **Issue**: Command `node --version` does not show the expected version.
  - **Solution**: Ensure you are using the correct command. If you have multiple versions of Node.js installed, you might need to update your PATH or use a version manager like `nvm` (Node Version Manager).

#### **3. Error Running `console.log("Hello, World!");`**
- **Issue**: SyntaxError or other errors when running the code.
  - **Solution**: Ensure you are typing the code correctly in the `app.js` file and that you are in the correct directory when running the command. Check for any typos or syntax errors.

#### **4. Issues with Installation**
- **Issue**: Installation errors or problems with running Node.js.
  - **Solution**: Refer to the [Node.js documentation](https://nodejs.org/en/docs/) or visit the Node.js [community forums](https://github.com/nodejs/help) for support. Ensure you are downloading Node.js from the official website.