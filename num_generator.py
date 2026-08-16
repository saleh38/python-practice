def number_pattern(n):
    num_str = ''
    if not isinstance(n , int) :
        return 'Argument must be an integer value.'
    elif n <= 0 :
        return 'Argument must be an integer greater than 0.'
    else :
        for num in range(1, n + 1):
            num_str +=str(num)+' ' 
    return num_str.strip()
print(number_pattern(4))
