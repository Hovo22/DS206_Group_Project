INSERT INTO Orders_Dimensional_DB.dbo.Shippers_Dim (ShipperID, CompanyName, Phone)
SELECT ShipperID, CompanyName, Phone
FROM Orders_Relational_DB.dbo.Shippers;
