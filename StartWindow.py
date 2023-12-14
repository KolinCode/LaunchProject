import tkinter as tk

def main():
    
    root = tk.Tk()


    image = tk.PhotoImage(file="C:\\Users\\kolin\\Downloads\\1678092179_gas-kvas-com-p-fon-kr.jpg")


    root.geometry(f"{image.width()}x{image.height()}")
    canvas = tk.Canvas(root, width=image.width(), height=image.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    canvas.pack()


    root.mainloop()

if __name__ == "__main__":
    main()
