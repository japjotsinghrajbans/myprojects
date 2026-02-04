"""
author: Japjot Singh Rajbans
date: December 3, 2025
Character Counter
"""

# I will be using the `rich` & the `time` module here for a better user experience!
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint
console = Console()

# The class that counts the characters
class CharacterCounter(object):
    def __init__(self, string: str) -> None:
        """
        Initializes the input string.
        """
        self.string = string

    def count_non_spaces(self) -> int:
        """
        This function is where the magic happens!
        Uses `i` as iterator, set to 0, initially.
        """
        count = 0
        for letter in self.string:
            if letter != " ":
                count += 1
        return count

# Main menu for the program
def main_menu() -> None:
    """
    This function creates the main menu, used when the program launches.
    It has a green 'Welcome!' line at the very top, and the main panel with a gradient-like feel.
    
    Args:
        None
    Returns:
        None
    """

    # A green 'Welcome!' line at the very top
    console.rule("[bold green]Welcome!", style="green")

    # Main panel with gradient-like feel
    menu_text = Text()
    menu_text.append("Welcome to Character Counter, a precise counter for your everyday needs! Before we begin, would you like to count the spaces too?\n\n", style="white")
    menu_text.append("1", style="bold yellow")
    menu_text.append(" > With spaces (count everything)\n", style="dim white")
    menu_text.append("2", style="bold yellow")
    menu_text.append(" > Without spaces (everything excluding spaces)\n", style="dim white")
    menu_text.append("\nPlease enter your choice (1 or 2).", style="bold green")

    panel = Panel(
        menu_text,
        title="[bold cyan]Character Counter's Menu[/bold cyan]",
        title_align="center",
        border_style="bright_blue",
        padding=(1, 2),
        highlight=True
    )

    # Prints the panel in the end
    console.print(panel)

# The main function
def main():
    """
    This function runs the entire program!

    Args:
        None

    Returns:
        None
    """
    while True:
        main_menu()

        # Asks the user to enter their choice
        choice = console.input("[bold yellow]> [/bold yellow]").strip()

        # If choice is not `1` or `2`  
        if choice not in ["1", "2"]:
            rprint("[bold red]Uh oh, invalid choice! Please launch the program again and enter 1 or 2.[/]")
            return  # Exits gracefully!

        include_spaces = (choice == "1") # Include spaces if choice is recorded as `1`
        input_string = console.input("[bold green]Alright! Now enter a string: [/bold green]").strip() # Ask for the string
        counter = CharacterCounter(input_string) # Counting the characters of the string

        # A teeny-tiny delay for better UX
        time.sleep(1)

        # If choice is recorded as `1`
        if include_spaces:
            total_count = len(input_string)  # Counts absolutely everything
            # Output
            rprint(Panel(
                f"[bold white]Given string:[/] [italic]{input_string}[/]\n\n"
                f"[bold green]Total characters (including spaces):[/] [bold yellow]{total_count}[/]",
                title="Result (Including Spaces)",
                border_style="green"
            ))
        
        # If choice is recorded as `2`
        else:
            non_space_count = counter.count_non_spaces()  # Counts everything except spaces
            # Output
            rprint(Panel(
                f"[bold white]Given string:[/] [italic]{input_string}[/]\n\n"
                f"[bold blue]Total characters (excluding spaces):[/] [bold yellow]{non_space_count}[/]",
                title="Result (Excluding Spaces)",
                border_style="blue"
            ))

        # Asks if the user wants to run again
        time.sleep(0.8)
        console.print()  # An empty line for symmetrical spacing
        again_text = Text()
        again_text.append("Do you want to count another string?\n\n", style="white")
        again_text.append("y", style="bold green")
        again_text.append(" > Yes\n", style="dim white")
        again_text.append("n", style="bold red")
        again_text.append(" > No (this will close the program)\n", style="dim white")
        again_text.append("\nEnter your choice (y/n): ", style="bold magenta")

        again_panel = Panel(
            again_text,
            title="[bold cyan]Run again?[/bold cyan]",
            title_align="center",
            border_style="bright_magenta",
            padding=(1, 2),
            highlight=True
        )
        console.print(again_panel)

        rerun = console.input("[bold yellow]> [/bold yellow]").strip().lower()

        # If rerun (input) is NOT `y` or `yes`
        if rerun not in ["y", "yes"]:
            rprint("\n[bold green]Thank you for using Character Counter! Goodbye! :)[/]")
            time.sleep(1)
            return

        # Small separation before restarting
        console.clear()
        time.sleep(0.5)

# Roaring the project into life.
if __name__ == "__main__":
    main()