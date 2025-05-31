import customtkinter as ctk
from modules import *  # Make sure this imports the correct module for gen and article functions.
import tkinter as tk
import re

app = ctk.CTk()
app.geometry("600x500")
app.title("GenAI & Article App")

# Frame for top buttons
top_button_frame = ctk.CTkFrame(app)
top_button_frame.pack(pady=10)

# Output frame
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

text_box = tk.Text(frame, wrap="word", font=("Arial", 14))
text_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.configure(yscrollcommand=scrollbar.set)

# Tag for bold text
text_box.tag_configure("bold", font=("Arial", 14, "bold"))

# Helper: clear output
def clear_output():
    text_box.delete("1.0", tk.END)

# Helper: insert styled text
def insert_text(text):
    text_box.delete("1.0", tk.END)  # Remove old content
    parts = re.split(r"(\*\*.*?\*\*)", text)  # Handle bold text
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            text_box.insert(tk.END, part[2:-2], "bold")  # Insert bold text
        else:
            text_box.insert(tk.END, part)  # Insert regular text

# Remove both buttons
def remove_top_buttons():
    for widget in top_button_frame.winfo_children():
        widget.destroy()

# Show Top Buttons again
def show_top_buttons():
    remove_top_buttons()
    ctk.CTkLabel(top_button_frame, text="Choose an Option", font=("Arial", 18)).pack(pady=5)
    article_btn = ctk.CTkButton(top_button_frame, text="📄 Article", command=show_article)
    genai_btn = ctk.CTkButton(top_button_frame, text="🤖 GenAI", command=show_genai)
    article_btn.pack(side="left", padx=10)
    genai_btn.pack(side="left", padx=10)

# === Functions for Article and GenAI ===
def show_article():
    remove_top_buttons()
    insert_text("🔍 Please enter the name of the article you want.")

    input_frame = ctk.CTkFrame(app)
    input_frame.pack(pady=10)

    entry = ctk.CTkEntry(input_frame, width=300, placeholder_text="Enter article name")
    entry.pack(side="left", padx=5)

    def fetch_article():
        name = entry.get()
        if name:
            try:
                # Fetch the article using your imported module, make sure `article.getarticle()` works correctly
                result = article.getarticle(article_name=name)
                if result:
                    insert_text(result)  # Display the result inside the text box
                else:
                    insert_text("No result found for this article.")
            except Exception as e:
                insert_text(f"Error fetching article: {str(e)}")

    send_button = ctk.CTkButton(input_frame, text="Fetch", command=fetch_article)
    send_button.pack(side="left")

    # Back button
    back_button = ctk.CTkButton(app, text="Back to Menu", command=show_top_buttons)
    back_button.pack(pady=5)

def show_genai():
    remove_top_buttons()
    insert_text("🤖 Type your prompt for the AI (type 'exit' to quit).")

    input_frame = ctk.CTkFrame(app)
    input_frame.pack(pady=10)

    entry = ctk.CTkEntry(input_frame, width=300, placeholder_text="Enter your prompt")
    entry.pack(side="left", padx=5)

    def send_prompt():
        prompt = entry.get()
        if prompt.lower() == "exit":
            app.destroy()
        else:
            try:
                # Generate AI response using the gen module (make sure gen.generate() works correctly)
                result = gen.generate(promt=prompt)
                # if result:
                #     insert_text(result)  # Display the result inside the text box
                # else:
                #     insert_text("No response from AI.")
                label = ctk.CTkLabel(text_box, text=result, font=("Arial", 20))
                label.pack(pady=4)
            except Exception as e:
                insert_text(f"Error generating AI response: {str(e)}")

    send_button = ctk.CTkButton(input_frame, text="Send", command=send_prompt)
    send_button.pack(side="left")

    # Back button
    back_button = ctk.CTkButton(app, text="Back to Menu", command=show_top_buttons)
    back_button.pack(pady=5)

# === Create Top Buttons ===
show_top_buttons()

# Start GUI loop
app.mainloop()
