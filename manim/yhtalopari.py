from manim import *

class displayEquations(Scene):
    def construct(self):

        eq1_mob = MathTex( '4', 'x','+','3', 'y', '=', '-2', color=BLACK ) ## MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")
        eq2_mob = MathTex( '5', 'x','-','2', 'y', '=', '3', color=BLACK )
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(0.75*DOWN)

        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT).set_color(BLACK  )

        self.add(braces)
        self.play(Write(eq1),Write(eq2))
        self.wait(1)

        #
        # Change the colors of variables
        #
        eq1_mob.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_mob.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        self.play(Write(eq1_mob), Write( eq2_mob ) )
        self.wait(1)

        #
        # The rectangle and copied equation
        framebox1 = SurroundingRectangle(eq1_mob, buff = .1)
        self.play( Create( framebox1 ) )
        self.wait(1)

        eq1_dest =MathTex( '4', 'x','+','3', 'y', '=', '-2', color=BLACK )
        eq1_dest.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq1_dest.shift(2*DOWN)
        self.play( TransformMatchingTex( eq1_mob.copy(),  eq1_dest, path_arc=0*DEGREES ) )

        #
        # Move to up/down
        self.play( eq_group.animate.shift(3*UP),
                   framebox1.animate.shift(3*UP),
                   braces.animate.shift(3*UP),
                   eq1_dest.animate.shift(3*UP)
                  )
        self.wait(1)


        #
        # Solve for x:
        eq1_wall = MathTex( '4', 'x','+','3', 'y', '=', '-2', '||','-','3','y', color=BLACK ).shift(UP).shift(2*RIGHT)
        for i,item in enumerate(eq1_wall[:-4] ):
            item.align_to(eq1_dest[i],LEFT)
        eq1_wall.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        self.add( eq1_wall )
        c1 = eq1_wall[5].get_center()


        #Subtract 3y
        eq1_wall2 = MathTex('4', 'x','=', '-2','-', '3','y', color=BLACK).shift(0.25)
        c2 = eq1_wall2[2].get_center()
        eq1_wall2.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall2.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        self.play( TransformMatchingTex( eq1_wall.copy(), eq1_wall2, path_arc = -90*DEGREES ), run_time=2 )

        eq1_wall3 = MathTex('4', 'x','=', '-2','-', '3','y', '||', '\divisionsymbol', '4', color=BLACK).shift(1.9*RIGHT).shift(0.25*UP)
        for i,item in enumerate(eq1_wall3[:-3]):
            item.align_to(eq1_wall2[i],LEFT)
        eq1_wall3.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        self.add( eq1_wall3 )


        #Division by four (4)
        eq1_wall4 = MathTex('x','=','{-2','-', '3','y', ' \\over ', '4','}' , color=BLACK).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4[1].get_center()
        eq1_wall4.shift( -RIGHT*(c2-c1)[0] )
        self.play( TransformMatchingTex( eq1_wall3.copy(), eq1_wall4, path_arc = 0 ), run_time=2 )
        #Create a copy of last equation for the substitution
        eq1_wall4b = MathTex('{-2 - 3 y \\over 4}', color=RED_B ).shift(0.75*DOWN).shift(2.3*LEFT)

        #
        # Substitute x

        #Framebox
        framebox2 = SurroundingRectangle(eq2_mob, buff = .1)
        self.play( ReplacementTransform( framebox1, framebox2 ) )

        #Hide some and move others
        self.remove( eq1_dest )
        self.remove( eq1_wall2 )

        #Move 1st eq to left
        self.play( eq1_wall.animate.shift(5*LEFT),
                   eq1_wall3.animate.shift(5*LEFT),
                   eq1_wall4.animate.shift(5*LEFT)
                   )
        self.wait(1)

        #Move
        eq2_dest =MathTex( '5', 'x','-','2', 'y', '=', '3' , color=BLACK)
        eq2_dest.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest.shift(1*UP+3.5*RIGHT)
        self.play( TransformMatchingTex( eq2_mob.copy(),  eq2_dest, path_arc=0*DEGREES ) )
        c1 = eq2_dest[5].get_center()
        self.wait(1)

        #Copy the original and slide down
        eq2_dest1 =MathTex( '5', 'x','-','2', 'y', '=', '3' , color=BLACK)
        c2 = eq2_dest1[5].get_center()
        eq2_dest1.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest1.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest1.shift(.25*UP)
        self.play( TransformMatchingTex( eq2_dest.copy(),  eq2_dest1, path_arc=0*DEGREES ) )
        self.wait(1)

        #substitute the x from the left column
        eq2_dest2 =MathTex( '5', '{ -2 -3y \\over4}','-','2', 'y', '=', '3' , color=BLACK)
        eq2_dest2[1].set_color(RED_B)
        c2 = eq2_dest2[5].get_center()
        eq2_dest2.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest2.shift(.25*UP)
        self.play( TransformMatchingTex( eq1_wall4b,  eq2_dest2, path_arc=0*DEGREES ),
                   TransformMatchingTex( eq2_dest1, eq2_dest2, path_arc=0 ), run_time=2)

        #
        #
        #create a hidden copy
        eq2_dest3 =MathTex( '5', '{-2' , '-3' , 'y', '\\over 4}', '-','2', 'y', '=', '3' , color=BLACK)
        c2 = eq2_dest3[8].get_center()
        eq2_dest3.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest3.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest3.shift(0.25*UP)

        # Move the hidden copy (from top) to here. 
        eq2_dest4 =MathTex( '5', '{-2' , '-3' , 'y', '\\over 4}', '-','2', 'y', '=', '3' , color=BLACK)
        c2 = eq2_dest4[8].get_center()
        eq2_dest4.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest4.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest4.shift(-1*UP)
        self.play( TransformMatchingTex( eq2_dest3,  eq2_dest4, path_arc=0*DEGREES ) )
        self.wait(1)

        #distribute
        eq2_dest5 =MathTex( '5', '{-2 \\over 4}' , '-', '5',' {3' , 'y', '\\over 4}', '-','2', 'y', '=', '3', color=BLACK )
        c2 = eq2_dest5[10].get_center()
        eq2_dest5.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest5.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest5.shift(-1*UP)
        self.play( TransformMatchingTex( eq2_dest4,  eq2_dest5, path_arc=0*DEGREES ) )
        self.wait(1)

        #multiplication
        eq2_dest6 =MathTex( '-', '{5 \\over 2}' , '-' ,' {15' , 'y', '\\over 4}', '-','2', 'y', '=', '3' , color=BLACK)
        c2 = eq2_dest6[9].get_center()
        eq2_dest6.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest6.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest6.shift(-1*UP)
        self.play( TransformMatchingTex( eq2_dest5,  eq2_dest6, path_arc=0*DEGREES ) )
        self.wait(1)

        #Add the brace below
        b1 = Brace( eq2_dest6[2:9]).set_color(BLACK )
        self.play( Create( b1 )  )

        eq2_dest7 =MathTex( '-' ,' {15' , 'y', '\\over 4}', '-','{2\\times4', 'y', '\\over 4}' , color=BLACK).scale(0.7)
        eq2_dest7.shift( 3.1*RIGHT )
        eq2_dest7.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest7.shift(-2.5*UP)
        self.play( Create ( eq2_dest7  ) )
        self.wait(1)

        eq2_dest8 =MathTex( '-' ,' {15' , 'y', '+','8', 'y', '\\over 4}' , color=BLACK).scale(0.7)
        eq2_dest8.shift( 2.8*RIGHT )
        eq2_dest8.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest8.shift(-2.5*UP)
        self.play( TransformMatchingTex ( eq2_dest7, eq2_dest8, path_arc=0 ) )
        self.wait(1)

        eq2_dest9 =MathTex( '-' ,' {23' , 'y', '\\over','4}' , color=BLACK ).scale(0.7)
        eq2_dest9.shift( 2.8*RIGHT )
        eq2_dest9.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest9.shift(-2.5*UP)
        self.play( TransformMatchingTex ( eq2_dest8, eq2_dest9, path_arc=0 ) )
        self.wait(1)

        #
        #
        #

        eq2_dest10 =MathTex( '-', '{5 \\over 2}' , '-' ,' {23' , 'y', '\\over 4}', '=', '3', color=BLACK )
        c2 = eq2_dest10[6].get_center()
        eq2_dest10.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10.shift(-1*UP)
        self.play( Uncreate(b1), Uncreate(eq2_dest9), TransformMatchingTex( eq2_dest6,  eq2_dest10, path_arc=0*DEGREES ) )
        self.wait(1)

        #
        eq2_dest10_w1 =MathTex( '-', '{5 \\over 2}' , '-' ,' {23' , 'y', '\\over 4}', '=', '3', '  \\hspace{0.3cm}|| + ', '{5 \\over 2}', color=BLACK )
        c2 = eq2_dest10_w1[6].get_center()
        eq2_dest10_w1.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w1.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w1.shift(-1*UP)
        self.add( eq2_dest10_w1 )
        self.wait(1)

        #
        eq2_dest10_w2 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '3','+', '{5 \\over 2}' , color=BLACK)
        c2 = eq2_dest10_w2[4].get_center()
        eq2_dest10_w2.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w2.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w2.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w1.copy(), eq2_dest10_w2))
        self.wait(1)

        #
        eq2_dest10_w3 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '{3\\times2\\over 2}','+', '{5 \\over 2}' , color=BLACK)
        c2 = eq2_dest10_w3[4].get_center()
        eq2_dest10_w3.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w3.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w3.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w2, eq2_dest10_w3))
        self.wait(1)

        #
        eq2_dest10_w4 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '{6+5\\over 2}', color=BLACK )
        c2 = eq2_dest10_w4[4].get_center()
        eq2_dest10_w4.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w4.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w4.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w3, eq2_dest10_w4))
        self.wait(1)

        #
        eq2_dest10_w5 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '{11\\over 2}', color=BLACK )
        c2 = eq2_dest10_w5[4].get_center()
        eq2_dest10_w5.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w5.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w5.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w4, eq2_dest10_w5))
        self.wait(1)

        #
        eq2_dest10_w6 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '{11\\over 2}', '  \\hspace{0.1cm}|| \\times ', '{-4 \\over 23}' , color=BLACK)
        c2 = eq2_dest10_w6[4].get_center()
        eq2_dest10_w6.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w6.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w6.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w5, eq2_dest10_w6))
        self.wait(1)
 
        #
        eq2_dest10_w6 =MathTex( '-' ,' {23' , 'y', '\\over 4}', '=', '{11\\over 2}', '  \\hspace{0.1cm}|| \\times ', '{-4 \\over 23}' , color=BLACK)
        c2 = eq2_dest10_w6[4].get_center()
        eq2_dest10_w6.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w6.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w6.shift(-2.25*UP)
        self.play( TransformMatchingTex( eq2_dest10_w5, eq2_dest10_w6))
        self.wait(1)

        #
        eq2_dest10_w7 =MathTex( 'y', '=', '{11\\over 2}', '\\times', '{-4 \\over 23}', color=BLACK )
        c2 = eq2_dest10_w7[1].get_center()
        eq2_dest10_w7.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w7.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w7.shift(-3.55*UP)
        self.play( TransformMatchingTex( eq2_dest10_w6, eq2_dest10_w7))
        self.wait(1)

        #
        eq2_dest10_w8 =MathTex( 'y', '=', '{11\\over 1}', '\\times', '{-2 \\over 23}' , color=BLACK)
        c2 = eq2_dest10_w8[1].get_center()
        eq2_dest10_w8.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w8.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w8.shift(-3.55*UP)
        self.play( TransformMatchingTex( eq2_dest10_w7, eq2_dest10_w8))
        self.wait(1)

        #    
        eq2_dest10_w9 =MathTex( 'y', '=', '{-22\\over 23}', color=BLACK )
        c2 = eq2_dest10_w9[1].get_center()
        eq2_dest10_w9.shift( -RIGHT*(c2-c1)[0] )
        eq2_dest10_w9.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        eq2_dest10_w9.shift(-3.55*UP)
        self.play( TransformMatchingTex( eq2_dest10_w8, eq2_dest10_w9))
        self.wait(1)


        #
        # Back to X
        #
        c1 = eq1_wall[5].get_center()

        eq1_wall4 = MathTex('x','=','{-2','-', '3','y', ' \\over ', '4','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4[1].get_center()
        eq1_wall4.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4.shift( 1.2*DOWN )
        self.play( Create( eq1_wall4 ))

        eq1_wall4_1 = MathTex('x','=','{-2','-', '3','{-22\\over 23}', ' \\over ', '4','}' , color=BLACK).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_1.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_1[1].get_center()
        eq1_wall4_1.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_1.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex( eq2_dest10_w9.copy(), eq1_wall4_1), TransformMatchingTex( eq1_wall4, eq1_wall4_1 ))

        eq1_wall4_2 = MathTex('x','=','{-2','+', '{66\\over 23}', ' \\over ', '4','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_2.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_2[1].get_center()
        eq1_wall4_2.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_2.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_1, eq1_wall4_2) )

        eq1_wall4_3 = MathTex('x','=','{','{-2 \\times 23 \\over 23}','+', '{66\\over 4}', ' \\over ', '4','}' , color=BLACK).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_3.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_3[1].get_center()
        eq1_wall4_3.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_3.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_2, eq1_wall4_3) )

        eq1_wall4_4 = MathTex('x','=','{','{-46 \\over 23}','+', '{66\\over 23}', ' \\over ', '4','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_4.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_4[1].get_center()
        eq1_wall4_4.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_4.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_3, eq1_wall4_4) )

        eq1_wall4_5 = MathTex('x','=','{','{-46 +66 \\over 23}', ' \\over ', '4','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_5.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_5[1].get_center()
        eq1_wall4_5.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_5.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_4, eq1_wall4_5) )

        eq1_wall4_6 = MathTex('x','=','{','{20 \\over 23}', ' \\over ', '4','}' , color=BLACK).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_6.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_6[1].get_center()
        eq1_wall4_6.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_6.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_5, eq1_wall4_6) )

        eq1_wall4_7 = MathTex('x','=','{','20 ', ' \\over ', '4\\times 23','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_7.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_7[1].get_center()
        eq1_wall4_7.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_7.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_6, eq1_wall4_7) )

        eq1_wall4_8 = MathTex('x','=','{','4\\times 5 ', ' \\over ', '4\\times23 ','}', color=BLACK ).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_8.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_8[1].get_center()
        eq1_wall4_8.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_8.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_7, eq1_wall4_8) )

        eq1_wall4_9 = MathTex('x','=','{','5 ', ' \\over ', '23 ','}' , color=BLACK).shift(1.9*RIGHT).shift(0.75*DOWN)
        eq1_wall4_9.set_color_by_tex_to_color_map({ "x":RED_B, "y":GREEN_C })
        c2 = eq1_wall4_9[1].get_center()
        eq1_wall4_9.shift( -RIGHT*(c2-c1)[0] )
        eq1_wall4_9.shift( 1.2*DOWN )
        self.play(  TransformMatchingTex(eq1_wall4_8, eq1_wall4_9) )


        #
        #
        #
        self.wait(3)
        # https://3b1b.github.io/manim/getting_started/example_scenes.html
