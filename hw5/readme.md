написать код на пролог - сумма всех элементов массива

summa_array([], 0).   
summa_array([X|T], Sum) :-
  summa_array(T, SUM1),    
  Sum is X + SUM1. 
