from manim import *
pi = 3.14159

class MoreShapes(Scene):
    #A few more simple shapes
    def construct(self):
        pointer = CurvedArrow(-1*RIGHT,1*RIGHT+1*UP,angle=pi, color=MAROON_C)
    
        self.add(pointer)
        self.play( Rotating( pointer, radians=4.9*pi), run_time=5)

        a = Arrow( start=np.array([-1.1,-0.3,0]), end=np.array([3, -0.3,0]), color=MAROON_C )
        self.play(GrowArrow( a ), run_time=2 )


        self.wait(2)