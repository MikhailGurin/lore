#**Draft: PostgreSQL**  


##Массивы
Массивы — это не множества; необходимость поиска определённых элементов в массиве может быть признаком неудачно 
сконструированной базы данных. Возможно, вместо массива лучше использовать отдельную таблицу, строки которой будут 
содержать данные элементов массива. Это может быть лучше и для поиска, и для работы с большим количеством элементов.