import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Organizer")
        self.master.geometry("700x500")

        self.source_folder = tk.StringVar()
        self.folder_extensions = {}
        self.process_subfolders = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # Source folder selection
        tk.Label(self.master, text="Select source folder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(self.master, textvariable=self.source_folder, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Browse", command=self.browse_source).grid(row=0, column=2, padx=5, pady=5)

        # Checkbox for processing subfolders
        tk.Checkbutton(self.master, text="Process subfolders", variable=self.process_subfolders).grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Treeview for folder-extension mapping
        self.tree = ttk.Treeview(self.master, columns=('Folder', 'Extensions'), show='headings')
        self.tree.heading('Folder', text='Folder')
        self.tree.heading('Extensions', text='Extensions')
        self.tree.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=2, column=3, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Entry fields for new folder-extension pair
        self.new_folder = tk.StringVar()
        self.new_extension = tk.StringVar()
        tk.Label(self.master, text="Folder:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.master, textvariable=self.new_folder, width=20).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        tk.Label(self.master, text="Extension:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.master, textvariable=self.new_extension, width=20).grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        tk.Button(self.master, text="Add/Update", command=self.add_update_extension).grid(row=3, column=2, rowspan=2, padx=5, pady=5)
        tk.Button(self.master, text="Remove Selected", command=self.remove_selected).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.master, text="Organize Files", command=self.organize_files).grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        # Configure grid weights
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def browse_source(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)

    def add_update_extension(self):
        folder = self.new_folder.get().strip()
        extension = self.new_extension.get().strip().lower()
        
        if not folder or not extension:
            messagebox.showerror("Error", "Both folder and extension must be specified.")
            return

        if folder in self.folder_extensions:
            if extension not in self.folder_extensions[folder]:
                self.folder_extensions[folder].append(extension)
        else:
            self.folder_extensions[folder] = [extension]

        self.update_treeview()
        self.new_folder.set("")
        self.new_extension.set("")

    def remove_selected(self):
        selected_item = self.tree.selection()
        if selected_item:
            folder = self.tree.item(selected_item)['values'][0]
            del self.folder_extensions[folder]
            self.update_treeview()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for folder, extensions in self.folder_extensions.items():
            self.tree.insert('', 'end', values=(folder, ', '.join(extensions)))

    def organize_files(self):
        source = self.source_folder.get()
        if not source:
            messagebox.showerror("Error", "Please select a source folder.")
            return

        self.process_directory(source)
        messagebox.showinfo("Success", "Files organized successfully!")

    def process_directory(self, directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                self.process_file(root, file)

            if not self.process_subfolders.get():
                break  # Stop after processing the top-level directory

    def process_file(self, root, file):
        source_path = os.path.join(root, file)
        file_extension = os.path.splitext(file)[1][1:].lower()

        for folder, extensions in self.folder_extensions.items():
            if file_extension in extensions:
                target_folder = os.path.join(self.source_folder.get(), folder)
                os.makedirs(target_folder, exist_ok=True)
                target_path = os.path.join(target_folder, file)

                # Handle duplicate filenames
                if os.path.exists(target_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(target_path):
                        new_filename = f"{base}_{counter}{extension}"
                        target_path = os.path.join(target_folder, new_filename)
                        counter += 1

                shutil.move(source_path, target_path)
                break  # Stop after moving the file to the first matching folder

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()
