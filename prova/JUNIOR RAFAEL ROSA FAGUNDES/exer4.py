from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x, y, drawSize, firstColor

def inicia():
    global x, y, drawSize,firstColor
    x = 150.0
    y = 100.0
    drawSize = 700
    firstColor = [1.0,1.0,1.0]

def flag():
    global x, y, drawSize, firstColor
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x, y+drawSize)
    glVertex2f(x+drawSize,y+drawSize)
    glVertex2f(x+drawSize, y)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x+200,y)
    glVertex2f(x+200, y+drawSize)
    glVertex2f(x+500,y+drawSize)
    glVertex2f(x+500, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(firstColor[0],firstColor[1], firstColor[2])
    glVertex2f(x+250,y+drawSize/2)
    glVertex2f(x+drawSize/2, y+drawSize/2+100)
    glVertex2f(x+drawSize/2+100,y+drawSize/2)
    glVertex2f(x+drawSize/2, y+drawSize/2-100)
    glEnd()
        
    glFlush()

def tamanhoTela(w, h):
    wo = w
    ho = h
    glViewport(0, 0, wo, ho)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0, wo, 0, ho)

def MenuPrincipal(op):
    return 0

def makeMenu():
    submenu1 = glutCreateMenu(colorMenu1)
    glutAddMenuEntry("ROSA", 0)
    menu = glutCreateMenu(MenuPrincipal)
    glutAddSubMenu("Polygono", submenu1)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    return 0

def colorMenu1(op):
    global firstColor
    if(op == 0):
        firstColor = [1.0, 0.0, 1.0]
    glutPostRedisplay()
    return 0

def KeepMouse(button, state, a, b):
    global x, y, drawSize, wo, ho
    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_UP):
            makeMenu()
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,900)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'PROVA')
    glutDisplayFunc(flag)
    glutReshapeFunc(tamanhoTela)
    inicia()
    glutMouseFunc(KeepMouse)
    glutMainLoop()
