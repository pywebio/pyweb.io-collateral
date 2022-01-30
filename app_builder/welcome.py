from pywebio import *
from pywebio.output import *
import sys as s
from typing import Tuple, List

# Given a markdown string, this class adds TOC and anchor link to titles.
# Both md_formatter.toc and .content are string objects that can be displayed using put_markdown() as is. 
class md_formatter(object):
    def __init__(self, md_string: str) -> None:
        self._md_string = md_string
        self._toc: List[str] = []
        self._content = self._md_string.split('\n')
        self.add_toc()
        self.toc = '\n'.join(self._toc)
        self.content = '\n'.join(self._content)

    def add_toc(self):
        for index, line in enumerate(self._content):
            level, title, anchor = self._get_title(line)
            if level > 1:
                self._content[index] = line + f' <sub><sup>⚓</sup></sub> <a name="{anchor}"/></a>'
                self._toc.append('  ' * (level-2) +
                                    f"* [{title}](#{anchor})")

    def _get_title(self, line: str) -> Tuple[int, str, str]:
        level = 0
        for c in line:
            if c == '#':
                level += 1
            else:
                break
        title = line[level+1:]
        return (level, title, title.replace(" ",""))

# The markdown content of the instruction
md = r"""
## Quick Start: Launch your first app in 4 steps
    
### 1. Create a project in `Projects Page`
- After logging in, you will be re-directed to this page. A project must be created before app development. 
- When creating a project, the only thing that needs 10+ secs of attention is `project slug`.
>  **[IMPORTANT]** About Project Slug
>  - A slug is part of an app URL, and cannot be changed later. 
>  - App URLs follow this pattern: *<ins>{username}.pyweb.io/{project_slug}/{folder_name}/{python_filename}</ins>* (See more details in the section of "App URL rule")

- Once a project is created successfully, you can click its name and enter `App Builder Page`.

  <img src="https://github.com/pywebio/pyweb.io-collateral/blob/main/app_builder/images/project_page.png?raw=true" width="400">


### 2. Create a new app file and select it in `File Manager`
- In `App Builder Page`, use `File Manager` UI (in the pop-up window brought up by the 📁 button) to add/delete/rename files and folders.
    <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/file_manager.png" width="400">

- Make sure to add correct file extension names. Only `.py` files can be run as PyWebIO apps. Other files types, e.g. TXT, CSV, JSON, can be created and saved, but they are not runnable.
- To open a file, click its name.


### 3. Develop your app in `Cloud IDE`
- Open a `.py` file, start typing your own code or paste the following one. Each PyWebIO app file must include a `main()` function that runs as the app. Running a `.py` file without `def main():` will only save the file but not start an app.

    ```python
    from pywebio.output import *
    from pywebio.input import *

    def main():
        '''
        An interactive web app that takes user's name 
        and output hello <username> on the webpage
        '''
        put_markdown('# My first PyWebIO App')
        username = input('Input your name')
        put_text('Hello, %s' % username)
    ```
- **Remove or comment out `start_server(main, port=...)` before the next step.** `App Builder` manages all hosting configurations.
- Click `Save & Run` button to test the app. Your app's test version now runs in the right panel.

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/hello_app.png" width="500">

- More demo code: https://github.com/pywebio/demos

### 4. One-button-click `Launch` to cloud
- Once you are happy with the test result, it's time to launch it. Simply click the `Launch` button on the upper right corner.

- After a page is launched, there're some changes indicating its launching status:
  - Two new buttons show up next to the `Launch` button. The left one is for you to copy the public URL of the page. The other one is to unluanch the page.
    
    <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/buttons.png" width="81">
  - In `File Manager`, a 🚀 icon appears next to the file name. In the following example, *welcome.py* has been launched, whereas *hello.py* has not.
    
    <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/luanch_status.png" width="150">

## Multi-Page App

### What a multi-page app looks like

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/multipage.png" width="500">

### The concept of `page` in PyWebIO 
- Every `.py` file using PyWebIO modules to define I/O can be a `page`.
- State sharing among pages can use URL query parameters. An example of using `eval_js()` to extract URL queries:
  ```python
  from pywebio.session import eval_js

  # `query` is a dict
  query = eval_js("Object.fromEntries(new URLSearchParams(window.location.search))")
  ```

### How to build one (Release soon)
> We're working on it, and will release it soon.

### URL rule



## The `Function to App` Button

It converts a Python function to a web app. It can be used to create a simple app, a GUI app of an API, and more.

### How to use

1. Define a function in the IDE.

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/f2a-1.png" width="600">

2. Click the `Function to App` button.

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/f2a-2.png" width="600">

3. Config inputs and outputs, and test run the app.

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/f2a-3.png" width="600">

4. The app function is generated and saved in the file, and ready to launch.

  <img src="https://raw.githubusercontent.com/pywebio/pyweb.io-collateral/main/app_builder/images/f2a-4.png" width="600">

## Platform Supported Modules 
> You can manage your own dependencies soon.
"""

# PyWebIO App function
def main():
    '''
    pyweb.io app builder onboarding
    
    A quick onboarding instruction for new users on pyweb.io platform
    '''
    # To display the onboarding instructions
    md_content = md_formatter(md)
    put_markdown('# 👋 Welcome to `App Builder`!')
    put_collapse('Table of Content', put_markdown(md_content.toc), open=True)
    put_markdown(md_content.content)

    # To display supported module list
    module_list =[m for m in list(s.modules.keys()) if all(c not in m for c in '._')]
    module_list.sort()
    put_scrollable(put_text('    '.join(module_list)), height=150, keep_bottom=True)
