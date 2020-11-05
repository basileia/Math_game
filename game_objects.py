from pyglet import gl
import pyglet


class Text_to_print:
    def __init__(self, font_size, coord, speed, text, color):
        self.font_size = font_size
        self.coord = coord
        self.speed = speed
        self.text = text
        self.color = color

    def draw_text(self, position_x):
        """Text rendering function"""
        int1, int2, int3, int4 = self.color
        text_to_print = pyglet.text.Label(
            self.text,
            font_size=self.font_size,
            color=(int1, int2, int3, int4),
            x=self.coord[0], y=self.coord[1], anchor_x=position_x,
        )
        text_to_print.draw()


class Line:
    def __init__(self, coordx, coordy, color, thickness):
        self.coordx = coordx
        self.coordy = coordy
        self.color = color
        self.thickness = thickness

    def draw_line(self):
        """Function for drawing a line"""
        gl.glColor4f(*self.color)
        gl.glLineWidth(self.thickness)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(self.coordx[0], self.coordy[0])
        gl.glVertex2f(self.coordx[1], self.coordy[1])
        gl.glEnd()


class Rectangle(Line):
    def __init__(self, coordx, coordy, color, thickness):
        super().__init__(coordx, coordy, color, thickness)

    def draw_rectangle(self):
        """Function for drawing a rectangle"""
        gl.glColor4f(*self.color)
        gl.glLineWidth(self.thickness)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(self.coordx[0], self.coordy[0])
        gl.glVertex2f(self.coordx[1], self.coordy[1])
        gl.glVertex2f(self.coordx[1], self.coordy[1])
        gl.glVertex2f(self.coordx[2], self.coordy[2])
        gl.glVertex2f(self.coordx[2], self.coordy[2])
        gl.glVertex2f(self.coordx[3], self.coordy[3])
        gl.glVertex2f(self.coordx[3], self.coordy[3])
        gl.glVertex2f(self.coordx[0], self.coordy[0])
        gl.glEnd()


class Bucket(Rectangle):
    def draw_bucket(self):
        """Function for drawing a line angled at two points"""
        gl.glColor4f(*self.color)
        gl.glLineWidth(self.thickness)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(self.coordx[0], self.coordy[0])
        gl.glVertex2f(self.coordx[1], self.coordy[1])
        gl.glVertex2f(self.coordx[1], self.coordy[1])
        gl.glVertex2f(self.coordx[2], self.coordy[2])
        gl.glVertex2f(self.coordx[2], self.coordy[2])
        gl.glVertex2f(self.coordx[3], self.coordy[3])
        gl.glEnd()
