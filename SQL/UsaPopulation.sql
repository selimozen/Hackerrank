--Eng: Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
-- Tr: 100.000'in üzerinde nüfusu olan ABD şehilerini seçiniz.
SELECT * FROM CITY WHERE 
    COUNTRYCODE = 'USA' 
    AND POPULATION > 100000;
