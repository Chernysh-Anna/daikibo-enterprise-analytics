# Enterprise Telemetry & Forensic Compensation Analytics
> Dual-Track Business Intelligence & Forensic Audit for Daikibo Industrials (Deloitte Job Simulation)

[![Tableau](https://img.shields.io/badge/Tableau-Desktop%202024+-E97627?logo=tableau&logoColor=white)](https://public.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Excel](https://img.shields.io/badge/Microsoft%20Excel-Advanced%20Logic-217346?logo=microsoftexcel&logoColor=white)](https://office.microsoft.com/)

---

## 📌 Executive Summary
This project investigates two distinct enterprise challenges for global manufacturer **Daikibo Industrials**:
1. **Operational Telemetry (IoT Analytics):** Isolating the root causes of recurring unscheduled production downtime across 4 international manufacturing hubs.
2. **Forensic HR Analytics (Governance & Equity):** Auditing corporate compensation structures across 37 job roles to identify systemic gender pay disparities and regulatory exposure.

---

##  High-Level Insights

* **87.4% of Global Downtime is Isolated to 2 Sites:** Out of 1,030 total failure minutes, **Factory Seiko** (480 min) and **Shenzhen** (420 min) drive the vast majority of operational losses.
* **Component-Level Vulnerability:** Downtime is heavily concentrated in just two device types: **Laser Welders** (100% of Seiko's downtime) and **Laser Cutters** (92.8% of Shenzhen's downtime). Machine operating temperatures remained normal (23°C–27°C), isolating failures to mechanical/servicing issues rather than overheating.
* **Severe Executive Pay Inequity:** Compensation disparity increases with organizational seniority. Executive tiers (C-Level, VP, Jr. Manager) average scores below $-20.0$ (categorized as **Highly Discriminative**), while entry-level engineering roles exhibit strong gender parity.

---

##  Data Pipeline & Architecture

### 1. Telemetry Ingestion & Engineering
* **Source:** 160,704 records (`daikibo-telemetry-data.json`) across 4 global locations.
* **Transformation:** Unpacked nested schema elements (`location`, `data`).
* **KPI Derivation:** Since telemetry pings occur every 10 minutes, unhealthy status pings were transformed into downtime minutes:
  ```sql
  -- Equivalent SQL Logic
  SELECT 
      location_factory,
      device_type,
      SUM(CASE WHEN data_status = 'unhealthy' THEN 10 ELSE 0 END) AS downtime_minutes
  FROM telemetry_records
  GROUP BY 1, 2;
  ```

### 2. Forensic HR Logic Model
* **Source:** Compensation parity indices across 37 factory roles.
* **Model Formula (Excel):**
  ```excel
  =IF(ABS(C2)<=10, "Fair", IF(ABS(C2)<=20, "Unfair", "Highly Discriminative"))
  ```

---

##  Dashboard Interface 
* Built an interactive dashboard allowing stakeholders to drill down from regional facility totals to device-level health diagnostics.
* Configured dynamic **Action Filters** on the regional downtime bar chart to auto-filter subordinate device metrics.

---

##  Strategic Recommendations

| Priority | Area | Finding | Recommended Action |
| :--- | :--- | :--- | :--- |
| **P1** | **Asset Reliability** | Laser Welders (Seiko) and Cutters (Shenzhen) cause 88.3% of global downtime. | Re-negotiate vendor SLAs and deploy targeted predictive maintenance sensors on optical alignment heads. |
| **P2** | **Governance** | C-Level (-25) and VP (-22.5) roles present high legal/reputational exposure. | Institute standardized salary bands across international sites; establish executive salary review committees. |
| **P3** | **Operations** | Meiyo facility exhibits systemic management-tier pay gaps (Mean: -14.36). | Audit promotion and compensation criteria specifically within Tokyo operations. |

---

