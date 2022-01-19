# Graph Visualization via pyecharts

> by WangYC_99
>
> @NWPU changan Jan.18th 2022

### 1. environment

python=3.6

| pac        | version |
| ---------- | ------- |
| pip        | 21.2.2  |
| pyecharts  | 1.9.1   |
| xlrd       | 1.2.0   |
| simplejson | 3.17.6  |

### 2. usage

1. clone or download the repositry

```
git clone https://github.com/Frederick-the-Fox/Graph_Visualization.git
```

2. Put your xlsx file at the project dir

```
.
├── data.xlsx
├── readExcel.py
├── readme.md
└── visualize.py
```

3. parse the xlsx file and create the json file

```
python readExcel.py 
```

4. use the json file to create the javascript Graph

```
python visualize.py
```



*END*

