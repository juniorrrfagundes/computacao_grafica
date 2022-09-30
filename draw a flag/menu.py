from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global fisrtColor, secondColor, flagSize, latlong, viewx, viewy, drawSize, xInitial, yInitial



def flag():
    global latlong
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    first_triangulo()
    second_triangulo()
    red_star()
    WriteLatLong(latlong)
    glutSwapBuffers()

def first_triangulo():
    global xInitial, yInitial, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(fisrtColor[0], fisrtColor[1], fisrtColor[2])
    glVertex2f(xInitial,yInitial)
    glVertex2f(xInitial,yInitial+drawSize)
    glVertex2f(xInitial+drawSize,yInitial)
    glEnd()

def second_triangulo():
    global xInitial, yInitial, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(secondColor[0], secondColor[1], secondColor[2])
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


def Iniciar():
    global fisrtColor, secondColor, latlong, flagSize, drawSize, xInitial, yInitial
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo da janela de visualização como preta

    xInitial = 5.0
    yInitial = 5.0
    drawSize = 50

    fisrtColor = [1.0, 1.0, 0.0]
    secondColor = [0.0, 0.5, 0.0]

    flagSize = 150
    latlong = '(0,0)'


# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global viewx, viewy
    #Evita a divisao por zero
    if(h == 0): h = 1
    #Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    viewx = w
    viewy = h
    #Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    print(w, h, "\n")
    #Estabelece a janela de seleção (left, right, bottom, top)
    gluOrtho2D (-flagSize, flagSize, flagSize, -flagSize)

def MenuPrincipal(op):
    return 0

def MakeMenu():
    submenu1 = glutCreateMenu(colorMenu1)
    glutAddMenuEntry("Vermelho", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    submenu2 = glutCreateMenu(colorMenu2)
    glutAddMenuEntry("Vermelho", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    submenu3 = glutCreateMenu(ChangeSize)
    glutAddMenuEntry("Diminuir", 0)
    glutAddMenuEntry("Aumentar", 1)

    menu = glutCreateMenu(MenuPrincipal)
    glutAddSubMenu("Triangulo Superior",submenu1)
    glutAddSubMenu("Triangulo Inferior", submenu2)
    glutAddSubMenu("Alterar Tamanho", submenu3)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    return 0;

def colorMenu1(op):
    global fisrtColor, secondColor
    if (op == 0):
        fisrtColor = [1.0, 0.0, 0.0]
    elif (op == 1):
        fisrtColor = [0.0, 1.0, 0.0]
    elif(op == 2):
        fisrtColor = [0.0, 0.0, 1.0]
    glutPostRedisplay();
    return 0

def colorMenu2(op):
    global fisrtColor, secondColor
    if (op == 0):
        secondColor = [1.0, 0.0, 0.0]
    elif (op == 1):
        secondColor = [0.0, 1.0, 0.0]
    elif(op == 2):
        secondColor = [0.0, 0.0, 1.0]
    glutPostRedisplay();
    return 0

def ChangeSize(op):
    global flagSize
    if (op == 0):
        flagSize = flagSize + 10
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-flagSize, flagSize, flagSize, -flagSize)
    elif(op == 1):
        flagSize = flagSize - 10
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-flagSize, flagSize, flagSize, -flagSize)
    glutPostRedisplay()
    return 0

def KeepMouse(button, state, x, y):
    if (button == GLUT_RIGHT_BUTTON):
        if(state == GLUT_DOWN):
            MakeMenu()
    glutPostRedisplay()

def WriteLatLong(string):
    global viewx, viewy
    glPushMatrix()
    glRasterPos2f(0, 0)
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glPopMatrix()

def MoveMouse(x, y):
    global latlong
    latlong = "("+str(x)+","+str(y)+")"
    glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400,350)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'Bandeira Acre')
    glutDisplayFunc(flag)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutPassiveMotionFunc(MoveMouse)
    glutMouseFunc(KeepMouse)
    Iniciar()
    glutMainLoop()
