# Task 10
### Последовательность с фильтрацией.
Реализовать класс, соответствующий некоторой последовательности объектов и имеющий следующие методы:
- Создать объект на основе произвольного `iterable`-объекта
- Итерирование (`__iter__`)по элементам (неистощимое — можно несколько раз использовать объект в качестве `iterable` для `for`)
- Отфильтровать последовательность с помощью некоторой функции и вернуть новую сокращённую последовательность, в которой присутствуют только элементы, для которых эта функция вернула `True`
