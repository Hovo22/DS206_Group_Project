INSERT INTO Orders_Dimensional_DB.dbo.Region_Dim (RegionID, RegionDescription)
SELECT RegionID, RegionDescription
FROM Orders_Relational_DB.dbo.Region;
