import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("24-Hour Digital Clock")

# Set up the clock label with a large font
clock_label = tk.Label(root, font=("Comic Sans MS", 48), background="red", foreground="blue")
clock_label.pack(anchor="center")

# Function to update the time on the clock
def update_clock():
    # Get the current time in 24-hour format
    current_time = strftime("%H:%M:%S")
    # Display the current time in the label
    clock_label.config(text=current_time)
    # Schedule the function to be called again after 1000 ms (1 second)
    clock_label.after(1000, update_clock)

# Start the clock
update_clock()

# Run the application
root.mainloop()