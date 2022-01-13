from manim import *

config.background_color = WHITE

class PolygonExample(ThreeDScene):
    def construct(self):
        points = []
        points.append( np.array([-6, 1,0]) )
        points.append( np.array([-4, 0 ,0]) )
        points.append( np.array([-2, 1 ,0]) )
        points.append( np.array([0, 0 ,0]) )
        points.append( np.array([2, 1 ,0]) )
        points.append( np.array([4, 0 ,0]) )
        points.append( np.array([6, 1 ,0]) )
        points.append( np.array([8, 0 ,0]) )

        #axes = ThreeDAxes()
        #self.add( axes )

        lines = []
        for i,j in zip( points, points[1:]):
            a = Line( i, j ).set_color( ORANGE )
            a.set_stroke( BLUE, width=8 )
            lines.append(a)

        for i in lines:
            self.play(Write( i ), run_time=1 )
        self.wait(1)


        self.move_camera( phi=50*DEGREES, run_time=2)
        self.wait(2)

class Exponentation(Scene):
    def construct(self):
        eq1 = MathTex( '(-1)^1', '= -1', color=BLACK)
        eq2 = MathTex( '(-1)^2', '= (-1)(-1)',' = 1', color=BLACK).shift(DOWN)
        eq3 = MathTex( '(-1)^3', '= (-1)(-1)(-1)','= -1', color=BLACK).shift(2*DOWN)

        #Align at left
        eq2.align_to( eq1[0], LEFT)
        eq3.align_to( eq1[0], LEFT)


        self.play( Write( eq1 ))
        self.wait(2)
        self.play( Write( eq2 ))
        self.wait(2)
        self.play( Write( eq3 ))
        self.wait(2)

