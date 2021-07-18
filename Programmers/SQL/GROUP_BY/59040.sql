-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(ANIMAL_ID) count FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
-- 개와 고양이의 개체수를 나타내어라(단 고양이가 먼저 나오도록 할 것.)