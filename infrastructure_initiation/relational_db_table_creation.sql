USE ORDERS_RELATIONAL_DB;

DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Shippers;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Territories;
DROP TABLE IF EXISTS Region;

CREATE TABLE Categories (
    CategoryID INT NOT NULL,
    CategoryName VARCHAR(255),
    Description VARCHAR(1000)
);

CREATE TABLE Customers (
    CustomerID NVARCHAR(255) PRIMARY KEY,
    CompanyName NVARCHAR(255),
    ContactName NVARCHAR(255),
    ContactTitle NVARCHAR(255),
    Address NVARCHAR(255),
    City NVARCHAR(255),
    Region NVARCHAR(255),
    PostalCode NVARCHAR(20),
    Country NVARCHAR(255),
    Phone NVARCHAR(20),
    Fax NVARCHAR(20)
)
CREATE TABLE Employees (
    EmployeeID INT NOT NULL,
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
    ReportsTo FLOAT,
    PhotoPath VARCHAR(255)
);

CREATE TABLE OrderDetails (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    UnitPrice FLOAT,
    Quantity INT,
    Discount FLOAT,
);


CREATE TABLE Orders (
    OrderID INT NOT NULL,
    CustomerID VARCHAR(10),
    EmployeeID INT,
    OrderDate DATE,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipVia INT,
    Freight FLOAT,  
    ShipName VARCHAR(255),
    ShipAddress VARCHAR(255),
    ShipCity VARCHAR(100),
    ShipRegion VARCHAR(50), 
    ShipPostalCode VARCHAR(20),  
    ShipCountry VARCHAR(50),
    TerritoryID VARCHAR(10)          
);

CREATE TABLE Products (
    ProductID INT NOT NULL,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit VARCHAR(255),
    UnitPrice FLOAT, 
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BIT
);


CREATE TABLE Region (
    RegionID INT NOT NULL,
    RegionDescription VARCHAR(255) 
);

CREATE TABLE Shippers (
    ShipperID INT NOT NULL,
    CompanyName VARCHAR(255),
    Phone VARCHAR(20)        
);

CREATE TABLE Suppliers (
    SupplierID INT NOT NULL,
    CompanyName VARCHAR(255),
    ContactName VARCHAR(255),
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(100),
    Fax VARCHAR(20),
    HomePage VARCHAR(255)
);


CREATE TABLE Territories (
    TerritoryID VARCHAR(10) NOT NULL,  
    TerritoryDescription VARCHAR(255),
    RegionID INT
);


















































































