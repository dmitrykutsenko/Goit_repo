from setuptools import setup

def do_setup(args_dict, requires):

    # Unpack the dictionary and pass it as keyword arguments to the setup function
    # Add the install_requires parameter with the value requires
    setup(install_requires=requires, **args_dict)

# This function will do the same thing as the previous one, but it will also add the install_requires parameter with the value requires. This parameter specifies a list of dependencies that the project needs. It will unpack the dictionary and pass it as keyword arguments to the setup function, using the **](https://www.bing.com/search?form=SKPBOT&q=args_dict%29%0D%0A%0D%0AThis%20function%20will%20do%20the%20same%20thing%20as%20the%20previous%20one%2C%20but%20it%20will%20also%20add%20the%20install_requires%20parameter%20with%20the%20value%20requires.%20This%20parameter%20specifies%20a%20list%20of%20dependencies%20that%20the%20project%20needs.%20It%20will%20unpack%20the%20dictionary%20and%20pass%20it%20as%20keyword%20arguments%20to%20the%20setup%20function%2C%20using%20the%20) operator. This way, the setup function will receive the name, version, description, url, author, author_email, license, packages, and install_requires parameters from the function arguments. However, this function will not handle any errors or exceptions that may occur while calling the setup function

#Структура словника для параметра args_dicts має бути наступною

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

 # OR
 
def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires = requires)