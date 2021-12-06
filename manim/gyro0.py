from manim import *

config.background_color = WHITE

class LineExample(Scene):
    def construct(self):

        # y = -0.0714285714x + 0.71
        a = Line( np.array([-4,1,0]), np.array([3, 0.5,0]) )
        a.set_stroke( BLUE, width=8 )
        self.play(Write( a ), run_time=2 )
        self.wait()

        #Create perpendicular: y = 14x+57
        #and draw the angle.
        b = Line( np.array([-4.3,14*(-4.3)+57,0]), np.array([-3.7,14*(-3.7)+57,0]) )
        b.set_stroke( RED, width=4 )
        angle = Angle( a, b, radius = 1, quadrant=(1,1), elbow=True, color=BLACK)
        self.play(Write( b ), run_time=1 )
        self.add( angle )
        self.wait()


        #Add an errorrenous line
        x1 = -1.5
        y1 = -0.0714285714*x1 + 0.71
        
        x3 = 1.1
        y3 = -0.0714285714*x3 + 0.71+1.07
        x4 = 4.1
        y4 = -0.0714285714*x4 + 0.71+1.07

        c = Line( np.array([x1, y1, 0]), np.array([1.1,1.7, 0]) )
        c.set_stroke( PURPLE )
        self.play( Write( c ), run_time=2 )
        d = Line( np.array([x3, y3, 0]), np.array([x4,y4, 0]) )
        d.set_stroke( BLUE, width=4 )
        self.play( Write( d ), run_time=2 )


        self.wait()
        
