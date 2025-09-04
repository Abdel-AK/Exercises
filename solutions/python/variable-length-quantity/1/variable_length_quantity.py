def encode(numbers):
    
    
    result = []  
    
    for number in numbers:
        if number>(2**32-1):
            raise ValueError("Number should fit in 32 bit")
        if len(bin(number)[2:])<8:
            result.append(int("0"+bin(number)[2:],2))
            continue
        vlq_bytes = encode_single_number(number)
        
        result.extend(vlq_bytes)  # Use extend, not append!
    
    return result

def encode_single_number(number):
    binary=bin(number)[2:]
    
    slicer = (len(binary) + 6) // 7
    binary_32bit = binary.zfill(32)
    result=[]
    i=1
    while i <= slicer:
        result.append((binary_32bit[-7*i:] if i == 1 else binary_32bit[-7*i:-7*(i-1)]).zfill(7))
        i += 1
    result.reverse()
    for index, chunk in enumerate(result):
        if index == len(result) - 1:
            # last chunk → MSB 0
            result[index] = int('0' + chunk, 2)
        else:
            # continuation → MSB 1
            result[index] = int('1' + chunk, 2)

    return result
        
    
    


def decode(bytes_):
    result=""
    
    fin=[]
    for  number in bytes_:
       
        data_bits = bin(number & 0x7F)[2:].zfill(7)
        result += data_bits
        
        # Check if this is the last byte (continuation bit is 0)
        if (number & 0x80) == 0:
            fin.append(int(result,2))
            result=""
    if result != "":
        raise ValueError("incomplete sequence")
            
        
    return fin    
