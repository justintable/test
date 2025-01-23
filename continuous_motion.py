from manim import *
import numpy as np

class ContinuousMotion(Scene):
    def construct(self):
        # 创建一个基于正弦和余弦函数的参数方程
        # 这将生成一个流动的曲线效果
        func = lambda pos: np.sin(pos[0] / 3) * UP + np.cos(pos[1] / 3) * LEFT
        
        # 创建流线动画
        # stroke_width: 线条粗细
        # max_anchors_per_line: 每条线的最大锚点数
        stream_lines = StreamLines(
            func,
            stroke_width=3,
            max_anchors_per_line=40
        )
        
        # 将流线添加到场景中
        self.add(stream_lines)
        
        # 开始动画，设置预热和流动速度
        stream_lines.start_animation(
            warm_up=False,
            flow_speed=1.5
        )
        
        # 等待动画完成
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

if __name__ == "__main__":
    config.preview = True
    scene = ContinuousMotion()
    scene.render() 