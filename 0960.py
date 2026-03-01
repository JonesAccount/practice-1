from os import system, name

newline = "\n"
prompt = ">>> "
output = print


class Utils:
    def clear(self):
        system('cls' if name == 'nt' else 'clear')
        

class Instruction:
    def menu(self):
        utils.clear()
        output(f"[1] Команды{newline}[2] Утилиты{newline}[3] Файловая система{newline}[4] Об WK-26{newline}")
        try:
            command = int(input("Input: "))
            if command == 1:
                self.commands()
        except:
            pass
    
    
    def commands(self):
        utils.clear()
        orders = ("terminal/term – терминал", "help – помощь")
        for el in orders:
            output(":", el, sep="")
        try:
            command = input(f"{newline}Enter")
            utils.clear()
            terminal()
        except:
            pass

def arithmetic(operation):
    try:
        output(eval(operation))
    except:
        pass
    
    
def terminal():
    output(f"Консольная система WK-26{newline}{"– " * 20}")
    output(f"Терминал | help для справки{newline}")
    while True:
        command = input(prompt)
        if command[0].isdigit() or command[1].isdigit() if len(command) > 1 else False:
            arithmetic(command)
        elif command.lower() == "help":
            instruction.menu()
        
            
            
instruction = Instruction()
utils = Utils()
terminal()