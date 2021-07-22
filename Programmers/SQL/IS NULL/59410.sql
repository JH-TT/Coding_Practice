-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IF(NAME IS NULL, "No name", NAME), SEX_UPON_INTAKE FROM ANIMAL_INS
ORDER BY ANIMAL_ID
-- type, name, sex_upon_intake를 출력하되, 이름이 NULL이면 No name으로 출력하도록 해라.