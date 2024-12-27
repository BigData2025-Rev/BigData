USE dec23;
DROP TABLE IF EXISTS bankaccounts;

CREATE TABLE bankaccounts(account_no varchar(20) PRIMARY KEY NOT NULL,
 funds decimal(8,2)
 );
 
 INSERT INTO bankaccounts VALUES ('ACC1', 1000);
 INSERT INTO bankaccounts VALUES ('ACC2', 1000);
 
 START Transaction;
 UPDATE bankaccounts SET funds = funds -100 WHERE account_no='ACC1';
 UPDATE bankaccounts SET funds = funds +100 WHERE account_no='ACC2';
 Commit;
 
 SELECT * FROM bankaccounts;
 
 START Transaction;
 INSERT INTO bankaccounts VALUES ('ACC3',10000);
 SAVEPOINT sv;
 INSERT INTO bankaccounts VALUES ('ACC4', 900000);
 rollback TO sv;
 INSERT INTO bankaccounts VALUES('ACC4',90000);
 COMMIT;
 
 SELECT * FROM bankaccounts;
 
 
