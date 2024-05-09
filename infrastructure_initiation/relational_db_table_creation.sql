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
    CustomerID VARCHAR(10) NOT NULL,
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
    ReportsTo INT,
    PhotoPath VARCHAR(255)
);

CREATE TABLE OrderDetails (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    UnitPrice DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(5, 5)
);


CREATE TABLE Orders (
    OrderID INT NOT NULL,
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
    TerritoryID VARCHAR(10)          
);

CREATE TABLE Products (
    ProductID INT NOT NULL,
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
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    HomePage VARCHAR(255)
);


CREATE TABLE Territories (
    TerritoryID VARCHAR(10) NOT NULL,  
    TerritoryDescription VARCHAR(255),
    RegionID INT
);

-- Adding Primary Key Constraints
ALTER TABLE Categories ADD CONSTRAINT PK_Categories PRIMARY KEY (CategoryID);
ALTER TABLE Customers ADD CONSTRAINT PK_Customers PRIMARY KEY (CustomerID);
ALTER TABLE Employees ADD CONSTRAINT PK_Employees PRIMARY KEY (EmployeeID);
ALTER TABLE OrderDetails ADD CONSTRAINT PK_OrderDetails PRIMARY KEY (OrderID, ProductID);
ALTER TABLE Orders ADD CONSTRAINT PK_Orders PRIMARY KEY (OrderID);
ALTER TABLE Products ADD CONSTRAINT PK_Products PRIMARY KEY (ProductID);
ALTER TABLE Region ADD CONSTRAINT PK_Region PRIMARY KEY (RegionID);
ALTER TABLE Shippers ADD CONSTRAINT PK_Shippers PRIMARY KEY (ShipperID);
ALTER TABLE Suppliers ADD CONSTRAINT PK_Suppliers PRIMARY KEY (SupplierID);
ALTER TABLE Territories ADD CONSTRAINT PK_Territories PRIMARY KEY (TerritoryID);

-- Adding Foreign Key Constraints
ALTER TABLE Employees ADD CONSTRAINT FK_Employees_Employees FOREIGN KEY (ReportsTo)
REFERENCES Employees (EmployeeID);

ALTER TABLE OrderDetails ADD CONSTRAINT FK_OrderDetails_Orders FOREIGN KEY (OrderID)
REFERENCES Orders (OrderID);
ALTER TABLE OrderDetails ADD CONSTRAINT FK_OrderDetails_Products FOREIGN KEY (ProductID)
REFERENCES Products (ProductID);

ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Customers FOREIGN KEY (CustomerID)
REFERENCES Customers (CustomerID);
ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Employees FOREIGN KEY (EmployeeID)
REFERENCES Employees (EmployeeID);
ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Shippers FOREIGN KEY (ShipVia)
REFERENCES Shippers (ShipperID);
ALTER TABLE Orders ADD CONSTRAINT FK_Orders_Territories FOREIGN KEY (TerritoryID)
REFERENCES Territories (TerritoryID);

ALTER TABLE Products ADD CONSTRAINT FK_Products_Categories FOREIGN KEY (CategoryID)
REFERENCES Categories (CategoryID);
ALTER TABLE Products ADD CONSTRAINT FK_Products_Suppliers FOREIGN KEY (SupplierID)
REFERENCES Suppliers (SupplierID);

ALTER TABLE Territories ADD CONSTRAINT FK_Territories_Region FOREIGN KEY (RegionID)
REFERENCES Region (RegionID);
