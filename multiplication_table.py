
def print_multiplaction_table(field):
    line = ""
    for i in range(0, field):
        line = ""
        for j in range(0, field):
            line += str((j*i) % field) + " "
        print(line)


def find_generators(mod):
    generators = []
    for j in range(1, mod):
        for i in range(1, mod):
            if pow(j, i, mod) == 1:
                # must go through all elements of the field before repeating 
                if i == (mod -1):
                    generators.append(j) 

                break

    return generators

print_multiplaction_table(19)
print("Generators: ",find_generators(19))