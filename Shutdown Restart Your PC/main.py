import os
import sys

class System:

    def __init__(self,input_char):
        self.input_char=input_char

    def restart(self):
        os.system('shutdown /r')

    def shutdown(self):
        os.system('shutdown /s')

    def exit_prg(self):
        sys.exit()

print('Enter \'r\' for restart')
print('Enter \'s\' for shutdown')
print('Enter any char to exit from the program.')
input_char = input('Enter r|s: ')

system = System(input_char)
if input_char=='r':
    system.restart()
    
elif input_char=='s':
    system.shutdown()
    
else:
    system.exit_prg()
