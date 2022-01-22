# Function that return the direction you will face after the turn.
def direction(facing:str, turn:int) -> str:
    # Define list of directions
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    
    # Get index of direction
    try:
        start_position = directions.index(facing)
    except ValueError:
        return "Error: 'facing' must be one of %s directions" % (str(directions))
    
    # Get required steps
    try:
        steps = turn//45
    except TypeError:
         return "Error: 'turn' must be <int>"
    
    # Calculate end position direction index
    end_position = (start_position+steps) % len(directions)
    return directions[end_position]
