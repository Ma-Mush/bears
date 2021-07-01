import zipfile
import cv2
import os
import numpy as np

def archive(name):
    ch = 0
    if zipfile.is_zipfile(name):
        try:
            fzip = zipfile.ZipFile(name)
            fzip.extractall(name)
            fzip.close()
            for file in [i for i in os.walk(f"./{name}/")][0][2]:
                img = cv2.imread(f'./{name}/{file}')
                img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                mask = cv2.inRange(img_hsv, (44, 10, 20), (60, 20, 80))
                position = np.unravel_index(np.argmax(mask), mask.shape)
                print(position)
                y=position[0]-100
                x=position[1]-100
                if (x, y) == (0, 0): 
                    continue
                else:
                    ch += 1
                    cv2.rectangle(img, (x,y), (x+200,y+200), (255, 0, 0), 20)
                    with zipfile.ZipFile(f"ret_{name}", "w") as zip:
                        zip.write(cv2.resize(img, (1920, 1080), interpolation = cv2.INTER_AREA))
            return True, ch, f"ret_{name}"
        except:
            return False, "Ошибка в архиве, необходимо отправить архив с фотографиями для поиска медведей"
    else:
        return False, "Ошибка, этот файл не является архивом"
