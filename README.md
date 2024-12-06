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