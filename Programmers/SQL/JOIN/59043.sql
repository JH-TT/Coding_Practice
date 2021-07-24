-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME FROM ANIMAL_INS i
LEFT JOIN ANIMAL_OUTS o
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE o.DATETIME < i.DATETIME
ORDER BY i.DATETIME

-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
-- 정렬 기준을 보면, ANIMAL_INS 기준으로 JOIN돼야 한다는 것을 유추할 수 있다.