import customtkinter
import random
import time
from sorting_algos import *

# default values for launch
array_length = 100
new_array = []
speed_selected = .04
algor_choice = 0
is_called = False

# theming
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# button functions
def createArray(size):
    global is_called
    is_called = True
    global new_array 
    new_array = []
    
    for i in range(size):
        new_array.append(random.randint(5, 1000))
    
    var_numbers.set("Numbers: " + str(size))
    
    drawData(new_array, ["#9592F7" for x in range(len(new_array))]) # array of purple for individual rect

def arraySizer(value):
    global array_length
    array_length = int(value)

def speedChoice(value):
    global speed_selected
    speed_selected = value
    var_delay.set("Delay: " + str(int(speed_selected*1000)) + "ms")
    
def drawData(data, colorArray):
    # canvas sizing and spacing
    canvas.delete("all")
    canvas_height = 720
    canvas_width = 840
    x_width = canvas_width / (len(data) + 1)
    offset = 50
    spacing_rect = 2
    
    normalized_data = [i / max(data) for i in data]
    
    # remove spacing if larger array
    if array_length > 100:
        spacing_rect = 0
    else:
        spacing_rect = 2

    # formula that creates shape, size and bounds of items(elements of array)
    for i, height in enumerate(normalized_data):
        x0 = i*x_width + offset + spacing_rect
        y0 = canvas_height - height * 700
        
        x1 = (i+1) * x_width + offset
        y1 = canvas_height
        
        canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
    
    
    app.update_idletasks()

def algoPicker(value):
    global algor_choice
    algor_choice = value
       
def sortButton():
    if algor_choice == 1:
        start = time.perf_counter()
        bubbleSort(new_array, drawData, speed_selected)
        drawData(new_array, ["#EA706C" for i in range(len(new_array))])
        end = time.perf_counter()
    elif algor_choice == 2:
        start = time.perf_counter()
        mergeSort(new_array, drawData, speed_selected)
        drawData(new_array, ["#EA706C" for i in range(len(new_array))])
        end = time.perf_counter()
    elif algor_choice == 3:
        start = time.perf_counter()
        quickSort(new_array, 0, array_length - 1, drawData, speed_selected)
        drawData(new_array, ["#EA706C" for i in range(len(new_array))])
        end = time.perf_counter()
    elif algor_choice == 4:
        start = time.perf_counter()
        insertionSort(new_array,drawData, speed_selected)
        drawData(new_array, ["#EA706C" for i in range(len(new_array))])
        end = time.perf_counter()
    elif algor_choice == 5:
        start = time.perf_counter()
        selectionSort(new_array, array_length, speed_selected, drawData)
        drawData(new_array, ["#EA706C" for i in range(len(new_array))])
        end = time.perf_counter()
        
    var_time.set("Visual Time: " + "{:.2f}".format((end-start)) + "s")

def buttonState(): # horrible way to make buttons stay highlighted LOL
    if algor_choice == 1:
        bubble_button.configure(fg_color="#1F222A")
        merge_button.configure(fg_color="transparent")
        quick_button.configure(fg_color="transparent")
        insertion_button.configure(fg_color="transparent")
        selection_button.configure(fg_color="transparent")
        
    elif algor_choice == 2:
        bubble_button.configure(fg_color="transparent")
        merge_button.configure(fg_color="#1F222A")
        quick_button.configure(fg_color="transparent")
        insertion_button.configure(fg_color="transparent")
        selection_button.configure(fg_color="transparent")

    elif algor_choice == 3:
        bubble_button.configure(fg_color="transparent")
        merge_button.configure(fg_color="transparent")
        quick_button.configure(fg_color="#1F222A")
        insertion_button.configure(fg_color="transparent")
        selection_button.configure(fg_color="transparent")
        
    elif algor_choice == 4:
        bubble_button.configure(fg_color="transparent")
        merge_button.configure(fg_color="transparent")
        quick_button.configure(fg_color="transparent")
        insertion_button.configure(fg_color="#1F222A")
        selection_button.configure(fg_color="transparent")

    elif algor_choice == 5:
        bubble_button.configure(fg_color="transparent")
        merge_button.configure(fg_color="transparent")
        quick_button.configure(fg_color="transparent")
        insertion_button.configure(fg_color="transparent")
        selection_button.configure(fg_color="#1F222A")
        
    if is_called == True and algor_choice != 0:
        sort_button.configure(state="normal")

# Menus (GUI)
class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.title = customtkinter.CTkLabel(
            self, 
            text="Sorting Viewer", 
            font=customtkinter.CTkFont(
                family="Roboto", 
                size=22), 
                text_color="white")
        self.title.grid(row=0, column=0, pady=14, padx=(14, 70),)
        
        global bubble_button
        bubble_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Bubble Sort",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[algoPicker(1), buttonState()])
        bubble_button.grid(row=1, column=0, pady=(14,8), padx=10, sticky="ew")
        
        global merge_button
        merge_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Merge Sort",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[algoPicker(2), buttonState()])
        merge_button.grid(row=2, column=0, pady=(2,8), padx=10, sticky="ew")
        
        global quick_button
        quick_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Quick Sort",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[algoPicker(3), buttonState()])
        quick_button.grid(row=3, column=0, pady=(2,8), padx=10, sticky="ew")
        
        global insertion_button
        insertion_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Insertion Sort",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[algoPicker(4), buttonState()])
        insertion_button.grid(row=4, column=0, pady=(2,8), padx=10, sticky="ew")

        global selection_button
        selection_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Selection Sort",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[algoPicker(5), buttonState()])
        selection_button.grid(row=5, column=0, pady=(2,8), padx=10, sticky="ew")
        
        global var_numbers
        var_numbers = customtkinter.StringVar()
        self.numbers = customtkinter.CTkLabel(
            self, 
            textvariable=var_numbers, 
            font=customtkinter.CTkFont(
                family="Roboto light", 
                size=14), 
                text_color="white")
        self.numbers.grid(row=6, column=0, pady=(250, 8), padx=(40, 40), sticky="ew")
        var_numbers.set("Numbers: N/A")

        global var_delay
        var_delay = customtkinter.StringVar()
        self.delay = customtkinter.CTkLabel(
            self, 
            textvariable=var_delay, 
            font=customtkinter.CTkFont(
                family="Roboto light", 
                size=14), 
                text_color="white")
        self.delay.grid(row=7, column=0, pady=(14, 8), padx=(40, 40), sticky="ew")
        var_delay.set("Delay: N/A")
        
        global var_time
        var_time = customtkinter.StringVar()
        self.time = customtkinter.CTkLabel(
            self, 
            textvariable=var_time, 
            font=customtkinter.CTkFont(
                family="Roboto light", 
                size=14), 
                text_color="white")
        self.time.grid(row=8, column=0, pady=(14, 8), padx=(40, 40), sticky="ew")
        var_time.set("Visual Time: N/A")
        
class Rightbar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.title = customtkinter.CTkLabel(
            self, 
            text="Options", 
            font=customtkinter.CTkFont(
                family="Roboto", 
                size=22), 
                text_color="white")
        self.title.grid(row=0, column=0, pady=14, padx=(4, 70))
        
        self.new_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="New Array",
            font=customtkinter.CTkFont(
            family="Roboto light", 
            size=16), 
            text_color="white",
            cursor="hand2",
            command=lambda:[createArray(array_length), buttonState()])
        self.new_button.grid(row=1, column=0, pady=(14,8), padx=10, sticky="ew")
        
        self.size_text = customtkinter.CTkLabel(
            self, 
            text="Array Size:", 
            font=customtkinter.CTkFont(
                family="Roboto light", 
                size=16), 
                text_color="white")
        self.size_text.grid(row=3, column=0, pady=(14,6), padx=10, sticky="ew")
        
        self.size_slider = customtkinter.CTkSlider(
            self,
            button_color="#9592F7",
            button_hover_color="#1B215A",
            from_=10,
            to=200,
            number_of_steps=100,
            cursor="hand2",
            command=arraySizer)
        self.size_slider.grid(row=4, column=0, padx=10, sticky="ew")
        
        self.speed_text = customtkinter.CTkLabel(
            self, 
            text="Sort Speed:", 
            font=customtkinter.CTkFont(
                family="Roboto light", 
                size=16), 
                text_color="white")
        self.speed_text.grid(row=5, column=0, pady=(14,6), padx=10, sticky="ew")
        
        self.speed_slider = customtkinter.CTkSlider(
            self,
            button_color="#9592F7",
            button_hover_color="#1B215A",
            from_=1,
            to=0,
            number_of_steps=14,
            command=speedChoice)
        self.speed_slider.grid(row=6, column=0, padx=10, sticky="ew")
        
        global sort_button
        sort_button = customtkinter.CTkButton(
            self,
            fg_color="transparent",
            hover_color="#1F222A",
            border_spacing=6,
            text="Sort!",
            font=customtkinter.CTkFont(
            family="Roboto bold", 
            size=20), 
            text_color="white",
            cursor="hand2",
            command=sortButton,
            state="disabled")
        sort_button.grid(row=7, column=0, pady=(25,8), padx=10, sticky="ew")
        
# main app class (GUI)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1400x720")
        self.title("")
        self.resizable(width=False, height=False)
        self.configure(fg_color="#242627")
        
        self.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        
        self.sidebar_frame = Sidebar(master=self)
        self.sidebar_frame.configure(
                                    fg_color="#111315", 
                                    border_width=0,
                                    corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, columnspan=2, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        
        self.rightbar_frame = Rightbar(master=self)
        self.rightbar_frame.configure(
                                    fg_color="#111315", 
                                    border_width=4, 
                                    border_color="#111015",
                                    corner_radius=25)
        self.rightbar_frame.grid(row=0, column=7, rowspan=10, sticky="ns", padx=(0,26), pady=(190))
        self.rightbar_frame.grid_rowconfigure(10, weight=1)
        
        global canvas
        canvas = customtkinter.CTkCanvas(height=720, width=900, bg="#242627", bd=0, highlightthickness=0)
        canvas.grid(row=1, column=0, columnspan=10, rowspan=10, sticky="se", padx=(0, 280))
        
# run
app = App()
app.mainloop()