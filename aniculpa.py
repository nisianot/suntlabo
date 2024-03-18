from rich.console import Console

console = Console()

def cprint(text: str, color: str):
    """Prints colored text to the console."""
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> approve GPX | {address_wallet} | {error}', 'red')
