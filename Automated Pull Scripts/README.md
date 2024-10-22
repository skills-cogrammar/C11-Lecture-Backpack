Below are the commands for Linux (Same for MacOS). You can save this as a shell script (`.sh` file):

```bash
#!/bin/bash
# Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/skills-cogrammar/C8-Lecture-Backpack.git

# Changing directory to the cloned repository
cd C8-Lecture-Backpack

# Adding the specific folders to sparse checkout
git sparse-checkout add "Software Engineering (SE)"
git sparse-checkout add "StarterPack"
```

### Instructions:
1. Copy the above code into a text editor.
2. Save the file with a `.sh` extension, for example, `clone_sparse_checkout.sh`.
3. Open a terminal and navigate to the directory where the script is saved.
4. Make the script executable by running: 
   ```bash
   chmod +x clone_sparse_checkout.sh
   ```
5. Run the script by executing:
   ```bash
   ./clone_sparse_checkout.sh
   ```

This script will clone the repository with a sparse checkout and include both the `Software Engineering (SE)` and `StarterPack` directories.