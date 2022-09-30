from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global wo,ho, windowWidth, windowHeight, xInitial, yInitial, drawSize, xPixel, yPixel, fisrtColor, secondColor, indexfisrt, indexsecond, xSecond, ySecond

xInitial = 100
yInitial = 100
drawSize = 80

# Definindo o numero de pixeis para se mover
xPixel = 1.0
yPixel = 1.0

# Definindo vetor de cores para cada triangulo grande
xSecond = 5
ySecond = 5
fisrtColor = [1.0,1.0,0.0]
secondColor = [0.0,0.5,0.0]
indexfisrt = 0
indexsecond = 0

#Definindo o tamanho da janela
windowWidth = 400
windowHeigth = 350

def flag():
    global wo, ho, windowWidth, windowHeight
    #Definindo as medidas da janela
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0,0,int(wo/2), ho) # Aqui devidimos a tela ao meio
    #Iniciando o sistema de coordenadas
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #Entendi nada do porque isso aqui embaixo.
    if (wo <= ho):
        windowHeight = 250.0*ho/wo
        windowWidth = 250
    else:
        windowWidth = 250.0*wo/ho
        windowHeight = 250.0
    gluOrtho2D(0.0, windowWidth, windowHeight, 0.0)
    #Desenhando na primeira view
    first_triangulo()
    second_triangulo()
    red_star()

    # Definindo a segunda view
    glViewport(int(wo/2), 0, int(wo/2), ho)
    #Iniciando o sistema de coordenadas
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D (0, windowWidth, 0, windowHeight)
    secondview_first_triangulo()
    secondview_second_triangulo()

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

def secondview_first_triangulo():
    global xSecond, ySecond, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(fisrtColor[0], fisrtColor[1], fisrtColor[2])
    glVertex2f(xSecond,ySecond)
    glVertex2f(xSecond,ySecond+drawSize)
    glVertex2f(xSecond+drawSize,ySecond)
    glEnd()

def secondview_second_triangulo():
    global xSecond, ySecond, drawSize
    glBegin(GL_TRIANGLES)
    glColor3f(secondColor[0], secondColor[1], secondColor[2])
    glVertex2f(xSecond+drawSize,ySecond)
    glVertex2f(xSecond,ySecond+drawSize)
    glVertex2f(xSecond+drawSize,ySecond+drawSize)
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
    global wo,ho
    if(h == 0): h = 1
    wo=w;
    ho=h;

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
    global xSecond, ySecond, wo, ho
    if (button == GLUT_LEFT_BUTTON):
        if(state == GLUT_UP):
            escalax = 100.0/(wo)
            xSecond = x * escalax
            escalay = 100.0/(ho)
            ySecond = 100 - (y * escalay)

    glutPostRedisplay()

def EspecialKeyboard(key, x, y):
    global xSecond, ySecond, viewX, viewY
    if(key == GLUT_KEY_UP):
        ySecond = ySecond +10
    if(key == GLUT_KEY_DOWN):
        ySecond = ySecond -10
    if(key == GLUT_KEY_LEFT):
        xSecond = xSecond -10
    if(key == GLUT_KEY_RIGHT):
        xSecond = xSecond +10
    glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(windowWidth,windowHeigth)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b'Bandeira Acre')
    glutDisplayFunc(flag)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(33, Timer, 1)
    glutKeyboardFunc(KeepKeyboard)
    glutMouseFunc(KeepMouse)
    glutSpecialFunc(EspecialKeyboard)
    glutMainLoop()
