-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
AND NAME LIKE '%el%'
ORDER BY NAME
-- 동물중에 이름이 el을 포함하는 개를 출력해라.