import re
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

# Function to extract emails from input text
def extract_emails():
    text = input_text.get("1.0", tk.END)
    emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
    
    if not emails:
        messagebox.showinfo("No Emails Found", "No valid email addresses were found in the input.")
        email_count_label.config(text="Emails Extracted: 0")
        return
    
    format_option = format_var.get()
    if format_option == "Each on a new line":
        result = "\n".join(emails)
    else:
        result = ", ".join(emails)
    
    output_text.config(state="normal")  # Unlock output box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state="normal")  # Keep output box editable
    
    email_count_label.config(text=f"Emails Extracted: {len(emails)}")

# Function to copy output to clipboard
def copy_to_clipboard():
    extracted_emails = output_text.get("1.0", tk.END).strip()
    if extracted_emails:
        root.clipboard_clear()
        root.clipboard_append(extracted_emails)
        root.update()
        messagebox.showinfo("Copied", "Emails copied to clipboard!")
    else:
        messagebox.showwarning("No Output", "There is nothing to copy!")

# Function to save extracted emails to a text file
def save_to_txt():
    extracted_emails = output_text.get("1.0", tk.END).strip()
    if not extracted_emails:
        messagebox.showwarning("No Output", "No emails to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(extracted_emails)
        messagebox.showinfo("Saved", f"Emails saved to {file_path}")

# Function to save extracted emails to a CSV file
def save_to_csv():
    extracted_emails = output_text.get("1.0", tk.END).strip()
    if not extracted_emails:
        messagebox.showwarning("No Output", "No emails to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(extracted_emails.replace("\n", ","))  # Convert new lines to CSV format
        messagebox.showinfo("Saved", f"Emails saved to {file_path}")

# Creating the GUI window
root = tk.Tk()
root.title("Email Extractor")
root.geometry("600x700")  # Increased height for better button visibility
root.resizable(False, False)

# Input text box
input_label = tk.Label(root, text="Enter text here:", font=("Arial", 10, "bold"))
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(root, width=70, height=10)
input_text.pack(pady=5)

# Format selection
format_var = tk.StringVar(value="Each on a new line")
format_label = tk.Label(root, text="Choose output format:", font=("Arial", 10, "bold"))
format_label.pack(pady=5)
format_option1 = tk.Radiobutton(root, text="Each on a new line", variable=format_var, value="Each on a new line")
format_option2 = tk.Radiobutton(root, text="Separated by comma", variable=format_var, value="Separated by comma")
format_option1.pack()
format_option2.pack()

# Extract button
extract_button = tk.Button(root, text="Extract Emails", command=extract_emails, bg="#4CAF50", fg="white", padx=10, pady=5)
extract_button.pack(pady=10)

# Email count label
email_count_label = tk.Label(root, text="Emails Extracted: 0", font=("Arial", 10, "bold"), fg="dark red")
email_count_label.pack(pady=5)

# Output text box
output_label = tk.Label(root, text="Extracted Emails:", font=("Arial", 10, "bold"))
output_label.pack(pady=5)
output_text = scrolledtext.ScrolledText(root, width=70, height=10)
output_text.pack(pady=5)

# Button Frame for better layout
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Copy to clipboard button
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#008CBA", fg="white", padx=10, pady=5)
copy_button.pack(side="left", padx=5)

# Save to file buttons
save_txt_button = tk.Button(button_frame, text="Save as TXT", command=save_to_txt, bg="#FFA500", fg="white", padx=10, pady=5)
save_txt_button.pack(side="left", padx=5)

save_csv_button = tk.Button(button_frame, text="Save as CSV", command=save_to_csv, bg="#FFA500", fg="white", padx=10, pady=5)
save_csv_button.pack(side="left", padx=5)

# Run the Tkinter event loop
root.mainloop()
