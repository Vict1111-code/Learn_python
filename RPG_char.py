full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # 1. Name Type Validation
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # 2. Empty Name Validation
    if name == '':
        return 'The character should have a name' 
        
    # 3. Name Length Validation (fixed 'len()')
    if len(name) > 10:
        return 'The character name is too long'
        
    # 4. Contain Spaces Validation (fixed to look for any space)
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # 5. Stats Type Validation
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
        
    # 6. Minimum Stats Validation
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    # 7. Maximum Stats Validation
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    # 8. Stats Sum Validation
    if (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    
    # 9. Format and return character card
    str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
    int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))
    
    character_card = (
        f"{name}\n"
        f"STR {str_dots}\n"
        f"INT {int_dots}\n"
        f"CHA {cha_dots}"
    )
    
    return character_card
