/*
* Author: donsky
* Org: www.donskytech.com
* Purpose:  Test Database for IOT Projects
*/
CREATE TABLE Students (
 student_id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 rf_id_code TEXT NOT NULL UNIQUE
);