# import modules
import tkinter as tk
from tkinter import ttk

import scripts


def start():

    print("starting")
    scripts.start(spinbox.get(), delay_sb.get())


# window setup
root = tk.Tk()
root.title("auto clicker v2.1")
root.geometry("400x300")
root.resizable(False, False)

# label
title_label = ttk.Label(master=root, text="Setup")


# interval input field
input_frame = ttk.Frame(master=root)
input_instr = ttk.Label(master=input_frame, text="Interval (sec)")

# setting default value for spinbox
i_default_val = tk.StringVar(input_frame)
i_default_val.set("0.05")

spinbox = ttk.Spinbox(
    master=input_frame,
    from_=0.05,
    to=float("inf"),
    increment=0.01,
    width=4,
    textvariable=i_default_val
)


input_instr.pack(side="left")
spinbox.pack(side="right")

# info
info = ttk.Label(master=root, text="!!Press esc to stop!!", foreground="red")


# start delay field

delay_frame = ttk.Frame(master=root)
delay_text = ttk.Label(master=delay_frame, text="Delay (sec)")

# setting default value
d_default_val = tk.StringVar(delay_frame)
d_default_val.set("3")

delay_sb = ttk.Spinbox(
    master=delay_frame,
    from_=0,
    to=float("inf"),
    textvariable=d_default_val,
    width=4
)

delay_text.pack(side="left")
delay_sb.pack(side="right")


# button
start_btn = ttk.Button(master=root, text="Start", command=start)


# layout
title_label.grid(column=0, row=0, sticky="w")

input_frame.grid(column=0, row=1, sticky="w", padx=20, pady=10)

delay_frame.grid(column=0, row=2, stick="w", padx=20)

info.grid(column=0, row=3, sticky="w", pady=50)

start_btn.grid(column=0, row=4, sticky="SE", pady=45, padx=295)


# mainloop
root.mainloop()
