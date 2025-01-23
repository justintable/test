from manim import *
import numpy as np

class TrigAnimation(Scene):
    def construct(self):
        # 设置基本参数
        radius_length = 1  # 单位圆半径
        scale_factor = 0.5  # 整体缩放
        x_length_factor = 1.2  # x轴延长因子
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-2, 2, 1],  # y轴范围扩大，但保持单位刻度不变
            x_length=10 * x_length_factor,
            y_length=8,  # y轴物理长度增加
            axis_config={
                "color": WHITE,
                "include_tip": True,
                "include_numbers": False,
                "line_to_number_buff": 0.2,
            },
        ).scale(scale_factor)
        
        # 添加 π 标记
        x_labels = [
            Text("π"), Text("2π"), 
            Text("3π"), Text("4π")
        ]
        for i, label in enumerate(x_labels):
            label.scale(0.5)
            label.next_to(
                axes.c2p((i+1)*PI, 0),
                DOWN * 0.3
            )
            self.add(label)
        
        # 计算正确的单位大小，确保圆和函数对齐
        unit_size = axes.get_y_unit_size()
        
        # 创建单位圆
        circle = Circle(
            radius=unit_size,
            color=WHITE
        )
        circle.move_to(axes.c2p(0, 0))
        
        # 创建旋转半径
        radius_line = Line(
            circle.get_center(),
            circle.get_center() + RIGHT * unit_size,
            color=RED
        )
        
        # 创建跟踪点
        dot_circle = Dot(color=RED).scale(0.5)
        dot_circle.add_updater(lambda d: d.move_to(radius_line.get_end()))
        
        curve_dot = Dot(color=RED).scale(0.5)
        
        # 创建水平虚线
        h_line = DashedLine(
            stroke_width=1,
            color=RED_A,
            stroke_opacity=0.7
        )
        
        def update_h_line(line):
            current_x = t.get_value()
            # 获取当前旋转半径端点的y值
            current_y = radius_line.get_end()[1] - circle.get_center()[1]
            # 更新虚线位置
            line.put_start_and_end_on(
                radius_line.get_end(),  # 从旋转半径端点开始
                axes.c2p(current_x, current_y/unit_size)  # 到当前x位置
            )
            # 更新函数跟踪点位置
            curve_dot.move_to(axes.c2p(current_x, current_y/unit_size))
            
        h_line.add_updater(update_h_line)
        
        # 创建正弦函数路径
        t = ValueTracker(0)
        sin_path = VMobject(color=RED, stroke_width=1)
        
        def update_path(path):
            new_path = VMobject()
            new_path.set_points_as_corners([
                axes.c2p(x, np.sin(x))
                for x in np.linspace(0, t.get_value(), 100)
            ])
            path.become(new_path)
        
        sin_path.add_updater(update_path)
        
        # 添加所有元素到场景
        self.play(Create(axes))
        self.play(Create(circle))
        self.add(radius_line, dot_circle, h_line, sin_path, curve_dot)
        
        # 创建动画
        self.play(
            Rotate(radius_line, angle=4*PI, about_point=circle.get_center()),
            t.animate.set_value(4*PI),
            run_time=8,
            rate_func=linear
        )
        
        self.wait()

if __name__ == "__main__":
    config.preview = True 