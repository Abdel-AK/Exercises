def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2 :
        raise ValueError("output base must be >= 2")
    
    
    
    output=0
    index=len(digits)-1
    for digit in digits:
        output+=digit*(input_base**index)
        index -=1    
    reminder_list=[]
    if output == 0:
        reminder_list.append(0)

    while output > 0:
        reminder_list.append(output % output_base)
        output = output // output_base
    reminder_list.reverse()
    return reminder_list
        
