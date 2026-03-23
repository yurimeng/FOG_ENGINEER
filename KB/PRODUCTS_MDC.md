# MDC – Modular Data Center
**适用对象：ACC（Advanced Computing Cluster）标准计算单元**  
**版本：V1.0**


## 1. 定义

MDC 是由多个 AC40 / DC40 组成的模块化数据中心。其中：

-IT ZONE： 
	AC40: - ./KB/PRODUCTS_AC40.md
	DC40: - ./KB/PRODUCTS_DC40.md
	NETWORK: ./KB/3RD-PARTY/PRODUCTS_NETWORK.md
-Cooling Zone：- ./KB/3RD-PARTY/PRODUCTS_COOLING.md
-Power Zone：- ./PROCESS/ATS/POWER_SYSTEMS


---

## 2. 扩展等级

| 等级 | 容量 |
|------|------|
| Single | 0.5MW |
| Small | 1-2MW |
| Medium | 2-4MW |
| Large | 8MW |


---

## 3. 组成结构

- Power Zone
- Cooling Zone
- IT Zone
- Generator Zone （或者用BESS代替）

---

## 4. 设计原则

- 模块独立
- 并联扩展
- 分区消防
- 冗余供电

---

## 5. 并网逻辑

支持：

- 并网模式
- 孤岛模式
- BESS调节

---

## 6. 风险

- 多模块同步控制
- 电网波动冲击
- 负载不均