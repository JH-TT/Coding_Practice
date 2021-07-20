-- 코드를 입력하세요
SELECT HOUR(DATETIME) HOUR, count(*) count FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) < 20
GROUP BY HOUR
ORDER BY HOUR
-- 입양시간이 9시에서 20시 전까지 중에서 각 시간때 마다 입양 개체 수를 출력해라.