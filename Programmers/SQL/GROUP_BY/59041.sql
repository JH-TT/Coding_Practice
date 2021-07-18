-- 코드를 입력하세요
SELECT NAME, count(NAME) count FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
-- 동물 이름중에 같은 이름이 2번이상 쓰인 이름을 이름순으로 출력해라.
-- having은 group by이후에 작성하는 것. where처럼 쓰임.