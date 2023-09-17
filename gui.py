import time
from tkinter import *
from goly import *


class GameTable(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        super().geometry("800x600")
        self.wm_title("Game Of Life")
        self.game = Goly()

        # creating a frame and assigning it to container
        self.container = Frame(self, background="#000")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # specifying the region where the frame is packed in root
        self.container.grid(row=0, column=0, sticky="news")

        # configuring the location of the container using grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.left_panel = Frame(self.container, background="#666", width=480, height=480)
        self.left_panel.grid(row=0, column=0, sticky="news")
        self.left_panel.grid_rowconfigure(0, weight=1)
        self.left_panel.grid_columnconfigure(0, weight=1)
        #
        self.right_panel = Frame(self.container, background="#0f0", height=480, width=160)
        self.right_panel.grid(row=0, column=1, sticky="ns")
        self.right_panel.grid_columnconfigure(0, weight=1)

        titulo = Label(self.right_panel, text="Game Of Life", font=("Arial", 25), background="#666")
        #
        titulo.grid(row=0, column=0, sticky=N)

        Label(
            self.right_panel,
            text="Número de filas",
            background="#0f0",
            fg="#000", font=("Arial", 16)
            ).grid()

        self.inp_box1 = Entry(self.right_panel)
        self.inp_box1.grid()

        Label(self.right_panel, text="Número de columnas",
              background="#0f0",
              fg="#000",
              font=("Arial", 16)
              ).grid()

        self.inp_box2 = Entry(self.right_panel)
        self.inp_box2.grid()

        Label(
            self.right_panel,
            text="Segundos entre actualización",
            background="#0f0",
            fg="#000",
            font=("Arial", 16)
        ).grid()
        self.inp_box4 = Entry(self.right_panel)
        self.inp_box4.insert(0, "0.1")
        self.inp_box4.grid()

        grid_size_button = Button(self.right_panel, text="Mostrar rejilla", command=self.makeboard)
        grid_size_button.grid()

        self.play = Button(
            self.right_panel,
            text="Play!",
            command=self.play_game
        )
        self.play.grid()
        self.right_panel.grid_rowconfigure("all", weight=1)

    def makeboard(self):
        if self.play["text"] == "STOP":
            self.swap_play_stop()
        for child in self.left_panel.winfo_children():
            child.destroy()
        self.game = Goly(int(self.inp_box1.get()), int(self.inp_box2.get()))
        for i in range(0, len(self.game.tabla)):
            for j in range(0, len(self.game.tabla[i])):
                pixel_button = Button(
                    self.left_panel,
                    background="black",
                    command=lambda ies=i, jes=j: self.button_click(ies, jes)
                )
                pixel_button.grid(row=i, column=j, sticky="news")
                self.left_panel.columnconfigure(j, weight=1)
            self.left_panel.rowconfigure(i, weight=1)
        self.left_panel.grid(row=0, column=0, sticky="news")
        self.update()
        self.left_panel.configure(width=self.right_panel.winfo_height())

    def update_board(self):
        for i in range(0, len(self.game.tabla)):
            for j in range(0, len(self.game.tabla[i])):
                if self.game.tabla[i][j]:
                    self.left_panel.grid_slaves(i, j)[0].configure(background="#0f0")
                else:
                    self.left_panel.grid_slaves(i, j)[0].configure(background="#000")

    def swap_play_stop(self):
        if self.play["text"] == "Play!":
            self.play.configure(text="STOP", command=self.makeboard)
        else:
            self.play.configure(text="Play!", command=self.play_game)

    def button_click(self, i, j):
        if self.game.tabla[i][j]:
            self.game.tabla[i][j] = False
            self.left_panel.grid_slaves(i, j)[0].configure(background="#000")
        else:
            self.game.tabla[i][j] = True
            self.left_panel.grid_slaves(i, j)[0].configure(background="#0f0")

    def play_game(self):
        self.swap_play_stop()
        # iteraciones = int(self.inp_box3.get())
        segundos = 0.1 if self.inp_box4.get() == "" else float(self.inp_box4.get())
        while self.play["text"] == "STOP":
            self.game.comprobarCambios()
            self.update_board()
            super().update()
            time.sleep(segundos)
            if self.game.isGameDead():
                self.swap_play_stop()
                break
