def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):   
    correct = ""
    jp_list = []
    sg_list = []
    tw_list = []
    ua_list = []
    for each in list_phones:
        correct = sanitize_phone_number(each)
        if correct.startswith("81"):
            # JP
            jp_list.append(correct)
        elif correct.startswith("65"):
            # SG
            sg_list.append(correct)
        elif correct.startswith("886"):
            # TW
            tw_list.append(correct)
        else:
            # UA
            ua_list.append(correct)
    
    codes = {
        "JP": jp_list,
 	    "SG": sg_list,
        "TW": tw_list,
	    "UA": ua_list
    }

    print(codes)

    return codes
    
        
get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976'])   
        
            
        
            
        
            
    