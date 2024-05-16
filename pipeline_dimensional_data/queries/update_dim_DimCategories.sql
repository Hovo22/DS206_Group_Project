-- update_dim_Categories.sql
INSERT INTO Orders_Dimensional_DB.dbo.Categories_Dim (CategoryID, CategoryName, Description, Picture)
SELECT CategoryID, CategoryName, Description, Picture
FROM Orders_Relational_DB.dbo.Categories;
