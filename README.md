# CV Лабораторная работа №1
## Цель работы:
Научиться реализовывать один из простых алгоритмов обработки изображений.
Задание:
1. Реализовать программу согласно варианту задания. Базовый алгоритм, используемый в программе, необходимо реализовать в 2 вариантах: с использованием встроенных функций какой-либо библиотеки (OpenCV, PIL и др.) и нативно на Python или C++.
2. Сравнить быстродействие реализованных вариантов.
3. Сделать отчёт в виде readme на GitHub, там же должен быть выложен исходный код.

## Задание
Вариант 7 - Эрозия, примитив размера 3 на 3, бинаризацию можно не реализовывать вручную.

## Теоретическая база
<b>Эрозия</b> в компьютерном зрении – это метод обработки изображений, который уменьшает размеры светлых областей на бинарных изображениях. 

Основная идея этой операции заключается в том, чтобы "съедать" края объектов, используя структурный элемент или ядро, заданное пользователем. Эта операция помогает выделять формы, удалять шум и уточнять границы.

Во время работы эрозии каждый пиксель изображения проверяется на соответствие заданному ядру. Если ядро полностью помещается в текущей области (например, все активные элементы ядра совпадают с белыми пикселями изображения), то пиксель в центре этой области остаётся белым. В противном случае пиксель становится чёрным.

Эрозия применяется в задачах очистки изображений от мелких артефактов, улучшения контуров объектов, а также в комплексных морфологических операциях, где она часто комбинируется с дилатацией для получения более точных результатов.

![alt text](https://github.com/Okoyaki/CV-Lab1/blob/28c592f33cd3a3c7dbe518b3394e65835ee39d69/data/other/opening.png)

## Описание разработанной системы
В качестве алгоритмов реализации эрозии была взята функция ```cv2.erode``` из библиотеки ```opencv``` и отдельно написанная на библиотеке ```numpy``` функция. Бинаризация изображений проводилась с использованием метода Оцу, используя библиотеку ```opencv```.

Всего были обработаны 6 изображений:

1. <b>Обычные цветные изображения</b> 

![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/img_rgb1.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/img_rgb2.png)

2. <b>Чернобелые изображения с шумом</b>

![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/noisy_img_gs1.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/noisy_img_gs2.png)

3. <b>Цветные изображения с шумом</b>

![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/noisy_img_rgb1.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/b6b82539496619334019598e7a073ef3b218bb8f/data/orig/noisy_img_rgb2.png)

В результате обработки конечные изображения сохранялись в папку ```data/eroded``` отдельно для двух функций.

## Результаты работы и тестирования системы
Сначала была проведена бинаризация исходных изображений используя функцию ```cv2.threshold``` с методом Оцу (```cv2.THRESH_OTSU```). 

![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img0.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img1.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img2.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img3.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img4.png)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/bin/bin_img5.png)

Далее полученные бинарные виды изображений были использованы для описанных выше алгоритмов:

### Алгоритм через библиотеку OpenCV
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img2.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img3.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img4.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/cv2/cv2_img5.jpg)

### Алгоритм через библиотеку Numpy
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img2.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img3.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img4.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab1/blob/16e2f566b17cc55e6ad852c8d9a9aac7e3df526d/data/eroded/native/native_img5.jpg)

## Выводы по работе
В результате выполнения работы можно сделать следующие выводы:

1. Результат обработки цветных зашумленных изображений хуже, чем чернобелых
2. Изображения с более высоким разрешением показали результаты лучше, чем с меньшим разрешением.