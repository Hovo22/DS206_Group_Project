-- update_fact_Orders.sql
INSERT INTO Orders_Dimensional_DB.dbo.FactOrders (OrderID, ProductID, UnitPrice, Quantity, Discount)
SELECT OrderID, ProductID, UnitPrice, Quantity, Discount
FROM Orders_Relational_DB.dbo.OrderDetails;
