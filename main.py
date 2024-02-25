from cryptography.fernet import Fernet

from tkinter import Tk, filedialog, Button, messagebox, Entry, Label
import tkinter as tk

print("This Project was made for RowdyHacks 2024 by Team Coderunner")

# Print program logo
print("\033[95m" + """
░█████╗░░█████╗░██████╗░███████╗██████╗░██╗░░░██╗███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░██║████╗░██║████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝██║░░░██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗██║░░░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║╚██████╔╝██║░╚███║██║░╚███║███████╗██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
""" + "\033[0m")


def create_key():
    key = Fernet.generate_key()

    with open("mykey.key", "wb") as mykey:
        mykey.write(key)

def select_file():
    """
    Select a file.
    """
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, 'end')
    file_path_entry.insert('end', file_path)


def encrypt_file():
    file_path = file_path_entry.get()

    if not file_path:
        messagebox.showerror("Error", "Please select a valid file.")
        return

    with open(file_path, 'rb') as original_file:
        original = original_file.read()

    with open("mykey.key", "rb") as mykey:
        key = mykey.read()

    print(key)

    f = Fernet(key)

    encrypted = f.encrypt(original)

    destination_file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if not destination_file_path:
        return

    with open(destination_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    messagebox.showinfo("Success", "File encrypted and saved successfully.")


def decrypt_file():
    file_path = file_path_entry.get()

    if not file_path:
        messagebox.showerror("Error", "Please select a valid file.")
        return

    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    with open("mykey.key", "rb") as mykey:
        key = mykey.read()

    print(key)

    f = Fernet(key)

    decrypted = f.decrypt(encrypted)

    destination_file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*")]
    )

    if not destination_file_path:
        return

    with open(destination_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    messagebox.showinfo("Success", "File decrypted and saved successfully.")


def change_button_color(button, index=0):
    # idk this just looks cool lmao
    """
    Change the color of the given button to a random color and apply a smooth rainbow effect to the lettering.
    """
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    random_color = colors[index % len(colors)]
    button.configure(fg=random_color)
    button.configure(font=("Arial", 15, "bold italic underline"))
    button.after(1000, lambda: change_button_color(button, index + 1))


# Creates the main GUI
root = tk.Tk()
root.title("Coderunner Encryptor")  # The Title of the GUI

# Create a label for the program name
#label = tk.Label(root, text="Welcome to CodeRunner Encryptor!", font=("Arial", 15))
#label.pack(pady=10)

# Create a label and entry for file path
#file_path_label = Label(root, text="File:")
#file_path_label.pack()
file_path_entry = Entry(root)
file_path_entry.pack()

# Create a button to select file
select_file_button = Button(root, text="Select File", command=select_file, activebackground="green", bd=1,
                            relief="solid")
select_file_button.pack()

# Create a button to create a key
create_key_button = Button(root, text="Create Key", command=create_key, activebackground="blue", bd=1, relief="solid")
create_key_button.pack()

# Create a button to encrypt a file
encrypt_button = Button(root, text="Encrypt File", command=encrypt_file, activebackground="blue", bd=1, relief="solid")
encrypt_button.pack()

# Create a button to decrypt a file
decrypt_button = Button(root, text="Decrypt File", command=decrypt_file, activebackground="blue", bd=1, relief="solid")
decrypt_button.pack()

# Change color of the buttons =)
change_button_color(select_file_button)
change_button_color(create_key_button)
change_button_color(encrypt_button)
change_button_color(decrypt_button)

# Run the main loops
root.mainloop()
if __name__ == "__main__":
    root.mainloop()
