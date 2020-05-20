def create_updated_file(read_file):
    file_type = read_file.name.split('.')[1]
    dict_file = get_dict(file_type)
    # print(get_dict(file_type))
    dict = create_dict(dict_file)
    updated_file_copy = create_copied_file_name(read_file.name)
    with open(updated_file_copy, 'w') as wf:
        for line in read_file:
            for key in dict:
                testString = key
                a = line.lower()
                pos = a.find(testString)
                if pos != -1:
                    new_string = dict[key]
                    b = line[0:pos]
                    c = line[(pos+len(testString)):-1]
                    wf.write(str(b) + str(new_string) + str(c) + str('\n'))
                    break
                elif dict[key] == "eof":
                    wf.write(line)

def create_dict(file_name):
    dict = {}
    with open(file_name, 'r') as dictFile:
        for line in dictFile:
            (key, val) = line.split()
            dict[str(key)] = val
    return dict

def create_copied_file_name(file_name):
    a = file_name.split('.')[0]
    b = file_name.split('.')[1]
    new_name = str(a) + "_updated_copy." + str(b)
    return new_name

def get_dict(file_type):
    dict = {
        "java": "Java8to11PackageDictionary.txt",
        "properties": "Java8to11PropertiesDictionary.txt"
    }
    return (str(dict[file_type]))

with open('Main.java', 'r') as rf:
    create_updated_file(rf)

with open('application.properties', 'r') as rf:
    create_updated_file(rf)





























    # with open('test_copy.java', 'w') as wf:
    #     with open('Java8to11PackageDictionary.txt', 'r') as dictFile:
    #         dict = {}
    #         for line in dictFile:
    #             (key, val) = line.split()
    #             dict[str(key)] = val
    #         # print(dict)
    #         for line in rf:
    #             for key in dict:
    #                 testString = key
    #                 a = line.lower()
    #                 pos = a.find(testString)
    #                 if pos != -1:
    #                     newString = dict[key]
    #                     b = line[0:pos]
    #                     c = line[(pos+len(testString)):-1]
    #                     wf.write(str(b) + str(newString) + str(c) + str('\n'))
    #                     break
    #                 elif dict[key] == "eof":
    #                     wf.write(line)



#optimize this code by checking package names in alphabetical order

# with open('Text.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#             a = wf.name.split('.')[0]
#             print(a)
#