import json
D=json.load(open('design.json'))
CAP_W,CAP_PV,CAP_BESS,SAVE=4.5,3.5,0.85,0.40
P_MECH=0.4012

def run(key,cap,lab,P_MKT,base_name):
    d=[x for x in D[key] if x['Eh']==40][0]
    G,gen,cov=d['G'],d['gen'],d['cov']; su=d['direct']+d['sout']; ex=d['exp']
    inv_src=G*cap/100; inv_b=d['Eh']*CAP_BESS/100; save=20*SAVE/100
    inv_t=inv_src+inv_b; inv_n=inv_t-save
    rev_t=gen*P_MKT
    print(f"\n{'═'*96}")
    print(f"【{lab} · DC 20MW(整体) · BESS 20MW/40MWh】就近消纳电源边界 {G:.0f}MW · 年发电 {gen:.2f}亿kWh")
    print(f"  自发自用 {su:.2f}亿kWh(占发电{d['f1']:.0%}, 占DC用电{d['f2']:.0%}) · 余电上网 {ex:.2f}亿 · DC下网 {d['imp']:.2f}亿 · DC绿电覆盖 {cov:.0%}")
    print(f"  投资：电源 {inv_src:.2f}亿 + 储能 {inv_b:.2f}亿 = {inv_t:.2f}亿；就近侧免两级变电 -{save:.2f}亿 → {inv_n:.2f}亿")
    print(f"  基准：{base_name} = {P_MKT:.4f} 元/kWh → 年收入 {rev_t:.3f}亿 · 回本 {inv_t/rev_t:.1f}年 · ROI {rev_t/inv_t:.1%}")
    print(f"{'─'*96}")
    print(f"{'直供电价':>9}{'年收入':>9}{'静态回本':>10}{'简单ROI':>9}{'Δ回本':>9}{'ΔROI':>8}   结论")
    for p in [0.25,0.28,0.30,0.33,0.35,0.40]:
        rev=su*p+ex*P_MKT
        pb=inv_n/rev; roi=rev/inv_n
        print(f"{p:>8.2f}元{rev:>8.3f}亿{pb:>9.1f}年{roi:>8.1%}{inv_t/rev_t-pb:>+8.1f}年{roi-rev_t/inv_t:>+7.1%}   "
              +('优于基准' if pb<inv_t/rev_t else '劣于基准'))
    lo,hi=0.10,0.80
    for _ in range(60):
        m=(lo+hi)/2
        if inv_n/(su*m+ex*P_MKT)>inv_t/rev_t: lo=m
        else: hi=m
    print(f"  ▶ 盈亏平衡直供电价 = {(lo+hi)/2:.3f} 元/kWh")
    return d

print("█"*96)
print("情形一：增量项目（2025-06-01后投产）— 全量入市，综合上网均价按原PPT口径 0.25 元/kWh")
print("█"*96)
run('wind20',CAP_W,'风电',0.25,'传统全额上网市场均价')
run('pv20',CAP_PV,'光伏',0.25,'传统全额上网市场均价')
print("\n"+"█"*96)
print("情形二：存量项目（2025-06-01前投产）— 享机制电价 0.4012 元/kWh（就近消纳后放弃机制电价）")
print("█"*96)
run('wind20',CAP_W,'风电',P_MECH,'机制电价')
run('pv20',CAP_PV,'光伏',P_MECH,'机制电价')
