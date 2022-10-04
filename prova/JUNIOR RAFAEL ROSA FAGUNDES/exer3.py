from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x, y, drawSize, wo, ho

def inicia():
    global x, y, drawSize
    x = 150.0
    y = 100.0
    drawSize = 700

def flag():
    global x, y, drawSize
    glClear(GL_COLOR_BUFFER_BIT)
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
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x+250,y+drawSize/2)
    glVertex2f(x+drawSize/2, y+drawSize/2+100)
    glVertex2f(x+drawSize/2+100,y+drawSize/2)
    glVertex2f(x+drawSize/2, y+drawSize/2-100)
    glEnd()
        
    glFlush()

def tamanhoTela(w, h):
    global wo, ho
    wo = w
    ho = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0, wo, ho, 0)

def keepKeyboard(key, a, b):
    global x, y, drawSize
    if(key==b'L' or key==b'l'):
        x = x - 10
        if (x < 0):
            x = 0
    if(key==b'R' or key==b'r'):
        x = x + 10
        if(x+drawSize > wo):
            x = wo - drawSize
    if(key==b'B' or key==b'b'):
        y = y + 10
        if(y+drawSize > ho):
            y = ho - drawSize
    if(key==b'T' or key==b't'):
        y = y - 10
        if(y < 0):
            y = 0
    glutPostRedisplay()

def KeepMouse(button, state, a, b):
    global x, y, drawSize, wo, ho
    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_UP):
            x = a
            y = b
    glutPostRedisplay()

    glutPostRedisplay()
if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,900)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'PROVA')
    glutDisplayFunc(flag)
    glutReshapeFunc(tamanhoTela)
    glutKeyboardFunc(keepKeyboard)
    glutMouseFunc(KeepMouse)
    inicia()
    glutMainLoop()
