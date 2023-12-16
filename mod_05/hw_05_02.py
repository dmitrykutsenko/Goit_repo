articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):

    # To iterate over the keys
    # for k in articles_dict.keys(): # or `for key in dictionary`
        # print(k)

    # To iterate over the values
    # for v in articles_dict.values():
        # print(v)
    
    res_list = []
    res_list.clear()

    for each_d in articles_dict:
        new_dict = {}
        
        # To iterate both the keys and values
        for k, v in each_d.items():
            # print(k, '\t', v)
            if not letter_case:
                print("F ", str(v).lower(), '\t', key.lower(), '\t', str(v).lower().find(key.lower()))
                if str(v).lower().find(key.lower()) >= 0:
                    print("yes", str(v).lower().find(key.lower()))
                    # new_dict.update({str(k): v})
                    res_list.append(each_d)
                    break
            else:
                #print("T ", str(v).capitalize(), '\t', key)
                if str(v).find(key) >= 0:
                    # new_dict.update({str(k): v})
                    res_list.append(each_d)
                    break
                    
        # res_list.append(dict(sorted(new_dict.items())))
        # if len(new_dict) > 0:
        #     res_list.append(new_dict)

    print(res_list)
    return res_list
    
        
find_articles("Ocean")        
        
        
            
        
        
            
        
        
            
        
            
    