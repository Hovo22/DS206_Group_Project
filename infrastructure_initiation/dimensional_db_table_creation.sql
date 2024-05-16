USE ORDERS_DIMENSIONAL_DB;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS FactOrders;
DROP TABLE IF EXISTS DimCategories;
DROP TABLE IF EXISTS DimCustomers;
DROP TABLE IF EXISTS DimEmployees;
DROP TABLE IF EXISTS DimProducts;
DROP TABLE IF EXISTS DimRegion;
DROP TABLE IF EXISTS DimShippers;
DROP TABLE IF EXISTS DimSuppliers;
DROP TABLE IF EXISTS DimTerritories;

-- Create dimension tables
CREATE TABLE DimCategories (
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryName NVARCHAR(255),
    Description NVARCHAR(1000)
);

CREATE TABLE DimCustomers (
    CustomerSK INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID NVARCHAR(255),
    CompanyName NVARCHAR(255),
    ContactName NVARCHAR(255),
    ContactTitle NVARCHAR(255),
    Address NVARCHAR(255),
    City NVARCHAR(255),
    Region NVARCHAR(255),
    PostalCode NVARCHAR(20),
    Country NVARCHAR(255),
    Phone NVARCHAR(20),
    Fax NVARCHAR(20),
    EffectiveDate DATETIME,
    ExpiryDate DATETIME,
    IsCurrent BIT
);

CREATE TABLE DimEmployees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    LastName NVARCHAR(255),
    FirstName NVARCHAR(255),
    Title NVARCHAR(255),
    TitleOfCourtesy NVARCHAR(50),
    BirthDate DATE,
    HireDate DATE,
    Address NVARCHAR(255),
    City NVARCHAR(255),
    Region NVARCHAR(255),
    PostalCode NVARCHAR(10),
    Country NVARCHAR(255),
    HomePhone NVARCHAR(255),
    Extension NVARCHAR(10),
    Notes TEXT,
    ReportsTo INT,
    PhotoPath NVARCHAR(255),
    IsDeleted BIT
);

CREATE TABLE DimProducts (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit NVARCHAR(255),
    UnitPrice FLOAT,
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BIT
);

CREATE TABLE DimRegion (
    RegionID INT IDENTITY(1,1) PRIMARY KEY,
    RegionDescription NVARCHAR(255)
);

CREATE TABLE DimShippers (
    ShipperID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyName NVARCHAR(255),
    Phone NVARCHAR(20),
    IsDeleted BIT
);

CREATE TABLE DimSuppliers (
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyName NVARCHAR(255),
    ContactName NVARCHAR(255),
    ContactTitle NVARCHAR(255),
    Address NVARCHAR(255),
    City NVARCHAR(100),
    Region NVARCHAR(100),
    PostalCode NVARCHAR(20),
    Country NVARCHAR(100),
    Phone NVARCHAR(100),
    Fax NVARCHAR(20),
    HomePage NVARCHAR(255),
    PriorContactName NVARCHAR(255)  -- SCD3 specific column
);

CREATE TABLE DimTerritories (
    TerritoryID NVARCHAR(10) PRIMARY KEY,
    TerritoryDescription NVARCHAR(255),
    RegionID INT,
    EffectiveDate DATETIME,
    ExpiryDate DATETIME,
    IsCurrent BIT
);

-- Create fact table
CREATE TABLE FactOrders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerSK INT,
    EmployeeSK INT,
    OrderDate DATE,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipperSK INT,
    Freight DECIMAL(19,4),
    TotalAmount DECIMAL(19,4)
);
