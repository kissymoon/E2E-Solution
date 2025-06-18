from .Basic_gui import BaseGui


class ControlGui(BaseGui):
    time_ls = ["任何时间",  "一天内",  "一周内",  "一个月内",  "一年内"]
    def __init__(self, title="控制面板", size="410x550", on_submit=None):
        """
        初始化控制面板
        :param title: 窗口标题
        :param size: 窗口尺寸
        :param on_submit: 提交按钮的回调函数，返回收集数据
        """
        self.on_submit_callback = on_submit  # 提交回调（由外部传入）
        self.result = None
        super().__init__(title, size)

    def setup_gui(self):
        """
        构建界面组件
        """
        # 关键字：多行输入框
        self.add_multi_line_input("关键字", "keywords", height=4)
        
        # 必包含：单行输入框，默认值为 whatsapp.com
        self.add_single_line_input("必包含", "must_include")
        self.inputs["must_include"].insert(0, "whatsapp.com")

        # 单选下拉框：语言、地区、域名、时间范围
        self.add_dropdown("语言", "language", ["英语"])
        self.add_dropdown("地区", "region", ["美国"])
        self.add_dropdown("域名", "domain", ["facebook.com", ".com", "instagram.com", "reddit.com"])
        self.add_dropdown("时间范围", "time_range", self.time_ls)

        # 默认选择“一个月内”
        self.inputs["time_range"].set("一个月内")

        # 添加cookies
        self.add_multi_line_input("cookies", "cookies", height=10)

        # 提交按钮
        self.add_submit_button(self.handle_submit)

        self.add_watermark()

    def handle_submit(self):
        """
        提交按钮的事件处理：
        - 收集用户填写或选择的信息
        - 返回字典形式数据
        - 执行外部回调
        - 关闭窗口
        """
        raw_keywords = self.get_input_value("keywords")
        keywords_list = [kw.strip() for kw in raw_keywords.splitlines() if kw.strip()]

        self.result = {
            "keywords": keywords_list,
            "must_include": self.get_input_value("must_include"),
            "language": self.get_input_value("language"),
            "region": self.get_input_value("region"),
            "domain": self.get_input_value("domain"),
            "time_range": self.time_ls.index(self.get_input_value("time_range")) +1
        }

        if self.on_submit_callback:
            self.on_submit_callback()

        self.root.destroy()  # 关闭窗口
