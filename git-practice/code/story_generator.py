# story_generator.py
from story_functions import (
    generate_character_name,
    generate_story_setting,
    generate_plot_twist
)

def generate_story():
    """Generate a complete random story."""
    character = generate_character_name()
    setting = generate_story_setting()
    twist = generate_plot_twist()
    
    story = f"""
    In a {setting}, {character} discovers something unexpected:
    {twist}
    """
    return story

if __name__ == "__main__":
    print(generate_story())