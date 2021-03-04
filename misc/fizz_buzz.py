modulo_list = [
  (3,"Fizz"),
  (5,"Buzz")
]

for i in range(1, 101):
    print_string = ""
    for mod in modulo_list:
        if i % mod[0] == 0:
            print_string += mod[1]

    if not print_string:
        print(i)
    else:
        print(print_string)
