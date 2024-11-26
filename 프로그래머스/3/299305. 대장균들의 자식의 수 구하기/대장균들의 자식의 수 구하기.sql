-- 코드를 작성해주세요
# 방법 1
# SELECT 
#     E1.ID, 
#     COUNT(E2.ID) AS CHILD_COUNT
# FROM ECOLI_DATA AS E1
# LEFT JOIN ECOLI_DATA AS E2 ON E1.ID = E2.PARENT_ID
# GROUP BY E1.ID
# ORDER BY E1.ID;

# 방법 2
SELECT 
    ID,
    (SELECT COUNT(*) FROM ECOLI_DATA WHERE PARENT_ID = ED.ID) AS CHILD_COUNT
FROM ECOLI_DATA AS ED
ORDER BY ED.ID;
