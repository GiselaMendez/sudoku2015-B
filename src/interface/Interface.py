#Interface
import sys
from Tkinter import *
from settings_game import SettingsGame

class Interface(Frame):
    
    def __init__(self, main=None):

        """
        main: tkinter frame object
        constructor -- it will get Tkinter object to construct the main UI window.
        this will call to initwindow() function , which will create and invoke all objects that will be available in the mainwindow
        
        """

        Frame.__init__(self, main)
        self.main = main
        self.init_window()

    def init_window(self):
        
        """
        The function will contain all objects (labels, buttons, text areas and so on) to be displayed in the window and also here has defined the size of the window
        this function will call the following command functions:
            --settings
            --quit
            
        ***** IT IS THE FIRST VERSION NEED TO IMPLEMENT THE RESTO OF THE BUTTONS AND FUNCTIONS
        """

        main.geometry("800x500+100+100")
        main.title("Sudoku Game Interface")
        
        #buttons section
        self.show_buttons()
        
        
        #canvas to show the game
        canvas_game_area = Canvas(main, height = 400, width = 400, bg = "white")
        canvas_game_area.place(x = 150, y = 10)
    
        #label
        label_time = Label(main, text = "Time: (15:25) Min.")
        label_time.place(x = 200, y = 430)

        main.mainloop()


    def show_buttons(self):
        """
        funtions will show the all available buttons  in the UI
        
        """
        settings_button = Button(self.main, text = "Settings", width = 10, heigh = 2, command = self.settings)
        settings_button.place(x = 10, y = 10)

        # generation button 
        generate_button = Button(self.main,text = "Generate", width = 10, heigh = 2)
        generate_button.place(x = 10, y = 60)

        # solve button
        solve_button = Button(self.main, text = "Solve", width = 10, heigh = 2)
        solve_button.place(x = 10, y = 120)

        # save button
        save_button = Button(main, text = "Save", width = 10, heigh = 2)
        save_button.place(x = 10, y = 180)

        # close button
        close_button = Button(main, text = "Close", width = 10, heigh = 2, command = self.quit)
        close_button.place(x = 10, y = 240)



    def settings(self):
        """
        the functions invokes to SettingsGame class to displays Soduko Configuration setting window
        """

        settings = SettingsGame(self.main)


    def quit(self):
        """
        the function will close the window and application

        """

        sys.exit()


if __name__ == '__main__':
    main = Tk()
    current = Interface(main)
    

