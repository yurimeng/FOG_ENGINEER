import numpy as np
rng = np.random.default_rng(20260728)
H = 8760
t = np.arange(H)
hod = t % 24
doy = t // 24

# ---------- 风电出力时序 (川西/凉山型: 冬春大风, 夏季弱) ----------
# AR(1) 驱动的风速, 叠加季节调制
def wind_series(cf_target):
    phi = 0.92                      # 小时级自相关
    e = rng.normal(0, 1, H)
    z = np.zeros(H)
    for i in range(1, H):
        z[i] = phi*z[i-1] + np.sqrt(1-phi**2)*e[i]
    # 季节: 12-4月大风(凉山干季), 6-9月小风(雨季)
    seas = 1.0 + 0.35*np.cos(2*np.pi*(doy-15)/365)
    # 日内: 午后略强
    diur = 1.0 + 0.10*np.sin(2*np.pi*(hod-9)/24)
    u = np.exp(0.55*z) * seas * diur        # 对数正态形态的风速代理
    # 标定风速使容量因子命中目标
    def power(v, s):
        v = v*s
        p = np.zeros_like(v)
        m = (v>=3)&(v<12)
        p[m] = ((v[m]-3)/(12-3))**3
        p[(v>=12)&(v<25)] = 1.0
        return np.clip(p,0,1)
    lo, hi = 0.1, 30.0
    for _ in range(200):
        mid = (lo+hi)/2
        if power(u, mid).mean() < cf_target: lo = mid
        else: hi = mid
    return power(u, (lo+hi)/2)

# ---------- 光伏出力时序 (川西高原) ----------
def solar_series(cf_target):
    decl = 23.45*np.sin(2*np.pi*(doy-81)/365)*np.pi/180
    lat  = 28.5*np.pi/180                  # 川西南 ~28.5N
    ha   = (hod-12)*15*np.pi/180
    cosz = np.sin(lat)*np.sin(decl)+np.cos(lat)*np.cos(decl)*np.cos(ha)
    clear = np.clip(cosz,0,None)**1.15
    # 云: 雨季(6-9月)云多
    wet = 1 - 0.45*np.exp(-((doy-225)/55.)**2)
    phi=0.85; e=rng.normal(0,1,H); z=np.zeros(H)
    for i in range(1,H): z[i]=phi*z[i-1]+np.sqrt(1-phi**2)*e[i]
    cloud = np.clip(0.72+0.30*z,0.05,1.0)*wet
    p = clear*cloud
    return np.clip(p*(cf_target/p.mean()),0,1)

# ---------- 调度 ----------
def dispatch(gen_mw, P_dc, P_bess, E_bess, rte=0.90, dod=0.90, soc0=0.5):
    """gen_mw: 发电出力(MW); P_dc: 数据中心恒定整体负荷(MW)
       返回各类电量(MWh)"""
    eff = np.sqrt(rte)
    Emax = E_bess*dod
    soc = Emax*soc0
    direct=stored_in=stored_out=export_=import_=0.0
    for g in gen_mw:
        d = min(g, P_dc); direct += d
        surplus = g - d; deficit = P_dc - d
        if surplus > 0 and E_bess > 0:
            c = min(surplus, P_bess, (Emax-soc)/eff)
            soc += c*eff; stored_in += c; surplus -= c
        export_ += surplus
        if deficit > 0 and E_bess > 0:
            dch = min(deficit, P_bess, soc*eff)
            soc -= dch/eff; stored_out += dch; deficit -= dch
        import_ += deficit
    return dict(direct=direct, stored_in=stored_in, stored_out=stored_out,
                export=export_, imp=import_)

CAP = 100.0
wind = wind_series(2000/8760)*CAP
solar= solar_series(1800/8760)*CAP
print(f"风电年发电 {wind.sum()/1e4:.3f} 亿kWh  CF={wind.mean()/CAP:.1%}  最大出力{wind.max():.1f}MW")
print(f"光伏年发电 {solar.sum()/1e4:.3f} 亿kWh  CF={solar.mean()/CAP:.1%}  最大出力{solar.max():.1f}MW")
np.save('wind.npy', wind); np.save('solar.npy', solar)
