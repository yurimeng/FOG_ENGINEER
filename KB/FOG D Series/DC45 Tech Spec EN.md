# DC45 — Quick Tech Spec
**PowerPod with Direct Liquid Cooling (45ft Container)**

Version: V1.4 | Date: 2026-05-21

> **V1.4 Update (per [[DESIGN/DC45 三支路冷却重评估 2026-05-21|DC45 Three-Branch Cooling Reassessment Rev 11]]):**
> 1. CDU spec uprated: heat-rejection ≥ 1500 kW / secondary flow ≥ 175 m³/h / secondary head ≥ 220 kPa / VFD secondary pump / 2N or N+1 redundancy
> 2. TCS coolant locked as **PG25** (25% propylene glycol solution); TCS inlet 26–28°C
> 3. Three-branch cooling architecture defined: primary CDU cold plates / 9× VERTIV DCD35 passive RDHX / 9× STULZ OHS-084-DG-FC ceiling units
> 4. Outdoor-side total heat-rejection baseline ≥ 1700 kW
> 5. Cold-plate manifold lock: 2 per rack (≤100 cold plates) or 3 per rack (>100), 1.6–2.1 L/min per branch, PICV + flow meter on every manifold inlet

---

## 1. Layout / 布局图

![[../../KB/FOG D Series/DC45 Layout/TOP.svg|TOP.svg]]
*TOP View / 俯视图*

![[FRONT.jpg]]
*Front View / 正视图*

![[SIDE.jpg]]
*Side View / 侧视图*

---

## 2. Product Positioning

DC45 is a **45ft containerized modular data center with Direct Liquid Cooling (DLC)**, employing cold-plate liquid cooling technology for ultra-high-density AI/HPC cluster deployments.

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

> **Cooling Architecture**: DC45 uses a **three-branch parallel TCS loop on PG25**, with all heat carried to the outdoor side (hybrid dry-cooler + DX) via the TCS secondary loop:
> - **Branch 1 — Primary CDU cold-plate loop**: 73% liquid-cooled heat from 8× DLC racks
> - **Branch 2 — 9× passive RDHX**: absorbs 47–55% of rear-door exhaust air heat
> - **Branch 3 — 9× ceiling-mounted STULZ OHS-084-DG-FC**: handles residual room air heat + UPS/auxiliary heat

---

## 3. IT Capacity

| Item | Parameter |
|------|-----------|
| **Total IT Capacity** | **1240kW** |
| DLC Racks | 8 × 150kW (150kW per rack, 73% liquid-cooled / 27% air-cooled) |
| Air-Cooled Rack | 1 × 40kW |
| TCS Inlet Temperature | **26–28°C** (CDU secondary supply to cold plates / RDHX / CeilAir condensers) |
| Rack Front Intake Temperature | **25–27°C** (CeilAir DX evaporator output 12–18°C, decoupled from TCS water temperature) |
| Server Exhaust Temperature | **41–48°C** at S-Max (exceeds DCD35 datasheet 40°C inlet ceiling by 1–8°C; under Vertiv review) |
| DLC Air-Cool Ratio (φ_air) | Design upper limit **27%**, CDU guardrail ≥ **8%** |
| Power Factor (UPS Output Side) | 0.9 |

### IT Load vs. Total Facility Load

| Item | Value | Notes |
|------|-------|-------|
| **IT Load** | 1240kW | Actual server/GPU consumption |
| **Total Facility Load** | ~1325–1675kW | Depends on PUE |
| **PUE (Low temp zone, dry cooler priority)** | ~1.07–1.15 | Low ambient; CeilAir compressors partially stage off |
| **PUE (High temp zone, DX-dominant)** | ~1.25–1.35 | High ambient; 9× CeilAir compressors run ~58 kW total |

---

## 4. Rack Specifications

| Item | Parameter |
|------|-----------|
| Rack Type | 48U Standard Rack |
| Rack Depth | 1200mm |
| Rack Width | 800mm |
| Rack Quantity | 9 racks (8 DLC + 1 air-cooled) |
| Liquid Cooling | Side-Mounted Manifold |
| PDU Position | Rear-mounted |
| Rack Rear Door to Container Wall Gap | 350mm |
| Bottom Cable/Pipe Space | 350–400mm (no raised floor in power distribution zone) |

### 4.1 Cold-Plate Manifold Configuration

| Item | Parameter |
|------|-----------|
| Manifolds per rack | **2** (cold plates ≤ 100) / **3** (cold plates > 100, NVL72-class) |
| Branches per manifold | 20–50 |
| Design flow per branch | **1.6–2.1 L/min** (30%+ margin inside the 1–3 L/min spec) |
| Manifold inlet fitting | **PICV (Pressure-Independent Control Valve) + flow meter** (prevents inter-manifold imbalance) |
| Total manifolds (DC45) | **16–24** (8 racks × 2–3 manifolds/rack) |
| Imbalance tolerance | ≤ 10% (within a manifold) / ≤ 15% (including inter-manifold) |

---

## 5. Cooling System (Three-Branch TCS PG25 Architecture)

### 5.1 TCS Overview

| Item | Parameter |
|------|-----------|
| Circulating fluid | **PG25** (25% propylene-glycol/water; all wetted equipment must be PG-compatible) |
| TCS inlet temperature | 26–28°C |
| TCS design ΔT | 10 °C (CDU secondary) / 8 °C (RDHX branch) |
| Total circulating flow (S-Max) | ≈ 148 m³/h |
| Total circulating flow (φ_air = 8% case) | ≈ 154 m³/h ← design ceiling |
| Total heat rejected (S-Max) | ≈ 1352 kW |
| Total TDH | 19–25 m H₂O |
| TCS main pump | **Nameplate 200 m³/h @ 25 m H₂O, PG-compatible impeller/seals, VFD, 2N or N+1** |
| Outdoor-side heat-rejection baseline | **≥ 1700 kW** (hybrid dry-cooler + DX plate-HX combo) |

### 5.2 Primary CDU (Branch 1)

| Item | Parameter |
|------|-----------|
| Heat-rejection capacity | **≥ 1500 kW** |
| Secondary-side flow | **≥ 175 m³/h** |
| Secondary-side head | **≥ 220 kPa (≈ 22 m H₂O)** |
| Secondary pump | **VFD-driven** |
| Redundancy | **2N or N+1** secondary pumps |
| Branch 1 design flow (S-Max) | 78 m³/h |
| Branch 1 design flow (φ_air = 8% ceiling) | 98.6 m³/h |
| Branch 1 ΔP | 47–128 kPa (varies with φ_air) |
| Served load | 8 × DLC racks cold plates (109.5 kW liquid load per rack) |

### 5.3 RDHX Branch (Branch 2)

| Item | Parameter |
|------|-----------|
| Quantity & model | **9 × VERTIV CoolLoop DCD35 (passive)**: 8 on DLC rack rear doors + 1 on the air-cooled rack rear door |
| Nominal capacity per unit | 35 kW (max 66 kW) |
| Max airflow per unit | 11,200 m³/h |
| Max water flow per unit | 5.3 m³/h |
| Water connection | DN25 (1") |
| Operating air inlet range | datasheet 10–40°C ⚠️ DC45 S-Max 41–48°C exceeds limit by 1–8°C, under Vertiv review |
| Actual air-heat absorption (TCS 26–28°C) | 47–55% (ε ≈ 0.55 passive-RDHX physical ceiling) |
| Branch 2 design flow (PG25) | ≈ 21 m³/h |
| Branch 2 ΔP | 36–62 kPa |

### 5.4 Ceiling-Mounted CeilAir Branch (Branch 3)

| Item | Parameter |
|------|-----------|
| Quantity & model | **9 × STULZ OHS-084-DG-FC** (self-contained DX with free-cooling loop, EG/PG compatible) |
| Nominal total cooling per unit | 25.6 kW (80°F DB / 67°F WB / 50% RH) |
| Sensible cooling per unit (DC45 conditions, PG25 27°C) | ≈ 26 kW (+13% PG25 uplift + +10% return-air temperature correction + +5% low-humidity correction) |
| 9-unit total sensible | ≈ 234 kW |
| Compressor input per unit | 8.2 kW (datasheet) / ≈ 6.4 kW (after PG25 27°C uplift) |
| Condenser flow per unit | **5.41 m³/h** (23.8 GPM, locked from datasheet) |
| Condenser ΔP per unit | 41.5 kPa @ EG40 / ≈ 48 kPa (PG25 corrected, +15%) |
| Weight per unit | 250 kg (~ 2250 kg total roof load for 9 units; requires structural review) |
| Branch 3 design flow | **48.7 m³/h** |
| Branch 3 ΔP | 63–73 kPa |
| Installation | Evenly distributed along container roof (13.7 m length) |

### 5.5 Three-Branch Hydraulic Summary (PG25, S-Max)

| Branch | Design flow | Peak-case flow | ΔP | TCS heat recovered |
|--------|------------|----------------|-----|-------------------|
| Branch 1 — Primary CDU cold plates | 78 m³/h | 98.6 m³/h @ φ_air=8% | 47–128 kPa | 876 kW |
| Branch 2 — 9× RDHX | 21 m³/h | 21 m³/h | 36–62 kPa | ≈ 189 kW |
| Branch 3 — 9× CeilAir | 48.7 m³/h | 48.7 m³/h | 63–73 kPa | ≈ 287 kW (incl. ~58 kW compressor input) |
| **TCS Total** | **≈ 148 m³/h** | **≈ 154 m³/h** | TDH 19–25 m H₂O | **≈ 1352 kW** |

### 5.6 Control Strategy

| Control layer | Logic |
|---------------|-------|
| **Flow distribution** | Every branch has a **PICV (Pressure-Independent Control Valve)** that holds setpoint flow regardless of upstream ΔP swings |
| **Cold-plate branch → GPU interlock** | Branch 1 flow < 70 m³/h → GPU throttle to 80%; < 60 m³/h → GPU throttle to 60% |
| **RDHX branch** | Any single RDHX < 1.5 m³/h → that rack's GPUs throttle + alarm |
| **CeilAir branch** | Branch 3 < 40 m³/h → alarm + roof-supply temperature trending |
| **CeilAir redundancy** | All 9 roof positions are occupied — no N+1; failure mitigation relies on GPU throttling |
| **Free Cooling (FC)** | The -FC variant carries a free-cooling loop; DC45's 26–28°C TCS sits above typical FC activation thresholds (< 10°C), so FC stays dormant under normal operation |

---

## 6. Power Distribution

### 6.1 POD Main Distribution

Power Distribution SLD

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

| Device | Qty | Notes |
|--------|-----|-------|
| Incoming Switchgear | 1 panel | Main breaker / CT / metering |
| UPS Main Cabinet | 1 panel | Online double-conversion, includes static bypass transfer logic |
| Bypass Panel | 1 panel | Contains MCCB + mechanical interlock (prevents both paths closing simultaneously) |
| Battery Bank (BESS) | Standalone config | Capacity based on backup time requirement |
| Busbar System | 1 set | **SIEMENS 2500A** enclosed plug-in busbar, includes end feed box |

**Tap-off Unit (TOU) Configuration:**

| Load Type | Qty | Current per Unit | MCB Rating |
|-----------|-----|-----------------|------------|
| DLC Water-Cooled Racks | 8 | ~200A | 250A MCB |
| Air-Cooled Rack | 1 | ~80A | 100A MCB |
| Main CDU (≥1500 kW, VFD secondary pump) | 1 | ~35A* | 50A MCB* |
| Ceiling-Mounted STULZ OHS-084-DG-FC | 9 | ~15A* | 20A MCB* |
| TCS Main Circulating Pump + RDHX Controllers | 1 group | ~20A* | 32A MCB* |

> *Current and MCB values are upper-bound estimates derived from the V1.4 three-branch cooling architecture. Power Engineer must verify against actual nameplate ratings at BOM lock (9× CeilAir total compressor input ≈ 58 kW; including fans + controls ≈ 70 kW).

### 6.2 Rack PDU

| Item | Parameter |
|------|-----------|
| Input Rating | **60A 415V** |
| Output Interface | **24-position C19 Output** |
| Protection | **Magnetic Hydraulic Circuit Breaker** |
| Power Cable | **1.5m AWG Cable** (factory pre-installed) |
| Installation Position | Rear-mounted |
| Monitoring | Current monitoring (PDU panel display) |

### 6.3 PDU Model Comparison

| Product     | Input Rating      | Output Interface   | Protection                 |
| ----------- | ----------------- | ------------------ | -------------------------- |
| **DC45**    | 60A 415V          | 24-position C19    | Magnetic Hydraulic Breaker |
| HP POD 240a | 30A / 60A 415V 3Ø | C13 / C19 optional | Standard MCCB              |

---

## 7. Structural Specifications

| Item | Parameter |
|------|-----------|
| Container Type | **45ft High Cube** |
| Exterior Dimensions (L×W×H) | **13,716mm × 2,438mm × 2,992mm** |
| Interior Clear Height | Varies by installation and cooling configuration (refer to actual drawings) |
| Interior Usable Width | Varies by installation and cooling configuration (refer to actual drawings) |
| Enclosure Rating | **Custom per requirement** |
| Empty Weight | ~16T (without IT load) |
| Loaded Weight (with IT) | ~20–25T (depends on configuration) |
| Foundation Requirements | ~20–25T load capacity, ground levelness ±0.5° |

---

## 8. Network & Cable Management

| Item | Parameter |
|------|-----------|
| Cable Penetration | **Supports top and bottom entry** (cable or busbar) |
| Cable Tray | **Located above racks (top-mounted)** |
| Fiber/Network Entry | **Container side entry** |

---

## 9. Environmental & Compliance

### 9.1 Operating Environment

| Item | Parameter |
|------|-----------|
| Operating Temperature | **-45°C to +45°C** |
| Operating Humidity | Per standard data center (typically 40%–60% RH, non-condensing) |
| Operating Altitude | **TBD** |

### 9.2 Certifications

| Certification | Status |
|--------------|--------|
| UL Certification | **Components UL certified; complete unit requires on-site TUV field certification** |
| TUV Field Certification | **Required — arranged during deployment** |

---

## 10. Monitoring & Management System

| Item | Parameter |
|------|-----------|
| Monitoring System | **PLC-based MODBUS** |
| Communication Protocols | MODBUS / TCP/IP |
| Monitored Parameters | Voltage, current, power, temperature, humidity, UPS status, EPO circuits |
| Remote Access | **SNMP / Web** |
| Building Management System Integration | Supported (MODBUS protocol) |

---

## 11. Fire Protection & Safety

| Item | Parameter |
|------|-----------|
| Extinguishing Agent | **FM-200 (HFC-227ea)** |
| Detection System | **ASSD (Air Sampling Smoke Detection) / VESDA** |
| Fire Alarm Panel | **Included** |
| Manual Pull Station | **Included** |
| Horn/Strobe Alarm | **Included** |
| Access Control | **Card reader / Facial recognition supported** |

---

## 12. Service & Support

| Item | Parameter |
|------|-----------|
| Warranty Period | **1 Year** |
| Support Response Level | **9×5 NBD (Next Business Day on-site)** |
| Deployment Lead Time | **~185–230 days** (see SOP below) |
| On-site Commissioning | **Included in installation service** |
| Annual Maintenance Contract | **TBD** |

---

### Deployment SOP

| Phase | Duration | Notes |
|-------|----------|-------|
| Site Survey | 15 days | On-site condition assessment |
| Business Prep | 15 days | Contract signing, payment, procurement |
| Manufacturing | 90–120 days | Container fabrication + equipment integration |
| Logistics | 45–60 days | Ocean freight + customs clearance |
| Deployment | 10–20 days | On-site installation + commissioning |
| **Total Lead Time** | **~185–230 days** | From contract signing |

---

## 13. Site & Installation Requirements

| Item | Requirement |
|------|-------------|
| Ground Load Capacity | ~20–25T (requires professional engineering assessment) |
| Ground Levelness | ±0.5° |
| Clearance Requirements | Sufficient maintenance clearance around all four sides of container |
| Cooling System Connection | Dry cooler or cooling tower interface (based on heat rejection solution) |
| On-site Commissioning | **TBD** |
| Local Permits | **TBD** |

> **Site Recommendation**: Prioritize cold, dry climate locations (reduces DX dependence, improves PUE). The closer TCS inlet sits to 26°C, the lower the CeilAir compressor draw.

---

## 14. DC45 Key Specifications Summary

| Item | Parameter |
|------|-----------|
| Container Type | 45ft High Cube (13,716mm × 2,438mm × 2,992mm) |
| IT Capacity | 1240kW (8 × 150kW DLC + 1 × 40kW air-cooled) |
| Cooling Method | DLC + RDHX + ceiling-mounted CeilAir on a three-branch parallel TCS PG25 loop |
| Rack Quantity | 9 (8 DLC + 1 air-cooled) |
| UPS Model | EATON 9395XR-1500 (1500kW) |
| UPS Battery Backup | ~8 min (3×93LiG2) |
| Busbar | SIEMENS 2500A |
| **CDU** | **Heat-rejection ≥ 1500 kW / secondary ≥ 175 m³/h / ≥ 220 kPa, VFD, 2N or N+1** |
| **RDHX** | **9 × VERTIV CoolLoop DCD35 (passive, DN25)** |
| **CeilAir** | **9 × STULZ OHS-084-DG-FC (self-contained DX + FC, EG/PG compatible)** |
| **TCS Fluid** | **PG25 (25% propylene-glycol/water)** |
| **TCS Inlet Temperature** | **26–28°C** |
| **TCS Total Circulating Flow** | **≈ 148–154 m³/h** |
| **Outdoor-side Heat-Rejection Baseline** | **≥ 1700 kW** (hybrid dry cooler + DX plate-HX) |
| Rack Front Intake Temperature | 25–27°C (CeilAir DX decoupled) |
| PDU Input | 60A 415V |
| PDU Output | 24-position C19, magnetic hydraulic breaker |
| Empty Weight | ~16T |
| Operating Temperature | -45°C to +45°C |
| Operating Humidity | Per standard data center |
| Extinguishing Agent | FM-200 |
| Detection System | ASSD / VESDA |
| Access Control | Card reader / Facial recognition |
| Monitoring | PLC MODBUS / SNMP / Web |
| Certification | Components UL certified; TUV field certification required |
| Warranty | 1 year (9×5 NBD) |

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| V1.4 | 2026-05-21 | Sync with [[DESIGN/DC45 三支路冷却重评估 2026-05-21\|Rev 11 Three-Branch Cooling Reassessment]]: CDU uprated to ≥ 1500 kW / ≥ 175 m³/h / ≥ 220 kPa (VFD + 2N/N+1); TCS fluid locked at PG25; locked 9× DCD35 RDHX + 9× STULZ OHS-084-DG-FC; added §5 Cooling System and §4.1 cold-plate manifold; outdoor-side baseline ≥ 1700 kW. EN: server inlet temperature corrected to 26–28°C; Deployment SOP translated to English. |
| V1.3 | 2026-05-09 | Server inlet temperature revised from 24°C to 26–28°C (TCS range) |

---

*Document Version: V1.4 | Last Updated: 2026-05-21*
