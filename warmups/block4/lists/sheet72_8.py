def longest_consecutive(sequence:list) -> int:
    longest = 0
    consecutive = 1
    last_i = None
    
    for i in sequence:
        if i == last_i:
            consecutive += 1
        else:
            if consecutive > longest:
                longest = consecutive
            consecutive = 1
        last_i = i
    
    return longest