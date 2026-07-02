#!/usr/bin/env python3
"""Create a reproducible figure-redraw package for Chinese core papers."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FIGURE_PRESETS = {
    "cnn": {
        "title": "CNN 模块结构图复现包",
        "script": "draw_cnn_pipeline.py",
        "outputs": ["cnn_pipeline.svg", "cnn_pipeline.pdf", "cnn_pipeline.png"],
        "data": ["cnn_blocks_synthetic.json"],
        "notes": [
            "白底、低饱和、模块化分组框、左到右流水线。",
            "保留卷积、池化、全连接、输出层和图例，不做海报式 3D 块。",
        ],
    },
    "topology": {
        "title": "工程拓扑/系统框图复现包",
        "script": "draw_topology_svg.py",
        "outputs": ["topology_refined.svg", "topology_refined.pdf", "topology_refined.png"],
        "data": ["topology_nodes_assumptions.json"],
        "notes": [
            "优先矢量重绘，保留器件、节点、变量、母线和反馈关系。",
            "不得让位图模型自动决定拓扑、电路符号、坐标轴或公式。",
        ],
    },
    "curve": {
        "title": "曲线/标定/性能图复现包",
        "script": "draw_curves.py",
        "outputs": ["curves_refined.svg", "curves_refined.pdf", "curves_refined.png"],
        "data": ["curve_data_synthetic.csv", "curve_metadata.json"],
        "notes": [
            "曲线、误差棒、坐标轴和图例必须由代码生成。",
            "没有原始数据时只能使用 synthetic/demo/illustrative 数据并写入 assumptions。",
        ],
    },
    "mpc": {
        "title": "显式 MPC 分区图复现包",
        "script": "draw_explicit_mpc_partition.py",
        "outputs": ["mpc_partition.svg", "mpc_partition.pdf", "mpc_partition.png"],
        "data": ["region_vertices_synthetic.json"],
        "notes": [
            "保留硬边界、多边形/多面体分区、极窄区域和参数轴。",
            "没有原 mpQP 矩阵时必须标为 toy mpQP / synthetic partition。",
        ],
    },
    "spectral": {
        "title": "谱相干/三维诊断图复现包",
        "script": "draw_spectral_coherence.py",
        "outputs": ["spectral_surface.png", "spectral_contour.svg", "spectral_contour.pdf"],
        "data": ["spectral_grid_synthetic.npz", "spectral_metadata.json"],
        "notes": [
            "保留坐标系统、色标范围、峰脊结构和诊断标注。",
            "不得把随机纹理当作诊断结果。",
        ],
    },
    "multi-panel": {
        "title": "多面板综合示意图复现包",
        "script": "draw_multi_panel_summary.py",
        "outputs": ["multi_panel_summary.svg", "multi_panel_summary.pdf", "multi_panel_summary.png"],
        "data": ["panel_layout_assumptions.json"],
        "notes": [
            "按制备/结构/机理/性能组织叙事，低饱和白底。",
            "曲线图、柱状图和验证图必须像论文图，不像 PPT 截图。",
        ],
    },
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff_-]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "figure_package"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_readme(package_name: str, figure_type: str, preset: dict[str, object]) -> str:
    outputs = "\n".join(f"- `{item}`" for item in preset["outputs"])
    data_files = "\n".join(f"- `{item}`" for item in preset["data"])
    notes = "\n".join(f"- {item}" for item in preset["notes"])
    return f"""# {preset["title"]}

本目录用于中文核心论文图件的重绘式复现、期刊化精修和可复现交付。

## 图件信息

- 包名：`{package_name}`
- 图件类型：`{figure_type}`
- 生成脚本：`{preset["script"]}`

## 预期输出

{outputs}

## 数据与假设文件

{data_files}
- `assumptions.md`
- `STYLE_GUIDE.md`

## 工作边界

{notes}

## 验收清单

- 原图对象、子图结构、图号关系和关键变量已保留。
- 数据图有脚本、数据文件或明确生成逻辑。
- 没有原始数据时，所有数据都标为 synthetic/demo/illustrative。
- 图件可导出 SVG/PDF 和高分辨率 PNG。
- 黑白打印和缩印后仍可读。
- 图中不塞长句解释，长解释放入正文、图注或 README。
"""


def build_assumptions(package_name: str, figure_type: str) -> str:
    return f"""# assumptions

本文件记录 `{package_name}` 的数据来源、重绘边界和假设。

## 数据边界

- 图件类型：`{figure_type}`
- 原始数据状态：待填写
- 若无原始数据：仅允许使用 synthetic/demo/illustrative 数据。
- synthetic 数据不得写成实验数据、实测数据或原文数据。

## 结构保真

- 必须保留的对象：待填写
- 必须保留的变量/坐标轴/器件编号：待填写
- 可以优化的视觉项：线宽、字体、灰度、对齐、标注拥挤、导出格式。
- 不得改变的内容：物理关系、数学关系、图号关系、核心结论。

## 人工确认

- 参考文献和图源是否合法引用。
- 数据口径与正文是否一致。
- 导师或目标期刊是否有格式要求。
"""


def build_style_guide() -> str:
    return """# STYLE_GUIDE

## 默认风格

- 白底优先，避免海报风、炫光、复杂背景和重阴影。
- 中文使用宋体或等效宋体；英文、数字、变量使用 Times New Roman。
- 低饱和配色，黑白打印仍能区分。
- 主轮廓线约 0.8-1.2 pt，辅助线约 0.35-0.7 pt。
- 图内文字只保留必要标签，长解释放正文或图注。

## 导出

- 矢量源优先：SVG/PDF。
- PNG 用于预览或投稿替代，分辨率不低于 300 dpi。
- 数据图必须保留脚本和数据文件。
"""


def build_common_style() -> str:
    return '''"""Shared plotting style for Chinese core-paper figures."""

from __future__ import annotations

import matplotlib.pyplot as plt


CN_CORE_COLORS = {
    "blue": "#4C78A8",
    "green": "#59A14F",
    "orange": "#F28E2B",
    "red": "#E15759",
    "purple": "#B07AA1",
    "gray": "#6B7280",
}


def apply_cn_core_style() -> None:
    """Apply a restrained journal-like Matplotlib style."""
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.9,
            "axes.grid": True,
            "grid.color": "#DDDDDD",
            "grid.linewidth": 0.45,
            "grid.alpha": 0.7,
            "font.family": ["Times New Roman", "SimSun", "serif"],
            "font.size": 8.5,
            "legend.frameon": False,
            "savefig.bbox": "tight",
            "savefig.dpi": 300,
        }
    )
'''


def build_script_stub(figure_type: str, preset: dict[str, object]) -> str:
    outputs = preset["outputs"]
    data_files = preset["data"]
    return f'''#!/usr/bin/env python3
"""TODO: generate {preset["title"]}."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUTS = {outputs!r}
DATA_FILES = {data_files!r}


def main() -> None:
    print("图件类型: {figure_type}")
    print("请在本脚本中实现可复现绘图逻辑，并输出:")
    for item in OUTPUTS:
        print(" -", ROOT / item)
    print("数据/假设文件:")
    for item in DATA_FILES:
        print(" -", ROOT / item)


if __name__ == "__main__":
    main()
'''


def create_package(output_dir: Path, package_name: str, figure_type: str, force: bool) -> Path:
    if figure_type not in FIGURE_PRESETS:
        valid = ", ".join(sorted(FIGURE_PRESETS))
        raise SystemExit(f"Unknown figure type: {figure_type}. Valid types: {valid}")

    preset = FIGURE_PRESETS[figure_type]
    package_dir = output_dir / slugify(package_name)
    if package_dir.exists() and any(package_dir.iterdir()) and not force:
        raise SystemExit(f"Output directory already exists and is not empty: {package_dir}")
    package_dir.mkdir(parents=True, exist_ok=True)

    write_text(package_dir / "README.md", build_readme(package_name, figure_type, preset))
    write_text(package_dir / "assumptions.md", build_assumptions(package_name, figure_type))
    write_text(package_dir / "STYLE_GUIDE.md", build_style_guide())
    write_text(package_dir / "common_style.py", build_common_style())
    write_text(package_dir / preset["script"], build_script_stub(figure_type, preset))

    for data_name in preset["data"]:
        data_path = package_dir / data_name
        if data_path.suffix == ".json":
            write_text(
                data_path,
                json.dumps(
                    {
                        "data_status": "synthetic_placeholder",
                        "figure_type": figure_type,
                        "note": "Replace with real data only when verified.",
                    },
                    ensure_ascii=False,
                    indent=2,
                )
                + "\n",
            )
        elif data_path.suffix == ".csv":
            write_text(data_path, "x,y,series\n0,0,synthetic_placeholder\n")
        elif data_path.suffix == ".npz":
            write_text(data_path.with_suffix(".npz.README.md"), "请用绘图脚本生成真实 .npz 文件。\n")
        else:
            write_text(data_path, "synthetic_placeholder\n")

    manifest = {
        "package_name": package_name,
        "figure_type": figure_type,
        "script": preset["script"],
        "outputs": preset["outputs"],
        "data": preset["data"],
        "synthetic_boundary": "未核验原始数据前，全部数据只能作为 synthetic/demo/illustrative。",
    }
    write_text(package_dir / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return package_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="outputs", help="Root output directory.")
    parser.add_argument("--name", default="cn_core_figure_package", help="Package name.")
    parser.add_argument(
        "--type",
        choices=sorted(FIGURE_PRESETS),
        default="cnn",
        help="Figure package type.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite files in an existing package directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    package_dir = create_package(Path(args.output_dir), args.name, args.type, args.force)
    print(package_dir)


if __name__ == "__main__":
    main()
