import os
import shutil
from tkinter import Tk, Label, Entry, Button, Text, END, filedialog

class FileExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("File Extractor")
        master.geometry("600x400")
        master.configure(bg="#333")

        # Output directory for extracted files
        self.output_directory = "extracted_files"
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        # GUI Components
        Label(master, text="Enter file extensions (comma-separated, e.g., jpg,mp4,png):", fg="white", bg="#333").pack(pady=5)
        self.entry_extensions = Entry(master, width=50)
        self.entry_extensions.pack(pady=5)

        Button(master, text="Select Source Directory and Extract Files", command=self.extract_files).pack(pady=10)

        self.text_log = Text(master, height=15, width=75, bg="#222", fg="white")
        self.text_log.pack(pady=10)

    def extract_files(self):
        file_extensions = self.entry_extensions.get().split(",")
        file_extensions = [ext.strip().lower() for ext in file_extensions if ext.strip()]
        src_dir = filedialog.askdirectory(title="Select Source Directory")
        
        if not src_dir:
            self.log("Operation cancelled or no directory selected.")
            return
        
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in file_extensions):
                    src_file_path = os.path.join(root, file)
                    shutil.copy(src_file_path, self.output_directory)
                    self.log(f"Copied: {src_file_path}")
                else:
                    self.log(f"Skipped (unsupported): {os.path.join(root, file)}")

    def log(self, message):
        self.text_log.insert(END, f"{message}\n")
        self.text_log.see(END)

if __name__ == "__main__":
    root = Tk()
    app = FileExtractorApp(root)
    root.mainloop()
