from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Definindo variáveis globais
global windowWidth, windowHeigth, fisrtColor, secondColor, indexfisrt, indexsecond, drawSize, xInitial, yInitial, viewX, viewY
# Posição inicial do quadrado e tamanho de largura definida por drawSize
xInitial = 5.0
yInitial = 5.0
drawSize = 25

# Definindo vetor de cores para cada triangulo grande
fisrtColor = [1.0,1.0,0.0]
secondColor = [0.0,0.5,0.0]
indexfisrt = 0
indexsecond = 0

#Definindo tamanho da janela
windowWidth = 1000
windowHeigth = 1000


def flag():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    first_triangulo()
    second_triangulo()
    red_star()
    glFlush()

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

# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global viewX, viewY
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    viewX = w
    viewY = h

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0, 100, 0, 100)

def KeepKeyboard(key, x, y):
    global fisrtColor, secondColor, indexfisrt, indexsecond
    if (key == b'R' or key == b'r'):
        if (indexfisrt <= 2):
            if(fisrtColor[indexfisrt] == 1.0):
                fisrtColor[indexfisrt] = 0
                indexfisrt += 1
            else:
                fisrtColor[indexfisrt] = fisrtColor[indexfisrt] + 0.5
                indexfisrt += 1
        else:
            indexfisrt = 0

    if(key==b'G' or key==b'g'):
        if (indexsecond <= 2):
            if (secondColor[indexsecond] == 1.0):
                secondColor[indexsecond] = 0
                indexsecond += 1
            else:
                secondColor[indexsecond] = secondColor[indexsecond] + 0.5
        else:
            indexsecond = 0
    glutPostRedisplay()

def KeepMouse(button, state, x, y):
    global xInitial, yInitial, viewX, viewY
    if (button == GLUT_LEFT_BUTTON):
        if(state == GLUT_UP):
            escalax = 100.0/(viewX)
            xInitial = x * escalax
            escalay = 100.0/(viewY)
            yInitial = 100 - (y * escalay)

    glutPostRedisplay()

def EspecialKeyboard(key, x, y):
    global xInitial, yInitial, viewX, viewY
    if(key == GLUT_KEY_UP):
        yInitial = yInitial +10
    if(key == GLUT_KEY_DOWN):
        yInitial = yInitial -10
    if(key == GLUT_KEY_LEFT):
        xInitial = xInitial -10
    if(key == GLUT_KEY_RIGHT):
        xInitial = xInitial +10
    glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(windowWidth,windowHeigth)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'Bandeira Acre')
    glutDisplayFunc(flag)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutKeyboardFunc(KeepKeyboard)
    glutMouseFunc(KeepMouse)
    glutSpecialFunc(EspecialKeyboard)
    glutMainLoop()
