def sort(width, height, length, mass):
    """
    Sorts packages into STANDARD, SPECIAL, or REJECTED.

    Args:
        width (int): width in cm
        height (int): height in cm
        length (int): length in cm
        mass (int): mass in kg

    Returns:
        str: category of the package ("STANDARD", "SPECIAL", or "REJECTED")
    """
    volume = width * height * length

    bulky = True if (volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150) else False
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
