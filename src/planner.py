import tkinter as tk
import datetime as dt
from tkinter import font as tkfont, ttk
from tkcalendar import *


class CalFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        # self.config(bg='red')
        self.title = tk.Label(self, text='Calendar', font=controller.title_font)
        self.title.grid(column=0, row=0, sticky='n', columnspan=5, pady=5)
        self.cal = Calendar(self, selectmode='day', date_pattern='dd/mm/yyyy', textvariable=self.controller.shared_data["Selected date"])
        self.cal.grid(column=0, row=1, rowspan=3, columnspan=5, pady=20)
        self.select_day_button = tk.Button(self, text="Select Day", command=lambda: controller.openFrame(DayFrame))
        self.select_day_button.grid(row=4, column=0, columnspan=5)


class DayFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)

        self.title = tk.Label(self, font=controller.title_font, textvariable=self.controller.shared_data["Selected date"])
        self.title.grid(row=0, column=2)

        #Buttons
        self.prev_button = tk.Button(self, text='Prev', command=self.prev_day)
        self.prev_button.grid(row=0, column=0, sticky='nw')
        self.next_button = tk.Button(self, text='Next', command=self.next_day)
        self.next_button.grid(row=0, column=4, sticky='ne')
        self.back_button = tk.Button(self, text='Back', command=lambda: controller.openFrame(CalFrame))
        self.back_button.grid(row=6, column=2)
        self.suggestion_button = tk.Button(self, text='Suggestions', command=controller.suggest)
        self.suggestion_button.grid(row=3, column=2)
        self.clear_button = tk.Button(self, text='Clear', command=self.clear_workout)
        self.clear_button.grid(row=5, column=0)
        self.save_workout_button = tk.Button(self, text='Save', command=self.save_workout)
        self.save_workout_button.grid(row=6, column=0)
        self.add_remove_button = tk.Button(self, text='Add/Remove', command=self.edit_workout)
        self.add_remove_button.grid(row=6, column=1)

        #Labels
        self.workout_label = tk.Label(self, text='Workout', font=controller.subtitle_font)
        self.workout_label.grid(row=1, column=0, columnspan=2, sticky='s')
        self.saved_label = tk.Label(self, text='Saved Workouts', font=controller.subtitle_font)
        self.saved_label.grid(row=1, column=3, sticky='s')
        self.notes_label = tk.Label(self, text='Notes', font=controller.subtitle_font)
        self.notes_label.grid(row=4, column=3, columnspan=2, sticky='s')

        #Treeviews
        self.day_workout_tree = ttk.Treeview(self)
        self.saved_workouts_tree = ttk.Treeview(self)
        self.suggestion_tree = ttk.Treeview(self)

        #Treeview columns for daily workout.
        self.day_workout_tree['columns'] = ('Tags', 'Target', 'Completed', '%')
        self.day_workout_tree.column('#0', width=110)
        self.day_workout_tree.column('Tags', width=120, minwidth=80, anchor='w')
        self.day_workout_tree.column('Target', width=70, anchor='e')
        self.day_workout_tree.column('Completed', width=70, anchor='e')
        self.day_workout_tree.column('%', width=30, anchor='e')

        self.day_workout_tree.heading('#0', text='Exercise')
        self.day_workout_tree.heading('Tags', text='Tags', anchor='w')
        self.day_workout_tree.heading('Target', text='Target')
        self.day_workout_tree.heading('Completed', text='Completed')
        self.day_workout_tree.heading('%', text='%')

        self.day_workout_tree.insert(parent='', index='end', text='Pushup', values=(['One', 'Two', 'Three', 10]))

        self.day_workout_tree.grid(column=0, columnspan=2, row=2, rowspan=3, sticky='nsew')


        #Treeview columns for saved workouts.
        self.saved_workouts_tree['columns'] = ('Tags', 'Weekly Target', 'Weekly Completed', '%', 'Days since')
        self.saved_workouts_tree.column('#0', width=100)
        self.saved_workouts_tree.column('Tags', width=110, anchor='w')
        self.saved_workouts_tree.column('Weekly Target', width=65, anchor='e')
        self.saved_workouts_tree.column('Weekly Completed', width=65, anchor='e')
        self.saved_workouts_tree.column('%', width=25, anchor='e')
        self.saved_workouts_tree.column('Days since', width=35, anchor='e')

        self.saved_workouts_tree.heading('#0', text='Exercise\n')
        self.saved_workouts_tree.heading('Tags', text='Tags\n', anchor='w')
        self.saved_workouts_tree.heading('Weekly Target', text='Weekly\nTarget ', anchor='e')
        self.saved_workouts_tree.heading('Weekly Completed', text='Weekly\nCompleted ', anchor='e')
        self.saved_workouts_tree.heading('%', text='%', anchor='e')
        self.saved_workouts_tree.heading('Days since', text='Days Since', anchor='e')

        self.saved_workouts_tree.insert(parent='', index='end', text='pushup', values=(['one', 'two', 'three', '4', '5']))
        self.saved_workouts_tree.grid(column=3, columnspan=2, row=2, rowspan=2, sticky='nsew')

        #Notes text box
        self.notes_text = tk.Text(self, wrap='word', height=5, width=50)
        self.notes_text.grid(row=5, column=3, rowspan=2, columnspan=2, sticky='ns')

    def prev_day(self):
        selected_day = self.controller.shared_data["Selected date"].get()
        format_str = '%d/%m/%Y'
        day = dt.datetime.strptime(selected_day, format_str) - dt.timedelta(1)
        self.controller.date_change(day)

    def next_day(self):
        selected_day = self.controller.shared_data["Selected date"].get()
        format_str = '%d/%m/%Y'
        day = dt.datetime.strptime(selected_day, format_str) + dt.timedelta(1)
        self.controller.date_change(day)

    def clear_workout(self):
        #TODO
        pass

    def save_workout(self):
        #TODO
        pass

    def edit_workout(self):
        pass
        #TODO

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title_font = tkfont.Font(name='TF', family='Helvetica', size=18, weight="bold")
        self.subtitle_font = tkfont.Font(family='Helvetica', size=12, weight="normal")
        self.title('Workout Log')
        self.geometry('1200x600')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky='nsew')
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.shared_data = {
            "Selected date": tk.StringVar()
        }

        self.frames = {}
        for x in (CalFrame, DayFrame):
            frame = x(self.container, self)
            self.frames[x] = frame
            frame.grid(row=0, column=0, sticky='nsew')


        self.openFrame(CalFrame)

    def openFrame(self, f):
        for x in self.frames.values():
            x.grid_remove()
        frame = self.frames[f]
        frame.grid()

    def suggest(self):
        pass



    def date_change(self, day):
        instance = self.frames[CalFrame]
        instance.cal.selection_set(day)


    def data_setter(self, key, value):
        # if self.shared_data[key]
        self.shared_data[key] = value



def main():
    root = MainApp()
    root.mainloop()
main()