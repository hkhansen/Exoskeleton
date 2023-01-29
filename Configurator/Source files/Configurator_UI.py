import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import configurator as config

# Root window
root = tk.Tk()
root.title('Exoskeleton configurator')

# Geometry of the window
window_width = 400
window_height = 200

# Settings for the measurement guide window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

# Configure the grid
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

# Set up string variables for measurement inputs
wrist_width = tk.StringVar()
biceps_width = tk.StringVar()
under_length = tk.StringVar()
upper_length = tk.StringVar()

# Load arm picture for the guide
img = Image.open("guide.jpg")
resized_image= img.resize((583,827), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

def info():
	info = tk.Toplevel(root)
	info.title('Files generated')
	info.geometry(f'400x50+{center_x}+{center_y+50}')
	info.resizable(False, False)
	message = tk.Label(info, text = "STL files have been generated in folder!", font =("Helvetica", 16))
	message.pack(ipadx=10, ipady=10)

def generate_exo():
    # Convert input strings to floats
	wrist = float(wrist_width.get())
	under = float(under_length.get())
	biceps = float(biceps_width.get())
	upper = float(upper_length.get())
    # Run the generator functions with each of the measurements
	config.wrist_mount_generator(wrist)
	config.biceps_mount_generator(biceps)
	config.biceps_side_beam_generator(upper)
	config.lower_arm_beam_generator(under)
    # Display info pop-up
	info()

def guide():
    guide = tk.Toplevel(root)
    guide.title('Measurement guide')
    guide.geometry(f'583x827+{center_x+500}+{center_y-250}')
    label1 = tk.Label(guide, image=new_image)
    label1.image = new_image
    label1.place(x=5, y=5)

# Create the input fields for the 4 parameters
wrist_label = ttk.Label(root, text = "Wrist width in mm:")
wrist_label.grid(column=0, row=0, sticky=tk.W, ipadx=5, ipady=5)
wrist_entry = ttk.Entry(root, textvariable=wrist_width)
wrist_entry.grid(column=1, row=0, sticky=tk.W, ipadx=5, ipady=5)

under_label = ttk.Label(root, text = "Lower-arm length in mm:")
under_label.grid(column=0, row=1, sticky=tk.W, ipadx=5, ipady=5)
under_entry = ttk.Entry(root, textvariable=under_length)
under_entry.grid(column=1, row=1, sticky=tk.W, ipadx=5, ipady=5)

biceps_label = ttk.Label(root, text = "Biceps width in mm:")
biceps_label.grid(column=0, row=2, sticky=tk.W, ipadx=5, ipady=5)
biceps_entry = ttk.Entry(root, textvariable=biceps_width)
biceps_entry.grid(column=1, row=2, sticky=tk.W, ipadx=5, ipady=5)

upper_label = ttk.Label(root, text = "Upper arm length in mm:")
upper_label.grid(column=0, row=3, sticky=tk.W, ipadx=5, ipady=5)
upper_entry = ttk.Entry(root, textvariable=upper_length)
upper_entry.grid(column=1, row=3, sticky=tk.W, ipadx=5, ipady=5)

# Add buttons for generating files, opening the measurement guide, and exiting the program
button = ttk.Button(root, text="Generate files", command=generate_exo)
button.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

guide_button = ttk.Button(root, text="Measurement guide", command=guide)
guide_button.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())
exit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

root.mainloop()