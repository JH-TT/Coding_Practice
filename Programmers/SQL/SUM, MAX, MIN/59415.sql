-- 코드를 입력하세요
SELECT DATETIME as 시간 FROM ANIMAL_INS
where datetime = (select max(datetime) from animal_ins)
# ORDER BY DATETIME desc
# LIMIT 1
-- line 3 랑 line 4 중 어떤걸 써도 됨.(그런데 출제 의도는 max를 사용하는 것이기 때문에 line 3으로 가는게 맞을듯)
-- 이 문제는 가장 최근에 들어온 시간을 출력. 그래서 날짜별로 내림차순하고 그중에 가장 높은거 출력으로 해도됨.(line 4)
-- line 4, line 5 는 세트.
-- line 2에 "as 시간"은 datetime을 시간이라고 출력한다는거. 그런데 문제에선 굳이 시간으로 출력 안해도 된다함.(안써도 된다는 뜻)