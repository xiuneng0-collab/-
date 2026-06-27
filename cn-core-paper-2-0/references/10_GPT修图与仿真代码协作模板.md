# GPT 修图与仿真代码协作模板

当用户要求“给 GPT 修图建议”“让 GPT 继续优化图”“希望 GPT 生成仿真代码”“把现有图修到中文核心 T1/T2/T3 水平并补代码”时，使用本模板。它应与 `06_中文核心图表公式细则.md` 和 `09_T1级工科绘图审美与复现规范.md` 配合使用。

## 1. 总原则

把任务拆成两条线同时交给 GPT：

1. **修图线**：基于现有图和原论文图号，指出结构、标注、线宽、字体、灰度、版式、导出格式的具体修正。
2. **代码线**：要求 GPT 输出可运行的 Python/MATLAB/SVG 代码，生成曲线、分区、谱图、拓扑图或矢量重绘图。

不要只让 GPT “给建议”。提示词必须要求它交付文件、代码、数据和自检说明。

## 2. 必须写入提示词的边界

- 这是“重绘式复现”和“期刊化精修”，不是发明新图。
- 不得改变原论文图的表达对象、子图结构、核心器件、坐标轴、变量和图号关系。
- 没有原始数据时，只能生成 synthetic / demo / illustrative 数据，并明确标注 assumptions。
- 曲线、谱图、MPC 分区图、标定曲线必须由代码生成，并保留数据文件或生成逻辑。
- 系统图、拓扑图、流程图、等效电路和建模框图优先交 SVG/PDF 矢量版本。
- image2 只能做位图型辅助视觉，不得控制电路拓扑、坐标轴、公式、曲线和器件编号。

当任务是 CNN 结构图复现时，再额外加一句：参考图的最佳风格不是 3D 立体块，而是白底、低饱和、模块化分组框、阶段箭头和底部图例的论文式结构图；默认按“复现风格”而不是“重新设计”处理。

当任务是材料、催化、环境、生物类多面板总图时，提醒 GPT：目标不是做成海报或商业信息图，而是做成中文核心期刊的“制备 / 结构 / 机理 / 性能”综合示意图。主面板必须有清晰叙事关系，少用花哨材质，少用高光和重阴影，曲线图与柱状图必须像论文图，不像 PPT 截图。

## 3. 给 GPT 的通用提示词骨架

```text
请按中文核心 T1 级工科论文图件标准，基于我提供的深度研究报告、原论文图号、参考页截图和现有重绘图，继续完成“修图建议 + 可复现代码”任务。

目标不是重新设计主题图，而是进行重绘式复现和期刊化精修。必须保留原图的表达对象、子图结构、核心器件、坐标轴、变量、标注逻辑和图号关系。不得逐像素复制原图，也不得把它改成泛化 AI 插画。

如果当前对象是 CNN 结构图，请优先复现以下论文式样式：白底、低饱和、模块化分组框、顶部模块名、底部重复次数、左到右流水线、底部统一图例、输出层单独收束。不要重新发明 3D 块风格，不要把它改成海报式插画。

请为每张图输出：
1. 结构保真检查：哪些对象和关系必须保留。
2. 修图建议：线宽、字体、灰度、对齐、标注、图例、坐标轴和导出格式。
3. 代码任务：应生成哪些 Python/MATLAB/SVG 脚本，脚本输入、输出和假设参数是什么。
4. 输出文件：SVG/PDF/PNG、CSV/JSON/NPZ、README 和 assumptions。
5. 自检清单：是否可复现、是否黑白可读、是否缩印可读、是否标明 synthetic 数据。

没有原始实验数据时，必须把仿真数据写为 synthetic/demo/illustrative，不得称为原文实验数据。

如果对象是 CNN 图，请额外输出：
1. 模块级重绘草图说明。
2. 分组框、图例、箭头和层次关系的具体排布建议。
3. 可直接复制给 GPT 的 CNN 重绘提示词。
4. 若要实现，优先给出 Python/Matplotlib 或 SVG 脚本骨架。

如果对象是多面板总图，请额外输出：
1. 主面板数量与叙事顺序。
2. 每个面板的内部分区和标题层级。
3. 哪些元素必须保留体积感，哪些必须改成纯矢量。
4. image2 提示词应如何压制 AI 味。
```

## 4. 图件类型与代码要求

### 概念装备图

- 修图重点：人体轮廓弱、装备杆件强、关节链清楚、引线不交叉。
- 代码要求：矢量重绘脚本；可选二维运动链姿态示意。
- 注意：通常不要求真实动力学仿真。

### 电力电子系统图与拓扑图

- 修图重点：母线对齐、器件方向、相桥臂对称、编号顺序、输出节点统一。
- 代码要求：SVG 拓扑图；可选阶梯波、调制序列或功率流示意仿真。
- 注意：调制策略不明确时，只能写 demo switching sequence。

### 传感器原理图与标定曲线

- 修图重点：结构、工作状态、等效电路和标定曲线形成闭环。
- 代码要求：简化传感器模型、校准曲线、误差棒、合成实验扰动。
- 注意：实验样式数据必须标注 synthetic。

### 机构爆炸图与运动支路图

- 修图重点：装配轴、部件分组、连接关系和运动学抽象。
- 代码要求：矢量爆炸图；简化几何/刚度/力矩曲线。
- 注意：没有 CAD 时不得假装有真实三维模型。

### 显式 MPC 分区图

- 修图重点：硬边界、多面体/多边形、极窄区域、参数轴和截面关系。
- 代码要求：region vertices、2D/3D 分区图、JSON 数据。
- 注意：没有原 mpQP 矩阵时，必须标为 toy mpQP / synthetic partition。

### 谱相干图与三维诊断图

- 修图重点：坐标轴、色条范围、峰脊结构、诊断标注。
- 代码要求：合成信号、谱相干/循环谱相干曲面、2D contour、网格数据。
- 注意：不得把随机纹理当诊断结果。

### 微电极工艺流程图与 i-c 曲线

- 修图重点：工艺对象、局部放大、尺寸标注、尺度尺和响应曲线对应。
- 代码要求：工艺流程 SVG、浓度-电流曲线、噪声时序、CSV。
- 注意：曲线斜率和噪声水平要可追溯。

### 风电全功率变流系统与建模框图

- 修图重点：物理系统主流程、背靠背变流器、DC link、滤波器、反馈变量。
- 代码要求：系统拓扑 SVG、模型框图 SVG、可选 DC-link 动态响应示意。
- 注意：参数假设必须写入 assumptions。

## 5. 推荐输出目录

```text
outputs/
  README.md
  STYLE_GUIDE.md
  assumptions.md
  common_style.py
  01_bleex_kinematic_redraw.py
  01_bleex_concept_refined.svg
  01_bleex_pose_overlay.png
  02_pv_dcmli_topology_and_waveform.py
  02_pv_dcmli_topology_refined.svg
  02_pv_dcmli_six_level_waveform.png
  03_touch_sensor_capacitance_calibration.py
  03_touch_sensor_principle_circuit.svg
  03_touch_sensor_calibration_curves.png
  04_lvsa_kinematics_stiffness.py
  04_lvsa_exploded_branch_refined.svg
  04_lvsa_stiffness_curves.png
  05_explicit_mpc_partition_generator.py
  05_explicit_mpc_partition_3d.png
  05_region_vertices_synthetic.json
  06_spectral_coherence_simulation.py
  06_spectral_coherence_surface.png
  06_spectral_coherence_contour.png
  07_microelectrode_process_ic_curves.py
  07_microelectrode_process_refined.svg
  07_microelectrode_ic_curves.png
  08_wind_converter_model_diagram.py
  08_wind_converter_system_model_refined.svg
  08_wind_converter_dc_link_response.png
  data_*.csv / data_*.json / data_*.npz
  logs_*.txt
```

## 6. 最终验收清单

- 原论文图号、子图结构和关键对象已保留。
- 修图建议不是泛泛审美词，而是可执行项。
- 每张数据图有脚本和数据路径。
- synthetic 数据、真实数据、重绘结构之间边界清楚。
- 图中没有长句解释，解释放 README 或正文。
- 黑白打印和缩印后仍可读。
- image2 没有生成拓扑、电路、坐标轴、公式和曲线。
- 输出包含 SVG/PDF 与高分辨率 PNG。
