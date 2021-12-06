from manim import *

class LineExample(Scene):
    def construct(self):

        #bg_im = ImageMobject("bg.png")
        #self.add( bg_im)

        points = []
        points.append( np.array([-5,-2,0]) )
        points.append( np.array([-5, 1.,0]) )
        points.append( np.array([ 1, 1.,0]) )

        lines = []
        for i,j in zip( points, points[1:]):
            a = Line( i, j )
            a.set_stroke( BLUE, width=8 )
            lines.append(a)

        for i in lines:
            self.play(Write( i ), run_time=1 )
        self.wait()
