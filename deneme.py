import tkinter as tk
import subprocess


def os_com():
    print("kaç dakika %s" % e1.get())
    subprocess.call(["shutdown", "-s", "-t", e1.get()*60])



root = tk.Tk()
root.title("Zamanlı Kapatma")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

instructions = tk.Label(root, text="Bilgisayarı Zamanlı Kapatma")
instructions.grid(column=1, row=0)

tk.Label(root,
         text="Kaç dakika").grid(row=1)

e1 = tk.Entry(root)
e1.grid(row=1, column=1)

tk.Button(root,
          text='Shutdown', command=os_com).grid(row=3,
                                                column=1,
                                                sticky=tk.W
                                                )

root.mainloop()
