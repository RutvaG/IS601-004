CREATE TABLE
    IF NOT EXISTS IS601_S_Products(
        id int AUTO_INCREMENT PRIMARY KEY,
        name varchar(30) UNIQUE,
        description text,
        category VARCHAR(30),
        stock int DEFAULT 0,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        unit_price float(5,2) DEFAULT 999.99,
        check (stock >= 0),
        check (unit_price >= 0) 
    )