import random
import pickle



def read_lib(q_file):
    """Builds library list => [('quote','author'),...] from a txt file
    with alternating quote and attribution lines, starting with a quote."""
    qu= ''
    au= ''
    f = open(q_file)
    for line in f.readlines():
        # if there is a quote and author line assigned to au, qu vars...
        if qu and au:
            # append a (quotestring, attributionstring) tuple to lib data object
            lib.append((qu,au))
            qu = au = ''
        # as every other line is a quote, if au is unnassigned and the
        # previous line was a quote, then the current line must be an attribution.
        elif qu:
            au += line
        else:
            qu += line

def ranksort(tup, dictn):
    return dictn[tup]

def sort_and_write(q_list):
    write_list = sorted(q_list, key=ranksort)
    f = open('/home/nathan/Python/projects/quotes/data.txt', 'w')
    for tup in write_list:
        f.write(str(tup[0])+'\n')
        f.write(str(tup[1]+'\n')
    
def Quoth(lib):
    """Prints two library tuples and then gives a raw_input prompt to choose between them.
    chosen quote gets two added to its rank; quote not chosen has one subtracted."""
    while True:
        cont = raw_input('Another? Y/N')
        if cont.upper() == 'N':
            break
        else:
            maxint = len(lib) - 1
            i = random.randint(0, maxint)
            j = random.randint(0, maxint)
        print '1. "%s"'+'\n-%s' % (lib[i][0], lib[i][1])
        print '2. "%s"'+'\n-%s' % (lib[j][0], lib[j][1])
        action = raw_input('Which quote would win in an argument? 1 or 2?')
        if action == '1':
            ranks[lib[i]]+=2
            ranks[lib[j]]-=1 
        else:
            ranks[lib[j]]+=2
            ranks[lib[i]]-=1
        
def quote():
    q_string = raw_input('Quote?')
    a_string = raw_input('Quoth...')
    new_tup = (q_string, a_string)
    lib.append(new_tup)
    ranks[new_tup] = 2
    print 'Quote by %s added at rank: %d' % (a_string, ranks[new_tup])

