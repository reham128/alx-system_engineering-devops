# Web Stack Infrastructure with Sysadmin/DevOps Track
This project is a collaboration between Aalaa Fahim and Reham Saeed, cohort 19 students of ALX Software Engineering using the Holberton School curriculum.

## Overview:
This project aims to showcase the implementation of a web stack infrastructure using the LAMP (Linux, Apache, MySQL, PHP) stack. The infrastructure consists of multiple components working together to host a website. This README file provides an overview of the infrastructure, explains the role of each component, discusses system redundancy, and defines relevant acronyms used in the project.

## Diagram:
Please refer to the attached diagram that illustrates the web stack infrastructure.

### Components and Their Roles:
- Linux (Operating System): The Linux operating system serves as the foundation of the infrastructure. It provides a stable and secure environment for hosting the web services and applications.

- Apache (Web Server): Apache, also known as Apache HTTP Server, is a widely-used web server. It receives HTTP requests from clients and responds with the appropriate web content. It acts as the intermediary between the user's browser and the web application.

- MySQL (Database Management System): MySQL is a popular open-source relational database management system. It stores and manages the website's data, allowing efficient storage, retrieval, and manipulation of structured information. The application server interacts with the MySQL database to fetch or update data.

- PHP (Server-Side Scripting Language): PHP is a server-side scripting language used for developing dynamic web applications. It runs on the web server and generates dynamic web content based on user requests. PHP interacts with the database, performs business logic, and generates the appropriate response to be sent back to the user's browser.

## System Redundancy:
To ensure system redundancy and mitigate the risk of a Single Point of Failure (SPOF), it is recommended to implement the following measures:

1- Load Balancing: Introduce a load balancer that distributes incoming traffic across multiple web servers. This helps distribute the workload and provides redundancy. If one web server fails, the load balancer can redirect traffic to other functioning servers, ensuring high availability.

2- Database Replication: Implement database replication to create redundant copies of the MySQL database. Replication ensures that data is synchronized across multiple database servers. If one database server fails, the others can continue serving data, minimizing downtime and ensuring data availability.

## Acronyms:
1- LAMP: LAMP stands for Linux, Apache, MySQL, and PHP. It refers to a popular open-source web stack used for building dynamic websites and applications.

2- SPOF: SPOF stands for Single Point of Failure. It refers to a component or part of a system that, if it fails, will cause the entire system to fail.

3- QPS: QPS stands for Queries Per Second. It is a metric used to measure the number of database queries or requests processed by a system within a second.

## Conclusion:
This project demonstrates the implementation of a web stack infrastructure using the LAMP stack. The README file provides an overview of the components, their roles, and the concept of system redundancy. Understanding the acronyms (LAMP, SPOF, QPS) mentioned in the project is essential for comprehending the concepts discussed. For further details, refer to the accompanying diagram and explore the individual components' documentation.


