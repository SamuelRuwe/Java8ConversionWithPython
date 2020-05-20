with open('Main.java', 'r') as rf:
    with open('test_copy.java', 'w') as wf:
        with open('Java8to11Dictionary.txt', 'r') as dictFile:
            dict = {}
            for line in dictFile:
                (key, val) = line.split()
                dict[str(key)] = val
            # print(dict)
            for line in rf:
                for key in dict:
                    testString = key
                    a = line.lower()
                    pos = a.find(testString)
                    if pos != -1:
                        newString = dict[key]
                        b = line[0:pos]
                        c = line[(pos+len(testString)):-1]
                        wf.write(str(b) + str(newString) + str(c) + str('\n'))
                        break
                    elif dict[key] == "eof":
                        wf.write(line)

#optimize this code by checking package names in alphabetical order

# with open('Text.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#             a = wf.name.split('.')[0]
#             print(a)
#