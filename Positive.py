import tkinter as tk
import random

def flash_reset():
    """Resets the background to the standard color."""
    root.configure(bg="SystemButtonFace")
    label.configure(bg="SystemButtonFace")

def show_message():
    messages = [
        "Stay positive",
        "Do not take anything at work personally",
        "Focus on the good",
        "If there are two ways to take something, take it the positive way",
        "Your hard work will pay off",
        "Take a deep breath; you've got this",
        "Progress over perfection",
        "View challenges as opportunities to improve, not as personal failures",
        "Every setback is just setup for a comeback",
        "Focus on what is already going well",
        "Separate intent from impact",
        "Not everything is meant to hurt",
        "Control the controllables",
        "Be the best I can be within the parameters of my own role",
        "Don't own what's not yours",
        "Hard work is what brings good things",
        "When things are difficult, keep going",
        "Don't stop, you're almost there",
        "Be kind to yourself",
        "Diamonds are nothing more than chunks of coal that stuck to their jobs",
        "Start your day with gratitude",
        "You've overcome challenges before",
        "Set boundaries to protect your energy",
        "Celebrate small wins and contributions",
        "You don't have to be perfect to be amazing"
    ]
    
    # Update the text
    label.config(text=random.choice(messages))
    
    # Trigger the "Flash" (Yellow-Gold color)
    root.configure(bg="#FFD700")
    label.configure(bg="#FFD700")
    
    # Reset the color after 500 milliseconds (half a second)
    root.after(500, flash_reset)
    
    # Schedule the next message (30 to 60 mins)
    schedule_next_update()

def schedule_next_update():
    # 30 mins (1,800,000 ms) to 60 mins (3,600,000 ms)
    wait_time = random.randint(1800000, 3600000)
    root.after(wait_time, show_message)

# Setup the main window
root = tk.Tk()
root.title("Auto-Positivity")
root.geometry("400x200")
root.configure(padx=20, pady=20)

# Keep window on top
root.attributes('-topmost', True)

label = tk.Label(
    root, 
    text="App started! Waiting for your first dose of positivity...", 
    wraplength=350, 
    font=("Arial", 12, "bold italic"),
    pady=40
)
label.pack(expand=True, fill='both')

# Start the cycle
show_message()

root.mainloop()
