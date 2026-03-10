
# 0.5MW Immersion AI Inference Unit
0.5MW 浸没式AI推理算力单元

Reference Architecture Version: v1.0  
Last Updated: 2026-03-10

---

# 1 Overview / 架构概述

EN

This architecture is designed as a high-efficiency AI inference unit based on immersion cooling.

The system integrates compute, cooling, and power infrastructure into a single modular deployment.

It is optimized for low CAPEX, high density, and rapid deployment.

CN

该架构为基于浸没式液冷的AI推理算力单元。

系统将计算、冷却与电力基础设施整合为模块化部署单元。

设计目标为：

- 极低 CAPEX
- 高算力密度
- 快速部署

---

# 2 System Capacity / 系统规模

Total IT Power

0.5 MW

Server Count

64 Servers

Total GPUs

512 GPUs

Deployment Unit

AC40 Immersion Container

---

# 3 Compute Architecture / 计算架构

Server Specification

Dual Socket CPU

Memory

1.5 TB RAM

GPU

8 × NVIDIA RTX PRO 6000 Blackwell Server Edition

Networking

NVIDIA BlueField-3 DPU

Network Interface

OCP 25G × 1

Server Form Factor

4U

Server Count

64

Total GPU Count

512 GPUs

Primary Use Case

AI Inference

---

# 4 Cooling Architecture / 冷却架构

Cooling Technology

Immersion Cooling

Heat Rejection

Dry Cooler

Auxiliary Cooling

DX Cooling Support

Cooling Loop

Primary Loop

Immersion Tank → CDU → Heat Rejection System

Secondary Loop

Dry Cooler + DX Assist

Cooling Water Temperature

Supply: 32–35°C

Return: 35–40°C

---

# 5 Power Architecture / 电力架构

Grid Connection

Utility Grid

UPS System

EATON 9395XR

Energy Storage

1 MW Battery Energy Storage System (BESS)

Power Flow

GRID → BESS → SWITCHGEAR → AC40

Backup Time

Designed for short-duration ride-through and power stability.

---

# 6 Infrastructure / 基础设施

Deployment Type

Containerized Datacenter

Compute Module

AC40 Immersion Computing Container

Integrated Systems

Compute  
Cooling  
Power Distribution

Deployment Timeline

75–90 Days

---

# 7 Redundancy Strategy / 冗余策略

Power

T2 Infrastructure Level

Service Availability

Near T3 Operational Availability

Cooling

N+1 Cooling Capacity

Network

Single uplink expandable to dual uplink

---

# 8 Advantages / 优势

Ultra-low CAPEX per GPU

High density immersion cooling

Rapid deployment

Modular expansion capability

较低 GPU 单位成本  
高密度浸没散热  
部署速度快  
模块化扩展

---

# 9 Limitations / 局限

Energy storage system is used primarily for power stability.

BESS cannot be used for peak-shaving or energy trading.

储能系统主要用于电力稳定。

不适合进行峰谷套利。

---

# 10 Typical Use Cases / 典型应用

AI inference clusters

Regional AI service nodes

Edge AI infrastructure

AI 推理集群  
区域 AI 服务节点  
边缘 AI 算力基础设施