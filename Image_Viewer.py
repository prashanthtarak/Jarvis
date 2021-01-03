from PIL import Image
import os
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.withdraw()

save_path = askdirectory(parent=root, initialdir=f"D:/", title="Please Select A Directory")


class MyApp():
    def showing(self):
        list_of_files = []
        for root, folders, files in os.walk(save_path):
            for file in files:
                
                if file.endswith('.jpg')| file.endswith('.JPG'):
                    list_of_files.append(file)

        print(list_of_files)
        print("Pls Enter A Number")
        number = input()
        
        img = Image.open(f'{save_path}/{list_of_files[int(number)-1]}')
        img.show()


MyApp().showing()