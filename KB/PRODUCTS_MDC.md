# MDC – Modular Datacenter Cluster
**标准计算单元**  
**版本：V1.0**


## 1. 定义

MDC 是由多个模块组成的模块化数据中心。其中：

### 组成结构
- IT Zone
- Cooling Zone
- Power Zone

### 细化及参考
-IT ZONE： 算力单元，提供服务器容纳，UPS
	[[PRODUCTS_AC40]]: - ./KB/PRODUCTS_AC40.md
	[[PRODUCTS_DC45]]: - ./KB/PRODUCTS_DC45.md
	[[PRODUCTS_NETWORK]]: ./KB/3RD-PARTY/NETWORK/PRODUCTS_NETWORK.md
	[[UPS_EATON_9395XR]]：./KB/3RD-PARTY/POWER/UPS_EATON_9395XR.md
	[[AC40_NETWORK_CONF.pdf]] : AC40内部组网
-Cooling Zone：外制冷，为IT Zone内服务器提供额外的散热能力
	- ./KB/3RD-PARTY/COOLING/COOLING_SYSTEM_SOLUTION.md
	- ./KB/3RD-PARTY/COOLING/DRYCOOL_with_DX.md
-Power Zone：后备电源系统，在FOG COMPUTING中由BESS替换掉传统的柴油发电机系统
	- ./PROCESS/ATS/POWER_SYSTEMS

---

## 2. 最小节点

| 等级     | 容量     | 冷却方式 | 典型配置            | 使用场景       |
| ------ | ------ | ---- | --------------- | ---------- |
| Single | 0.5MW  | 浸没液冷 | 64*RTX Pro 6000 | 边缘推理       |
| Small  | 1.2 MW | DLC  | 64*B300         | 边缘推理/模型再训练 |


---

## 3. 设计原则

- 模块独立
- 并联扩展
- 分区消防
- 冗余供电

---

## 4. 并网逻辑

支持：
- 并网模式
- 孤岛模式
- BESS调节

---

## 5. Power Flow

参考MDC Power Flow.png

![[MDC Power Flow.png]]