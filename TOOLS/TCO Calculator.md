---
tags:
  - #MDC
---

# Fog Computing TCO Calculator
## Financial KPI & Baseline Assumptions

### Purpose

本计算器面向三类核心用户：

1. GPU Investor（GPU资产投资人）
2. EPC Investor（EPC/数据中心开发商）
3. Infrastructure Investor（基础设施基金、数据中心运营商）

由于不同投资主体关注点不同，应采用不同的KPI展示逻辑。

---

# 1. GPU Investor View

## 投资逻辑

购买GPU资产 → 出租GPU → 获取现金流 → 回收残值

重点关注股东回报（Equity Return）。

## Recommended KPIs

### Equity IRR

股东投入资本后的内部收益率。

最重要指标。

---

### Equity Multiple

股东投入资金最终获得的总回报倍数。

Formula:

Equity Multiple = Total Equity Returned / Equity Invested

Typical Range:

| Value | Assessment |
|---------|---------|
| <1.5x | Weak |
| 1.5x–2.0x | Acceptable |
| 2.0x–3.0x | Strong |
| >3.0x | Excellent |

---

### Payback Period

投资回收周期。

GPU资产折旧速度快，因此回本周期极为关键。

Target:

<3 years

---

### DSCR

Debt Service Coverage Ratio

用于衡量租金现金流覆盖债务的能力。

Target:

>1.5x

Preferred:

>2.0x

---

# 2. EPC Investor View

## 投资逻辑

建设并运营算力基础设施。

关注项目本身创造的价值，而非资本结构带来的杠杆收益。

## Recommended KPIs

### Project IRR

项目整体内部收益率。

最核心指标。

Target:

>20%

Excellent:

>30%

---

### NPV

Net Present Value

项目创造的绝对价值。

Target:

Positive

Preferred:

High positive value

---

### Payback Period

项目投资回收周期。

Target:

<4 years

Preferred:

<3 years

---

### IRR-WACC Spread

Formula:

IRR Spread = Project IRR − WACC

用于衡量项目超额收益能力。

Target:

>10%

Excellent:

>15%

---

# 3. Infrastructure Investor View

## 投资逻辑

长期持有基础设施资产。

关注稳定现金流和项目价值。

## Recommended KPIs

### Project IRR

核心收益指标。

---

### NPV

价值创造能力。

---

### DSCR

债务覆盖能力。

---

### Cash Yield

Formula:

Cash Yield = Annual Cash Distribution / Equity Invested

Target:

>10%

Preferred:

>15%

---

# 4. Lender / Bank View

## 投资逻辑

关注贷款安全性。

通常不重点关注IRR。

## Recommended KPIs

### DSCR

Debt Service Coverage Ratio

Target:

>1.30x

Preferred:

>1.50x

Excellent:

>2.00x

---

### LLCR

Loan Life Coverage Ratio

Target:

>1.50x

Preferred:

>2.00x

---

### Debt Yield

Formula:

Debt Yield = NOI / Outstanding Debt

Target:

>10%

Preferred:

>12%

---

### LTV

Loan To Value

Target:

<70%

Preferred:

<60%

---

# Recommended Homepage KPI Layout

## Basic Mode

适用于大多数投资人。

1. Project IRR
2. Equity IRR
3. Payback Period
4. NPV

---

## Advanced Mode

### Project Metrics

- Project IRR
- NPV
- IRR-WACC Spread

### Equity Metrics

- Equity IRR
- Equity Multiple

### Debt Metrics

- DSCR
- LLCR
- Debt Yield
- LTV

---

# Baseline Financial Assumptions

## Leverage Ratio

Recommended Default:

50%

Recommended Range:

0% – 80%

Reference:

| Ratio | Assessment |
|---------|---------|
| 0–30% | Conservative |
| 30–50% | Moderate |
| 50–65% | Market Standard |
| 65–80% | Aggressive |
| >80% | Highly Aggressive |

---

## GPU Utilization

Recommended Default:

85%

Recommended Range:

50% – 100%

Reference:

| Utilization | Assessment |
|---------|---------|
| <70% | Weak |
| 70–80% | Acceptable |
| 80–90% | Strong |
| >90% | Excellent |

---

## Electricity Cost

Recommended Default:

USD 0.06 / kWh

Recommended Range:

USD 0.03 – 0.12 / kWh

Reference:

| Cost | Region Example |
|---------|---------|
| 0.03–0.05 | Middle East |
| 0.05–0.07 | Texas |
| 0.07–0.10 | Europe |
| >0.10 | High Cost Markets |

---

## Contract Term

Recommended Default:

36 months

Recommended Range:

24–60 months

---

## Residual Value

Recommended Default:

15%

Recommended Range:

0–30%

Reference:

GPU residual values are highly uncertain and should remain conservative.

---

## GPU Price Decay

Recommended Default:

15% annually

Recommended Range:

10–25% annually

Example:

| Year | Relative Price |
|---------|---------|
| Y1 | 100% |
| Y2 | 85% |
| Y3 | 72% |
| Y4 | 61% |
| Y5 | 52% |

---

## WACC

Recommended Default:

10%

Recommended Range:

8–15%

Reference:

| WACC | Assessment |
|---------|---------|
| <8% | Institutional Capital |
| 8–10% | Infrastructure Projects |
| 10–12% | Private Capital |
| >12% | High Risk Projects |

---

# Recommended Base Case

用于所有公开演示和市场推广。

| Parameter | Baseline |
|------------|------------|
| Leverage Ratio | 50% |
| Utilization | 85% |
| Electricity Cost | $0.06/kWh |
| Contract Length | 36 Months |
| Residual Value | 15% |
| GPU Price Decay | 15% / Year |
| WACC | 10% |

该组合属于市场普遍认可的 Base Case，可用于投资人展示、融资讨论和项目初步可行性分析。