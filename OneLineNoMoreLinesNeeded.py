# OneLine
# OneLine is a programming language, where everything is in one line. Note: This line can get LONG.
# Think about your line of code as characters in a line in 1 dimension.

def run(code, debug_on=False, step_on = False):
    def debug(special=''):
        if debug_on:
            print(code)
            print((' '*(pointer))+'^', pointer, STACK, VARIABLE, special)
    STACK = []
    VARIABLE = None
    pointer = 0
    while code[pointer] != 's':
        command = code[pointer]
        if command == 's': # stop program instantly
            break

        elif command == 'ˇ': # push next char to STACK
            if code[pointer+1] == '{':
                STACK.append('\n')
            elif code[pointer+1] == '}':
                STACK.append('\t')
            else:
                STACK.append(code[pointer+1])
            pointer += 2
        elif command == 'p': # push next 4 char as a number to STACK
            STACK.append(float(code[pointer+1:pointer+5]))
            pointer += 5

        elif command == 'i': # invert STACK
            STACK.reverse()
            pointer += 1
        elif command == 'c': # duplicates last item in STACK
            STACK.append(STACK[-1])
            pointer += 1
        elif command == '+': # + last 2 STACK
            if not ((type(STACK[-1]) == type('') and type(STACK[-2]) == type(1.0)) or (type(STACK[-1]) == type(1.0) and type(STACK[-2]) == type(''))):
                STACK.append(STACK[-1]+STACK[-2])
                STACK.pop(-2)
                STACK.pop(-2)
            pointer += 1
        elif command == '-': # last - second to last STACK
            if type(STACK[-1]) == type(STACK[-2]) == type(1.0):
                STACK.append(STACK[-1]-STACK[-2])
                STACK.pop(-2)
                STACK.pop(-2)
            pointer += 1
        elif command == '*': # * last 2 STACK
            if not (type(STACK[-1]) == type(STACK[-2]) == type('')):
                STACK.append(STACK[-1]*STACK[-2])
                STACK.pop(-2)
                STACK.pop(-2)
            pointer += 1
        elif command == '/': # last / second to last STACK
            if type(STACK[-1]) == type(STACK[-2]) == type(1.0):
                STACK.append(STACK[-1]/STACK[-2])
                STACK.pop(-2)
                STACK.pop(-2)
            pointer += 1
        elif command == '%': # last % second to last STACK
            if type(STACK[-1]) == type(STACK[-2]) == type(1.0):
                STACK.append(STACK[-1]%STACK[-2])
                STACK.pop(-2)
                STACK.pop(-2)
            pointer += 1

        elif command == '^': # pop and print last item of STACK
            print(STACK.pop(), end='')
            pointer += 1
        elif command == 'r': # pop and print last item of STACK
            STACK.pop()
            pointer += 1
        elif command == 'd': # pop last item in STACK, if item > 0 or type(item) == type(''), pointer += 2, otherwise pointer += 1
            temp = STACK.pop()
            if type(temp) == type(1.0):
                if temp > 0.0:
                    debug('BEFORE d SWITCH')
                    pointer += 2
                elif temp <= 0.0:
                    debug('BEFORE d SWITCH')
                    pointer += 1
            else:
                debug('BEFORE d SWITCH')
                pointer += 2
            debug('AFTER d SWITCH')
        elif command == 'n': # pop last item in STACK, move pointer last item times, except at 0, move there 1 time
            temp = STACK.pop()
            if type(temp) == type(1.0):
                if temp == 0:
                    debug('BEFORE n SWITCH')
                    pointer += 1
                else:
                    try:
                        debug('BEFORE n SWITCH')
                        pointer += int(temp)
                    except:
                        pass
            elif type(temp) == type(''):
                if len(temp) == 1:
                    debug('BEFORE n SWITCH')
                    pointer += ord(temp)
            debug('AFTER n SWITCH')

        elif command == '>': # take user input and push it to STACK
            STACK.append(input())
            pointer += 1
        elif command == '$': # take user input and if it is numeric push it to as float STACK else push it to STACK
            temp = input()
            if temp.isdigit():
                STACK.append(float(temp))
            else:
                STACK.append(temp)
            pointer += 1
        elif command == 'w': # write/print next 8 characters
            print(code[pointer+1:pointer+9], end='')
            pointer += 9
        elif command == 'j': # reads next 4 characters and makes the pointer jump by that amount
            debug('BEFORE j')
            pointer += int(code[pointer+1:pointer+5])
            debug('AFTER j')
        elif command == '#':
            VARIABLE = STACK.pop()
            pointer += 1
        elif command == '@':
            STACK.append(VARIABLE)
            pointer += 1
        elif command == '&':
            print(VARIABLE, end='')
            pointer += 1
        elif command == '.':
            VARIABLE += 1.0
            pointer += 1
        elif command == ',':
            VARIABLE -= 1.0
            pointer += 1
        elif command == ':':
            VARIABLE += STACK.pop()
            pointer += 1

        elif command == '=':
            if STACK.pop() == STACK.pop():
                pointer += 2
            else:
                pointer += 1
        elif command == '?':
            temp = input()
            for i in temp:
                STACK.append(i)
            pointer += 1
        elif command == '}':
            STACK.append(float(STACK.pop()))
            pointer += 1
        elif command == ')':
            STACK.append(str(STACK.pop()))
            pointer += 1
        else:
            if command.isupper() and command.isalpha(): # uppercase letter
                found_pair = False
                for i in range(len(code)):
                    if i != pointer and code[i] == code[pointer] and not found_pair:
                        pointer = i+1
                        found_pair = True
                        debug('UPPERCASE')
            else:
                pointer += 1

        if pointer == len(code):
            break

        debug('AFTER RUN')
        if step_on:
            if input().lower() == 'exit':
                break
def main():
    run_program = True
    while run_program:
        code = input('\nOneLine (to choose by options, type nothing and press enter)\n> ')
        if code == '':
            userinput = input('Normal mode (type "normal")\nDebug mode (type "debug")\nStep-by-step normal mode (type "step", when in mode, press enter to step, to exit running code type "exit" and press enter)\nStep-by-step debug mode (type "stepdebug", when in mode, press enter to step, to exit running code type "exit" and press enter)\nExit (type nothing)\n')
            if userinput.lower() == 'normal':
                run(input('> '))
            elif userinput.lower() == 'debug':
                run(input('> '), True)
            elif userinput.lower() == 'step':
                run(input('> '), step_on=True)
            elif userinput.lower() == 'stepdebug':
                run(input('> '), True, True)
            elif userinput == '':
                run_program = False
        else:
            run(code)
if __name__ == '__main__':
    main()