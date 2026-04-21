create schema review_5;

-- Task 1: Create Customer Table

create table review_5.customers(
customer_id BIGSERIAL primary key,
customer_name VARCHAR(100) Not null,
Email VARCHAR(150) Unique,
created_at TIMESTAMP Default current_timestamp
);

-- Task 2: Create Orders Tabl

create table review_5.orders(
order_id BIGSERIAL primary key,
customer_id BIGINT references review_5.customers(customer_id),
order_date TIMESTAMP not null,
order_status VARCHAR(20), -- to store values such as created, delivered, and cancelled.
total_amount NUMERIC(12,2)
);

-- Task 3: Create Delivery Table

create table review_5.deliveries(
delivery_id BIGSERIAL Primary key,
order_id BIGINT references review_5.orders(order_id),
delivery_date TIMESTAMP,
delivery_status VARCHAR(30) --such as in_transit or delivered. One order should normally have one delivery row.
);

-- Task 4: Create Cancellation Table

create table review_5.cancellations(
cancel_id BIGSERIAL primary key,
order_id BIGINT references review_5.orders(order_id),
cancel_date TIMESTAMP,
cancel_reason TEXT -- Reason for cancellation.
);



-- Task 5: Write Basic SQL Queries

-- Show all orders with customer names.

select c.customer_name, o.*
from review_5.orders o join review_5.customers c on o.customer_id = c.customer_id;


-- Show all delivered orders.

select *
from review_5.orders
where order_status = 'delivered';
-- or----
select o.*
from review_5.orders o
join review_5.deliveries d on o.order_id = d.order_id
where d.delivery_status = 'delivered';



-- Show all cancelled orders with a cancel reason.

select o.*, c.cancel_reason
from review_5.orders o
join review_5.cancellations c on o.order_id = c.order_id;

-- Count total orders per customer.

select c.customer_name, count(o.order_id) as total_orders
from review_5.orders o join review_5.customers c on o.customer_id = c.customer_id
group by c.customer_name;

-- Find orders that are created but not yet delivered.

select o.*
from review_5.orders o
left join review_5.deliveries d on o.order_id = d.order_id
where d.order_id = null
and o.order_status = 'created';



-- ###############################################################
-- dummy data for testing

insert into review_5.customers(customer_id,customer_name,email) values
(1,'Ayush Agrawal','Ayush@gmail.com'),
(2,'Aaman Agrawal','Aman@gmail.com'),
(3,'Ankur Agrawal','Ankur@gmail.com'),
(4,'priya verma','priya@gmail.com'),
(5,'vikram patel','vikram@gmail.com');


Insert into review_5.orders(customer_id,order_date,order_status,total_amount) values
(1,'2025-04-01 10:15:00','created',1500.00),
(2,'2025-04-02 10:15:00','delivered',2000.00),
(3,'2025-04-04 10:15:00','created',500.00),
(1,'2025-04-05 10:15:00','delivered',1200.00),
(4,'2025-04-06 10:15:00','created',1750.75),
(5,'2025-04-07 10:15:00','cancelled',800.00),
(2,'2025-04-08 10:15:00','delivered',3000.00);

select * from review_5.orders


Insert into review_5.delivery(order_id,delivery_date,delivery_status) values
(2,'2025-04-01 12:15:00','delivered'),
(3,'2025-04-02 12:20:00','in-tansmit'),
(4,'2025-04-04 12:30:00','delivered');

Insert into review_5.cancelliation(order_id,cancel_date,cancel_reason) values
(5,'2025-04-08 10:20:00','Not intrested')



