# 标准 GUI 库导入（由基类统一导入）
import tkinter as tk
from tkinter import ttk
import webbrowser


class BaseGui:
    """
    GUI 基类，封装 Tkinter 常用控件的构建方式
    所有自定义 GUI 类继承该类即可使用 add_xxx 方法添加组件
    """

    def __init__(self, title="Base GUI", size="400x350"):
        """
        初始化窗口基础属性并执行组件布局方法
        :param title: 窗口标题
        :param size: 窗口尺寸（宽x高）
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)

        # 用于存储输入框/下拉框等组件的引用，方便统一获取值
        self.inputs = {}

        # 调用子类定义的 GUI 布局逻辑
        self.setup_gui()

    def setup_gui(self):
        """
        子类应重写此方法，实现具体的界面布局逻辑
        """
        pass

    def add_single_line_input(self, label_text, key):
        """
        添加单行输入框（Label + Entry）
        :param label_text: 标签文本（显示在输入框前）
        :param key: 存储该控件值的键
        """
        label = tk.Label(self.root, text=label_text)
        label.pack(anchor="w", padx=10)

        entry = tk.Entry(self.root)
        entry.pack(fill="x", padx=10)

        self.inputs[key] = entry

    def add_multi_line_input(self, label_text, key, height=5):
        """
        添加多行输入框（Label + Text）
        :param label_text: 标签文本
        :param key: 存储该控件值的键
        :param height: 文本行数
        """
        label = tk.Label(self.root, text=label_text)
        label.pack(anchor="w", padx=10)

        text = tk.Text(self.root, height=height)
        text.pack(fill="x", padx=10)

        self.inputs[key] = text

    def add_dropdown(self, label_text, key, options):
        """
        添加下拉框，标签和下拉框横向排列，限制宽度，提升界面美观度
        """
        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=10, pady=5)
        label = tk.Label(frame, text=label_text, width=10, anchor="w")
        label.pack(side="left")
        selected = tk.StringVar()
        selected.set(options[0])
        dropdown = ttk.Combobox(frame, textvariable=selected, values=options, state="readonly", width=20)
        dropdown.pack(side="left")
        self.inputs[key] = selected        

    def add_submit_button(self, command):
        """
        添加提交按钮
        :param command: 按钮绑定的事件函数
        """
        button = tk.Button(self.root, text="提交", command=command)
        button.pack(pady=10)

    def get_input_value(self, key):
        """
        获取某个输入组件的当前值
        :param key: 组件注册时使用的 key
        :return: 对应的用户输入或选择值
        """
        widget = self.inputs.get(key)

        if isinstance(widget, tk.Entry):
            return widget.get()

        elif isinstance(widget, tk.Text):
            return widget.get("1.0", tk.END).strip()

        elif isinstance(widget, tk.StringVar):
            return widget.get()

        return None

    def add_watermark(self):
        label = tk.Label(
            self.root,
            text="github.com/kissymoon",
            font=("Segoe UI", 12, "italic bold"),  # 放大并加粗
            fg="gray70",  # 浅灰色
            bg=self.root["bg"],  # 背景透明
            cursor="hand2",
            padx=15,  # 左右内边距
            pady=3,  # 上下内边距
            borderwidth=0,
            highlightthickness=0
        )

        # 关键点：底部居中 (relx=0.5横向居中, rely=1.0贴底部，anchor='s'底部对齐)
        label.place(relx=0.5, rely=1.0, anchor="s", y=-10)  # y=-10向上偏移10像素

        # 点击跳转（带超链接样式）
        label.bind("<Button-1>", lambda e: (
            webbrowser.open("https://github.com/kissymoon"),
            label.config(fg="#1E90FF")  # 点击瞬间变蓝
        ))

        # 悬停效果（更明显的交互反馈）
        label.bind("<Enter>", lambda e: label.config(
            fg="#1E90FF",  # 悬停亮蓝色
            font=("Segoe UI", 13, "italic bold")  # 轻微放大
        ))
        label.bind("<Leave>", lambda e: label.config(
            fg="gray70",  # 恢复浅灰
            font=("Segoe UI", 12, "italic bold")  # 恢复原大小
        ))
   

    def run(self):
        """
        启动 Tkinter 主事件循环（主线程挂起，直到窗口关闭）
        """
        self.root.mainloop()
