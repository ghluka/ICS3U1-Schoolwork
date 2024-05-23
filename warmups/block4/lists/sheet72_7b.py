def remove_n_largest(sequence:list, n:int) -> list:
    to_remove = sorted(sequence)[-n:]
    sequence_copy = sequence.copy()
    
    for i in to_remove:
        sequence_copy.remove(i)
        
    return sequence_copy