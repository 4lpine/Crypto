import sys, colorama 
from msvcrt import getch
from colorama import Fore
colorama.init()

def better_input(in_string, arguments):
    buffer = [];buffer.insert(0, in_string)
    while(True):
        try:guess = min(guesses).removeprefix(strbuffer);sys.stdout.write(' '*(len(guess)+len(buffer))+'\r'+''.join(buffer)+f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{guess}{Fore.RESET}")
        except:sys.stdout.write(' '*len(buffer)+'\r'+''.join(buffer))
        try:
            if char == '\t':sys.stdout.write(' '*(len(guess)+len(buffer))+'\r'+''.join(buffer)+guess);[buffer.append(letter) for letter in guess]
        except UnboundLocalError:pass
        guesses = [];char = getch().decode('latin1')
        if char not in ['\x08', "\t", "\x03"]:buffer.append(char)
        if char == "\x03":print(f"{Fore.RESET}\n^C{Fore.RESET}");sys.exit()
        if char == '\r':sys.stdout.write(" " * len(buffer) + "\r" + ''.join(buffer) + "\n");buffer.remove("\r");return ''.join(buffer).removeprefix(in_string);break
        if char == '\x08':
            buffer.reverse()
            if buffer[0] != in_string:buffer.remove(buffer[0]) 
            buffer.reverse()
            sys.stdout.write(" " * len(buffer)  + "\r" + ''.join(buffer));continue
        strbuffer = ''.join(buffer).removeprefix(in_string)
        for word in arguments:      
            if len(word) >= len(strbuffer):
                if word.startswith(strbuffer):
                    if word not in guesses:
                        guesses.append(word)
