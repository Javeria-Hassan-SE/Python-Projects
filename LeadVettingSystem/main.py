import tkinter as tk
from tkinter import messagebox

class LeadVettingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lead Vetting Software")
        self.root.geometry("600x400")

        self.background_image = tk.PhotoImage(file="background.png")  # Replace with actual background image path
        self.logo_image = tk.PhotoImage(file="logo.png")  # Replace with actual logo image path

        self.setup_ui()

    def setup_ui(self):
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.heading_label = tk.Label(self.root, text="Lead Vetting Software", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=20)

        self.logo_label = tk.Label(self.root, image=self.logo_image)
        self.logo_label.pack(side="left", padx=20)

        self.input_labels = [
            "Demographics", "Interests", "Travel History",
            "Countries Visited", "Work Abroad"
        ]

        self.input_entries = [None] * 5

        for label_text in self.input_labels:
            label = tk.Label(self.root, text=label_text)
            label.pack(anchor="w", padx=20, pady=(0, 5))

            if label_text == "Demographics":
                demographics_frame = tk.Frame(self.root)
                demographics_frame.pack(anchor="w", padx=20)

                self.input_entries[0] = tk.StringVar(value="")  # Set to empty initially
                male_radio = tk.Radiobutton(demographics_frame, text="Male", variable=self.input_entries[0], value="Male")
                female_radio = tk.Radiobutton(demographics_frame, text="Female", variable=self.input_entries[0], value="Female")

                male_radio.pack(side="left")
                female_radio.pack(side="left", padx=(10, 0))

            elif label_text == "Interests":
                self.input_entries[1] = tk.Entry(self.root)
                self.input_entries[1].pack(padx=20)

            elif label_text == "Travel History":
                travel_frame = tk.Frame(self.root)
                travel_frame.pack(anchor="w", padx=20)

                self.input_entries[2] = tk.StringVar(value="No")  # Set to No initially
                yes_radio = tk.Radiobutton(travel_frame, text="Yes", variable=self.input_entries[2], value="Yes")
                no_radio = tk.Radiobutton(travel_frame, text="No", variable=self.input_entries[2], value="No")

                yes_radio.pack(side="left")
                no_radio.pack(side="left", padx=(10, 0))

            elif label_text == "Countries Visited":
                self.input_entries[3] = tk.Entry(self.root, validate="key")
                self.input_entries[3].config(validatecommand=(self.input_entries[3].register(self.validate_integer), "%P"))
                self.input_entries[3].pack(padx=20)

            elif label_text == "Work Abroad":
                work_frame = tk.Frame(self.root)
                work_frame.pack(anchor="w", padx=20)

                self.input_entries[4] = tk.StringVar(value="No")  # Set to No initially
                yes_radio = tk.Radiobutton(work_frame, text="Yes", variable=self.input_entries[4], value="Yes")
                no_radio = tk.Radiobutton(work_frame, text="No", variable=self.input_entries[4], value="No")

                yes_radio.pack(side="left")
                no_radio.pack(side="left", padx=(10, 0))

        calculate_button = tk.Button(self.root, text="Calculate Score", command=self.calculate_score)
        calculate_button.pack(pady=20)

    def validate_integer(self, value):
        return value.isdigit() or value == ""

    def calculate_score(self):
        # Validation
        for entry in self.input_entries:
            if entry is None:
                continue
            if entry.get().strip() == "":
                messagebox.showwarning("Input Missing", "Please fill in all input fields.")
                return

        score = 0

        demographics_input = self.input_entries[0].get()
        travel_history_input = self.input_entries[2].get()
        work_abroad_input = self.input_entries[4].get()
        countries_visited_input = self.input_entries[3].get()

        if demographics_input == "Male":
            score += 5
        elif demographics_input == "Female":
            score += 5

        if travel_history_input == "Yes":
            score += 5

        if work_abroad_input == "Yes":
            score += 5

        if countries_visited_input.isdigit() and int(countries_visited_input) == 2:
            score += 5

        if score >= 10:
            result = "Work on the lead"
        else:
            result = "Don't waste time on this lead"

        messagebox.showinfo("Assessment Result", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = LeadVettingApp(root)
    root.mainloop()
