import customtkinter as ctk
from tkinter import filedialog

# List to keep track of uploaded files
uploaded_files = []

# Function to handle the upload button click
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Extract the file name from the file path
        file_name = file_path.split("/")[-1]
        
        # Add the file path to the list
        uploaded_files.append(file_path)

        # Create a new button for the uploaded file and pack it in the left frame
        file_button = ctk.CTkButton(left_frame, text=file_name, command=lambda path=file_path: read_file_content(path))
        file_button.pack(fill="x", padx=5, pady=5)

        # Bind mouse enter and leave events for hover effect
        file_button.bind("<Enter>", lambda event, button=file_button: on_button_hover_enter(button))
        file_button.bind("<Leave>", lambda event, button=file_button: on_button_hover_leave(button))

        # Display in the chat box for confirmation
        chat_box.configure(state="normal")  # Enable chat box for editing
        chat_box.insert(ctk.END, f"Uploaded: {file_name}\n")
        chat_box.configure(state="disabled")  # Disable chat box after inserting

# Function to read file content for review
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            chat_box.configure(state="normal")
            chat_box.insert(ctk.END, f"Content of {file_path}:\n{content}\n")
            chat_box.configure(state="disabled")
    except Exception as e:
        chat_box.configure(state="normal")
        chat_box.insert(ctk.END, f"Error reading file: {e}\n")
        chat_box.configure(state="disabled")

# Function to handle button hover enter event
def on_button_hover_enter(button):
    button.configure(fg_color="blue75")  # Change color on hover

# Function to handle button hover leave event
def on_button_hover_leave(button):
    button.configure(fg_color="gray20")  # Reset color when mouse leaves

# Function to send a message to chat
def send_message(event=None):  # Optional event parameter
    message = chat_input.get()
    if message:
        chat_box.configure(state="normal")  # Enable chat box for editing
        chat_box.insert(ctk.END, f"You: {message}\n")
        chat_box.configure(state="disabled")  # Disable chat box after inserting
        chat_input.delete(0, ctk.END)  # Clear the input box

# Functions for button click events
def forecast_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 1: I WAS CLICKED\n")
    chat_box.configure(state="disabled")

def billing_credits_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 2: IM HERE\n")
    chat_box.configure(state="disabled")
    
def eol_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 3: I WAS CLICKED\n")
    chat_box.configure(state="disabled")

def expiration_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 4: IM HERE\n")
    chat_box.configure(state="disabled")

def legal_review_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 5: I WAS CLICKED\n")
    chat_box.configure(state="disabled")

def avg_price_click():
    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, "Button 6: IM HERE\n")
    chat_box.configure(state="disabled")
    
# Create the main application window
app = ctk.CTk()
app.title("VisionAIry")
app.geometry("1600x800")

# Create a frame for the left section (upload button and files list)
left_frame = ctk.CTkFrame(app)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Add a label to the left section for "Contract List"
contract_list_label = ctk.CTkLabel(left_frame, text="Contract List", font=("Arial", 24, "underline"))
contract_list_label.pack(pady=(10, 20))  # Add some spacing above and below the label

# Create a frame for the center section (chat display)
center_frame = ctk.CTkFrame(app)
center_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Chat box to display messages
chat_box = ctk.CTkTextbox(center_frame, height=20, width=300)
chat_box.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)
chat_box.configure(state="disabled")  # Start as read-only

# Frame for input area at the bottom of the center section
input_frame = ctk.CTkFrame(center_frame)
input_frame.pack(pady=10, padx=10, fill=ctk.X)

# Upload button and chat input box at the bottom center
upload_button = ctk.CTkButton(input_frame, text="Upload File", command=upload_file)
upload_button.pack(side=ctk.LEFT, padx=(0, 5))

chat_input = ctk.CTkEntry(input_frame, placeholder_text="Message XXXXX", height=30)
chat_input.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=10)

send_button = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_button.pack(side=ctk.RIGHT)

# Bind the Enter key to the send_message function on the input field
chat_input.bind("<Return>", send_message)

# Create a frame for the right section (buttons)
right_frame = ctk.CTkFrame(app)
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Add 6 buttons to the right frame with specific click handlers for button 1 and button 2
forecast = ctk.CTkButton(right_frame, text="Forecast", command=forecast_click)
forecast.pack(fill="both", expand=True, pady=15, padx=15)

billing_credits = ctk.CTkButton(right_frame, text="Billing Credits", command=billing_credits_click)
billing_credits.pack(fill="both", expand=True, pady=15, padx=15)

eol = ctk.CTkButton(right_frame, text="EOL", command=eol_click)
eol.pack(fill="both", expand=True, pady=15, padx=15)

expiration = ctk.CTkButton(right_frame, text="Expirations", command=expiration_click)
expiration.pack(fill="both", expand=True, pady=15, padx=15)

legal_review = ctk.CTkButton(right_frame, text="Legal Review", command=legal_review_click)
legal_review.pack(fill="both", expand=True, pady=15, padx=15)

avg_price = ctk.CTkButton(right_frame, text="Average Price", command=avg_price_click)
avg_price.pack(fill="both", expand=True, pady=15, padx=15)

# Configure grid weights for responsive resizing
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)
app.grid_columnconfigure(2, weight=1)

# Start the application
app.mainloop()
