# DC45 — Quick Tech Spec
**PowerPod with Direct Liquid Cooling (45ft Container)**

Version: V1.3 | Date: 2026-05-09

---

## 1. Layout / 布局图

![[../../KB/FOG D Series/DC45 Layout/TOP.svg|TOP.svg]]
*TOP View / 俯视图*

![[../../KB/FOG D Series/DC45 Layout/FRONT.svg|FRONT.svg]]
*Front View / 正视图*

![[../../KB/FOG D Series/DC45 Layout/SIDE.svg|SIDE.svg]]
*Side View / 侧视图*

---

## 2. Product Positioning

DC45 is a **45ft containerized modular data center with Direct Liquid Cooling (DLC)**, employing cold-plate liquid cooling technology for ultra-high-density AI/HPC cluster deployments.


> **Cooling Note**: DC45 supports two air-cooled heat rejection options. Select based on site conditions:
> - **Wind Wall Module**: 有过滤系统，适合内陆或空气状况良好的区域
> - **FCU Module**: 内循环，适用于海边或环境较恶劣的场景，不需要对空气进行特殊优化处理

---

## 3. IT Capacity

| Item | Parameter |
|------|-----------|
| **Total IT Capacity** | **1240kW** |
| DLC Racks | 8 × 155kW (155kW per rack) |
| Air-Cooled Rack | 1 × 40kW |
| Server Inlet Temperature | 24°C |
| Power Factor (UPS Output Side) | 0.9 |

### IT Load vs. Total Facility Load

| Item | Value | Notes |
|------|-------|-------|
| **IT Load** | 1240kW | Actual server/GPU consumption |
| **Total Facility Load** | ~1380–1560kW | Depends on PUE |
| **PUE (Low temp zone, dry cooler priority)** | ~1.12–1.15 | Low ambient temperature |
| **PUE (High temp zone, DX-dominant)** | ~1.25–1.35 | High ambient temperature |

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

---

## 5. Power Distribution

### 4.1 POD Main Distribution

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
| Main CDU | 1 | ~25A | 32A MCB |
| FCU Unit / Wind Wall Module | 1 | ~50A | 63A MCB |

### 4.2 Rack PDU

| Item | Parameter |
|------|-----------|
| Input Rating | **60A 415V** |
| Output Interface | **24-position C19 Output** |
| Protection | **Magnetic Hydraulic Circuit Breaker** |
| Power Cable | **1.5m AWG Cable** (factory pre-installed) |
| Installation Position | Rear-mounted |
| Monitoring | Current monitoring (PDU panel display) |

### 4.3 PDU Model Comparison

| Product     | Input Rating      | Output Interface   | Protection                 |
| ----------- | ----------------- | ------------------ | -------------------------- |
| **DC45**    | 60A 415V          | 24-position C19    | Magnetic Hydraulic Breaker |
| HP POD 240a | 30A / 60A 415V 3Ø | C13 / C19 optional | Standard MCCB              |

---

## 6. Structural Specifications

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

## 7. Network & Cable Management

| Item | Parameter |
|------|-----------|
| Cable Penetration | **Supports top and bottom entry** (cable or busbar) |
| Cable Tray | **Located above racks (top-mounted)** |
| Fiber/Network Entry | **Container side entry** |

---

## 8. Environmental & Compliance

### 7.1 Operating Environment

| Item | Parameter |
|------|-----------|
| Operating Temperature | **-45°C to +45°C** |
| Operating Humidity | Per standard data center (typically 40%–60% RH, non-condensing) |
| Operating Altitude | **TBD** |

### 7.2 Certifications

| Certification | Status |
|--------------|--------|
| UL Certification | **Components UL certified; complete unit requires on-site TUV field certification** |
| TUV Field Certification | **Required — arranged during deployment** |

---

## 9. Monitoring & Management System

| Item | Parameter |
|------|-----------|
| Monitoring System | **PLC-based MODBUS** |
| Communication Protocols | MODBUS / TCP/IP |
| Monitored Parameters | Voltage, current, power, temperature, humidity, UPS status, EPO circuits |
| Remote Access | **SNMP / Web** |
| Building Management System Integration | Supported (MODBUS protocol) |

---

## 10. Fire Protection & Safety

| Item | Parameter |
|------|-----------|
| Extinguishing Agent | **FM-200 (HFC-227ea)** |
| Detection System | **ASSD (Air Sampling Smoke Detection) / VESDA** |
| Fire Alarm Panel | **Included** |
| Manual Pull Station | **Included** |
| Horn/Strobe Alarm | **Included** |
| Access Control | **Card reader / Facial recognition supported** |

---

## 11. Service & Support

| Item | Parameter |
|------|-----------|
| Warranty Period | **1 Year** |
| Support Response Level | **9×5 NBD (Next Business Day on-site)** |
| Deployment Lead Time | **~195–305 days** (see SOP below) |
| On-site Commissioning | **Included in installation service** |
| Annual Maintenance Contract | **TBD** |

---

### Deployment SOP

| 阶段 | 周期 | 说明 |
|------|------|------|
| 场地勘测 Site Survey | 2 周 | 现场条件评估 |
| 方案设计 Engineering | 2 周 | 技术方案确认 |
| 生产制造 Manufacturing | 16–20 周 | 集装箱制造 + 设备集成 |
| 运输报关 Logistics | 35–60 天 | 海运 + 清关 |
| 安装部署 Installation | 30 天 | 现场安装 + 调试 |
| **总周期** | **~195–305 天** | 合同签署后起算 |

---

## 12. Site & Installation Requirements

| Item | Requirement |
|------|-------------|
| Ground Load Capacity | ~20–25T (requires professional engineering assessment) |
| Ground Levelness | ±0.5° |
| Clearance Requirements | Sufficient maintenance clearance around all four sides of container |
| Cooling System Connection | Dry cooler or cooling tower interface (based on heat rejection solution) |
| On-site Commissioning | **TBD** |
| Local Permits | **TBD** |

> **Site Recommendation**: Prioritize cold, dry climate locations (reduces DX dependence, improves PUE). Wind Wall Module is better suited for dry climates; FCU Module provides more stable performance under extreme temperatures.

---

## 13. DC45 Key Specifications Summary

| Item | Parameter |
|------|-----------|
| Container Type | 45ft High Cube (13,716mm × 2,438mm × 2,992mm) |
| IT Capacity | 1240kW |
| Cooling Method | DLC (Cold-Plate Liquid Cooling) |
| Heat Rejection Module | Wind Wall / FCU Module |
| Rack Quantity | 9 (8 DLC + 1 air-cooled) |
| UPS Model | EATON 9395XR-1500 (1500kW) |
| UPS Battery Backup | ~8 min (3×93LiG2) |
| Busbar | SIEMENS 2500A |
| CDU | 1.2MW Rack CDU |
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

*Document Version: V1.3 | Last Updated: 2026-05-09*
