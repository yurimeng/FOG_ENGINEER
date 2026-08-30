import math
S3=math.sqrt(3)
print("="*92); print("A. IT 容量与集装箱数量（KB 口径：DC45 IT 1240kW，PUE 1.07–1.15 低温区 / 1.25–1.35 高温区）"); print("="*92)
IT=1240.0
for pue,zone in [(1.15,'川西高原 低温区上限'),(1.25,'夏季高温工况')]:
    tot=IT*pue
    n=20000/tot
    print(f"  PUE {pue}: 单台整体负荷 {tot:.0f} kW → 20MW 可容纳 {n:.1f} 台 DC45 → 取 {int(n)} 台, "
          f"IT 合计 {int(n)*IT/1000:.2f} MW, 整体 {int(n)*tot/1000:.2f} MW")
N=14; PUE=1.15; TOT=IT*PUE/1000
print(f"\n  ▶ 选定：14 × DC45  |  IT {N*IT/1000:.2f} MW  |  整体 {N*TOT:.2f} MW  |  PUE {PUE}")

print("\n"+"="*92); print("B. 35kV↔0.4kV 变压器选型与短路电流校核"); print("="*92)
PF=0.95
S_unit=TOT/PF
print(f"  单台 DC45 视在功率 = {TOT:.3f} MW / PF {PF} = {S_unit:.3f} MVA")
for kVA,uk in [(1600,6.0),(2000,6.5),(2500,6.5),(3150,7.0)]:
    load=S_unit*1000/kVA
    Sk=kVA/(uk/100)/1000      # MVA
    Isc=Sk*1e6/(S3*400)/1000  # kA
    tag='← 推荐 1:1 配对' if kVA==2000 else ('短路电流过高' if Isc>50 else '')
    print(f"  {kVA:>5} kVA (Uk={uk}%): 负载率 {load:>5.0%} | 0.4kV侧 Sk={Sk:>5.1f} MVA | Isc≈{Isc:>4.1f} kA  {tag}")
print(f"  ▶ 结论：35/0.4kV 单台容量宜 ≤2000kVA，1台变压器 : 1台DC45 模块化配对；0.4kV 开关柜 Icu ≥ 50kA，母排动稳定 ≥105kA(峰)")

print("\n"+"="*92); print("C. 35kV 侧载流与出线回路"); print("="*92)
for P,name in [(N*TOT,'DC 整体负荷'),(20,'BESS 充/放峰值'),(N*TOT+20,'DC+BESS 同时最大')]:
    I=P*1000/(S3*35*PF)
    print(f"  {name:<16} {P:>6.2f} MW → 35kV 侧 {I:>6.0f} A")
print(f"  单回 YJV22-26/35 3×300mm² 直埋载流 ≈ 520 A；场内标准集电线路间隔 630 A")
print(f"  ▶ 结论：DC 20MW 仅需 1 回 35kV（占集电间隔 ~55%）；按 N+1 配 2 回双母线分段，任一回可带全部负荷")

print("\n"+"="*92); print("D. BESS 双变换替代 UPS —— 效率代价量化（Eaton 9395XR: 双变换 97.5% / ESS 节能模式 99%）"); print("="*92)
P_IT=N*IT/1000
for eff,mode in [(0.975,'常在线双变换 VFI'),(0.99,'ESS 节能模式')]:
    loss=P_IT*(1-eff)
    kwh=loss*8760*1000
    print(f"  {mode:<16} 效率 {eff:.1%} → 常年损耗 {loss*1000:>5.0f} kW → 年电量损失 {kwh/1e4:>6.0f} 万kWh")
d=P_IT*(0.99-0.975)*8760*1000
print(f"  ▶ 双变换 vs ESS 模式 年增损耗 = {d/1e4:.0f} 万kWh；按 0.25 元/kWh 计 ≈ {d*0.25/1e4:.0f} 万元/年，10年 {d*0.25*10/1e8:.2f} 亿元")
print(f"  ▶ 该损耗还需额外制冷带走：约 {P_IT*0.015*1000:.0f} kW 显热，抵消部分 PUE 收益")
print(f"  ▶ 工程结论：不取消 UPS。BESS(小时级,UL9540)+UPS(分钟级,ESS模式99%)分层；BESS 取代柴发，UPS 后备维持 DC45 内置 ~8min")

print("\n"+"="*92); print("E. BESS 20MW/40MWh 设备数量（KB 3rd-Party 清单：国轩 ESC480-125P261-UL = 125kW/261kWh）"); print("="*92)
n_e=math.ceil(40000/261); n_p=math.ceil(20000/125)
print(f"  按能量 40 MWh → {n_e} 台 ；按功率 20 MW → {n_p} 台 → 取 {max(n_e,n_p)} 台（系统时长 {max(n_e,n_p)*261/1000/20:.1f} h）")
print(f"  或采用 Tesla Megapack 2XL 大单元方案，PCS 出口经 0.69/35kV 升压一体机接 35kV 母线")
