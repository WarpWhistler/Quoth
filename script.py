n = open('exercise.txt', 'r')

k = open('data.txt', 'w')



for line in n.readlines():
    print line
    action = raw_input('Q/A/D?')
    if action == 'Q':
        k.write(line)
    elif action == 'A':
        k.write(line[6:])
    else:
        pass
        
k.close()
n.close()
    
