from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def flag():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    first_triangulo()
    second_triangulo()
    # red_star()
    polygon()
    glFlush()

def first_triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,1.0,0.0)
    glVertex2i(0,0)
    glVertex2i(0,100)
    glVertex2i(100,0)
    glEnd()

def second_triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.5,0.0)
    glVertex2i(100,0)
    glVertex2i(0,100)
    glVertex2i(100,100)
    glEnd()

def red_star():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.0,0.0)
    glVertex2i(5,10)
    glVertex2i(15,10)
    glVertex2i(10,15)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.0,0.0)
    glVertex2i(10,5)
    glVertex2i(6,20)
    glVertex2i(12,13)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.0,0.0)
    glVertex2i(10,5)
    glVertex2i(13,20)
    glVertex2i(8,13)
    glEnd()

def polygon():
    glBegin(GL_POLYGON)
    glColor3f(0.9, 0.0, 0.0)
    glVertex2i(10, 5)
    glVertex2f(7.5, 20)
    glVertex2f(10,15)
    glVertex2f(12.5,20)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.0,0.0)
    glVertex2i(6,10)
    glVertex2i(14,10)
    glVertex2i(10,15)
    glEnd()

# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    #Evita a divisao por zero
    if(h == 0): h = 1
    #Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    #Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    print(w, h, "\n")
    #Estabelece a janela de seleção (left, right, bottom, top)
    gluOrtho2D (0.0, 100.0, 100.0, 0.0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1280,1024)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'Bandeira Acre')
    glutDisplayFunc(flag)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutMainLoop()
