-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID # 두개의 조건이 일치하는 케이스로 묶음
HAVING COUNT(USER_ID) > 1 # 각 행이 1개 이상인 경우에만 출력
ORDER BY USER_ID ASC, PRODUCT_ID DESC;