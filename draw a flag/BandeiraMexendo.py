from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Definindo variáveis globais.
global xInitial, yInitial, drawSize, xPixel, yPixel, windowWidth, windowHeigth
# Posição inicial do quadrado e tamanho de largura definida por drawSize
xInitial = 100
yInitial = 100
drawSize = 150

# Definindo o numero de pixeis para se mover
xPixel = 5.0
yPixel = 5.0

#Definindo o tamanho da janela
windowWidth = 400
windowHeigth = 350

def Timer(value):
    global xInitial, yInitial, drawSize, windowWidth, windowHeigth, xPixel, yPixel

    if (xInitial + drawSize >= windowWidth or xInitial <= 0):
        xPixel = -xPixel
    if (yInitial + drawSize >= windowHeigth or yInitial <= 0):
        yPixel = -yPixel

    xInitial += xPixel
    yInitial += yPixel

    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)

def flag():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    first_triangulo()
    second_triangulo()
    red_star()
    glutSwapBuffers()

def first_triangulo():
    global xInitial, yInitial, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(xInitial,yInitial)
    glVertex2f(xInitial,yInitial+drawSize)
    glVertex2f(xInitial+drawSize,yInitial)
    glEnd()

def second_triangulo():
    global xInitial, yInitial, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(xInitial+drawSize,yInitial)
    glVertex2f(xInitial,yInitial+drawSize)
    glVertex2f(xInitial+drawSize,yInitial+drawSize)
    glEnd()

def red_star():
    global xInitial, yInitial, drawSize
    glBegin(GL_POLYGON)
    glColor3f(0.9, 0.0, 0.0)
    glVertex2f(xInitial+drawSize/10, yInitial+drawSize/10)
    glVertex2f(xInitial+drawSize/12, yInitial+drawSize/4)
    glVertex2f(xInitial+drawSize/9.9, yInitial+drawSize/5)
    glVertex2f(xInitial+drawSize/8.1, yInitial+drawSize/4)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.9,0.0,0.0)
    glVertex2f(xInitial+drawSize/13, yInitial+drawSize/7)
    glVertex2f(xInitial+drawSize/10, yInitial+drawSize/5)
    glVertex2f(xInitial+drawSize/8, yInitial+drawSize/7)
    glEnd()

# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global windowWidth, windowHeigth
    #Evita a divisao por zero
    if(h == 0): h = 1
    #Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    #Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    print(w, h, "\n")
    #Estabelece a janela de seleção (left, right, bottom, top)
    gluOrtho2D (0.0, windowWidth, windowHeigth, 0.0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(windowWidth,windowHeigth)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'Bandeira Acre')
    glutDisplayFunc(flag)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(33, Timer, 1)
    glutMainLoop()
