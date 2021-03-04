def interpret(command):
    final = ['(']

    for char in command:
        if char.isalpha():
            if final[-1] in '(':
                final.pop()
            final.append(char)
        elif char == '(':
            if final[-1] == '(':
                final.pop()
            final.append(char)
        elif char == ')':
            if final[-1] == '(':
                final.pop()
                final.append('o')
        print(final)

    return ''.join(final)


command = "(al)G(al)()()G"
#Output
#"(alGalooG"
#Expected
#"alGalooG"
print(interpret(command))
