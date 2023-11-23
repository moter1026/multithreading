from multiprocessing import Process
import os
import sys


separators = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "~", "`", "'", "\"", "/", "?", ".", ",", "<", ">", "\\", "|", "]", "[", "{", "}", "\n", "\t"]

def finder(file, key_word):
    with open(file[1], "r") as TextFile:
        index = 0
        start = 0
        key_len = len(key_word)
        str_file = TextFile.read()
        while 1:
            # print("1.In ", file[1], "index: ", index)
            start = index
            index = str_file.find(key_word, start)
            # print("2.In ", file[1], "index: ", index)
            # print("key_word ", key_word)
            # print("str_file ", str_file)
            if ( index == -1 ) :
                break;
            elif(index == 0 and len(str_file) != key_len):
                if str_file[index + key_len] in separators:
                    break;
            elif(index == 0 and len(str_file) == key_len):
                break;
            elif(index != 0 or index != -1 and len(str_file) != key_len):
                if not(str_file[index - 1] in separators):
                    index = index + key_len;
                    continue;
                if not(str_file[index + key_len] in separators):
                    index = index + key_len;
                    continue;
                break;
        print(index);

 
 
if __name__ == '__main__':
    os.chdir("./text files")
    all_files = os.listdir()
    files = sys.argv[1:len(sys.argv)]
    print("Вы будете искть в  " + str(files))

    print("\n\nВведите ключевое слово...")
    key_word = input()
    procs = []
    
    for file in enumerate(files):
        proc = Process(target=finder, args=(file,key_word))
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()

    input('Press ENTER to exit') 