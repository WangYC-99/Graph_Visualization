import json
 
from pyecharts import options as opts
from pyecharts.charts import Graph
 
with open("class.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories = j

c = (
    Graph()
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=80,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="Graph-计算社会学2021班级朋友关系(班级分类)"),
    )
    .render("class.html")
)

print("graph has been created!!!")