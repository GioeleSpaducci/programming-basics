while True:
    
    bit_string = input("Enter a string of bits: ")
    
    if len(bit_string) > 8:
        print("Bits' string too long.")
        continue
    
    if bit_string == " ":
        print("Bye!")
        break
    
    if len(bit_string) <= 8 and bit_string != " " and bit_string.count("1") % 2 == 0:
        print("Parity bit should be 0")   
        continue
    
    if len(bit_string) <= 8 and bit_string != " " and bit_string.count("1") % 2 != 0:
        print("Parity bit should be 1")   
        continue
    
    