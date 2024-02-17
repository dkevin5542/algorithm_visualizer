from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visulizer")
root.geometry("900x600+200+80")
root.config(bg = '#082A46')


def drawData(data):
	board.delete("all")
	canvas_height = 450
	canvas_width = 870
	x_width = canvas_width / (len(data) + 1)
	offset = 10
	spacing_rect = 10
	normalized_data = [i / max(data) for i in data]

	for i, height in enumerate(normalized_data):
		x0 = i * x_width + offset + spacing_rect
		y0 = canvas_height - height * 400

		x1 = (i + 1) * x_width
		y1 = canvas_height

		board.create_rectangle(x0, y0, x1, y1, fill = "#A90042")
		board.create_text(x0 + 2, y0, anchor= SW, text = str(data[i]), font =("new_roman", 15, "italic bold"), 
					 fill = "orange")
         

def Generate():
	print("Selected Algorithm: " + selected_algorithm.get())

	try:
		mini_value = int(min_val.get())
	except:
		mini_value = 1
	
	try:
		max_value = int(max_val.get())
	except:
		max_value = 100

	try:
		size_value = int(size_val.get())
	except:
		size_value = 10

	if mini_value < 0:
		mini_value = 0
	if max_value > 100:
		max_value = 100
	if size_value > 40 or size_value < 3:
		size_value = 29

	
	if mini_value > max_value:
		mini_value, max_value = max_value, mini_value

	data = []
	for _ in range(size_value):
		data.append(random.randrange(mini_value, max_value + 1))


	drawData(data)



selected_algorithm = StringVar()


mainlabel = Label(root, text = "Algorithm: ", font = ("new roman", 16, "italic bold"), 
                  bg = "#05897A", width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x = 0, y = 0)

#menu for selecting which sorting algorithm
main_menu = ttk.Combobox(root, width = 15, font = ("new roman", 19, "italic bold"), 
                         textvariable = selected_algorithm, values = ["Bubble Sort", "Merge Sort", "Quick Sort"])
main_menu.place(x = 145, y = 0)
main_menu.current(0)


random_gen = Button(root, text = "Generate", bg = "#2DAE9A", font = ("arial", 12, "italic bold"), 
                    relief= SUNKEN, activebackground = "#05945B", activeforeground = "white", bd = 5, width = 10, command=Generate)
random_gen.place(x = 750, y = 60)


#sliding bar for selecting the sample size to sort
size_label = Label(root, text = "Size: ", font = ("new roman", 12, "italic bold"), 
                  bg = "#0E6DA5", width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
size_label.place(x = 0, y = 60)

size_val = Scale(root, from_ = 0, to = 30, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"),
                 relief= GROOVE, bd = 2, width = 10)
size_val.place(x = 120, y = 60)


#sliding bar for selecting the min size
min_label = Label(root, text = "Min Value: ", font = ("new roman", 12, "italic bold"), 
                  bg = "#0E6DA5", width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
min_label.place(x = 250, y = 60)
min_val = Scale(root, from_ = 0, to = 10, resolution= 1, orient= HORIZONTAL, font = ("arial", 14, "italic bold"),
                 relief= GROOVE, bd = 2, width = 10)
min_val.place(x = 370, y = 60)


#sliding bar for selecting the max size
max_label = Label(root, text = "Max Value: ", font = ("new roman", 12, "italic bold"), 
                  bg = "#0E6DA5", width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
max_label.place(x = 500, y = 60)
max_val = Scale(root, from_ = 0, to = 100, resolution= 1, orient= HORIZONTAL, font = ("arial", 14, "italic bold"),
                 relief= GROOVE, bd = 2, width = 10)
max_val.place(x = 620, y = 60)


#the start button to begin the sorting visualizer
start_button = Button(root, text = "Start", bg = "#C45B09", font = ("arial", 12, "italic bold"), 
                    relief= SUNKEN, activebackground = "#05945B", activeforeground = "white", bd = 5, width = 10)
start_button.place(x = 750, y = 0)


speed_label = Label(root, text = "Speed: ", font = ("new roman", 12, "italic bold"), 
                  bg = "#0E6DA5", width = 10, fg = "black", relief = GROOVE, bd = 5)
speed_label.place(x = 400, y = 0)


speed_scale = Scale(root, from_ = 0.0, to = 5.0, resolution= 1, orient= HORIZONTAL, font = ("arial", 14, "italic bold"),
                 relief= GROOVE, bd = 2, width = 10)
speed_scale.place(x = 520, y = 0)

board = Canvas(root, width = 870, height = 450, bg = "black")
board.place(x = 10, y = 130)




root.mainloop()