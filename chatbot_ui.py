import random
import tkinter as tk
from tkinter import scrolledtext

class DocsevaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Docseva Chatbot")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # --- Data Setup ---
        self.responses = {
            "hello": ["Hi!! there", "Hello, how can I help you?", "Heyyy....."],
            "hi": ["Hi!! there", "Hello, how can I help you?", "Heyyy....."],
            "how are you": ["I'm fine, thank you. Which document are you lookin for?", "I am fine, how are you?Which document are you lookin for?", "I am perfectly fine.Which document are you lookin for?"],
        }

        self.documents = {
            "aadhar": ["Identity proof", "Address proof", "Birth certificate", "Passport size photo"],
            "pan": ["Aadhar card", "Address proof", "Passport size photo"],
            "ration card": ["Aadhar card", "Address proof", "Income certificate", "Family details", "Passport size photo"],
            "voter id": ["Aadhar card", "Address proof", "Age proof", "Passport size photo"],
            "income certificate": ["Aadhar card", "Address proof", "Income proof", "Passport size photo"],
            "caste certificate": ["Aadhar card", "Address proof", "Caste proof", "Affidavit", "Passport size photo"],
            "domicile certificate": ["Aadhar proof", "Address proof", "Residence proof", "Affidavit", "Passport size photo"]
        }

        # --- Chat Display ---
        self.chat_display = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state='disabled',
            bg="#f4f4f4",
            font=("Arial", 11)
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Tag styles for alignment
        self.chat_display.tag_config("bot", justify='left', foreground="black", lmargin1=10, lmargin2=10)
        self.chat_display.tag_config("user", justify='right', foreground="blue", rmargin=10)

        # --- Entry Box ---
        self.user_input = tk.Entry(root, font=("Arial", 12))
        self.user_input.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.user_input.bind("<Return>", self.handle_send)

        # --- Send Button ---
        self.send_button = tk.Button(
            root,
            text="Send",
            command=self.handle_send,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.send_button.pack(pady=(0, 10))

        # Initial message
        self.display_message(
            "Bot: Hi, I am Docseva chatbot. Ask me about required documents! (Type 'bye' to exit)",
            "bot"
        )

    # --- Display Function ---
    def display_message(self, message, sender="bot"):
        self.chat_display.config(state='normal')

        if sender == "user":
            self.chat_display.insert(tk.END, message + "\n\n", "user")
        else:
            self.chat_display.insert(tk.END, message + "\n\n", "bot")

        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    # --- Handle Send ---
    def handle_send(self, event=None):
        user_text = self.user_input.get().lower().strip()
        if not user_text:
            return

        # Show user message (RIGHT)
        self.display_message(f"You: {user_text}", "user")
        self.user_input.delete(0, tk.END)

        # Exit logic
        if user_text in ["bye", "goodbye"]:
            self.display_message("Bot: Goodbye!! Take care", "bot")
            self.root.after(2000, self.root.destroy)
            return

        response_found = False

        # Greetings
        for key in ["hello", "hi"]:
            if key in user_text:
                res = random.choice(self.responses[key])
                self.display_message(f"Bot: {res}\nWhich document are you looking for?", "bot")
                response_found = True
                break

        # Other responses
        if not response_found:
            for key in self.responses:
                if key in user_text:
                    self.display_message(f"Bot: {random.choice(self.responses[key])}", "bot")
                    response_found = True
                    break

        # Document queries
        if not response_found:
            for doc in self.documents:
                if doc in user_text:
                    doc_list = "\n- ".join(self.documents[doc])
                    msg = f"Bot: Required for {doc.title()}:\n- {doc_list}\n(Note: May vary by state)"
                    self.display_message(msg, "bot")
                    response_found = True
                    break

        # Fallback
        if not response_found:
            fallback = [
                "Sorry, I didn't understand.",
                "Can you please clarify?",
                "Please simplify your question."
            ]
            self.display_message(f"Bot: {random.choice(fallback)}", "bot")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DocsevaGUI(root)
    root.mainloop()

