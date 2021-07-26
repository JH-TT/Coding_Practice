-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME FROM ANIMAL_OUTS o
LEFT JOIN ANIMAL_INS i -- 어떤걸 해도 상관없을듯
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE LIKE '%intact%' -- intake를 포함하는 애들중에, sex_upon_intake와 sex_upon_outcome이 다른 동물(즉 나갈땐 intake를 포함하지 않아야함).
AND i.SEX_UPON_INTAKE != o.SEX_UPON_OUTCOME
-- WHERE i.SEX_UPON_INTAKE <> o.SEX_UPON_OUTCOME <- (line5와 line6을)이렇게 해도 맞았음. 근데 효율성이 떨어지는듯.
ORDER BY ANIMAL_ID -- 아이디를 기준으로 정렬.
-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.