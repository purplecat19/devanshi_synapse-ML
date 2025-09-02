def lumos_step(target, runes):
    
    # turning into upper case
    runes = [r.upper() for r in runes]
    
    collected = ""   # tracks collected letters
    
    for i in range(len(runes)):   
        collected = collected + runes[i]
        
        # checking if we can form "LUMOS"
        can_form = True
        for letter in target:
            if collected.count(letter) < target.count(letter):    #if she has fewer copies of a word than req, she can't form the word, hence break.
                can_form = False
                break
        
        if can_form:
            return (i+1)  #starting steps from 1
    
    return -1   #if it's impossible to form LUMOS

#taking string from the user
runes = input("Enter your sequence of runes: ") 
target = "LUMOS"
result = lumos_step(target, runes)

print(result)
