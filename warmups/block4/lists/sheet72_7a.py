def remove_n_largest(sequence:list, n:int) -> None:
    to_remove = sorted(sequence)[-n:]
    
    for i in to_remove:
        sequence.remove(i)