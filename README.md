# File Organization Tool
A Python desktop application with a graphical user interface (GUI) that helps users automatically organize files based on their extensions. 

## Key Features:
1. Intuitive GUI built with tkinter for easy file management
2. Ability to create custom folder mappings for different file extensions
3. Multiple extensions can be mapped to a single folder (e.g., "images" folder for .jpg, .png, .gif)
4. Recursive directory processing - can organize files in nested subfolders
5. Smart duplicate file handling - automatically renames files to prevent overwrites
6. Folder structure preview before execution
7. Option to toggle subfolder processing

## Technical Implementation:
- Built using Python 3
- GUI implemented with tkinter library
- File operations handled through os and shutil modules
- Tree-view component for visualizing folder-extension mappings
- Error handling for common file operation issues

## Use Case:
This tool is particularly useful for:
- Cleaning up download folders
- Organizing large collections of mixed files
- Automating file management tasks
- Maintaining consistent file organization across projects
