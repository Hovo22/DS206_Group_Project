INSERT INTO Orders_Dimensional_DB.dbo.Territories_Dim (TerritoryID, TerritoryDescription, RegionID)
SELECT TerritoryID, TerritoryDescription, RegionID
FROM Orders_Relational_DB.dbo.Territories;
