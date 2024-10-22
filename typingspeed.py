import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        # Sample  text
        self.sample_text = "This is a sample text for the typing speed test. Type this text as quickly and accurately as possible."

        # Labels and entry
        self.sample_text_label = tk.Label(root, text=self.sample_text)
        self.sample_text_label.pack(pady=10)

        self.user_text_entry = tk.Entry(root)
        self.user_text_entry.pack()

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root)
        self.result_label.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.user_text_entry.configure(state=tk.NORMAL)
        self.user_text_entry.focus()

    def calculate_speed(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        # Count words typed
        words_typed = len(self.user_text_entry.get().split())

        # Calculate WPM (Words Per Minute)
        wpm = (words_typed / elapsed_time) * 60

        self.result_label.configure(text=f"Your typing speed is: {wpm:.2f} WPM")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()