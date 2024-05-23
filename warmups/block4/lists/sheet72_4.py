def rotated(sequence:list, rotations:int) -> list:
    rotations = len(sequence) - rotations
    
    rotated_sequence = []
    for i in range(0, len(sequence)):
        rotated_sequence.append(sequence[-len(sequence) + i + rotations])
    
    return rotated_sequence