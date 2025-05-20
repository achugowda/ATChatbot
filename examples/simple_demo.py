# examples/simple_chatbot.py
"""
A simple example of using the ATChatbot library to create a chatbot.
"""
import sys
import os

# Add the src directory to the path so we can import the library
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.atchatbot import generate_chatbot

def main():
    # Example description
    description = "I want a chatbot that books appointments for a clinic"
    
    # Generate a chatbot
    chatbot = generate_chatbot(description, name="ClinicBot")
    
    # Run the chatbot in interactive mode
    chatbot.run_interactive()

if __name__ == "__main__":
    main()
