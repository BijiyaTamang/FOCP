# Police Crime Data Mart - Assignment Report

**Student Name:** [Your Name]  
**Student ID:** [Your ID]  
**Module:** Advanced Data Systems  
**Date:** [Current Date]

---

## Table of Contents

1. [Data Warehouse](#data-warehouse)
2. [Features of Data Warehouse](#features-of-data-warehouse)
3. [Approaches of Data Warehouse](#approaches-of-data-warehouse)
4. [Difference in Two Approaches](#difference-in-two-approaches)
5. [Merit and Demerits of Data Warehouse](#merit-and-demerits-of-data-warehouse)
6. [Data Warehouse Schemas](#data-warehouse-schemas)
7. [Difference Between All the Schemas](#difference-between-all-the-schemas)
8. [Stakeholder](#stakeholder)
9. [Regional Crime Analyst](#regional-crime-analyst)
10. [Central Police Headquarter (HQ)](#central-police-headquarter-hq)
11. [Combined Stakeholder Role](#combined-stakeholder-role)
12. [Use Case](#use-case)
13. [Main KPI(s)](#main-kpis)
14. [Main Report Supported by the Star Schema](#main-report-supported-by-the-star-schema)
15. [QSEE - Star Schema for Police Crime Data Mart](#qsee---star-schema-for-police-crime-data-mart)
16. [Data Dictionary for Star Schema Model](#data-dictionary-for-star-schema-model)
17. [Report Suggested as per the Use Case](#report-suggested-as-per-the-use-case)
18. [Star Schema Table Implementation](#star-schema-table-implementation)
19. [Create a Script to Implement the Tables for the BASIC Star Schema](#create-a-script-to-implement-the-tables-for-the-basic-star-schema)
20. [ETL Process](#etl-process)
21. [Data Dictionary for ETL Process](#data-dictionary-for-etl-process)
22. [Data Extraction: Source System Data](#data-extraction-source-system-data)
23. [Data Extraction: Data Load from Source Systems](#data-extraction-data-load-from-source-systems)
24. [Data Transformation: Data Quality Handling](#data-transformation-data-quality-handling)
25. [Data Quality Issue](#data-quality-issue)
26. [Data Transformation: Data Load with Transformations](#data-transformation-data-load-with-transformations)
27. [Data Transformation: Bad Data into Good Data Transformation](#data-transformation-bad-data-into-good-data-transformation)
28. [Data Transformation: Transformation Rules](#data-transformation-transformation-rules)
29. [Data Load: Loading Data into Star Schema](#data-load-loading-data-into-star-schema)
30. [Appendix](#appendix)

---

## Data Warehouse

A data warehouse is a centralized repository that stores integrated data from multiple source systems. It is designed to support business intelligence activities, data analysis, and decision-making processes. Data warehouses are subject-oriented, integrated, time-variant, and non-volatile, making them ideal for historical analysis and reporting.

In this project, we are creating a **Data Mart** - a subset of a data warehouse focused on a specific business area. Our Data Mart is designed specifically for Police Crime Analysis, consolidating data from:

1. **Police Reporting Crime System (PRCS)** - Oracle database for England
2. **Police System - Wales (PS_Wales)** - Database for Wales  
3. **Leeds Crime Spreadsheet** - Summary data for crimes in Leeds

The Data Mart uses a star schema design to enable efficient querying and analysis of crime data for performance monitoring and strategic decision-making.

---

## Features of Data Warehouse

Data warehouses possess several key features that distinguish them from operational databases:

1. **Subject-Oriented:** Organized around major subjects (e.g., crime analysis) rather than applications
2. **Integrated:** Data from multiple sources is combined into a consistent format
3. **Time-Variant:** Historical data is maintained, enabling trend analysis over time
4. **Non-Volatile:** Data is read-only once loaded, ensuring data stability for analysis
5. **Optimized for Querying:** Designed for analytical queries rather than transactional processing
6. **Denormalized Structure:** Uses star or snowflake schemas for faster query performance

**Application in This Project:**
- Subject-oriented: Focused on crime performance analysis
- Integrated: Combines PRCS (England) and PS_Wales data into unified structure
- Time-variant: Time dimension enables year-over-year comparisons
- Non-volatile: Data loaded into star schema remains stable for reporting
- Query optimization: Star schema with indexes supports efficient reporting queries

---

## Approaches of Data Warehouse

There are two main approaches to building data warehouses:

### 1. Top-Down Approach (Inmon Approach)

The top-down approach builds a centralized enterprise data warehouse first, then creates data marts as subsets. This approach:
- Creates a single, integrated enterprise data warehouse
- Data marts are derived from the central warehouse
- Ensures consistency across the organization
- Requires significant upfront investment

### 2. Bottom-Up Approach (Kimball Approach)

The bottom-up approach builds independent data marts first, which can later be integrated. This approach:
- Starts with individual data marts for specific business areas
- Faster to implement and deliver value
- Can be integrated later if needed
- More flexible and agile

**Application in This Project:**
This project follows the **Bottom-Up (Kimball) Approach**:
- We are building a focused Data Mart for Police Crime Analysis
- The Data Mart is independent and can deliver immediate value
- Uses star schema design (Kimball methodology)
- Can be integrated into a larger data warehouse in the future if needed

---

## Difference in Two Approaches

| Aspect | Top-Down (Inmon) | Bottom-Up (Kimball) |
|--------|------------------|---------------------|
| **Starting Point** | Enterprise data warehouse | Individual data marts |
| **Design Philosophy** | Normalized, enterprise-wide | Denormalized, subject-specific |
| **Implementation Time** | Longer, more complex | Faster, iterative |
| **Cost** | Higher upfront investment | Lower initial cost |
| **Flexibility** | Less flexible, rigid structure | More flexible, adaptable |
| **Data Consistency** | High consistency across organization | Consistency within data mart |
| **Scalability** | Better for large enterprises | Better for departmental needs |
| **Best For** | Large organizations, enterprise-wide needs | Specific business areas, quick delivery |

**This Project Uses:** Bottom-Up (Kimball) Approach - Building a focused Data Mart for crime analysis

---

## Merit and Demerits of Data Warehouse

### Merits (Advantages)

1. **Improved Decision Making:** Provides historical and integrated data for better business decisions
2. **Data Consistency:** Integrates data from multiple sources into consistent format
3. **Performance:** Optimized for analytical queries, faster than querying operational systems
4. **Historical Analysis:** Maintains historical data for trend analysis
5. **Reduced Load on Operational Systems:** Offloads analytical queries from production systems
6. **Business Intelligence Support:** Enables reporting, dashboards, and analytics
7. **Data Quality:** Data cleansing and transformation improve data quality

### Demerits (Disadvantages)

1. **High Cost:** Requires significant investment in hardware, software, and resources
2. **Complexity:** Complex design and implementation process
3. **Time-Consuming:** Takes time to build and populate
4. **Maintenance:** Requires ongoing maintenance and updates
5. **Data Latency:** May not reflect real-time data
6. **Resource Intensive:** Requires skilled personnel and technical expertise

**Application in This Project:**
- **Merits Realized:** Improved crime analysis, data integration from multiple sources, historical trend analysis
- **Demerits Mitigated:** Focused scope (Data Mart), simplified design, clear requirements

---

## Data Warehouse Schemas

Data warehouse schemas define the structure and organization of data. The main schema types are:

### 1. Star Schema
- Central fact table surrounded by dimension tables
- Denormalized structure
- Simple and easy to understand
- Fast query performance

### 2. Snowflake Schema
- Normalized version of star schema
- Dimension tables are normalized into sub-dimensions
- Reduces data redundancy
- More complex queries

### 3. Galaxy Schema (Fact Constellation)
- Multiple fact tables sharing dimension tables
- Used for complex analytical requirements
- Most complex structure

**Application in This Project:**
We use **Star Schema** design for simplicity and performance.

---

## Difference Between All the Schemas

| Feature | Star Schema | Snowflake Schema | Galaxy Schema |
|---------|-------------|------------------|---------------|
| **Structure** | Fact table + flat dimensions | Fact table + normalized dimensions | Multiple fact tables + shared dimensions |
| **Normalization** | Denormalized | Normalized | Partially normalized |
| **Complexity** | Simple | Moderate | Complex |
| **Query Performance** | Fast | Moderate | Varies |
| **Storage** | More storage needed | Less storage | Moderate |
| **Maintenance** | Easy | Moderate | Complex |
| **Best For** | Simple analysis, fast queries | Large dimensions, storage optimization | Complex multi-fact analysis |

**This Project Uses:** Star Schema - Simple, fast, and suitable for crime analysis requirements

---

## Stakeholder

**Primary Stakeholder:** Police Force Management and Crime Analysis Team

The Data Mart is designed to serve multiple stakeholder groups within the Police Force organization who need access to crime performance data for decision-making and analysis.

---

## Regional Crime Analyst

**Role:** Regional Crime Analysts are responsible for analyzing crime patterns, trends, and performance within specific geographic regions.

**Needs:**
- Access to crime data by region and station
- Trend analysis over time
- Crime type distribution analysis
- Performance metrics by area

**How Data Mart Supports:**
- `dim_station` provides regional and area information
- `dim_time` enables time-based trend analysis
- `dim_crime_type` supports crime type analysis
- Fact table measures enable performance calculations

---

## Central Police Headquarter (HQ)

**Role:** Central Police Headquarters manages overall police operations, resource allocation, and strategic planning across all regions.

**Needs:**
- High-level performance metrics across all stations
- Resource allocation decisions
- Strategic planning support
- Comparative analysis between regions

**How Data Mart Supports:**
- Station performance comparison reports
- Year-over-year crime rate analysis
- Escalation rate monitoring
- Overall crime statistics and trends

---

## Combined Stakeholder Role

**Combined Stakeholder Group:** Police Force Management and Crime Analysis Team

This group includes:
- **Police Force Senior Management:** Strategic decision-makers
- **Regional Crime Analysts:** Operational analysts
- **Station Commanders:** Local management
- **Performance Monitoring Team:** Performance evaluators
- **Resource Planning Team:** Resource allocators

**Unified Needs:**
- Comprehensive crime performance analysis
- Station and officer performance metrics
- Trend analysis and forecasting
- Resource allocation support
- Performance monitoring and evaluation

**How Data Mart Supports All:**
The star schema design provides flexible analysis capabilities that serve all stakeholder needs through different report combinations and aggregations.

---

## Use Case

**Use Case: Crime Performance Analysis and Monitoring**

The Data Mart supports comprehensive analysis of crime reporting, investigation, and resolution performance across different dimensions to enable data-driven decision-making.

**Business Objectives:**
1. Monitor crime trends over time
2. Evaluate station performance and efficiency
3. Analyze crime resolution rates and times
4. Identify escalation patterns and hotspots
5. Assess officer workload and effectiveness
6. Support resource allocation decisions

**Key Business Questions:**
1. What is the resolution rate for crimes by station and crime type?
2. How long does it take on average to resolve different types of crimes?
3. Which stations have the highest escalation rates?
4. What is the distribution of crimes by type across different stations?
5. How many open cases are currently in the backlog?
6. How do current crime rates compare to previous years?
7. Which officers handle the most crimes (hotspots)?

**Scope:**
- Geographic: England and Wales
- Time Period: 2015-2020 (extendable)
- Focus: Crime performance, resolution, and resource management

---

## Main KPI(s)

### KPI 1: Open vs Closed Case Comparison

**Definition:** Comparison of open and closed crimes by station, month, and crime type

**Formula:**
- Open Cases: COUNT(*) WHERE status = 'OPEN'
- Closed Cases: COUNT(*) WHERE status = 'CLOSED'
- Comparison Ratio: (Closed Cases / Total Cases) × 100

**Target:** > 70% closed cases ratio

**Business Value:** Shows overall case resolution performance and identifies areas needing attention

---

### KPI 2: Crimes Closed Count

**Definition:** Total number of crimes closed by station, officer, and time period

**Formula:** SUM(crimes_closed_count)

**Purpose:** Track closure performance

**Business Value:** Measures productivity and effectiveness of crime resolution

---

### KPI 3: Station Performance Comparison

**Definition:** Scaled performance metrics across all stations

**Metrics:**
- Total crimes per station
- Closed crimes per station
- Resolution rate per station: (Closed Crimes / Total Crimes) × 100
- Average resolution time per station: AVG(resolution_days)

**Purpose:** Compare and rank station performance

**Business Value:** Identifies high and low performing stations for resource allocation

---

### KPI 4: Year-over-Year Crime Rate Comparison

**Definition:** Comparison of crime rates between current year and previous year

**Formula:**
- Current Year Rate: COUNT(crimes) for current year
- Previous Year Rate: COUNT(crimes) for previous year
- Change: ((Current - Previous) / Previous) × 100

**Purpose:** Track crime trends over time

**Business Value:** Identifies increasing or decreasing crime patterns

---

### KPI 5: Officer Crime Hotspot Analysis

**Definition:** Analysis of crime distribution and workload by officer

**Metrics:**
- Total crimes assigned per officer: total_crimes_assigned
- Closed crimes per officer: crimes_closed_count
- Closure rate: (crimes_closed_count / total_crimes_assigned) × 100
- Crime types handled per officer

**Purpose:** Identify officers handling most crimes (hotspots)

**Business Value:** Supports workload balancing and identifies high-performing officers

---

## Main Report Supported by the Star Schema

The star schema supports the following main reports:

1. **Open vs Closed Case Comparison Report**
   - Compares open and closed cases by station, month, and crime type
   - Uses: fact_crime, dim_station, dim_time, dim_crime_type, dim_status

2. **Crimes Closed Count Report**
   - Shows crimes closed by officer and station over time
   - Uses: fact_crime, dim_officer, dim_station, dim_time

3. **Station Performance Comparison Report**
   - Ranks all stations by performance metrics
   - Uses: fact_crime, dim_station (aggregated measures)

4. **Year-over-Year Crime Rate Comparison Report**
   - Compares current year vs previous year crime rates
   - Uses: fact_crime, dim_time, dim_station (year-over-year joins)

5. **Officer Crime Hotspot Analysis Report**
   - Identifies officers with highest crime workloads
   - Uses: fact_crime, dim_officer, dim_crime_type

**Star Schema Benefits:**
- Fast query performance due to denormalized structure
- Easy to understand and query
- Supports multiple report types through dimension combinations
- Efficient aggregations on fact table measures

---

## QSEE - Star Schema for Police Crime Data Mart

The star schema design for the Police Crime Data Mart consists of:

### Fact Table: fact_crime

**Purpose:** Central fact table storing crime events with measures

**Grain:** One row per reported crime

**Measures:**
- `crime_count` - Count of crimes (typically 1)
- `crimes_closed_count` - Count of closed crimes (1 if closed, 0 if open)
- `resolution_days` - Calculated: days between reported and closed dates
- `is_escalated` - Flag indicating if crime was escalated

**Foreign Keys:**
- `time_key_reported` → dim_time
- `time_key_closed` → dim_time (nullable)
- `station_key` → dim_station
- `crime_type_key` → dim_crime_type
- `officer_key` → dim_officer (nullable)
- `status_key` → dim_status

### Dimension Tables

**dim_station:**
- station_key (PK)
- station_id
- station_name
- area_name
- region

**dim_crime_type:**
- crime_type_key (PK)
- crime_type_id
- crime_type_desc
- crime_category

**dim_officer:**
- officer_key (PK)
- officer_id
- officer_name
- officer_grade
- department
- total_crimes_assigned
- crimes_closed_count

**dim_status:**
- status_key (PK)
- status_code
- status_description
- is_escalated
- is_closed

**dim_time:**
- time_key (PK)
- full_date
- year
- month
- month_name
- quarter
- quarter_name
- year_month

**Star Schema Diagram:**
```
                    dim_time
                        |
                        | (reported)
                        |
        dim_station ----+---- fact_crime ---- dim_crime_type
                        |         |
                        |         |
                   dim_officer    |
                                 |
                            dim_status
```

---

## Data Dictionary for Star Schema Model

### Fact Table: fact_crime

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| fact_crime_id | INTEGER | NO | Primary key | Generated | Auto-increment |
| time_key_reported | INTEGER | NO | FK to dim_time | pl_reported_crime.date_reported | Year/month lookup |
| time_key_closed | INTEGER | YES | FK to dim_time | pl_reported_crime.date_closed | Year/month lookup, handle NULL |
| station_key | INTEGER | NO | FK to dim_station | pl_reported_crime.fk2_station_id | Station lookup |
| crime_type_key | INTEGER | NO | FK to dim_crime_type | pl_reported_crime.fk1_crime_type_id | Crime type lookup |
| officer_key | INTEGER | YES | FK to dim_officer | pl_work_allocation.lead_police_officer | Officer lookup, handle NULL |
| status_key | INTEGER | NO | FK to dim_status | pl_reported_crime.crime_status | Status mapping |
| crime_count | INTEGER | NO | Count measure | Default: 1 | Default value |
| crimes_closed_count | INTEGER | NO | Closed crimes count | Derived | CASE: 1 if closed, 0 if open |
| resolution_days | INTEGER | YES | Calculated measure | date_closed - date_reported | CALCULATION |
| is_escalated | CHAR(1) | NO | Escalation flag | crime_status = 'ESCALATE' | Boolean transformation |

### Dimension Table: dim_station

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| station_key | INTEGER | NO | Primary key | Generated | Auto-increment |
| station_id | INTEGER | YES | Source ID | pl_station.station_id | Direct |
| station_name | VARCHAR(50) | NO | Station name | pl_station.station_name | INITCAP - Case standardization |
| area_name | VARCHAR(50) | YES | Area name | pl_area.area_name | Direct |
| region | VARCHAR(50) | YES | Region classification | Derived | CASE statement - Region mapping |
| is_current | CHAR(1) | NO | Current flag | 'Y' | Default |

### Dimension Table: dim_crime_type

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| crime_type_key | INTEGER | NO | Primary key | Generated | Auto-increment |
| crime_type_id | INTEGER | YES | Source ID | pl_crime_type.crime_type_id | Direct |
| crime_type_desc | VARCHAR(100) | NO | Crime description | pl_crime_type.crime_type_desc | INITCAP - Case standardization |
| crime_category | VARCHAR(50) | YES | Crime category | Derived | CASE statement - Categorization |

### Dimension Table: dim_officer

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| officer_key | INTEGER | NO | Primary key | Generated | Auto-increment |
| officer_id | INTEGER | YES | Source ID | pl_police_employee.emp_id | Direct |
| officer_name | VARCHAR(100) | NO | Officer name | pl_police_employee.emp_name | TRIM - Remove whitespace |
| officer_grade | INTEGER | YES | Grade level | pl_police_employee.emp_grade | Direct |
| department | VARCHAR(50) | YES | Department | Default | Default value for missing data |
| total_crimes_assigned | INTEGER | YES | Total crimes | Calculated | COUNT from work_allocation |
| crimes_closed_count | INTEGER | YES | Closed crimes | Calculated | COUNT where status = CLOSED |

### Dimension Table: dim_status

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| status_key | INTEGER | NO | Primary key | Generated | Sequential |
| status_code | VARCHAR(20) | NO | Status code | pl_reported_crime.crime_status | UPPER - Standardization |
| status_description | VARCHAR(100) | NO | Description | Derived | Manual mapping |
| is_escalated | CHAR(1) | NO | Escalation flag | Derived | Boolean from status_code |
| is_closed | CHAR(1) | NO | Closed flag | Derived | Boolean from status_code |

### Dimension Table: dim_time

| Column Name | Data Type | Nullable | Description | Source | Transformation |
|------------|-----------|----------|-------------|--------|----------------|
| time_key | INTEGER | NO | Primary key | Generated | Sequential |
| full_date | DATE | NO | First day of month | Generated | Date generation |
| year | INTEGER | NO | Year | EXTRACT | Date component |
| month | INTEGER | NO | Month number | EXTRACT | Date component |
| month_name | VARCHAR(20) | YES | Month name | TO_CHAR | Text representation |
| quarter | INTEGER | YES | Quarter number | Calculated | CEIL(month/3) |
| quarter_name | VARCHAR(10) | YES | Quarter name | Derived | 'Q' + quarter |
| year_month | VARCHAR(7) | YES | Year-month format | Derived | YYYY-MM format |

---

## Report Suggested as per the Use Case

Based on the use case and KPIs, the following reports are suggested:

### Report 1: Open vs Closed Case Comparison Report

**Purpose:** Compare open and closed cases by station, month, and crime type

**Columns:**
- Year, Month, Station Name, Crime Type
- Total Crimes, Open Cases, Closed Cases
- Closed Percentage

**Supports:** KPI 1 - Open vs Closed Case Comparison

---

### Report 2: Crimes Closed Count Report

**Purpose:** Track crimes closed by officer and station over time

**Columns:**
- Station Name, Officer Name, Year, Month
- Total Closed, Total Assigned, Closure Rate

**Supports:** KPI 2 - Crimes Closed Count

---

### Report 3: Station Performance Comparison Report

**Purpose:** Rank all stations by performance metrics

**Columns:**
- Station Name, Region
- Total Crimes, Closed Crimes, Resolution Rate, Avg Resolution Days
- Performance Scale

**Supports:** KPI 3 - Station Performance Comparison

---

### Report 4: Year-over-Year Crime Rate Comparison Report

**Purpose:** Compare current year vs previous year crime rates

**Columns:**
- Current Year, Previous Year, Station Name
- Current Year Crimes, Previous Year Crimes, Percentage Change

**Supports:** KPI 4 - Year-over-Year Crime Rate Comparison

---

### Report 5: Officer Crime Hotspot Analysis Report

**Purpose:** Identify officers with highest crime workloads

**Columns:**
- Officer Name, Officer Grade
- Total Crimes Assigned, Crimes Closed, Closure Rate
- Crime Types Handled

**Supports:** KPI 5 - Officer Crime Hotspot Analysis

---

## Star Schema Table Implementation

The star schema is implemented using Oracle SQL DDL. The implementation includes:

**Tables Created:**
1. dim_station - Station dimension
2. dim_crime_type - Crime type dimension
3. dim_officer - Officer dimension
4. dim_status - Status dimension
5. dim_time - Time dimension
6. fact_crime - Crime fact table

**Constraints:**
- Primary keys on all tables
- Foreign keys from fact table to all dimensions
- Check constraints for data validation
- Unique constraints where needed

**Indexes:**
- Indexes on all foreign key columns for query performance
- Indexes on frequently queried dimension attributes

**Implementation Details:**
- All tables use INTEGER for surrogate keys
- VARCHAR for text attributes with appropriate lengths
- DATE for time-related attributes
- Proper NULL handling for optional attributes

---

## Create a Script to Implement the Tables for the BASIC Star Schema

The script `SS_DDL.sql` creates all tables for the basic star schema.

**Script Contents:**
- DROP statements for existing tables (if any)
- CREATE TABLE statements for all dimension tables
- CREATE TABLE statement for fact table
- ALTER TABLE statements for foreign key constraints
- CREATE INDEX statements for performance
- COMMIT statement

**Key Features:**
- Creates 1 fact table and 5 dimension tables
- Implements primary key constraints
- Implements foreign key constraints for referential integrity
- Creates indexes on foreign keys for query performance
- Includes check constraints for data validation

**Script Location:** See Appendix A: SS_DDL.sql

---

## ETL Process

ETL (Extract, Transform, Load) is the process of:
1. **Extract:** Getting data from source systems
2. **Transform:** Cleaning, standardizing, and transforming data
3. **Load:** Loading transformed data into the data warehouse

**ETL Process in This Project:**

**Extract:**
- Data extracted from PRCS system tables (pl_reported_crime, pl_station, pl_crime_type, pl_police_employee, pl_work_allocation)
- Data extracted from integrated Wales data (after data_integration.sql)

**Transform:**
- Case standardization (INITCAP, UPPER, TRIM)
- Crime type categorization
- Region mapping
- Date conversions (VARCHAR to DATE)
- Measure calculations (resolution_days, crimes_closed_count)

**Load:**
- Populate dimension tables first
- Populate fact table last (depends on dimensions)
- Handle NULL values appropriately
- Validate data quality

**ETL Script:** See Appendix C: ETL.sql

---

## Data Dictionary for ETL Process

### Source Tables (PRCS System)

**pl_reported_crime:**
- reported_crime_id, date_reported, crime_postcode, crime_status, date_closed, fk1_crime_type_id, fk2_station_id

**pl_station:**
- station_id, station_name, fk1_area_id

**pl_area:**
- area_id, area_name, parent_area

**pl_crime_type:**
- crime_type_id, crime_type_desc

**pl_police_employee:**
- emp_id, emp_name, emp_grade

**pl_work_allocation:**
- s_reported_crime_id, d_emp_id, lead_police_officer, work_start_date, work_end_date

### Target Tables (Star Schema)

**fact_crime:**
- fact_crime_id, time_key_reported, time_key_closed, station_key, crime_type_key, officer_key, status_key, crime_count, crimes_closed_count, resolution_days, is_escalated

**dim_station:**
- station_key, station_id, station_name, area_name, region, is_current

**dim_crime_type:**
- crime_type_key, crime_type_id, crime_type_desc, crime_category

**dim_officer:**
- officer_key, officer_id, officer_name, officer_grade, department, total_crimes_assigned, crimes_closed_count

**dim_status:**
- status_key, status_code, status_description, is_escalated, is_closed

**dim_time:**
- time_key, full_date, year, month, month_name, quarter, quarter_name, year_month

### Transformation Rules

| Source Column | Target Column | Transformation |
|--------------|---------------|---------------|
| pl_station.station_name | dim_station.station_name | INITCAP(TRIM()) |
| pl_crime_type.crime_type_desc | dim_crime_type.crime_type_desc | INITCAP(TRIM()) |
| pl_crime_type.crime_type_desc | dim_crime_type.crime_category | CASE statement categorization |
| pl_area.area_name | dim_station.region | CASE statement mapping |
| pl_reported_crime.date_closed | fact_crime.resolution_days | TO_DATE() - date_reported |
| pl_reported_crime.crime_status | fact_crime.crimes_closed_count | CASE: 1 if CLOSED, 0 if OPEN |

---

## Data Extraction: Source System Data

Data is extracted from the following source systems:

### PRCS System (England)
- **pl_reported_crime:** Crime records with dates, status, postcodes
- **pl_station:** Police station information
- **pl_area:** Geographic area hierarchy
- **pl_crime_type:** Crime type classifications
- **pl_police_employee:** Officer information
- **pl_work_allocation:** Officer-crime assignments

### PS_Wales System (Wales)
- **CRIME_REGISTER:** Crime records (after integration)
- **LOCATION:** Location information
- **REGION:** Regional information
- **OFFICER:** Officer information
- **OFFENCE:** Offence types

**Extraction Method:**
- Direct SQL SELECT statements from source tables
- Joins between related tables
- Filters applied as needed
- Data extracted in batches for processing

---

## Data Extraction: Data Load from Source Systems

Data is loaded from source systems into the star schema through the ETL process:

**Step 1: Extract from Source**
```sql
SELECT * FROM pl_reported_crime;
SELECT * FROM pl_station;
SELECT * FROM pl_crime_type;
-- etc.
```

**Step 2: Transform During Load**
- Apply transformations while inserting into dimension tables
- Calculate measures while inserting into fact table
- Handle data quality issues during transformation

**Step 3: Load into Star Schema**
- Insert into dimension tables first
- Insert into fact table last (requires dimension keys)

**Load Process:**
- Dimension tables populated sequentially
- Fact table populated with joins to dimensions
- Validation queries executed after load
- COMMIT after successful load

---

## Data Transformation: Data Quality Handling

Data transformation addresses data quality issues and applies business rules:

### Transformation Types Applied

1. **Case Standardization:**
   - INITCAP() for proper case
   - UPPER() for status codes
   - TRIM() for whitespace removal

2. **Categorization:**
   - CASE statements to categorize crime types
   - Region mapping from areas

3. **Date Handling:**
   - VARCHAR to DATE conversion
   - Date arithmetic for calculations
   - NULL handling for missing dates

4. **Measure Calculations:**
   - resolution_days = date_closed - date_reported
   - crimes_closed_count = 1 if closed, 0 if open

5. **Default Values:**
   - Default department for missing officer data
   - Default 'Y' for is_current flags

---

## Data Quality Issue

Three main data quality issues were identified and addressed:

### Issue 1: Inconsistent Case in Station Names

**Problem:** Station names have mixed case (e.g., "lawnswood", "MEANWOOD", "Kings Cross")

**Impact:** Inconsistent reporting and filtering

**Solution:** Applied INITCAP() transformation in ETL
```sql
INITCAP(TRIM(s.station_name)) AS station_name
```

**Location:** dim_station.station_name

---

### Issue 2: Inconsistent Crime Type Descriptions

**Problem:** Crime types have inconsistent formatting (e.g., "Drunk and DisOrder", "car theft")

**Impact:** Inaccurate grouping and analysis

**Solution:** Applied INITCAP() and TRIM() transformations
```sql
TRIM(INITCAP(ct.crime_type_desc)) AS crime_type_desc
```

**Location:** dim_crime_type.crime_type_desc

---

### Issue 3: Missing Officer Assignments

**Problem:** Some crimes may not have assigned officers

**Impact:** Data loss if not handled properly

**Solution:** Used LEFT JOIN and handled NULL values
```sql
LEFT JOIN dim_officer do_officer ON ...
WHERE do_officer.officer_name IS NOT NULL
```

**Location:** fact_crime.officer_key

---

## Data Transformation: Data Load with Transformations

Data is loaded into the star schema with transformations applied:

### Dimension Tables Load

**dim_station:**
```sql
INSERT INTO dim_station (station_key, station_name, ...)
SELECT 
    ROW_NUMBER() OVER (...) AS station_key,
    INITCAP(TRIM(s.station_name)) AS station_name,  -- Transformation
    ...
FROM pl_station s
```

**dim_crime_type:**
```sql
INSERT INTO dim_crime_type (crime_type_key, crime_type_desc, crime_category)
SELECT 
    ROW_NUMBER() OVER (...) AS crime_type_key,
    TRIM(INITCAP(ct.crime_type_desc)) AS crime_type_desc,  -- Transformation
    CASE ... END AS crime_category  -- Transformation
FROM pl_crime_type ct
```

### Fact Table Load

**fact_crime:**
```sql
INSERT INTO fact_crime (..., crimes_closed_count, resolution_days)
SELECT 
    ...,
    CASE WHEN dst.is_closed = 'Y' THEN 1 ELSE 0 END AS crimes_closed_count,  -- Transformation
    TO_NUMBER(TO_DATE(TRIM(rc.date_closed), 'MM/DD/YYYY') - rc.date_reported) AS resolution_days  -- Transformation
FROM pl_reported_crime rc
...
```

---

## Data Transformation: Bad Data into Good Data Transformation

Bad data is transformed into good data through various techniques:

### Transformation Techniques

1. **Case Standardization:**
   - Bad: "lawnswood", "MEANWOOD"
   - Good: "Lawnswood", "Meanwood"
   - Method: INITCAP()

2. **Whitespace Removal:**
   - Bad: "  Drugs Offence  "
   - Good: "Drugs Offence"
   - Method: TRIM()

3. **Date Format Conversion:**
   - Bad: "09/30/2019" (VARCHAR)
   - Good: DATE value
   - Method: TO_DATE(TRIM(date_closed), 'MM/DD/YYYY')

4. **Status Standardization:**
   - Bad: "open", "closed", "OPEN", "CLOSED"
   - Good: "OPEN", "CLOSED"
   - Method: UPPER()

5. **Categorization:**
   - Bad: "car theft", "Burglary", "theft"
   - Good: "Property Crime" category
   - Method: CASE statement

6. **NULL Handling:**
   - Bad: Missing officer assignments
   - Good: NULL handled with LEFT JOIN, default values provided
   - Method: LEFT JOIN, COALESCE, default values

**Examples in ETL:**
- Station names: "lawnswood" → "Lawnswood"
- Crime types: "Drunk and DisOrder" → "Drunk And Disorder"
- Dates: "09/30/2019" → DATE(2019-09-30)
- Status: "open" → "OPEN"

---

## Data Transformation: Transformation Rules

Transformation rules define how source data is converted to target format:

### Rule 1: Case Standardization

**Rule:** All text fields should use proper case (first letter uppercase, rest lowercase)

**Applied To:**
- station_name
- crime_type_desc

**Implementation:**
```sql
INITCAP(TRIM(column_name))
```

---

### Rule 2: Crime Type Categorization

**Rule:** Crime types should be categorized into broader groups

**Categories:**
- Violent Crime (Violent, Robbery, Murder)
- Property Crime (Theft, Burglary)
- Drugs Offence
- Financial Crime (Fraud, Forgery)
- Public Order (Drunk, Disorder)
- Other

**Implementation:**
```sql
CASE 
    WHEN UPPER(crime_type_desc) LIKE '%VIOLENT%' THEN 'Violent Crime'
    WHEN UPPER(crime_type_desc) LIKE '%THEFT%' THEN 'Property Crime'
    ...
END
```

---

### Rule 3: Region Mapping

**Rule:** Areas should be mapped to high-level regions

**Mapping:**
- Yorkshire → Yorkshire
- Lancashire → Lancashire
- Wales/Cardiff → Wales
- Other → Other

**Implementation:**
```sql
CASE 
    WHEN area_name LIKE '%Yorkshire%' THEN 'Yorkshire'
    WHEN area_name LIKE '%Wales%' THEN 'Wales'
    ...
END
```

---

### Rule 4: Date Conversion

**Rule:** VARCHAR dates should be converted to DATE type

**Implementation:**
```sql
TO_DATE(TRIM(date_closed), 'MM/DD/YYYY')
```

---

### Rule 5: Measure Calculation

**Rule:** resolution_days = date_closed - date_reported

**Implementation:**
```sql
TO_NUMBER(TO_DATE(TRIM(date_closed), 'MM/DD/YYYY') - date_reported)
```

---

## Data Load: Loading Data into Star Schema

Data is loaded into the star schema in the following order:

### Load Sequence

1. **dim_status** - Loaded first (no dependencies)
   - Simple dimension with predefined values
   - 3 rows: OPEN, CLOSED, ESCALATE

2. **dim_time** - Loaded second (no dependencies)
   - Generated programmatically
   - 72 rows (2015-2020, 12 months each)

3. **dim_station** - Loaded third (depends on pl_area)
   - Extracted from pl_station and pl_area
   - Transformations applied during load

4. **dim_crime_type** - Loaded fourth (no dependencies)
   - Extracted from pl_crime_type
   - Transformations and categorization applied

5. **dim_officer** - Loaded fifth (depends on pl_police_employee)
   - Extracted from pl_police_employee
   - Calculated fields: total_crimes_assigned, crimes_closed_count

6. **fact_crime** - Loaded last (depends on all dimensions)
   - Extracted from pl_reported_crime
   - Joined with all dimension tables
   - Measures calculated during load
   - Limited to 10 rows as per requirements

### Load Process Details

**Validation:**
- Check for NULL values in critical fields
- Verify foreign key relationships
- Validate measure calculations
- Count rows loaded

**Error Handling:**
- Handle NULL values appropriately
- Skip invalid records
- Log errors for review

**Performance:**
- Use indexes for joins
- Batch processing where possible
- COMMIT after each table load

---

## Appendix

### Appendix A: SS_DDL.sql

[See separate file: SS_DDL.sql]

Complete script to create all star schema tables.

---

### Appendix B: data_integration.sql

[See separate file: data_integration.sql]

Script to integrate PS_Wales data into PRCS system.

---

### Appendix C: ETL.sql

[See separate file: ETL.sql]

Complete ETL script to populate star schema with data.

---

### Appendix D: Sample Report Queries

#### Report 1: Open vs Closed Case Comparison

```sql
SELECT 
    dt.year,
    dt.month_name,
    ds.station_name,
    dct.crime_type_desc,
    COUNT(*) AS total_crimes,
    SUM(CASE WHEN dst.is_closed = 'N' THEN 1 ELSE 0 END) AS open_cases,
    SUM(CASE WHEN dst.is_closed = 'Y' THEN 1 ELSE 0 END) AS closed_cases,
    ROUND(SUM(CASE WHEN dst.is_closed = 'Y' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS closed_percentage
FROM fact_crime fc
INNER JOIN dim_time dt ON fc.time_key_reported = dt.time_key
INNER JOIN dim_station ds ON fc.station_key = ds.station_key
INNER JOIN dim_crime_type dct ON fc.crime_type_key = dct.crime_type_key
INNER JOIN dim_status dst ON fc.status_key = dst.status_key
GROUP BY dt.year, dt.month_name, ds.station_name, dct.crime_type_desc
ORDER BY dt.year, dt.month, ds.station_name, dct.crime_type_desc;
```

#### Report 2: Crimes Closed Count by Station and Officer

```sql
SELECT 
    ds.station_name,
    do_officer.officer_name,
    dt.year,
    dt.month_name,
    SUM(fc.crimes_closed_count) AS total_closed,
    COUNT(*) AS total_crimes_assigned,
    ROUND(SUM(fc.crimes_closed_count) * 100.0 / COUNT(*), 2) AS closure_rate
FROM fact_crime fc
INNER JOIN dim_station ds ON fc.station_key = ds.station_key
INNER JOIN dim_officer do_officer ON fc.officer_key = do_officer.officer_key
INNER JOIN dim_time dt ON fc.time_key_reported = dt.time_key
WHERE do_officer.officer_name IS NOT NULL
GROUP BY ds.station_name, do_officer.officer_name, dt.year, dt.month_name
ORDER BY total_closed DESC;
```

#### Report 3: Station Performance Comparison

```sql
SELECT 
    ds.station_name,
    ds.region,
    COUNT(*) AS total_crimes,
    SUM(fc.crimes_closed_count) AS closed_crimes,
    ROUND(SUM(fc.crimes_closed_count) * 100.0 / COUNT(*), 2) AS resolution_rate,
    ROUND(AVG(fc.resolution_days), 1) AS avg_resolution_days
FROM fact_crime fc
INNER JOIN dim_station ds ON fc.station_key = ds.station_key
GROUP BY ds.station_name, ds.region
ORDER BY resolution_rate DESC, total_crimes DESC;
```

#### Report 4: Year-over-Year Crime Rate Comparison

```sql
SELECT 
    dt_current.year AS current_year,
    dt_previous.year AS previous_year,
    ds.station_name,
    COUNT(DISTINCT fc_current.fact_crime_id) AS current_year_crimes,
    COUNT(DISTINCT fc_previous.fact_crime_id) AS previous_year_crimes,
    CASE 
        WHEN COUNT(DISTINCT fc_previous.fact_crime_id) > 0 THEN
            ROUND((COUNT(DISTINCT fc_current.fact_crime_id) - COUNT(DISTINCT fc_previous.fact_crime_id)) * 100.0 / 
                  COUNT(DISTINCT fc_previous.fact_crime_id), 2)
        ELSE NULL
    END AS percentage_change
FROM fact_crime fc_current
INNER JOIN dim_time dt_current ON fc_current.time_key_reported = dt_current.time_key
INNER JOIN dim_station ds ON fc_current.station_key = ds.station_key
LEFT JOIN fact_crime fc_previous ON fc_previous.station_key = ds.station_key
    AND fc_previous.crime_type_key = fc_current.crime_type_key
LEFT JOIN dim_time dt_previous ON fc_previous.time_key_reported = dt_previous.time_key
    AND dt_previous.year = dt_current.year - 1
    AND dt_previous.month = dt_current.month
WHERE dt_current.year = EXTRACT(YEAR FROM SYSDATE)
GROUP BY dt_current.year, dt_previous.year, ds.station_name
ORDER BY percentage_change DESC;
```

#### Report 5: Officer Crime Hotspot Analysis

```sql
SELECT 
    do_officer.officer_name,
    do_officer.officer_grade,
    do_officer.total_crimes_assigned,
    do_officer.crimes_closed_count,
    COUNT(DISTINCT fc.crime_type_key) AS crime_types_handled,
    ROUND(do_officer.crimes_closed_count * 100.0 / 
        NULLIF(do_officer.total_crimes_assigned, 0), 2) AS closure_rate
FROM dim_officer do_officer
LEFT JOIN fact_crime fc ON do_officer.officer_key = fc.officer_key
WHERE do_officer.total_crimes_assigned > 0
GROUP BY do_officer.officer_name, do_officer.officer_grade, 
         do_officer.total_crimes_assigned, do_officer.crimes_closed_count
ORDER BY do_officer.total_crimes_assigned DESC, do_officer.crimes_closed_count DESC;
```

---

## Conclusion

This project successfully implements a Data Mart for Police Crime Analysis using star schema design. The Data Mart:

1. Integrates data from multiple source systems (PRCS and PS_Wales)
2. Provides a star schema structure optimized for analytical queries
3. Handles data quality issues through ETL transformations
4. Supports five key performance indicators through comprehensive reporting
5. Enables data-driven decision-making for Police Force Management

The implementation demonstrates understanding of data warehouse concepts, ETL processes, and business intelligence principles.

---

**End of Report**

