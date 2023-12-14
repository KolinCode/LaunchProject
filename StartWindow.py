import tkinter as tk

def main():
    # Создаем главное окно приложения
    root = tk.Tk()

    # Загружаем изображение с диска
    image = tk.PhotoImage(file="C:\\Users\\kolin\\Downloads\\1678092179_gas-kvas-com-p-fon-kr.jpg")

    # Устанавливаем изображение в качестве фона окна
    root.geometry(f"{image.width()}x{image.height()}")
    canvas = tk.Canvas(root, width=image.width(), height=image.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    canvas.pack()

    # Запускаем основной цикл приложения
    root.mainloop()

if __name__ == "__main__":
    main()
