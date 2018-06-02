def pigIt( original ): 
    frst = original [0].lower() 
    if frst in vocals: 
        return original + 'yay' 
    else: 
        return pigConsonant ( original[0], original [1:] ) + 'ay' 
     
def pigConsonant ( ini, original ): 
     frst = original [0] 
     if frst == 'a' or frst == 'e' or frst == 'i' or frst == 'o' or frst == 'u' or frst == 'y': 
        return original + ini 
     else: 
        return pigConsonant ( ini + original[0], original [1:] ) 
 
vocals = { 'a', 'e', 'i', 'o', 'u', 'y' } 
original = (input( 'Say something:\n' )) 
while len ( original ) != 0: 
    tokens = original.split ( ' ' ) 
    translated = '' 
    for i in range( len ( tokens ) ): 
        translated += ( pigIt ( tokens [i] ) ) + ' ' 
    print(translated)
    original = (input ( 'Say something:\n' ) )

