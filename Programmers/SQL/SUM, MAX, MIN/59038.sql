-- 코드를 입력하세요
SELECT DATETIME FROM ANIMAL_INS
WHERE DATETIME = (SELECT min(DATETIME) FROM ANIMAL_INS)
-- 가장 먼저 들어온 동물 출력(날짜 최솟값 출력)
-- 비슷한 코드는 59415번과 비슷하게 하면 될 듯(오름차순으로 정렬하고 limit이용).