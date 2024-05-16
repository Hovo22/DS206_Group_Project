-- update_dim_Customers.sql
INSERT INTO Orders_Dimensional_DB.dbo.Customers_Dim (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax
FROM Orders_Relational_DB.dbo.Customers;
