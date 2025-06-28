import tkinter as tk
from tkinter import scrolledtext, PhotoImage
import threading
from chatbot import generate
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class AurorMoodyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Auror Moody's Cybersecurity Lessons")
        master.geometry("800x600")
        
        # Set dark theme colors (like the dark halls of Hogwarts)
        self.bg_color = "#2C3E50"  # Dark blue-gray like Hogwarts stone
        self.text_color = "#ECF0F1"  # Light gray-white like a Patronus
        self.entry_bg = "#34495E"  # Slightly lighter blue-gray
        self.button_color = "#7D3C98"  # Deep purple like wizard robes
        self.highlight_color = "#F1C40F"  # Golden like a snitch
        self.chat_bg = "#1C2833"  # Darker for the chat area
        
        master.configure(bg=self.bg_color)
        
        # Title with Hogwarts-style font
        self.title_label = tk.Label(
            master,
            text="Auror Moody's Magical Cybersecurity Classroom",
            font=("Papyrus", 18, "bold"),
            bg=self.bg_color,
            fg=self.highlight_color,
            pady=10
        )
        self.title_label.pack(fill=tk.X)
        
        # Quote from Moody
        self.quote_label = tk.Label(
            master,
            text="\"CONSTANT VIGILANCE!\"",
            font=("Times New Roman", 12, "italic"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.quote_label.pack(pady=(0, 10))
        
        # Chat display area (like a Pensieve for conversations)
        self.chat_frame = tk.Frame(master, bg=self.bg_color, padx=20, pady=10)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            font=("Courier", 12),
            bg=self.chat_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            borderwidth=10,
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Input area (like sending an owl)
        self.input_frame = tk.Frame(master, bg=self.bg_color, padx=20, pady=15)
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.prompt_label = tk.Label(
            self.input_frame,
            text="Ask Auror Moody:",
            font=("Times New Roman", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.prompt_label.pack(anchor=tk.W)
        
        self.input_field = tk.Entry(
            self.input_frame,
            font=("Courier", 12),
            bg=self.entry_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            borderwidth=5
        )
        self.input_field.pack(fill=tk.X, pady=5)
        self.input_field.bind("<Return>", self.process_input)
        
        self.send_button = tk.Button(
            self.input_frame,
            text="Cast Inquiry",
            font=("Times New Roman", 10, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            relief=tk.FLAT,
            activebackground=self.highlight_color,
            activeforeground=self.bg_color,
            command=self.process_input
        )
        self.send_button.pack(pady=5)
        
        self.exit_button = tk.Button(
            self.input_frame,
            text="Disapparate (Exit)",
            font=("Times New Roman", 10),
            bg=self.entry_bg,
            fg=self.text_color,
            relief=tk.FLAT,
            command=self.master.destroy
        )
        self.exit_button.pack(side=tk.RIGHT, pady=5)
        
        # Display welcome message
        self.update_chat("Auror Moody", "Welcome to your Magical Cybersecurity lesson!\n\nI'm Auror Moody, and I'll be teaching you how to defend against the Dark Digital Arts. What would you like to know about cybersecurity today?\n\nRemember... CONSTANT VIGILANCE!")
        
    def update_chat(self, speaker, message):
        self.chat_display.config(state=tk.NORMAL)
        
        if speaker == "User":
            self.chat_display.insert(tk.END, "You: ", "user_name")
            self.chat_display.tag_configure("user_name", foreground=self.highlight_color, font=("Courier", 12, "bold"))
        else:
            self.chat_display.insert(tk.END, "Auror Moody: ", "bot_name")
            self.chat_display.tag_configure("bot_name", foreground="#9B59B6", font=("Courier", 12, "bold"))
            
        self.chat_display.insert(tk.END, f"{message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
    def process_input(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return
            
        # Clear input field
        self.input_field.delete(0, tk.END)
        
        # Show user message
        self.update_chat("User", user_input)
        
        # Disable input while processing
        self.input_field.config(state=tk.DISABLED)
        self.send_button.config(state=tk.DISABLED)
        
        # Update status
        self.prompt_label.config(text="Auror Moody is thinking...")
        
        # Process in separate thread to avoid freezing UI
        threading.Thread(target=self.get_bot_response, args=(user_input,), daemon=True).start()
    
    def get_bot_response(self, user_input):
        if user_input.lower() in ["exit", "quit", "disapparate"]:
            response = "Farewell! Remember to practice constant vigilance in the digital world!"
            self.master.after(0, lambda: self.update_chat("Auror Moody", response))
            self.master.after(2000, self.master.destroy)
        else:
            # Get response from the chatbot
            try:
                response = generate(user_input)
                self.master.after(0, lambda: self.update_chat("Auror Moody", response))
            except Exception as e:
                error_msg = f"My Foe-Glass seems to be malfunctioning! Error: {str(e)}"
                self.master.after(0, lambda: self.update_chat("Auror Moody", error_msg))
            
        # Re-enable input
        self.master.after(0, lambda: self.input_field.config(state=tk.NORMAL))
        self.master.after(0, lambda: self.send_button.config(state=tk.NORMAL))
        self.master.after(0, lambda: self.prompt_label.config(text="Ask Auror Moody:"))
        self.master.after(0, lambda: self.input_field.focus())

def bot():
    root = tk.Tk()
    app = AurorMoodyGUI(root)
    
    # Add icon if available
    try:
        root.iconbitmap("moody_icon.ico")
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    bot()