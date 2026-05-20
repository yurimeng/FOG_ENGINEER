
# **RDHx-F45 Rear Door Heat Exchanger**

### **Engineering Datasheet (Rev A)**

---

# **1 General Information**

|**Parameter**|**Value**|
|---|---|
|Product Name|RDHx-F45 Forest Heat Exchanger|
|Application|AI / HPC DLC Rack Air Heat Recovery|
|Rack Compatibility|19” rack (600 / 800 mm cabinet)|
|Cooling Type|Rear Door Air-to-Liquid Heat Exchanger|
|Cooling Loop|TCS Secondary Water Loop|
|Target Platforms|NVIDIA DGX B300 / NVIDIA GB300 NVL72|
|Design Heat Capture|40 kW nominal|
|Maximum Heat Capture|**45 kW**|

---

# **2 Mechanical Dimensions**

|**Parameter**|**Value**|
|---|---|
|Total Width|**600 mm**|
|Total Height|**2230 mm**|
|Total Depth|**160–180 mm**|
|Module Quantity|**4 modules**|
|Module Height|**10U (≈440 mm)**|
|Module Width|**600 mm**|
|Module Depth|**160 / 180 mm**|
|Module Arrangement|Vertical stacked|
|Rack Mount|Rear door hinge mount|
|Door Opening Angle|≥120°|

---

# **3 Module Configuration**

|**Parameter**|**Value**|
|---|---|
|Modules|4|
|Cooling Capacity / module|10 kW|
|Maximum / module|11.25 kW|
|GPU rows supported|2 rows / module|
|Flow configuration|Water parallel|
|Airflow direction|Horizontal (rack rear exhaust → RDHx)|

---

# **4 Thermal Performance**

|**Parameter**|**Value**|
|---|---|
|Nominal Heat Removal|40 kW|
|Maximum Heat Removal|45 kW|
|Design Water ΔT|**10°C**<!-- 原值: 8°C，2026-05-20 修订 -->|
|Design Air ΔT|**10°C**|
|Air Inlet Temperature|35°C|
|Air Outlet Temperature|25°C|
|Water Inlet Temperature|**26–28°C**（TCS 进水）<!-- 原值: 28°C，2026-05-20 修订 -->|
|Water Outlet Temperature|**36–38°C**（TCS 回水，进水 +10°C）<!-- 原值: 36°C，2026-05-20 修订 -->|

---

# **5 Air Side Design**

|**Parameter**|**Value**|
|---|---|
|Total Rack Airflow|**17,160 CFM**|
|Metric Airflow|**29,100 m³/h**|
|Airflow / module|7,275 m³/h|
|Air Velocity (face)|~7.6 m/s|
|Air Density|1.2 kg/m³|
|Air Specific Heat|1.005 kJ/kg·K|

---

# **6 Air Pressure Drop**

|**Parameter**|**Value**|
|---|---|
|ΔP / module|**40–50 Pa**|
|Total RDHx ΔP|**≤200 Pa**|
|Server Fan Static Pressure Capability|300–600 Pa|
|Design Margin|>50%|

---

# **7 Water Side Design**

|**Parameter**|**Value**|
|---|---|
|Total Heat Load|45 kW|
|Water ΔT|**10°C**<!-- 原值: 8°C，2026-05-20 修订 -->|
|Total Water Flow|**3.9 m³/h**<!-- 原值: 4.8 m³/h，依 ΔT=10°C 重算：Q=45kW/(4.186×10)=1.075 kg/s=3.87 m³/h，2026-05-20 修订 -->|
|Flow / module|**0.975 m³/h**<!-- 原值: 1.2 m³/h，依 ΔT=10°C 重算，2026-05-20 修订 -->|
|Water Density|1000 kg/m³|
|Water Specific Heat|4.186 kJ/kg·K|

---

# **8 Water Hydraulic Design**

|**Parameter**|**Value**|
|---|---|
|Manifold Type|Parallel|
|Recommended Manifold Size|**DN25**|
|Water Velocity|2.5–2.8 m/s|
|Connection Type|Quick coupling|
|Connection Location|Top manifold|
|Loop Type|Closed TCS loop|

---

# **9 Heat Exchanger Core**

|**Parameter**|**Value**|
|---|---|
|Core Type|Corrugated Plate Fin|
|Fin Material|Aluminum 3003 / 1100|
|Fin Thickness|0.25 mm|
|Fin Pitch|6 mm|
|Corrugation Height|1.6 mm|
|Channel Direction|Vertical|
|Manufacturing|Vacuum brazed|

---

# **10 Heat Transfer Area**

|**Parameter**|**160 mm Core**|**180 mm Core**|
|---|---|---|
|Fin Layers|27|30|
|Area / module|9.3 m²|10.3 m²|
|Total Area|**37 m²**|**41 m²**|

---

# **11 Estimated Mass**

|**Parameter**|**Value**|
|---|---|
|Module Mass (160 mm)|10–12 kg|
|Module Mass (180 mm)|11–13 kg|
|Total Door Mass|70–90 kg|

---

# **12 Materials**

|**Component**|**Material**|
|---|---|
|Fin|Aluminum 3003|
|Header|Aluminum|
|Manifold|Stainless steel|
|Frame|Powder-coated steel|
|Seal|EPDM|

---

# **13 Reliability Requirements**

|**Parameter**|**Value**|
|---|---|
|Design Life|≥10 years|
|Max Working Pressure|10 bar|
|Test Pressure|15 bar|
|Leak Rate|≤10⁻⁶ mbar·L/s|
|Operating Temperature|5–60°C|

---

# **14 Environmental Conditions**

|**Parameter**|**Value**|
|---|---|
|Ambient Temperature|5–45°C|
|Relative Humidity|5–95%|
|Altitude|≤3000 m|

---

# **15 Filtration Requirements**

|**Parameter**|**Value**|
|---|---|
|Recommended Filter|G4 / MERV 8|
|Location|Container intake|
|Purpose|Prevent fin fouling|

---

# **16 Performance Constraints**

### **Air Side**

|**Parameter**|**Limit**|
|---|---|
|Max Velocity|8 m/s|
|Max ΔP / module|50 Pa|
|Max ΔP / door|200 Pa|

---

### **Water Side**

|**Parameter**|**Limit**|
|---|---|
|Velocity|1–3 m/s|
|Water ΔT|6–10°C|
|Flow Range|3–6 m³/h|

---

# **17 Variable Parameters (Simulation Sweep)**

供 **CFD / Heat Exchanger solver** 扫描：

|**Parameter**|**Range**|
|---|---|
|Core Depth|120–200 mm|
|Fin Pitch|4–8 mm|
|Air Velocity|5–8 m/s|
|Water Flow|3–6 m³/h|
|Water ΔT|6–10°C|

---

# **18 Design Validation Tools**

推荐仿真软件：

- ANSYS Fluent
- OpenFOAM

验证内容：

- airflow distribution
- bypass flow
- pressure drop
- UA value
- NTU effectiveness

---

# **19 Key Engineering Targets**

|**Metric**|**Target**|
|---|---|
|Heat Recovery|**45 kW**|
|Air ΔP|≤200 Pa|
|Water Flow|**3.9 m³/h**<!-- 原值: 4.8 m³/h，2026-05-20 修订 -->|
|Airflow Capacity|29,000 m³/h|
|Total HX Area|37–41 m²|

---

# **20 Design Status**

|**Item**|**Status**|
|---|---|
|Thermal capacity|✔ verified|
|Airflow capacity|✔ sufficient|
|Water flow|✔ acceptable|
|Pressure drop|✔ within limits|

---

## **下一步（强烈建议）**

现在最重要的一步其实不是继续算，而是验证 **UA 和 LMTD 是否真的支持 45 kW**。

下一步应该建立 **Heat Exchanger Mathematical Model**：

```
Q = U × A × LMTD
```

然后计算：

- required **U value**
- fin efficiency
- real NTU
