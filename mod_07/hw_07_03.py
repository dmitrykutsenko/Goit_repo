# Структура словника для параметра args_dicts має бути наступною
#{
#    "name": "useful",
#    "version": "1",
#    "description": "Very useful code",
#    "url": "http://github.com/dummy_user/useful",
#    "author": "Flying Circus",
#    "author_email": "flyingcircus@example.com",
#    "license": "MIT",
#    "packages": ["useful"],
#}


def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points = entry_points
          )
    
    