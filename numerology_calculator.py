import os
import requests
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Step 1: Get CLIENT_ID and CLIENT_SECRET from environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Step 2: Function to get the access token
def get_access_token(client_id, client_secret):
    """
    Obtain an access token using the client ID and client secret
    """
    url = 'https://api.prokerala.com/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=payload)
    token_data = response.json()
    return token_data['access_token']

# Step 3: Function to get Life Path Number
def get_life_path_number(access_token, birth_date):
    """
    Fetch Life Path Number from Prokerala API
    """
    url = f'https://api.prokerala.com/v2/numerology/life-path-number?datetime={birth_date}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Step 4: Function to handle the button click
def on_submit():
    """
    Handle the submit button click event
    """
    birth_date = entry_date.get()
    birth_time = entry_time.get()

    # Check if the fields are empty
    if not birth_date or not birth_time:
        messagebox.showerror("Error", "Enter valid data")
        return

    # Combine date and time into ISO 8601 format with milliseconds set to 00
    birth_date_time = f"{birth_date}T{birth_time}:00Z"
    
    # Validate the date to ensure it is not in the future
    try:
        input_datetime = datetime.strptime(birth_date_time, "%Y-%m-%dT%H:%M:%SZ")
        if input_datetime > datetime.now():
            messagebox.showerror("Error", "Your birth date is in the future")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid data")
        return

    try:
        access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
        result = get_life_path_number(access_token, birth_date_time)
        
        # Extract the life path number and description
        life_path_number = result['data']['life_path_number']['number']
        description = result['data']['life_path_number']['description']
        
        # Show result in a message box
        messagebox.showinfo("Life Path Number", f"Life Path Number: {life_path_number}\nDescription: {description}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Step 5: Create the main application window
root = tk.Tk()
root.title("Numerology Calculator")

# Create and place labels and entry widgets
tk.Label(root, text="Please enter your birth date in the format 'YYYY-MM-DD'").pack(pady=10)
entry_date = tk.Entry(root)
entry_date.pack(pady=5)

tk.Label(root, text="Please enter your birth time in the format 'HH:MM'").pack(pady=10)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
