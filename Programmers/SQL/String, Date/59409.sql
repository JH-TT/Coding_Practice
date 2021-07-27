-- 코드를 입력하세요
SELECT 
    ANIMAL_ID, NAME,
    CASE
    WHEN
        SEX_UPON_INTAKE LIKE '%Neutered%'
        OR SEX_UPON_INTAKE LIKE '%Spayed%'
    THEN 'O'
    ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- 동물 아이디와, 이름, 중성화 여부를 출력하되, 동물중에 중성화가 돼 있으면 중성화란에 'O'를 아니면 'X'를 출력하도록 해라.
-- 아이디순으로 출력.