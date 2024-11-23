import subprocess
from rich.console import Console
from rich.prompt import Prompt

# Initialize the Rich Console for styling
console = Console()


# Function to interact with Llama 3.2 using Ollama
def chat_with_llama(prompt: str):
    try:
        # Run the Ollama command to generate a response using Llama 3.2
        result = subprocess.run(
            ["ollama", "run", "llama3.2"],
            input=prompt, text=True, capture_output=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return "Sorry, something went wrong while processing your request."


# CLI chat loop
def chat():
    console.print("[bold green]Welcome to the Llama 3.2 Chatbot![/bold green]")
    console.print("Type 'exit' to end the conversation.\n")

    while True:
        # Get user input with Rich prompt
        user_input = Prompt.ask("You", default="Hello, Llama!")

        if user_input.lower() == "exit":
            console.print("[bold red]Goodbye![/bold red]")
            break

        # Call Llama 3.2 to generate a response
        response = chat_with_llama(user_input)

        # Print the chatbot's response with Rich
        console.print(f"[bold blue]Llama 3.2[/bold blue]: {response}\n")


# Run the chat function
if __name__ == "__main__":
    chat()