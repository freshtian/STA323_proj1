this is STA323_proj1

本项目基于spark,使用lifelines包，实现了常用的生存分析方法和流程，包括但不限于Kaplan-Meier，Cox Proportional Hazards，Accelerated Failure Time，Customer Lifetime Value。

生存分析（Survival Analysis）是一种统计方法，用于分析从开始观察到关注事件（event of interest）发生所经历的时间。这一事件通常被称为“失效”（failure）或“事件”（event），其具体含义根据研究情境可能包括以下类型的结果：

1.死亡（death）

2.疾病复发（disease recurrence）

3.设备故障（equipment failure）

4.或其他可以记录发生时间的事件（any other event that can be timed）。

本报告采用的是[Telco-Customer-Churn](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv)数据集,相关代码参考我github仓库[Survival Analysis](https://github.com/freshtian/STA323_proj1/blob/master/Q2.ipynb)

