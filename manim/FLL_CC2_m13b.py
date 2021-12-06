from manim import *

class LineExample(Scene):
    def construct(self):

        #bg_im = ImageMobject("bg.png")
        #self.add( bg_im)
        #ax = Axes(x_range=[0, 10, 2] ).add_coordinates();
        #self.add( ax )
        plane = NumberPlane( background_line_style={
                "stroke_color": BLACK,
                "stroke_width": 4,
                "stroke_opacity": 1
            },
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
                            )
        #self.add( plane )

        points = []
        points.append( np.array([-5.5, -1,0]) )
        points.append( np.array([-4.2,-0.2 ,0]) )
        points.append( np.array([ -3.5, 0.,0]) )
        points.append( np.array([ -3.1, 0.4,0]) )
        points.append( np.array([ -2.6, 0.5,0]) )
        points.append( np.array([ -2.2,.9 ,0]) )
        points.append( np.array([ -1.7,.9 ,0]) )
        points.append( np.array([ -1.2,1.05 ,0]) )

        points.append( np.array([ -0.8,.95 ,0]) )
        points.append( np.array([ -0.4,1.05 ,0]) )
        points.append( np.array([ -0.0,.95 ,0]) )
        points.append( np.array([  0.4,1.05 ,0]) )
        points.append( np.array([  0.8,.95 ,0]) )
        points.append( np.array([  1.2,1.05 ,0]) )
        points.append( np.array([  1.6,.95 ,0]) )

        points.append( np.array([ -8,1.05 ,0]) )

        lines = []
        for i,j in zip( points, points[1:]):
            a = Line( i, j )
            a.set_stroke( BLUE, width=8 )
            lines.append(a)

        lines[0].set_stroke( PINK, width=8 )
        lines[-1].set_stroke( PINK, width=8 )


        for i in lines:
            self.play(Write( i ), run_time=1 )
        self.wait()
