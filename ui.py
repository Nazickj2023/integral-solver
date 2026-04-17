import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkButton

class IntegralSolverUI(CTk):
    def __init__(self):
        super().__init__()

        self.title("Integral Solver")
        self.geometry("400x300")

        self.light_theme = True

        # Theme toggle button
        self.toggle_button = CTkButton(self, text="Toggle Theme", command=self.toggle_theme)
        self.toggle_button.pack(pady=20)

        # Labels and UI elements
        self.label = CTkLabel(self, text="Welcome to Integral Solver!")
        self.label.pack(pady=10)

    def toggle_theme(self):
        if self.light_theme:
            self.dark_theme()  
        else:
            self.light_theme()  

    def dark_theme(self):
        self.dark_color = "#2E2E2E"
        self.light_color = "#FFFFFF"
        self.configure(bg=self.dark_color)
        self.label.configure(bg=self.dark_color, fg=self.light_color)
        self.toggle_button.configure(bg=self.dark_color)
        self.light_theme = False

    def light_theme(self):
        self.light_color = "#FFFFFF"
        self.dark_color = "#2E2E2E"
        self.configure(bg=self.light_color)
        self.label.configure(bg=self.light_color, fg=self.dark_color)
        self.toggle_button.configure(bg=self.light_color)
        self.light_theme = True

if __name__ == '__main__':
    app = IntegralSolverUI()
    app.mainloop()