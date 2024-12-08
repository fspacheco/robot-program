def generate_character_name():
    """
    Generate a random character name.
    
    Returns:
        str: A randomly generated character name
    """
    first_names = ['Ana', 'Beatriz', 'Clarissa', 'Diana', 'Elena']
    last_names = ['Rana', 'Gurung', 'Rai', 'Magar', 'Kumara']
    
    import random
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_story_setting():
    """
    Generate a random story setting.
    
    Returns:
        str: A randomly generated story setting
    """
    settings = [
        'mysterious forest',
        'abandoned castle',
        'futuristic city',
        'remote mountain village',
        'underwater research station'
    ]
    
    import random
    return random.choice(settings)

def generate_plot_twist():
    """
    Generate a random plot twist.
    
    Returns:
        str: A randomly generated plot twist
    """
    plot_twists = [
        'The world is actually a simulation',
        'Time travel reveals a hidden truth',
        'An ancient prophecy comes true',
        'A character has been dead all along',
        'The villain is a misunderstood hero'
    ]
    
    import random
    return random.choice(plot_twists)

