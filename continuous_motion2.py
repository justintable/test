from manim import *
import numpy as np

class OpeningManim(Scene):
    def construct(self):
        # 初始化场景
        self.wait()
        
        # 准备网格进行非线性变换
        grid = NumberPlane()
        grid.prepare_for_nonlinear_transform()
        
        # 创建化学方程式 (使用Text代替Tex避免LaTeX依赖)
        equation = Text("H2O + CO2 → H2CO3", font_size=36)
        equation.move_to(grid.get_center() + UP * 2)
        
        # 添加网格和方程式到场景
        self.add(grid, equation)
        
        # 播放动画
        self.play(
            grid.animate.apply_function(
                lambda p: np.array([
                    np.sin(p[1]),
                    np.sin(p[0]),
                    0,
                ]),
            ),
            equation.animate.apply_function(
                lambda p: np.array([
                    np.sin(p[1]) * 0.5,
                    np.sin(p[0]) * 0.5,
                    0,
                ]),
            ),
            run_time=3,
        )
        
        self.wait()

if __name__ == "__main__":
    config.preview = True 