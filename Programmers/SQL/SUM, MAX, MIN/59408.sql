-- 코드를 입력하세요
SELECT count(distinct(NAME)) count FROM ANIMAL_INS
WHERE NAME is not NULL
-- 이름이 NULL이 아니며 중복을 제거한 총 마릿수.