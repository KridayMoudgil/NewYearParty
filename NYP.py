import datetime
import pyttsx3
import customtkinter
import random

root = customtkinter.CTk()
root.attributes('-alpha', 0.4)
root.geometry("800x400")
root.title("New Year Party")

def start_disco():
    colors = ['white', 'blue', 'black', 'green', 'red', 'purple']
    bgcol = random.choice(colors)
    root.configure(fg_color=bgcol)
    root.after(500, start_disco)


def check_party_time():
    now = datetime.datetime.now().replace(microsecond=0)
    label_time.configure(text=now)

    if now == target_time:
        start_disco()
        engine.say("Party time")
        engine.runAndWait()
        start_disco()
    else:
        root.after(1000, check_party_time)




engine = pyttsx3.init()

target_time = datetime.datetime(2025, 1, 1, 00, 00, 00,0)


label = customtkinter.CTkLabel(root, text="New Year Party", font=("Helvetica", 35, "bold"))
label.pack(pady=20)

label_time = customtkinter.CTkLabel(root, text="Current Time: Updating...", font=("Helvetica", 22))
label_time.pack(pady=10)

btn = customtkinter.CTkButton(root, text="Party On", command=check_party_time)  # Pass the function reference
btn.pack(pady=10)




root.mainloop()
