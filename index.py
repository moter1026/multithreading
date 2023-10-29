from multiprocessing import Process
import os

separators = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "~", "`", "'", "\"", "/", "?", ".", ",", "<", ">", "\\", "|", "]", "[", "{", "}", "\n", "\t"]

def finder(file, key_word):
    with open(file[1], "r") as TextFile:
        index = 0
        key_len = len(key_word)
        while 1:
            str_file = TextFile.read()
            index = str_file.find(key_word)
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
    print("Вы можете выбрать до " + str(len(all_files)) + " файлов, в которых будет происходить поиск ключевого слова.")
    print("\nФайлы называются так: \"0001.txt\",\"0002.txt\", ... ,\"0010.txt\",\"0011.txt\", ... ,\"0100.txt\",\"0101.txt\", ...")
    print("\n\nВведите названия интересующих файлов: ")
    files = []
    index = 0
    while 1:
        print("Если закончили вводить названия, то введите 0")
        file = str(input())
        if(file == "0" or index == len(all_files)):
            break;
        if not(file in all_files) or (file in files):
            print("Такого файла не существует или его уже добавили!!!")
            continue;
        files.append(file)
        index += 1
    print("Вы будете искть в  " + str(files))

    print("\n\n Введите ключевое слово...")
    key_word = input()
    procs = []
    
    for file in enumerate(files):
        proc = Process(target=finder, args=(file,key_word))
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()

    input('Press ENTER to exit') 