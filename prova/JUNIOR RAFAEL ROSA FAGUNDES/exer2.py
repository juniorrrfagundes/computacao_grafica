from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x, y, drawSize, xlon, ylon, xpixel, wo, ho, ypixel

def inicia():
    global x, y, drawSize, xlon, ylon, xpixel, wo, ho, ypixel
    x = 150.0
    y = 100.0
    drawSize = 700
    xlon = 150.0
    ylon = 100.0
    xpixel = 5.0
    ypixel = 5.0
def flag():
    global x, y, drawSize, xlon, ylon
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
    glVertex2f(xlon+250,ylon+drawSize/2)
    glVertex2f(xlon+drawSize/2, ylon+drawSize/2+100)
    glVertex2f(xlon+drawSize/2+100,ylon+drawSize/2)
    glVertex2f(xlon+drawSize/2, ylon+drawSize/2-100)
    glEnd()
        
    glutSwapBuffers()

def tamanhoTela(w, h):
    global x, y, drawSize, xlon, ylon, xpixel, wo, ho
    wo = w
    ho = h
    glViewport(0, 0, wo, ho)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0, wo, 0, ho)

def Timer(value):
    global x, y, drawSize, xlon, ylon, xpixel, ypixel
    # if(xlon + x+200>= wo or xlon <=0 or xlon + x+500>=wo)
    if(xlon+250 <= x+200 or xlon+drawSize/2+100 >= x+500):
        xpixel = -xpixel
    if(ylon+drawSize/2+100 >= y+drawSize or ylon+drawSize/2-100 <= y):
        ypixel = -ypixel
    ylon += ypixel
    xlon += xpixel
    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000,900)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'PROVA')
    glutDisplayFunc(flag)
    glutReshapeFunc(tamanhoTela)
    glutTimerFunc(33, Timer, 1)
    inicia()
    glutMainLoop()
