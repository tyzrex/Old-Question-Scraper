# Questions

## Year: 2067

1. Answer the following questions in short:(5 x 2 = 10)

    a) Differentiate between logical data independence and physical data independence.

    b) Three-schema architectures.

    c) Differentiate between database schema and a database state.

    d) Different type of data attributes.

    e) The difference among a relationship instance, a relationship type, and relationship set.

2. a) Draw an ER diagram for database showing Bank. Each Bank can have multiple branches, and each branch can have multiple accounts and loans. (6)

    b) In what sense does a relational calculus differ from relational algebra, and in what sense are they similar? (4)

3. a) Assume a database about Company.(5)

     EMPLOYEE (ss#, name)

     COMPANY (cname, address)

     WORKS (ss#, cname)

     SUPERVISE ( superviser_ss#, employee_ss#)

     Write relational algebra and SQL queries for each of the following cases.

       i) Find the names of all supervisors that work in companies whose address equals ‘pokhara’.

       ii) Find the name of all the companies who have more than 4 supervisors.

       iii) Find the name of supervisor who has the largest number of employees.



    b) What is a view in SQL and how it is defined? Explain how views are typically implemented. (5)

4. a) Define a first, second, and third normal forms with suitable examples (5)

    b) What is a functional dependency? When are two sets of functional dependencies equivalent? How can we determine their equivalence(1+2+2)

5. a) Discuss the ACID properties of a database transaction with suitable example.(5)

    b) Describe the serial and serializable schedule? Why serializable schedule is consider correct?(5)

6.a) How does the granularity of data items affects the performance of concurrency control? What factors affect selections of granularity size for data items?(5)

    b) Describe the two-phase commit protocol for database transaction. (5)

## Year: 2067%20II

1.Answer the following questions in short.(5x2=10)

    a. Advantage of DBMS approach over file system approach.

    b. Differentiate between two-tier and three-tier client/server architecture.

    c. What is weak entity, owner entity type and identifying relationship?

    d.The null value attribute and its uses.

    e) The difference among a relationship instance, a relationship type and a relationship set.

2. a)Draw an ER diagram for a database showing Hospital system. The Hospital maintains data about Affiliated Hospitals, type of Treatments facilities given at each hospital, and Patients.(6)

    b)What is join operation? Differentiate between equijoin and natural join with suitable example.(4)

3.a)Assume a database about Company.

     EMPLOYEE (ss#, name)

     COMPANY (cname, address)

     WORKS (ss#, cname)

     SUPERVISES (supervisor_ss#, employee_ss#)

     Write relational algebra and SQL queries for each of the following cases.(5)

       (i)Find the names of all the supervisors that work in companies whose address equal ‘Kathmandu’.

       (ii)Find the names of all the companies who have more than 4 supervisors.

       (iii)Find the name of the supervisor who has the largest number of employees.

    b)How can define view in SQL? Explain the problems that may arise when one attempts to update a view.(1+4)

4.a)What are different update anomalies? Explain each in with suitable example.(1+4)

    b)Define functional dependency. Describe the closure of a set of functional dependencies with an example.(1+4)

5.a) Draw a state diagram, and discuss the typical state that a transaction goes through during transaction.(5)

b) Which of the following schedule is (conflict) Serializable? For each serializable schedule, determine the equivalent serial schedules.(5)

    i)r1(x); r3(x); w1(x); r2(x); w3(x);

    ii)r1(x); r3(x); w3(x); w1(x); r2(x);

    iii)r3(x); r2(x); w3(x); r1(x); w1(x);

    iv)r3(x); r2(x); r1(x); w3(x); w1(x);

6.a) Discuss the problems of deadlock and starvation, and the different approaches to dealing with these problems.(5)

    b)Describe write-ahead logging protocol.(5)

## Year: 2068

1. Answer the following questions in short:  (5 x 2 = 10)

    (a) Differentiate between program-data independence and program-operation independence.

    (b) The ANSI/SPARC architecture with diagram.

    (c) Differentiate between procedural and non procedural DMLs.

    (d) The difference among an entity, an entity type, and an entity set.

    (e) When is the concept of a weak entity is used in data modeling?

2. (a) Draw an ER diagram for a database to keep track of the teams and games of a sport league. A team has a number of players, not all of whom participate in each game. It is desired to keep track of the players participating in each game for each team, the position they played in that game, and the result of the game.(6)

    (b)What is union compatibility? Define operations union, intersection, and difference on two union compatible relations R and S with suitable example.(4)

3. (a) Describe the different clauses in the syntax of an SQL query, and show what type of constructs can be specified in each clause. (5)

    (b) What is constraint? How does SQL allow implementation of general integrity constraints? (1+4)

4. (a) Define Boyce-Codd normal form. How does it differ from 3 NF? Why is it considered a stronger form of 3NF?(1+4)

    (b) What is functional dependency? Describe full and partial functional dependency with suitable example. (1+4)

5. (a) Discuss the ACID properties of a database transaction with suitable example.(5)

    (b)What is schedule? Define the concept of recoverable, cascadeless, and strict schedule, and compare them in terms of their recoverability.(1+4)

6. (a) What is the two-phase locking protocol? How does it guarantee serializability?(5)

    (b) What do you mean by transaction rollback? What is meant by cascading rollback? Why do practical recovery methods use protocols that do not permit cascading rollback? (5)

## Year: 2069

1. Answer the following questions in short:    (5 x 2 =10)

    a) Differentiate between two-tier and three-tier client/server architecture.

    b) The null value attribute and its uses.

    c) Difference between logical data independence and physical data independence.

    d) When is the concept of a weak entity used in data modeling?

    e)The difference among a relationship instance, a relationship type, and relationship set.

2. a) Draw an ER diagram for database showing hospital system. The Hospital maintains data about affiliated Hospitals, type of treatments facilities given at each hospital and patients.(6)

    b) In what sense does a relational calculus differ from relational algebra, and in what sense are they similar?(4)

3. a)Assume a database about Company.(5)

     EMPLOYEE (ss#, name)

     COMPANY (cname, address)

     WORKS (ss#, cname)

     SUPERVISE ( superviser_ss#, employee_ss#)

     Write relational algebra and SQL queries for each of the following cases.

       i)Find the names of all supervisors that work in companies whose address equals ‘Biratnagar'.

       ii)Find the name of all the companies who have more than 10 employees.

       iii)Find the name of supervisor who has the minimum number of employees.

    b) What is constraint? How does SQL allow implementation of general integrity constraints?(1+4)

4. a) Define a first, second, and third normal forms with suitable examples (5)

    b) What is a functional dependency? Describe full and partial dependency with suitable example.(1+4)

5. a) Draw a state diagram, and discuss the typical state that a transaction goes through during transaction.(5)

    b) Describe the serial and serializable schedule? Why serializable schedule is consider correct?(5)

6.a) How does the granularity of data items affects the performance of concurrency control? What factors affect selections of granularity size for data items? (5)

    b) Describe write ahead logging protocol.(5)

## Year: 2070

1.(a) What is database management system? Discuss the advantages of using database management system over file system.(2+3 =5)

    (b) What is data abstraction? Discuss three levels of this abstraction (1+4=5)

2. a) Construct an ERD to record the marks that students get in different exams of different course offerings.(5)

    b) Define integrity constraint? Discuss domain constraint with suitable example.(1+4=5)

3. a) With the information given below, calculate any three members of F(6)

        R = (A, B, C, G, H, I)

        F = {A - > B, A - > C, CG - > I, B - > H}

    b) Discuss 2NF and 3NF with suitable example. (4)

4.Consider the following supplier database, where primary keys are underlined:(20)

Supplier (supplier-id, supplier-name, city)

Supplies (supplier-id, part-id, quantity)

Parts (part-id, part-name, color, weight)

Construct the following relational algebra queries for this relational database

a)Find the name of all supplies located in city "Kathmandu".

b) Find the name of all parts supplied "ABC Company".

c)Find the name of all parts that are supplied in quantity greater than 300.

d)Find the number of parts supplied by "ABC Company'.

e)Find the name of all suppliers who supply more than 30 different parts

5. a)What is serializable schedule? How can you test a schedule for conflict serializability?.(2+3=5)

    b) Discuss recovery technique base on deferred update with concurrent execution in multi-user environment.(5)

## Year: 2071

1.a) Why do we need database management system? Discuss drawbacks of file system and advantages of database management system. [2+3]

    b) What is database system architecture? Describe three levels and benefits of this architecture. [1+4]

2. A database is being constructed to keep track of the teams and games of a sports league. A team has a number of players, not all of whom participate in each game. If is desired to keep track of the players participating in each game. Design an ER diagram for this application. [10]

3.(a) Define integrity constraint? Discuss referential integrity in detail. [1+4]

    (b) What is functional dependency? How can we use functional dependency to normalize a relation in 3NF?Discuss with suitable example. [1+2+2]

4.Consider the following employee database, where primary keys are underlined. [20]

employee (employee-name, street, city)

works (employee-name, company-name, salary)

company (company-name, manager-name)

manages (employee-name, manager-name)

Give an expression in SQL for each of the following queries.

a)Find the names of all employees who work for Second Bank Corporation.

b) Find the names, street and cities of residence of all employees who work for Second Bank

Corporation.

c)Find the names, street addresses, and cities of residence of all employees who work for Second

Bank Corporation and earn less than $10,000.

d) Find the names of all employees who work under the manager “Devi Prasad”.

e)Find the number of employees having salary greater than or equal to 20000

5.(a) Why do we need concurrency control mechanism? Discuss basic, conservative, and rigorous two phase locking algorithm. [2+3]

    (b) What is shadow paging? How can we use this technique to recover our database? [5]

## Year: 2072

1. Answer the following questions in short: (5x2=10)

    a)Three-schema architecture

    b) Advantage of DBMS approach over file system approach.

    c) What is weak entity, owner entity type and identifying relationship?

    d) Different types of data attributes.

    e) Differentiate between program-data independence and program-operation independence.

2. (a) Given an ER diagram for a database showing Bank. Each Bank can have multiple Branches, and each branch can have multiple accounts and loans. [6]

    (b) What is union compatibility? Define operations union, intersection, and difference on two union compatible relations R and S with suitable example.[4]

3. (a) Describe the different clauses in the syntax of an SQL query, and show what types of constructs can be specified in each clause.[5]

    (b) How view is defined in SQL? Explain the problems that may arise when one attempts to update a view. [1+4]

4. (a) Define Boyce-Codd normal form. How does it differ from 3NF? Why is it considered a stronger form of 3NF? [1+4]

    (b) What is a functional dependency? When are two sets of functional dependencies equivalent? How can we determine their equivalence? [1+4]

5. (a) Discuss the ACID properties of a database transaction with suitable example.[5]

    (b) Indicate how the recovery scheme works in a single user environment if the system fails

        i)After the transaction starts and before the read.

        ii)After the read and before the write.

        iii)After the write and before the commit.

        iv)After the commit and before al database entries are flushed onto disk.[5]

6. (a) What is the two-phase locking protocol? How does it guarantee serializability?[5]

    (b) What is meant by transaction rollback? What is meant by cascading rollback? Why do practical recovery methods use protocols that do not permit cascading rollback? [5]

## Year: 2073

1. Answer the following questions in short:(5 x 2 = 10)

    (a) Differentiate between Database Manager and database Administrator.

    (b) Relational database

    (c) Data encryption

    (d) Lock base protocols

    (e) Deadlock handling

2. (a) What do you mean by Entity-relationship model? Explain strong and weak entity set.(6)

    (b) What is composite attributes? Explain.(4)

3.(a) Which part of the RDBMS taken care of the data dictionary? Explain.(4)

    (b) What do you mean by Hierarchical model? Explain.(6)

4.(a) Explain the functional dependency and Trivial functional dependency with examples.(5)

    (b) Differentiate between distributed DBMS and client-server DBMS.(5)

5. Comparision between 1NF, 2NF, 3NF and BCNF with example.(10)

6.(a) Explain the concurrences control mechanism in detail with example.(6)

    (b) What are the methods used to prevent the system from dead lock?(4)

## Year: 2074

1. Answer the following questions in short:(5 x 2 = 10)

    (a)Data abstraction

    (b) Network data model

    (c)Trigger

    (d)Trivial functional dependency

    (e) Serializable schedule

2.(a) Who is data administrator? What are the main function of database administrator?(2 + 3 = 5)

    (b) Construct an E-R diagram for online course registration where students registers courses online.(5)

3. Consider the following database, where primary keys are underlined

teaches(TID, TName, Qualification)

teaches(TID, CID)

course(CID, CName, CCode)

Construct the following relational algebra and SQL queries for this database.(10)

(a) Find the names of all teaches who have PhD qualification.

(b) Find the names of all courses taught by Ram Prasad.

(c) Find the total number of courses taught by Ram Prasad.

4.(a) Discuss referential integrity with example.(5)

4(b) What is functional dependency? Why do we need inference rules?(2.5 + 2.5 = 5)

5. What are the benefits of using normalization? Discuss 1NF, 2NF, and 3NF with suitable example.(2.5 + 7.5 = 10)

6.(a) Why do we need concurrency control? Discuss two phase locking protocol.(2 + 3 = 5 )

    (b) Why do we need database recovery? Discuss shadow paging technique for database recovery.(2 + 3 = 5)

## Year: 2075

1. Answer the following questions.(5 x 2 = 10)

    (a)Specialization

    (b)Hierarchical data model



    (c)Domain data model

(d) Non trivial functional dependency

    (e) Checkpoint

2.(a) What is data definition language? How is it different from data manipulation language?(2 + 3 = 5) 



2(b) Construct an E-R diagram for online book store where customers buy books online.(5)

3. Consider the following database, where primary keys are underlined

student (SID, SName, semester)

studies (SID, CID)

course (CID, CName, CCode)

Construct the following relational algebra and SQL queries for this database.(10)

(a) Find the names of all students in third semester.

(b) Find the names of all courses studied by Ram.

(c) Find the total number of students who study DBMS.

4.(a) Discuss loss-less decomposition and dependency preservation property of normalization.(2.5 + 2.5 = 5)

    (b) Discuss 3NF with example. How is it different from BCNF?(3 + 2 = 5)

5. (a) Discuss timestamp based concurrency control technique.(4)

    (b) What is deadlock? Discuss deadlock prevention, avoidence and detection and recovery techniques.(2 + 4 = 6)

6. (a) Why do you need recovery? Discuss different types of failures.(2 + 3 = 5)

    (b) What is log-based recovery? Discuss the recovery technique for the loss of non-volatile storage.(2 + 3 = 5)

## Year: 2076

1. What are the advantages of using Database Management System over traditional filing system? Explain different data models with example.(3 + 7)

2. What is concurrency control? Name various methods of controlling the concurrency control? Differentiate between Binary lock and shared/Exclusive lock.(3 + 3 + 4 = 10)

3. What is normal form? Explain their types. Explain about loss-less join decomposition.(3 + 3 + 4 = 10)

4. What is data abstraction? What are three levels of data abstraction? Explain.(2 + 3)

5. What is difference between Entities and Entity sets? Explain with example.(5)

6. Create two table Courses (CID, Course, Dept) and HoD (Dept, Head) using SQL language with all constraints [Primary key, Foreign key and Referential Integrity]. Assume the types of attributes by your own.(5)

7. Differentiate between Integrity and Security with example.(5)

8. Define schedule and serializability. How can you test the serializability?(2 + 3)

9. What is Granulity of data items? How does it effect in concurrency control?(2 + 3)

10. Explain 2 phase locking technique in brief.(5)

11. What are the different approaches of Database recover? What should log file maintain in log-based recovery?(3 +- 2 = 5)

12. Explain the use of primary and foreign key in DBMS with example. What is the role of foreign key?(3 + 2)

## Year: 2078

1. What are different types of Database users and their roles? Explain the Data independence with example.

2. what are the components of ER diagram? Explain the function of various symbols use in ER diagram. Construct an ER diagram to store data in a library of your college.

3. Explain deadlock and starvation. Explain Time stamp based protocol for concurrency control?

4. What is difference between logical data independence and physical data independence?

5. Explain Relationship and Relationship sets with example.

6. Retrieve the TName, SName, SPhone for "ABC" school using SQL from given relation as below.

        TEACHER(TID, TName, TAddress, TQualification)

        SCHOOL(SID, SName, SAddress, SPhone)

        SCHOOL_TEACHER(SID, TID, No_of Period).

7. What is integrity? Explain different types of database integrity.

8. Define Functional dependencies. Explain trivial and non trivial dependencies?

9. Explain the difference between "Join" and "Natural Join" of algebraic operators with example.

10. What is Checkpoints in database recovery? How does it help in database recovery? Explain.

11. Define schedule and serializability. How can you test the serializability?

12. Explain Boyce-Codd normal form with example. How it is different than 3rd Normal form.
