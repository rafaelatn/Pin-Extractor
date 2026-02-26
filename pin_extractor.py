    def pin_extractor(poems):
    # This list will store the final PIN generated for each poem
    secret_codes = []
    
    # Iterate through each poem in the list
    for poem in poems:
        
        # This string will accumulate digits for the current poem
        secret_code = ''
        
        # Split the poem into individual lines
        # Each '\n' represents a line break
        lines = poem.split('\n')
        
        # enumerate() gives:
        # line_index → position of the line (0, 1, 2, ...)
        # line → the actual line text
        for line_index, line in enumerate(lines):
            
            # Split the current line into words
            words = line.split()
            
            # Check if the current line contains
            # a word at the same position as the line index
            if len(words) > line_index:
                
                # If it exists:
                # Get that word and calculate its length
                selected_word_length = len(words[line_index])
                
                # Convert number to string and append to the PIN
                secret_code += str(selected_word_length)
            
            else:
                # If the word does not exist at that position,
                # append '0' to maintain positional consistency
                secret_code += '0'
        
        # After processing all lines of the poem,
        # add the completed PIN to the results list
        secret_codes.append(secret_code)
    
    # Return the list containing one PIN per poem
    return secret_codes


# ============================================================
# Example Usage
# ============================================================

# Multi-line poem using triple quotes
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

# Multi-line poem using explicit \n line breaks
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

# Poem with only one word per line
poem3 = 'There\nonce\nwas\na\ndragon'

# Calling the function with a list of poems
# The output will be a list of numeric PIN strings
print(pin_extractor([poem, poem2, poem3]))
