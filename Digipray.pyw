import sys
import time
import tkinter as tk
import tkinter.messagebox as messagebox
import psutil

class DigitalPrayerWheel:
    def __init__(self):
        # Create the main window.
        self.window = tk.Tk()
        self.window.title("Digital Prayer Wheel")

        # Create the UI elements for the first screen.
        self.string_label = tk.Label(self.window, text="Enter the string to repeat:")
        self.string_edit = tk.Text(self.window, width=30, height=3)
        self.next_button = tk.Button(self.window, text="Next", command=self.show_rate_input_screen)

        # Create the layout for the first screen.
        self.string_label.pack()
        self.string_edit.pack()
        self.next_button.pack()

        # Set the size of the window to the same size as the second screen.
        self.window.geometry("400x150")

    def show_rate_input_screen(self):
        # Get the string from the UI.
        self.string = self.string_edit.get("1.0", "end-1c")

        # Calculate the maximum repetition rate based on the size of the string.
        self.max_repeat_rate = int(psutil.virtual_memory().available / (sys.getsizeof(self.string) * 2))

        # Create the UI elements for the second screen.
        self.repeat_rate_label = tk.Label(self.window, text="Repetition rate (Hz)\n(empty: estimated maximum)")
        self.repeat_rate_edit = tk.Entry(self.window, textvariable=self.max_repeat_rate)
        self.start_button = tk.Button(self.window, text="Start", command=self.start)
        self.elapsed_time_label = tk.Label(self.window, text="Elapsed time: 0 hours 0 minutes 0 seconds")

        # Create the layout for the second screen.
        self.repeat_rate_label.pack()
        self.repeat_rate_edit.pack()
        self.start_button.pack()
        self.elapsed_time_label.pack()

        # Remove the first screen.
        self.string_label.destroy()
        self.string_edit.destroy()
        self.next_button.destroy()

        # Set the size of the window to make sure all text fits.
        self.window.geometry("400x200")

    def start(self):
        # Get the repetition rate from the UI.
        self.repeat_rate = self.repeat_rate_edit.get()

        # Use the suggested repetition rate if the user does not specify a different rate.
        if self.repeat_rate == "":
            self.repeat_rate = self.max_repeat_rate
        else:
            self.repeat_rate = int(self.repeat_rate)
        # Use the time.perf_counter function to measure the elapsed time.
        self.start_time = time.perf_counter()

        # Disable the start button.
        self.start_button.config(state="disabled")

        # Call the repeat method for the first time.
        self.repeat()

    def repeat(self):
        # Use the time.perf_counter function to measure the elapsed time.
        elapsed_time = time.perf_counter() - self.start_time

        # Convert the elapsed time to hours, minutes, and seconds.
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Get the size of the string in memory.
        size = sys.getsizeof(self.string)

        # Use the string.join method to concatenate the repeated string.
        repeated_string = self.string.join([self.string] * self.repeat_rate)

        # Get the size of the repeated string in memory.
        repeated_size = sys.getsizeof(repeated_string)

        # Print a warning if the size of the repeated string is smaller than the original string.
        if repeated_size < size:
            # Show the warning message.
            messagebox.showwarning("Warning", "The size of the repeated string is smaller than the original string. This may be due to compression or optimization.")

            # Update the elapsed time label.
            self.elapsed_time_label.config(text="Elapsed time: %d hours %d minutes %d seconds\nString: %s\nRepetition rate: ~%d Hz" % (hours, minutes, seconds, self.string, self.repeat_rate))

            # Schedule the repeat method to be called again after a delay.
            self.window.after(200, self.repeat)
        else:
            # Update the elapsed time label.
            self.elapsed_time_label.config(text="Elapsed time: %d hours %d minutes %d seconds\nString: %s\nRepetition rate: ~%d Hz" % (hours, minutes, seconds, self.string, self.repeat_rate))

            # Schedule the next repetition.
            self.window.after(200, self.repeat)

# Create an instance of the DigitalPrayerWheel class and start the main loop.
DigitalPrayerWheel()
tk.mainloop()

