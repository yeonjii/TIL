-- 데이터 조회 : SELECT 컬럼명 FROM 테이블명;
SELECT * FROM examples;


-- 1. DDL (Data Definition Language)

-- 테이블 생성
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  addresss TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

-- ALTER
-- 테이블명 변경
ALTER TABLE articles
RENAME TO news;

-- 컬럼 추가 (NOT NULL 제약조건 필요)
ALTER TABLE news
ADD COLUMN created_at TEXT;

ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;



-- DML (Data Manioulation Language)   /* 가장 많이 사용 */

-- 데이터 추가
INSERT INTO classmates(name, age)
VALUES('홍길동',23);

-- 모든 열에 데이터를 넣을 땐 컬럼 생략 가능
INSERT INTO classmates
VALUES('홍길동', 30, '서울');

-- 데이터 조회 : SELECT 컬럼명 FROM 테이블명;
SELECT * FROM classmates;

-- PRIMARY KEY를 지정하지 않으면 rowid가 생성된다.
SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;

-- LIMIT : 몇 개 갖고 올건지
SELECT rowid, name FROM classmates LIMIT 1;

-- LIMIT & OFFSET : 특정한 위치부터 몇 개 갖고 올건지
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

-- WHERE :  조건
SELECT rowid, name FROM classmates WHERE address='광주';

-- DISTINCT : 중복 제거
SELECT DISTINCT address FROM classmates;

-- 데이터 삭제 : DELETE
-- 기본적으로 rowid(PK)를 기준으로 삭제한다
DELETE FROM classmates 
WHERE rowid=4;

-- 데이터 수정 : UPDATE
UPDATE classmates
SET name='홍길동', address='제주'
WHERE rowid=1;

-- WHERE 문 심화
SELECT * FROM users WHERE age>=30;

SELECT age, last_name
FROM users
WHERE age>=30 and last_name='김';


-- Expressions (표현식)
 SELECT COUNT(*) FROM users;  

-- AGV
SELECT AVG(age)
FROM users
WHERE age >= 30;

SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age >=30;


SELECT * FROM users WHERE phone LIKE '02-%';

-- ORDER
SELECT * 
FROM users 
ORDER BY age ASC LIMIT 10;

-- 나이가 같으면 성 순으로 정렬
SELECT * 
FROM users 
ORDER BY age, last_name ASC LIMIT 10;