
import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


# Color for characters

def bold(text):
        bold_start = "\033[1m"
        bold_end = "\033[0m"
        return bold_start + text + bold_end

def blue(text):
        blue_start = "\033[34m"
        blue_end = "\033[0m"
        return blue_start + text + blue_end

def red(text):
        red_start = "\033[31m"
        red_end = "\033[0m"
        return red_start + text + red_end



def main():
        
        # Setting extra arguments
        
        parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT")
        
        parser.add_argument("--personality", 
                            type=str, 
                            help="A brief summary of the chatbot's personality",
                            default="You are a good explainer and friendly and helpful chatbot")
        
        args = parser.parse_args()
        
        # System message
        
        initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
        
        # Main code
        
        messages = [{"role": "system", "content": initial_prompt}]

        while True:
                try:
                        user_input = input(blue("You: "))
                        # Appending the inputs
                        messages.append({'role': 'user', 'content': user_input})
                        response = openai.chat.completions.create(
                                model="gpt-3.5-turbo", 
                                messages=messages,
                                max_tokens=500
                        )
                        
                        # Appending the answers from GPT
                        messages.append(
                                        {
                                        'role': response.choices[0].message.role,
                                        'content': response.choices[0].message.content
                                        }
                        )

                        print(red("Assistant: "), response.choices[0].message.content)
                except KeyboardInterrupt:
                        print("Existing...")
                        break
                
if __name__ == '__main__':
        main()
