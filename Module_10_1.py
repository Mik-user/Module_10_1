import time
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):
    with open (file_name,'w', encoding='utf-8')as file:
        for i in range(word_count):
            file.write(f'Слово № {i+1}\n')
            time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')
    return


func_time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words( 30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

print(f'Время работы потоков: {datetime.now()-func_time_start}')

func_time_start = datetime.now()

rez1 = Thread(wite_words(10,'example1.txt'))
rez2 = Thread(wite_words(30,'example2.txt'))
rez3 = Thread(wite_words(200,'example3.txt'))
rez4 = Thread(wite_words(100,'example4.txt'))

rez1.start()
rez2.start()
rez3.start()
rez4.start()

rez1.join()
rez2.join()
rez3.join()
rez4.join()


print(f'Время работы потоков: {datetime.now()-func_time_start}')