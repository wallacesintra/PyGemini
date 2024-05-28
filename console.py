#!/usr/bin/env python3

import cmd
import os
# import sys

from testGemini import MyGeminiApi

from rich.console import Console
from rich.markdown import Markdown

gemini = MyGeminiApi()
console = Console()
# md = Markdown()


class MyPrompt(cmd.Cmd):
    intro = 'Welcome to the gemini console. Type help or ? to list commands.\n'
    prompt = 'PyGemini> '
    # file = None


    def do_exit(self, arg):
        'Exit the console'
        console.print("Goodbye, see you soon ...", style= "bold yellow")
        return True
    
    def do_hello(self, arg):
        'Say hello'
        print('Hello', arg)

    def do_generate(self, arg):
        'Generate content'
        print('Generating content for', arg)

        # console.print("Response: \n" + Markdown(gemini.generate(arg)) ,style="bold green")
        console.print(Markdown(gemini.generate(arg)), style="bold green")

    def do_clear(self, arg):
        'Clear the screen'
        os.system('clear')
    
        



if __name__ == '__main__':
    MyPrompt().cmdloop()

