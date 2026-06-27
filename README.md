# 中文核心论文写作指令库与skill

这是一套面向高质量中文核心期刊的通用论文写作模板与修改指令库，适用于电子信息、仪器科学、测控技术、自动化、嵌入式系统等工程类论文。

本仓库重点解决几个常见问题：

- 论文容易写成项目汇报、技术说明书或 AI 综述
- 摘要、引言、结论缺乏期刊化表达
- 图表、公式、术语、单位不统一
- 结果很多，但结论不够凝练，参数不够“落地”
- 用大模型辅助改稿时，容易改乱主线、覆盖人工修改

## 仓库内容

本仓库目前包含以下几类模板与规范：

- 中文核心论文通用写作指令
- 论文章节组织模板
- 投稿前检查清单
- 大模型写作提示词模板
- Word 排版规范说明
- 图表与公式细则
- 最简使用指南

## 适用对象

适合以下人群使用：

- 正在撰写中文核心期刊论文的研究生和工程技术人员
- 需要反复修改摘要、引言、结论和图表口径的作者
- 希望借助 AI 提高写稿效率，但又不希望稿件出现明显 AI 味的人
- 需要形成团队统一论文写作规范的课题组

## 使用方法

如果你是第一次使用，建议按下面顺序阅读：

1. 先看“最简使用指南”
2. 再看“中文核心论文通用指令”
3. 按“章节模板”搭建论文框架
4. 用“投稿前检查清单”做终稿核查
5. 如需 AI 协助，再使用“大模型写作提示词模板”

## 特点

这套模板强调以下原则：

- 先定主线，再铺数据
- 先给证据，再下结论
- 语言工程化、克制、准确
- 少写空话，优先写参数、条件和验证结果
- 图表、公式、术语、单位全稿统一
- 明确区分实测结果、归档结果、配置推导和理论计算

## 适用范围说明

本仓库提供的是“高质量中文核心期刊通用底稿”，不是某一本期刊的官方模板。正式投稿前，仍建议结合目标期刊的最新格式要求进行最后调整。

## 说明

本仓库内容来自真实工程论文反复修改过程中的经验沉淀，目标是让论文更像正式期刊论文，而不是汇报材料或说明文档。

欢迎基于此继续扩展、细化和复用。

# GPT 图复现与修图仿真代码

这个文件夹保持平铺结构：图、代码、假设说明、合成数据放在同一层，便于你直接打包、直接改、直接导出。

## 这次更新了什么

- 重新整理了输出目录，让每张图的 `svg / pdf / png`、脚本、`assumptions`、合成数据都能放在一个文件夹里。
- 补齐了几张已重做的图：
  - `06_touch_sensor_principle_calibration.*`
  - `07_lvsa_fig1_fig2_redraw.*`
  - `09_spectral_coherence_map_redraw.*`
  - `10_microelectrode_process_ic_redraw.*`
- 保留了显式 MPC 的重绘版本：
  - `06_explicit_mpc_page_repro_v2.*`
- 统一了脚本输出方式，全部采用可编辑矢量优先的导出流程。
<img width="1306" height="1204" alt="ChatGPT Image 2026年6月27日 22_22_55" src="https://github.com/user-attachments/assets/16b7680a-42f4-4ee4-8fb5-c0c69af61515" />

## 相比之前的改进

- 图面更接近顶级中文核心期刊审美：白底、细线、低饱和、少装饰。
- 从“画新图”收回到“复现原图”，优先保留原论文的结构、信息层级和版式逻辑。
- 统一了导出格式，默认同时生成 `SVG / PDF / PNG`，其中 `SVG` 最适合继续在 Visio、Illustrator、Inkscape 里编辑。
- 合成数据和假设说明单独落盘，避免把“复现图”误写成真实实验数据。
- 图和代码放在同一目录，方便后续交给 GPT 继续修图、继续仿真、继续迭代。

## 输出内容

### 已生成图

- `01_bleex_fig1_conceptual_sketch.*`
- `02_pv_dcmli_fig1_system_configuration.*`
- `03_pv_dcmli_fig2_topology.*`
- `04_wind_converter_fig1_system_structure.*`
- `05_wind_converter_fig2_modeling_diagram.*`
- `06_touch_sensor_principle_calibration.*`
- `07_lvsa_fig1_fig2_redraw.*`
- `06_explicit_mpc_page_repro_v2.*`
- `09_spectral_coherence_map_redraw.*`
- `10_microelectrode_process_ic_redraw.*`

### 脚本

- `draw_first_batch.py`
- `draw_second_batch.py`
- `draw_remaining_batch.py`
- `06_explicit_mpc_page.py`
- `09_cnn_basic_structure.py`

### 辅助文件

- `*_assumptions.md`：说明哪些部分是复现、哪些部分是合成、哪些部分只是版式/结构近似。
- `*_synthetic.csv / *_synthetic.json / *_grid.npz`：给图复现用的合成数据。
- `00_reproduction_targets.md`：当前复现目标清单。

## 脚本和图的对应关系

- `draw_first_batch.py` -> `01` 到 `05`
- `draw_second_batch.py` -> `06_touch_sensor_principle_calibration`
- `draw_remaining_batch.py` -> `07_lvsa_fig1_fig2_redraw`、`09_spectral_coherence_map_redraw`、`10_microelectrode_process_ic_redraw`
- `06_explicit_mpc_page.py` -> `06_explicit_mpc_page_repro_v2`
- `09_cnn_basic_structure.py` -> CNN 结构图相关复现

## 如何使用

### 1. 直接重跑全部脚本

在这个目录下逐个运行脚本即可，运行后会覆盖同名输出文件：

```powershell
python draw_first_batch.py
python draw_second_batch.py
python draw_remaining_batch.py
python 06_explicit_mpc_page.py
python 09_cnn_basic_structure.py
```

### 2. 只重跑单张图

直接运行对应脚本，或者在脚本里只保留你想要的那一段绘图代码。

### 3. 找输出文件

每个脚本会把结果写回当前文件夹，默认生成：

- `*.svg`
- `*.pdf`
- `*.png`

如果图里带了合成数据，也会一并留下对应的 `csv / json / npz`。

### 4. 继续交给 GPT 修图

把这一个文件夹直接丢给 GPT，就可以让它继续做：

- 调整线宽、间距、字体、标注
- 改成更适合中文核心期刊的图面
- 基于现有结构继续写仿真代码
- 把更适合编辑的图导成更干净的 `SVG`

## `assumptions` 的作用

每张图旁边的 `assumptions.md` 用来写清楚：

- 哪些是原图结构复现
- 哪些是合成数据
- 哪些是版式近似
- 哪些内容不应当当成真实实验或真实仿真结果引用

## 推荐工作流

1. 先锁定原论文图和目标风格。
2. 再用脚本复现结构。
3. 再根据中文核心审美微调线条、字体、标注和留白。
4. 最后导出 `SVG / PDF / PNG`，必要时再进 Visio 做二次编辑。

## 备注

- 这里的目标是“复现原论文图并做审美升级”，不是重新设计一套自己的图。
- 目录刻意不拆子文件夹，方便你后续打包、交付和继续迭代。
<img width="1152" height="1152" alt="811cff07c6eb74926830642d24fdf170" src="https://github.com/user-attachments/assets/a6adc7cc-ac58-4beb-bce1-eccd61346091" />
你的支持是我最大的动力
# -
