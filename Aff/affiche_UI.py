from affiche_gen import *
import ctypes as ct
import tkinter as tk
import os

image: Image
text: str
text_input: tk.Entry   

image_preview:tk.Label
photo: ImageTk.PhotoImage

def loadsettings() -> tuple[int, int, bool]:
    try:
        if os.path.exists("./conf.ini"):
            with open("./conf.ini", "r") as file:
                settings = file.read().split(',')
                return (int(settings[0]), int(settings[1]), bool(settings[2]))
        else:
            with open("./conf.ini", "w") as file:
                file.write("50,35,True")
            return (50, 35, True)
    except Exception:
        return (50, 35, True)

settings: tuple[int, int, bool] = loadsettings()

def saveSettings():
    global settings
    with open("./conf.ini", "w") as file:
        file.write(str(settings[0]) + "," + str(settings[1]) + "," + str(settings[2]))


def preview_image():
    global image
    # Convert the image to PhotoImage
    photo = ImageTk.PhotoImage(image.resize((640,360)))
    try:
        image_preview.destroy()
    except Exception:
        pass
    # Create a label to display the image
    image_preview = tk.Label(window, image=photo)
    image_preview.image = photo
    image_preview.grid(row=1, column=0, padx=5, pady=5)
    image_preview.update()

    # Run the tkinter event loop

def switchSide(side_but: tk.Button):
    global settings, image, text
    if side_but.cget('text') == "Logo : Gauche":
        side_but.config(bg="#35a4ff", text="Logo : Droite")
        settings = (settings[0], settings[1], False)
        image = renderImage(imageList[0], text, settings_=settings)
    else:
        side_but.config(bg="#246055", text="Logo : Gauche")
        settings = (settings[0], settings[1], True)
        image = renderImage(imageList[0], text, settings_=settings)

    preview_image()

def resizeLogo(logo_size_slider: tk.Scale):
    global image, settings, text

    settings = (logo_size_slider.get(), settings[1], settings[2])
    image = renderImage(file=imageList[0], text=text, settings_=settings)
    preview_image()

def moveLogo(logo_position_slider: tk.Scale):
    global image, text, settings

    settings = (settings[0], logo_position_slider.get(), settings[2])
    image = renderImage(imageList[0], text, settings_=settings)
    preview_image()

def setting_tab(window:tk):
    global text_input, settings
    setting_tab = tk.Frame(window, width=200, height=200, bg="#202020")
    setting_tab.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    setting_tab.grid_columnconfigure(1, weight=1)

    # radiobutton and profile frame
    buts_and_infos = tk.Frame(setting_tab, bg="#202020")
    buts_and_infos.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    label_info = tk.Label(buts_and_infos, text="Mettre un '/' dans le titre force le retour à la ligne (si le text est trop long pour une ligne)", fg=('white') ,font=("Arial", 12, "bold"), bg="#202020")
    label_info.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    # text input frame
    text_input_frame = tk.Frame(setting_tab, bg="#202020")
    text_input_frame.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    text_input_frame.grid_columnconfigure(0, weight=1)
    # text input
    text_input = tk.Entry(text_input_frame, bg="white", fg="black", font=("Arial", 12, "bold"), border=1)
    text_input.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
    text_input.insert(0, text)

    # text input button
    text_input_button = tk.Button(text_input_frame, text="Valider", fg=('white') ,font=("Arial", 12, "bold"), bg="#b27300", command=lambda: applyText(text_input.get()))
    text_input_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    slider_and_button_frame = tk.Frame(setting_tab, bg="#202020")
    slider_and_button_frame.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    slider_and_button_frame.grid_columnconfigure((2, 1), weight=1)

    side_but = tk.Button(slider_and_button_frame, text="Logo : Gauche", fg=('white') ,font=("Arial", 12, "bold"), bg="#246055")
    side_but.grid(row=0, column=0, padx=5, pady=5)
    side_but.config(command=lambda: switchSide(side_but))
    # create save button
    save_button = tk.Button(slider_and_button_frame, text="Save", fg=('white') ,font=("Arial", 12, "bold"), bg="green", command= lambda : save_and_next(setting_tab))
    save_button.grid(row=0, column=3, padx=5, pady=5)

    # logo size slider
    logo_size_slider = tk.Scale(slider_and_button_frame, from_=10, to=150, orient=tk.HORIZONTAL, bg="#202020", fg="white", label="Logo taille")
    logo_size_slider.bind("<ButtonRelease-1>", lambda e : resizeLogo(logo_size_slider))
    logo_size_slider.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    logo_size_slider.set(settings[0])

    # logo position slider
    logo_position_slider = tk.Scale(slider_and_button_frame, from_=0, to=100, orient=tk.HORIZONTAL, bg="#202020", fg="white", label="Logo distance bord")
    logo_position_slider.bind("<ButtonRelease-1>", lambda e : moveLogo(logo_position_slider))
    logo_position_slider.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    logo_position_slider.set(settings[1])


def applyText(text_:str):
    global image, text
    text = text_.upper()
    image = renderImage(imageList[0], text, settings_=settings)
    preview_image()

def save_and_next(frame: tk.Frame):
    global image, text, text_input
    saveImage(image, text)
    print(imageList[0])
    os.rename(imageList[0], "./raw/" + imageList[0])
    if len(imageList) - 1 > 0:
        imageList.remove(imageList[0])
        print(imageList[0])
        text = imageList[0].upper().replace('.PNG', '')
        text_input.delete(0, tk.END)
        text_input.insert(0, text)
        image = renderImage(imageList[0], text, settings_=settings)
        preview_image()
    else:
        image = Image.open(resource_path('./assets/fini.png'))
        frame.destroy()
        preview_image()


def initWindow():
    window = tk.Tk()
    window.title("Affiche Film gen")
    window.iconbitmap(resource_path("./assets/F9.ico"))
    window.resizable(False, False)
    window.configure(bg="#202020")
    # window.grid_columnconfigure(0, weight=1)
    dark_title_bar(window)
    return window

def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

try:
    imageList = [file for file in os.listdir("./") if file.endswith('.png') and not file.startswith('logo')]
    text = imageList[0].upper().replace('.PNG', '')
except Exception:
    image = Image.open(resource_path('./assets/fini.png'))
    window = initWindow()
    photo = ImageTk.PhotoImage(image.resize((640,360)))
    img = tk.Label(window, image=photo)
    img.image = photo
    img.grid(row=1, column=0, padx=5, pady=5)
    img.update()
    window.mainloop()
    sys.exit()

if __name__ == "__main__":
    window = initWindow()
    image = renderImage(file=imageList[0], text=text, settings_=settings)
    setting_tab(window)
    preview_image()
    window.mainloop()
    os.remove(resource_path("./assets/image_temp.png"))
    saveSettings()