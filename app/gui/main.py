import tkinter as tk
# import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)

canvas.grid(columnspan=3)

# frame_a = tk.Frame()
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()

# frame_b = tk.Frame()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()

# # Swap the order of `frame_a` and `frame_b`
# frame_b.pack()
# frame_a.pack()

root.mainloop()