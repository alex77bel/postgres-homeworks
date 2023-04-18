-- SQL-команды для создания таблиц


CREATE TABLE employees
(
    employee_id smallserial PRIMARY KEY NOT NULL,
    first_name  varchar(100)            NOT NULL,
    last_name   varchar(100)            NOT NULL,
    title       varchar(100)            NOT NULL,
    birth_date  date                    NOT NULL,
    notes       text
);

CREATE TABLE customers
(
    customer_id  varchar(5) PRIMARY KEY NOT NULL,
    company_name varchar(100)           NOT NULL,
    contact_name varchar(100)           NOT NULL
)

CREATE TABLE orders
(
    order_id    smallint PRIMARY KEY NOT NULL,
    customer_id varchar(5) REFERENCES customers (customer_id),
    employee_id smallint REFERENCES employees (employee_id),
    order_date  date                 NOT NULL,
    ship_city   varchar(100)         NOT NULL
)