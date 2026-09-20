# -*- coding: utf-8 -*-
# SVG figures for TC-SHL-002 (units mm in labels; geometry in metres, doc datum: z from box bottom)
FONT='"Noto Sans CJK SC","Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif'
def plan(crop=None):
    S=64.0  # px per m
    ox,oy=110,95
    W,H=int(13.716*S+ox+150), int(2.438*S+oy+80)
    X=lambda x: ox+x*S
    Y=lambda y: oy+(2.438-y)*S   # y up on screen = rear at top
    o=[]
    vb=f'0 0 {W} {H}' if crop is None else f'{ox+crop[0]*S:.0f} 0 {(crop[1]-crop[0])*S:.0f} {H-20}'
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" font-family=\'{FONT}\' font-size="10">')
    def rect(x0,y0,x1,y1,fill,stroke="#333",sw=1,dash=None,op=1):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        o.append(f'<rect x="{X(x0):.1f}" y="{Y(y1):.1f}" width="{(x1-x0)*S:.1f}" height="{(y1-y0)*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')
    def txt(x,y,s,anchor="middle",size=10,fill="#222",rot=0):
        t=f' transform="rotate({rot} {X(x):.1f} {Y(y):.1f})"' if rot else ''
        o.append(f'<text x="{X(x):.1f}" y="{Y(y):.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill}"{t}>{s}</text>')
    def dim(x0,x1,y,label,above=True,at=None):
        yy=Y(y); 
        o.append(f'<line x1="{X(x0):.1f}" y1="{yy:.1f}" x2="{X(x1):.1f}" y2="{yy:.1f}" stroke="#555" stroke-width="0.8"/>')
        for x in (x0,x1): o.append(f'<line x1="{X(x):.1f}" y1="{yy-4:.1f}" x2="{X(x):.1f}" y2="{yy+4:.1f}" stroke="#555" stroke-width="0.8"/>')
        lx=(X(x0)+X(x1))/2 if at is None else X(at); anc="middle" if at is None else "start"
        o.append(f'<text x="{lx:.1f}" y="{yy-3 if above else yy+11:.1f}" text-anchor="{anc}" font-size="9" fill="#333">{label}</text>')
    # box outline
    rect(0,0,13.716,2.438,"#f7f7f7","#222",1.4)
    # fixed end sections (outside wing span)
    rect(0,0,0.940,2.438,"#e3e3e3","none")
    rect(12.776,0,13.716,2.438,"#e3e3e3","none")
    # 40ft posts
    for x0 in (0.762,12.776):
        rect(x0,0,x0+0.178,0.104,"#e0a020","#8a6000"); rect(x0,2.334,x0+0.178,2.438,"#e0a020","#8a6000")
    # wing panels
    rect(0.940,0.037,12.776,0.072,"#7fa8e0","#2b5fb0"); rect(0.940,2.367,12.776,2.402,"#7fa8e0","#2b5fb0")
    # hydraulic assemblies
    for x0 in (1.058,12.454):
        rect(x0,0.097,x0+0.200,0.297,"#e03030","#900"); rect(x0,2.142,x0+0.200,2.342,"#e03030","#900")
    # equipment zones (our boundaries; no product info)
    rect(0.350,0.919,1.250,2.119,"#cfe8ff","#4a7fb5",1,"3,2")
    rect(1.311,0.978,11.511,2.178,"#cfe8ff","#4a7fb5",1,"3,2")
    rect(11.511,0.978,12.411,2.178,"#cfe8ff","#4a7fb5",1,"3,2")
    rect(12.700,1.617,13.600,2.317,"#ffd9b3","#b56a20",1,"3,2")
    # doors end A
    rect(0.007,0.200,0.053,2.238,"#444","#222")
    txt(-0.25,1.22,"端门（双扇，外开）",size=8,rot=-90)
    txt(13.66,1.2,"封闭端墙（不开门）",size=8,rot=-90)
    txt(14.05,1.73,"爬梯（端墙外侧）",size=8,rot=-90)
    rect(13.716,1.494,13.830,1.966,"#999","#555")
    txt(0.8,1.55,"设备区 A",size=8); txt(3.9,1.58,"设备区 B（x 1 311 – 11 511）",size=9); txt(9.6,1.58,"设备区 B（x 1 311 – 11 511）",size=9); txt(11.96,1.55,"设备区 C",size=8); txt(13.15,1.96,"设备区 D",size=8)
    txt(3.9,0.5,"前通道",size=9,fill="#555"); txt(9.6,0.5,"前通道",size=9,fill="#555")
    txt(1.158,0.42,"液压总成",size=7.5,fill="#900"); txt(12.554,0.42,"液压总成",size=7.5,fill="#900")
    txt(1.158,2.50,"液压总成",size=7.5,fill="#900"); txt(12.554,2.50,"液压总成",size=7.5,fill="#900")
    txt(0.851,0.60,"40ft 立柱",size=7,rot=-90,fill="#8a6000"); txt(12.865,0.60,"40ft 立柱",size=7,rot=-90,fill="#8a6000")
    # dims
    dim(0,13.716,2.438+0.95,"总长 13 716（角件外缘）",True,0.15); dim(0,13.716,2.438+0.95,"总长 13 716（角件外缘）",True,7.3)
    dim(0.940,12.776,2.438+0.70,"飞翼开口 11 836（x 940 – 12 776）",True,1.1); dim(0.940,12.776,2.438+0.70,"飞翼开口 11 836（x 940 – 12 776）",True,7.3)
    dim(0,1.058,-0.30,"1 058",False); dim(1.058,1.258,-0.30,"200",False); dim(12.454,12.654,-0.30,"200",False); dim(12.654,13.716,-0.30,"1 062",False)
    # axes note
    o.append('</svg>')
    return "\n".join(o)

def section():
    S=170.0; ox,oy=120,40
    W,H=int(2.438*S+ox+480), int(3.30*S+oy+60)
    Yp=lambda y: ox+y*S
    Zp=lambda z: oy+(3.30-z)*S
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" data-fig="section" viewBox="0 0 {W} {H}" font-family=\'{FONT}\' font-size="17.5">']
    def rect(y0,z0,y1,z1,fill,stroke="#333",sw=1,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        o.append(f'<rect x="{Yp(y0):.1f}" y="{Zp(z1):.1f}" width="{(y1-y0)*S:.1f}" height="{(z1-z0)*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def txt(y,z,s,anchor="start",size=9,fill="#222"):
        o.append(f'<text x="{Yp(y):.1f}" y="{Zp(z):.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill}">{s}</text>')
    rect(0,0,2.438,0.172,"#dddddd","#333"); txt(1.219,0.10,"底架 + 地板（地板面 z 172）","middle",14.9)
    rect(0.978,0.172,2.178,2.472,"#f2f2f2","#4a7fb5",1,"3,2"); txt(1.578,1.3,"设备带 y 978 – 2 178","middle",15.8,"#4a7fb5")
    txt(0.52,1.3,"前通道","middle",15.8,"#555")
    rect(0.037,0.172,0.072,2.698,"#7fa8e0","#2b5fb0"); rect(2.367,0.172,2.402,2.698,"#7fa8e0","#2b5fb0")
    rect(0.024,2.588,0.069,2.688,"#4a7fb5","#1f3f70"); rect(2.370,2.588,2.415,2.688,"#4a7fb5","#1f3f70")
    rect(0.024,2.698,0.104,2.858,"#e0a020","#8a6000"); rect(2.335,2.698,2.415,2.858,"#e0a020","#8a6000")
    rect(0.041,2.861,2.397,2.886,"#bbbbbb","#333")
    rect(0,2.778,0.162,2.896,"#999","#333",1,"2,2"); rect(2.276,2.778,2.438,2.896,"#999","#333",1,"2,2")
    rect(-0.010,2.926,2.448,2.938,"#cfe8ff","#4a7fb5"); rect(0,2.938,0.120,3.038,"#cfe8ff","#4a7fb5"); rect(2.318,2.938,2.438,3.038,"#cfe8ff","#4a7fb5")
    rect(-0.010,3.038,2.448,3.25,"#eef5ff","#4a7fb5",1,"3,2")
    txt(1.219,3.16,"顶部设备模块（我方，底面 z 2 926，与角件顶面 2 896 留 30）","middle",14.9,"#2b5fb0")
    rect(2.142,0.172,2.342,1.230,"#e03030","#900"); rect(2.142,1.230,2.342,2.018,"#f0a0a0","#900",1,"2,2")
    txt(2.13,0.70,"液压总成 200 深","end",14.0,"#900"); txt(2.13,1.60,"活塞杆/支架包络至 z 2 018","end",14.0,"#900")
    # fanned labels
    labels=[(3.038,"z 3 038 顶模块底横梁上缘（我方）","#2b5fb0"),(2.926,"z 2 926 顶模块底面（我方）","#2b5fb0"),(2.896,"z 2 896 角件顶面","#333"),(2.886,"z 2 886 顶板上表面（板厚 25）","#333"),(2.858,"z 2 858 固定顶侧梁 80×160 上缘","#8a6000"),(2.698,"z 2 698 顶侧梁下缘 / 翼板上缘","#8a6000"),(2.688,"z 2 688 翼框顶杆 45×100 上缘","#1f3f70"),(2.588,"z 2 588 翼框顶杆下缘","#1f3f70"),(2.018,"z 2 018 液压总成包络上限","#900"),(1.230,"z 1 230 液压缸体上缘","#900"),(0.172,"z 172 地板面","#333")]
    ly=Zp(3.30)+6
    for z,t,c in labels:
        yy=max(ly, Zp(z)-6) if z>2.4 else Zp(z)
        ly=yy+24
        o.append(f'<polyline points="{Yp(2.45):.1f},{Zp(z):.1f} {Yp(2.55):.1f},{yy:.1f} {Yp(2.60):.1f},{yy:.1f}" fill="none" stroke="{c}" stroke-width="0.7"/>')
        o.append(f'<text x="{Yp(2.62):.1f}" y="{yy+3:.1f}" font-size="14.9" fill="{c}">{t}</text>')
    o.append(f'<text x="{Yp(2.62):.1f}" y="{Zp(1.80):.1f}" font-size="14.9" fill="#900">铰链轴位置与开翼回转包络：待厂家确认（问题 A1/A2）</text>')
    o.append(f'<line x1="{Yp(0):.1f}" y1="{Zp(-0.12):.1f}" x2="{Yp(2.438):.1f}" y2="{Zp(-0.12):.1f}" stroke="#555" stroke-width="0.8"/>')
    txt(1.219,-0.16,"2 438（角件外缘）；翼板内表面净宽 2 295（y 72 – 2 367）；地板面至顶板下表面 2 689","middle",14.9,"#333")
    o.append('</svg>')
    return "\n".join(o)
if __name__=="__main__":
    open("fig_plan.svg","w").write(plan()); open("fig_plan_L.svg","w").write(plan((-0.45,7.1))); open("fig_plan_R.svg","w").write(plan((6.6,14.3))); open("fig_section.svg","w").write(section())
    import cairosvg
    cairosvg.svg2png(url="fig_plan_L.svg", write_to="fig_plan_L.png", output_width=1200); cairosvg.svg2png(url="fig_plan_R.svg", write_to="fig_plan_R.png", output_width=1200)
    cairosvg.svg2png(url="fig_section.svg", write_to="fig_section.png", output_width=1200)
    print("ok")
