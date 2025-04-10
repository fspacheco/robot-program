"""
Tool to visualize vectors

Fernando 2025
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Function to update the plot
def update_plot():
    global fig, ax, canvas
    try:
        # Get input values
        x1, y1 = float(entry_x1.get()), float(entry_y1.get())
        x2, y2 = float(entry_x2.get()), float(entry_y2.get())
        x3, y3 = float(entry_x3.get()), float(entry_y3.get())
        x4, y4 = float(entry_x4.get()), float(entry_y4.get())
        x5, y5 = float(entry_x5.get()), float(entry_y5.get())

        vectors = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5]])
        cb_colors = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#F0E442']
        labels = ['$\\vec{a}$', '$\\vec{b}$', '$\\vec{c}$', '$\\vec{d}$',  '$\\vec{e}$']

        # Destroy previous figure
        for widget in frame.winfo_children():
            widget.destroy()

        # Create new figure with the selected mode
        if plot_mode.get() == "polar":
            fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6))
            r = np.sqrt(vectors[:, 0]**2 + vectors[:, 1]**2)
            theta = np.arctan2(vectors[:, 1], vectors[:, 0])
            ax.quiver(theta, np.zeros_like(r), np.zeros_like(r), r, color=cb_colors, angles='xy', scale_units='xy', scale=1)
            for i in range(len(vectors)):
                ax.text(theta[i], r[i] + 0.3, labels[i], fontsize=12, color=cb_colors[i], fontweight='bold')
            ax.set_rticks(np.arange(0, np.max(r) + 1, 1))
            ax.set_thetagrids(np.arange(0, 360, 30))
            ax.set_ylim(0, np.max(r) + 1)
        else:
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.quiver([0] * len(vectors), [0] * len(vectors), vectors[:, 0], vectors[:, 1], color=cb_colors, angles='xy', scale_units='xy', scale=1)
            for i in range(len(vectors)):
                ax.text(vectors[i, 0], vectors[i, 1], labels[i], fontsize=12, color=cb_colors[i], fontweight='bold')
            ax.set_xlim(-6, 6)
            ax.set_ylim(-6, 6)
            ax.set_aspect('equal')
            ax.set_xticks(np.arange(-6, 6, 1))
            ax.set_yticks(np.arange(-6, 6, 1))            
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.grid(True)

        # Create new canvas
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(expand=True, fill='both')
        canvas.draw()
    except ValueError:
        print("Please enter valid numbers.")

# Create GUI window
root = tk.Tk()
root.title("Interactive Vector Plot")
root.geometry("600x600")  # Set initial window size

# Input fields
tk.Label(root, text="Vector A (x1, y1):").grid(row=0, column=0)
entry_x1 = tk.Entry(root, width=5)
entry_x1.grid(row=0, column=1)
entry_x1.insert(0, "2")
entry_y1 = tk.Entry(root, width=5)
entry_y1.grid(row=0, column=2)
entry_y1.insert(0, "3")

tk.Label(root, text="Vector B (x2, y2):").grid(row=1, column=0)
entry_x2 = tk.Entry(root, width=5)
entry_x2.grid(row=1, column=1)
entry_x2.insert(0, "-1")
entry_y2 = tk.Entry(root, width=5)
entry_y2.grid(row=1, column=2)
entry_y2.insert(0, "4")

tk.Label(root, text="Vector C (x3, y3):").grid(row=2, column=0)
entry_x3 = tk.Entry(root, width=5)
entry_x3.grid(row=2, column=1)
entry_x3.insert(0, "3")
entry_y3 = tk.Entry(root, width=5)
entry_y3.grid(row=2, column=2)
entry_y3.insert(0, "-2")

tk.Label(root, text="Vector D (x4, y4):").grid(row=3, column=0)
entry_x4 = tk.Entry(root, width=5)
entry_x4.grid(row=3, column=1)
entry_x4.insert(0, "-3")
entry_y4 = tk.Entry(root, width=5)
entry_y4.grid(row=3, column=2)
entry_y4.insert(0, "1")

tk.Label(root, text="Vector E (x5, y5):").grid(row=4, column=0)
entry_x5 = tk.Entry(root, width=5)
entry_x5.grid(row=4, column=1)
entry_x5.insert(0, "1")
entry_y5 = tk.Entry(root, width=5)
entry_y5.grid(row=4, column=2)
entry_y5.insert(0, "-4")

# Radio buttons for plot mode
plot_mode = tk.StringVar(value="cartesian")
tk.Radiobutton(root, text="Polar", variable=plot_mode, value="polar", command=update_plot).grid(row=5, column=0)
tk.Radiobutton(root, text="Cartesian", variable=plot_mode, value="cartesian", command=update_plot).grid(row=5, column=1)

# Button to update plot
btn_update = tk.Button(root, text="Update Plot", command=update_plot)
btn_update.grid(row=5, column=2)

# Frame to hold the plot
frame = tk.Frame(root)
frame.grid(row=6, column=0, columnspan=3, sticky="nsew")

# Configure resizing behavior
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Initialize plot
update_plot()

# Run Tkinter event loop
root.mainloop()
