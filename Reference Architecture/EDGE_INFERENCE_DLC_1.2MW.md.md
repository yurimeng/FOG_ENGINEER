1.2MW 直冷式 AI 推理算力单元

  

Reference Architecture Version: v1.0
Last Updated: 2026-03-16

---

# **1 Overview / 架构概述**

### **EN**
This architecture is a high-density AI inference infrastructure based on direct liquid cooling (DLC).

The system integrates compute racks, cooling infrastructure, and power systems into a modular containerized deployment.


The architecture is designed for:

- High GPU density
    
- High power efficiency
    
- Rapid deployment
    
- Edge AI infrastructure
    
### **CN**
该架构为基于 **Direct Liquid Cooling（DLC）直冷技术** 的高密度 AI 推理算力单元。
系统将 **计算机柜、冷却系统和电力系统** 集成在一个模块化集装箱部署单元中。

设计目标包括：

- 高算力密度
    
- 高能源效率
    
- 快速部署
    
- 边缘 AI 算力基础设施
    

---

# **2 System Capacity / 系统规模**

  
Total IT Power
1.2 MW

DLC Rack Count
8 Racks


Air-Cooled Rack
1 Rack (Network / Control)

Power Density per Rack
150 kW

Deployment Unit
DC40 DLC Container

---

# **3 Compute Architecture / 计算架构**

Server Specification
Dual Socket CPU

Memory
≥ 1.5 TB RAM

GPU
NVIDIA H200/B200/B300 DLC Server

Networking
NVIDIA 400/800G IB

Network Interface
OCP 25G × 1

  

Server Form Factor
4U

Servers per Rack
8 Servers

Total Server Count
64 Servers

Total GPU Count
512 GPUs

Primary Use Case
AI Inference

---

# **4 Cooling Architecture / 冷却架构**

  

Cooling Technology
Direct Liquid Cooling (DLC)

  

Heat Rejection
Dry Cooler


Auxiliary Cooling
DX Cooling Support

  

Cooling Loop
Primary Loop
DLC Rack → Manifold → Plate Heat Exchanger → Dry Cooler

Secondary Loop
Dry Cooler + DX Assist

  

Cooling Water Temperature
Supply: 20–24°C
Return: 28–32°C

  

Air Cooling
One low-power air-cooled rack (network / management)

---

# **5 Power Architecture / 电力架构**

Grid Connection
Utility Grid

UPS System
Integrated Container UPS System

  

Energy Storage
External Battery Energy Storage System (BESS)

Power Flow
GRID → BESS → SWITCHGEAR → UPS → DC40

Backup Time
Short-duration ride-through and power stabilization.

---

# **6 Infrastructure / 基础设施**

  

Deployment Type
Containerized AI Datacenter

Compute Module
DC40 DLC Computing Container

Integrated Systems
- Compute
- Cooling
- Power Distribution
- UPS System

Deployment Timeline

  

75–90 Days

---

# **7 Redundancy Strategy / 冗余策略**

  

Power
T2 Infrastructure Level

  

Service Availability
Near T3 Operational Availability

Cooling
N+1 Cooling Capacity

  

Network
Single uplink expandable to dual uplink

---

# **8 Advantages / 优势**

High-density DLC cooling
Efficient GPU power density
Rapid containerized deployment
Lower cooling energy consumption

  

高密度直冷散热
GPU 功率密度高
集装箱快速部署
较低散热能耗

---

# **9 Limitations / 局限**

DLC infrastructure requires chilled water or hybrid cooling support.
DX assistance may be required in high ambient temperature regions.

DLC系统需要冷冻水或混合散热支持。
在高温地区可能需要 DX 辅助散热。

---

# **10 Typical Use Cases / 典型应用**
AI inference clusters
Regional AI service nodes
Edge AI infrastructure

AI 推理集群
区域 AI 服务节点
边缘 AI 算力基础设施