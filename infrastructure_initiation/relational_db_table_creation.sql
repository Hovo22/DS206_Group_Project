USE ORDERS_RELATIONAL_DB;

DROP TABLE IF EXISTS Categories;
CREATE TABLE Categories (
    CategoryID INT,
    CategoryName VARCHAR(255),
    Description VARCHAR(1000)
);


DROP TABLE IF EXISTS Customers;
CREATE TABLE Customers (
    CustomerID VARCHAR(10),
    CompanyName VARCHAR(255),
    ContactName VARCHAR(255),
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode VARCHAR(10),
    Country VARCHAR(255),
    Phone VARCHAR(255),
    Fax VARCHAR(255)
);


DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    EmployeeID INT,
    LastName VARCHAR(255),
    FirstName VARCHAR(255),
    Title VARCHAR(255),
    TitleOfCourtesy VARCHAR(50),
    BirthDate DATE,
    HireDate DATE,
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode VARCHAR(10),
    Country VARCHAR(255),
    HomePhone VARCHAR(255),
    Extension VARCHAR(10),
    Notes TEXT,
    ReportsTo INT,
    PhotoPath VARCHAR(255)
);

DROP TABLE IF EXISTS OrderDetails;
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    UnitPrice DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(5, 5)
);


DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    OrderID INT,
    CustomerID VARCHAR(10),
    EmployeeID INT,
    OrderDate DATE,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipVia INT,
    Freight DECIMAL(10, 2),  
    ShipName VARCHAR(255),
    ShipAddress VARCHAR(255),
    ShipCity VARCHAR(100),
    ShipRegion VARCHAR(50), 
    ShipPostalCode VARCHAR(20),  
    ShipCountry VARCHAR(50),
    Territory INT          
);

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit VARCHAR(255),
    UnitPrice DECIMAL(10, 2), 
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BIT
);


DROP TABLE IF EXISTS Region;
CREATE TABLE Region (
    RegionID INT,
    RegionDescription VARCHAR(255) 
);

DROP TABLE IF EXISTS Shippers;
CREATE TABLE Shippers (
    ShipperID INT,
    CompanyName VARCHAR(255),
    Phone VARCHAR(20)        
);

DROP TABLE IF EXISTS Suppliers;
CREATE TABLE Suppliers (
    SupplierID INT,
    CompanyName VARCHAR(255),
    ContactName VARCHAR(255),
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    HomePage VARCHAR(255)
);


DROP TABLE IF EXISTS Territories;
CREATE TABLE Territories (
    TerritoryID VARCHAR(10),  
    TerritoryDescription VARCHAR(255),
    RegionID INT
);


