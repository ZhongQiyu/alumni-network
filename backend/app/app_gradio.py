# run_gradio.py

import gradio as gr
import pandas as pd

def process_table(data):
    """
    处理表格数据
    Args:
        data: 表格数据，列表格式
    Returns:
        处理后的结果
    """
    # 将数据转换为 DataFrame 以便进一步处理
    df = pd.DataFrame(data[1:], columns=data[0])
    
    # 这里可以进行进一步的数据处理，例如计算或验证
    result = df.describe()  # 作为示例，我们展示数据的统计信息
    
    # 返回处理后的数据或结果
    return result.to_markdown()

def show_form():
    """
    展示包含表格的表单界面
    """
    # 定义表格的列名
    columns = ["姓名", "年龄", "性别", "成绩"]

    # 创建一个表格组件
    table = gr.DataFrame(headers=columns, row_count=3, col_count=len(columns), label="输入数据")

    # 创建一个提交按钮
    submit_button = gr.Button("提交")

    # 创建一个用于展示处理结果的组件
    output = gr.Markdown()

    # 定义交互逻辑
    submit_button.click(fn=process_table, inputs=[table], outputs=output)

    # 将所有组件组合成一个界面
    gr.Interface(
        fn=None,
        inputs=[table, submit_button],
        outputs=output,
        title="数据表单提交"
    ).launch(share=True)

# 展示表单
show_form()
