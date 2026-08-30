import numpy as np, json
from model import dispatch
w100=np.load('wind.npy'); s100=np.load('solar.npy'); YI=1e5

def design(shape100, Pdc, label):
    """固定 DC 整体功率，求可纳入'就近消纳项目'的最大电源容量 G 及所需储能。
       目标：最大化 G（=最大化绿电覆盖率与政策覆盖电量），约束 250号文双门槛。"""
    print(f"\n{'─'*96}\n【{label}】数据中心整体负荷 {Pdc} MW （恒定，年用电 {Pdc*8760/YI:.2f} 亿kWh）\n{'─'*96}")
    print(f"{'储能':>12}{'最大电源G':>10}{'年发电':>9}{'自用/发电':>10}{'自用/用电':>10}{'绿电覆盖':>9}{'下网':>8}{'上网':>8}")
    print(f"{'MW/MWh':>12}{'MW':>10}{'亿kWh':>9}{'≥60%':>10}{'≥30%':>10}{'DC用电':>9}{'亿kWh':>8}{'亿kWh':>8}")
    out=[]
    for Eh,Pb in [(0,0),(20,10),(40,20),(60,20),(80,20),(100,25),(120,30)]:
        bestG=None
        for G in np.arange(Pdc*0.8, Pdc*4.0, 0.5):
            sh=shape100*(G/100.0)
            r=dispatch(sh,Pdc,Pb,Eh)
            self_=r['direct']+r['stored_out']
            f1=self_/sh.sum(); f2=self_/(Pdc*8760)
            if f1>=0.60 and f2>=0.30: bestG=(G,f1,f2,r,sh.sum())
        if bestG:
            G,f1,f2,r,gen=bestG
            cov=(r['direct']+r['stored_out'])/(Pdc*8760)
            b=f"{Pb}/{Eh}" if Eh else "无"
            print(f"{b:>12}{G:>10.1f}{gen/YI:>9.2f}{f1:>10.1%}{f2:>10.1%}{cov:>9.1%}{r['imp']/YI:>8.2f}{r['export']/YI:>8.2f}")
            out.append(dict(Pb=Pb,Eh=Eh,G=G,gen=gen/YI,f1=f1,f2=f2,cov=cov,imp=r['imp']/YI,exp=r['export']/YI,
                            direct=r['direct']/YI,sout=r['stored_out']/YI))
    return out

res={}
for Pdc in [20,25]:
    res[f'wind{Pdc}']=design(w100,Pdc,f'风电场景')
    res[f'pv{Pdc}']=design(s100,Pdc,f'光伏场景')
json.dump(res,open('design.json','w'),ensure_ascii=False,indent=1)
