CREATE DATABASE RescueBite;
USE RescueBite;

-- Recipients table
CREATE TABLE Recipients (
    RecipientID VARCHAR(5) PRIMARY KEY,
    Type VARCHAR(15),
    Name VARCHAR(50),
    Location VARCHAR(100),
    ContactInformation VARCHAR(20),
    OperatingHours VARCHAR(50),
    MatchingAndRequestsInformation VARCHAR(500)
);

-- Requests table
CREATE TABLE Requests (
    RequestID VARCHAR(5) PRIMARY KEY,
    RequestedItems VARCHAR(50),
    QuantityNeeded VARCHAR(10),
    Status VARCHAR(20)
);

-- Donors table
CREATE TABLE Donors (
    DonorID VARCHAR(5) PRIMARY KEY,
    Type VARCHAR(15),
    Name VARCHAR(50),
    Location VARCHAR(100),
    ContactInformation VARCHAR(20),
    OperatingHours VARCHAR(50)
);

-- FoodDonation table
CREATE TABLE FoodDonation (
    FoodID VARCHAR(5) PRIMARY KEY,
    PreparationDate DATE,
    ExpirationDate DATE,
    StorageRequirements VARCHAR(50),
    Allergens VARCHAR(50),
    DonorID VARCHAR(5),
    FOREIGN KEY (DonorID)
        REFERENCES Donors (DonorID)
);

-- Insert data into Recipients table
INSERT INTO Recipients (RecipientID, Type, Name, Location, ContactInformation, OperatingHours, MatchingAndRequestsInformation)
VALUES 
    ('R1', 'Charity', 'Community Kitchen', '234 Oak St', '987-234-5543', '8am-6pm', 'Matching: Pasta Dish (10 kg), Fresh Produce (15 kg)'),
    ('R2', 'Individual', 'Sarah Johnson', '452 Maple Ave', 'sarahjohnson@gmail.com', 'Flexible', 'Requests: Fresh Fruit, Bread'),
    ('R3', 'Charity', 'Shelter of Hope', '879 Ceder Blvd', 'shelter123@gmail.com', '24/7', 'Matching: Homemade Soup (2 L)'),
    ('R4', 'Charity', 'Helping Hands', '987 Birch Ln', 'helpinghands@email.com', '7AM-6PM', 'Matching: Fresh Dairy (5 l), Comfort Soup (4 l)'),
    ('R5', 'Individual', 'Michael Thompsom', '221 Elm Ct', '876-543-2109', 'Flexible', 'Requests: Organic Vegetables, Salad Bowl'),
    ('R6', 'Individual', 'Lisa Davis', '875 Maple Dr', '345-678-9012', 'Flexible', 'Matching: Sushi Platter (15 pieces), Fresh Fruit Basket (6 kg)'),
    ('R7', 'Individual', 'Alex White', '887 Pine Ct', '789-012-3456', 'Flexible', 'Requests: Organic Granola, Canned Goods'),
    ('R8', 'Charity', 'Food for All', '835 Oakwood Dr', 'foodforall@email.com', '9AM-7PM', 'Matching: Homemade Cookies (3 dozen), Spicy Curry (10 kg)'),
    ('R9', 'Individual', 'Peter Johnson', '892 Cedar St', '438-894-9902', 'Flexible', 'Matching: Fresh Fruit Basket (6 kg), Canned Goods (20 units)'),
    ('R10', 'Charity', 'Community Outreach', '372 Aldrin Dr', 'communityoutreach@email.com', '24/7', 'Requests: Fresh Dairy, Comfort Soup');

-- Insert data into Requests table
INSERT INTO Requests (RequestID, RequestedItems, QuantityNeeded, Status)
VALUES 
    ('REQ1', 'Fresh Fruit', '10kg', 'Open'),
    ('REQ2', 'Bread', '5 loafs', 'Partially fulfilled'),
    ('REQ3', 'Pasta', '15kg', 'Cancelled'),
    ('REQ4', 'Homemade Soup', '2l', 'Open'),
    ('REQ5', 'Canned Goods', '20 units', 'Open'),
    ('REQ6', 'Salad Bowl', '12kg', 'Fulfilled'),
    ('REQ7', 'Fresh Dairy', '8l', 'Open'),
    ('REQ8', 'Sushi Platter', '15 pieces', 'Partially fulfilled'),
    ('REQ9', 'Comfort Soup', '4l', 'Open'),
    ('REQ10', 'Organic Granola', '5kg', 'Cancelled');

-- Insert data into Donors table
INSERT INTO Donors (DonorID, Type, Name, Location, ContactInformation, OperatingHours)
VALUES
    ('D01', 'Restaurant', 'Blue Swan', '103 Main St.', '123-456-7890', '9AM-8PM'),
    ('D02', 'Grocery', 'Fresh Mart', '456 Oak Dr.', 'freshmart@email.com', '7AM-9PM'),
    ('D03', 'Individual', 'Jane Doe', '334 Elm Ct.', '234-567-8901', 'Flexible'),
    ('D04', 'Restaurant', 'Green Leaf', '205 Oakwood Ave', '876-543-2109', '10AM-9PM'),
    ('D05', 'Grocery', 'Mega Mart', '789 Pine St', 'megamart@email.com', '8AM-8PM'),
    ('D06', 'Individual', 'Mark Johnson', '567 Ceder Blvd', '333-443-2232', 'Flexible'),
    ('D07', 'Restaurant', 'Spice Haven', '678 Maple Dr', '987-654-3210', '11AM-10PM'),
    ('D08', 'Grocery', 'Super Fresh', '901 Ceder Ct', 'superfresh@email.com', '9AM-8PM'),
    ('D09', 'Individual', 'Emily White', '345 Pine Ln', '345-678-9012', 'Flexible'),
    ('D10', 'Restaurant', 'Sushi Delight', '123 Elm St', '789-012-3456', '12PM-10PM');

-- Insert data into FoodDonation table
INSERT INTO FoodDonation (FoodID, PreparationDate, ExpirationDate, StorageRequirements, Allergens, DonorID)
VALUES
    ('F01', '2024-01-28', '2024-02-08', 'Refrigerate', 'Gluten, Dairy', 'D01'),
    ('F02', '2024-01-29', '2024-02-05', 'Cool & Dry', 'None', 'D02'),
    ('F03', '2024-02-05', '2024-02-10', 'Freeze', 'Dairy, Nuts', 'D03'),
    ('F04', '2024-02-06', '2024-02-11', 'Refrigerate', 'None', 'D04'),
    ('F05', '2024-02-07', '2024-02-12', 'Dry and Cool', 'None', 'D05'),
    ('F06', '2024-02-08', '2024-02-13', 'Room Temperature', 'Gluten, Nuts', 'D06'),
    ('F07', '2024-02-09', '2024-02-14', 'Refrigerate', 'Dairy', 'D07'),
    ('F08', '2024-02-10', '2024-02-15', 'Refrigerate', 'None', 'D08'),
    ('F09', '2024-02-11', '2024-02-16', 'Refrigerate', 'None', 'D09'),
    ('F10', '2024-02-12', '2024-02-17', 'Cool & Dry', 'Seafood', 'D10');
