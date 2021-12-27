from pywebio import *
from pywebio.output import *
import sys as s

def main():
    '''
    pyweb.io onboarding
    
    A quick onboarding instruction for new users on pyweb.io platform
    '''
    
   
    put_markdown(r"""# 👋 Welcome to pyweb.io `App Builder`!
    
### Quick Start: Build your first app on *pyweb.io* in 4 steps
    
#### 1. Register 
- Sign up: https://build.pyweb.io/accounts/signup/
- Join pywebio discord server, introduce yourself in #community to recieve an invitation code.

#### 2. Create a new py file
- In App Builder page, use the file manager button (📁) to add a new file (e.g. `my_app.py`) 
> **[IMPORTANT]** Remember to add `.py` at the end to run it as a web app. Other files types, e.g. TXT, CSV, JSON, can be created and saved, but they are not runnable.

#### 3. Script in the IDE
- Copy / paste the following code to the IDE:""")

    put_code(r"""from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    '''
    An interactive web app that takes user's name 
    and output hello <username> on the webpage
    '''
    username = input('Input your name')
    put_text('Hello, %s' % username)
""", language='python')

    put_markdown(r"""
- Click `> Save & Run` to test the app. If everything ok, you should see your app up and running like this""")

    put_image('https://raw.githubusercontent.com/pywebio/demos/main/images/hello_user_demo.gif', width='350px')

    put_markdown(r"""
> **Tips**
> - **[IMPORTANT]** pyweb.io executes `main()` function as the app function. Running a file without main() will lead to errors.
> - **[IMPORTANT]** pyweb.io manages all hosting configurations. `start_server(main, ...)` must be commented or deleted before hitting `Save and Run`.
> - More demo code: https://github.com/pywebio/demos

#### 4. Launch your app
Once ready, click the `Launch` button.

#### Supported packages (you can manage your own package soon)
""")

    module_list =[m for m in list(s.modules.keys()) if all(c not in m for c in '._')]
    module_list.sort()
    put_scrollable(put_text('\n'.join(module_list)), height=200, keep_bottom=True)
