# L1800C45 上部模块管路系统 · 独立 Blender 文件 ^mdc-5d0c7ab5b8

- **文件**：`MDCX_TA_Piping_Standalone_20260911.blend`（Blender 5.1，压缩，1.2 MB，无外部链接）
- **来源**：`Fog/3D/Final/L1800 DC45-Busway v2 20260904.blend` → `TOP Add-on.STD` 下的 `PIPING BAY.STD` + `DECK QC.STD` + `VALVE_ID.STD`，2026-09-11 抽取；世界坐标与 RFI-PIP-001 Rev.1 / GA Rev.1 / STEP 完全一致（已逐件校核） ^mdc-70d9a1fdc3
- **结构**：场景 `PIPING_SYSTEM`，单位 mm 显示（几何为米）；父级已全部烘焙、修改器已应用、无约束
  - `PIPING_SYSTEM/` 根集合
    - `PRIMARY_HEADER_DN150`（53）· `HT_LOOP`（26）· `LT_LOOP`（76）· `EQ_DROP_DLC`（96）· `EQ_DROP_CW`（96）· `CDU_DROP`（32）· `DECK_QC_FLANGE`（42）· `VALVE_TAG`（81，含 40 个文字对象）—— 与 STEP 装配树同名，合计 502 件
    - `_REF_TOPFRAME`（102 件上部模块框架/甲板/舱壁，**默认 exclude、线框显示**，只作净距参考，不属于管路供货范围）
- **对象命名**：已去掉 `.STD` 后缀，与 RFI 清单位号一致（`PRI_HDR_Sup_Run`、`TFQC_EQ_02_DLC_S_F`、`EQ_02_DLC_Pipe_S_Handwheel`…）
- **用途**：给管路供应商 / 深化设计 / 出图的独立工作文件；改动请另存版本，不要回写到 0904 主模型
- **对外发包**：脱敏文件名 `MDCX_TA_Piping_RFI.blend`（`MDC/procurement/RFI-PIP-001_Rev1_发包/`）与本文件几何相同，本文件多一个参考集合 ^mdc-d9166cecaa
