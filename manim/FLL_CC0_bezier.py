from manim import *

# Create animated bezier image.
# See more info @ https://cod3v.info/index.php?title=Short_introduction_to_Manim
#

config.background_color = WHITE

class BezierSplineExample(Scene):
    def construct(self):

        #bg_im = ImageMobject("bg.png")
        #self.add( bg_im)
        bezier = CubicBezier( start_anchor = np.array([-7,-2,0]), \
                             end_anchor = np.array([-9,2,0]), \
                             start_handle = np.array([-7,-1,0]), \
                             end_handle = np.array([23,.5,0]), \
                             )
        bezier.set_color(PINK)
        bezier.set_stroke_width(15)
        self.play(Write( bezier), run_time=15 )
        self.wait()
