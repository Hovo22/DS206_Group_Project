INSERT INTO Orders_Dimensional_DB.dbo.Suppliers_Dim (SupplierID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, HomePage)
SELECT SupplierID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, HomePage
FROM Orders_Relational_DB.dbo.Suppliers;
