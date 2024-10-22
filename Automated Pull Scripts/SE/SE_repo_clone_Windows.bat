@echo off
REM Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/skills-cogrammar/C8-Lecture-Backpack.git

REM Changing directory to the cloned repository
cd C8-Lecture-Backpack

REM Adding the specific folders to sparse checkout
git sparse-checkout add "Software Engineering (SE)"
git sparse-checkout add "StarterPack"

@echo on
