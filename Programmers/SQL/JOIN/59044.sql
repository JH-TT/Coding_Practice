-- 코드를 입력하세요
SELECT i.NAME, i.DATETIME FROM ANIMAL_INS i LEFT JOIN ANIMAL_OUTS o -- 보호 시작일 순으로 조회해야 한다고 했으니 ins를 기준으로 둬야함.
ON i.ANIMAL_ID = o.ANIMAL_ID -- id를 기준으로 봄.
WHERE o.ANIMAL_ID IS NULL -- 입양을 못 간 동물 추출.
ORDER BY i.DATETIME -- 가장 오래된 순으로 정렬
LIMIT 3 -- 그 중에 3개를 뽑음.
-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.