INSERT INTO workforce_department VALUES (null, 'HR', 2000);
INSERT INTO workforce_department VALUES (null, 'Sales', 4000);
INSERT INTO workforce_department VALUES (null, 'Administration', 3000);

INSERT INTO workforce_employee VALUES (null, 'Amy', 'Adams', "1999-03-03", 0, 1);
INSERT INTO workforce_employee VALUES (null, 'Blake', 'Bills', "2005-06-07", 0, 2);
INSERT INTO workforce_employee VALUES (null, 'Cat', 'Crescent', "2018-02-08", 0, 3);

INSERT INTO workforce_trainingprogram VALUES (null, 'Intro to SQL', "2019-01-28", "2019-01-30", 25);
INSERT INTO workforce_trainingprogram VALUES (null, 'Building with React', "2019-02-10", "2019-02-15", 50);
INSERT INTO workforce_trainingprogram VALUES (null, 'C# for idiots', "2019-02-19", "2019-02-20", 13);

INSERT INTO workforce_computer VALUES (null, "HP", "2019-01-24", "2022-01-24");
INSERT INTO workforce_computer VALUES (null, "APPLE", "2019-01-01", "2022-01-01");
INSERT INTO workforce_computer VALUES (null, "lenovo", "2018-12-29", "2021-12-29");

INSERT INTO workforce_computeremployee VALUES (null, 1, 3);
INSERT INTO workforce_computeremployee VALUES (null, 2, 2);
INSERT INTO workforce_computeremployee VALUES (null, 3, 1);

INSERT INTO workforce_employeetrainingprogram VALUES (null, 3, 1);
INSERT INTO workforce_employeetrainingprogram VALUES (null, 2, 2);
INSERT INTO workforce_employeetrainingprogram VALUES (null, 1, 3);