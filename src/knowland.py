import random
import time
def mate(nombre): #Esta funcion engloba el modo de juego de matemticas
    def entradas(choose): #Esta función valida si las entradas son numéricas
        while choose.isalnum():
            if choose.isnumeric():
                return choose
            else:
                print("Por favor, ingresa solo valores numéricos.")
                choose=input()
    def entradass(choose,R): #Esta función valida si las entradas son iguales a las disponibles, si no te da la opción de volver a ingresar.
        while not(choose in R):
            print("Error de dedo. Por favor, escoge una de las",len(R),"opciones")
            choose=input()
        return choose
    def mult(): #La función mult() hace el test de multiplicaciones.
        print("Test de multiplicaciones");
        print("Escribe el resultado de las multiplicaciones siguientes");
        repetir="1";
        correctas=0;
        incorrectas=0;
        while repetir=="1": #Este ciclo permite hacer tantas multiplicaciones como el usuario desee, a la par se le van sumando puntos a su puntuación.
            n1=random.randint(1,10);
            n2=random.randint(1,100);
            print(n1, "X", n2,"=");
            resultado=entradas(input());
            if int(resultado)==(n1*n2):
                print("Correcto");
                correctas+=5;
            else:
                print("Incorreto, respuesta es:", (n1*n2));
            print("¿Quieres continuar? Escribe 1");
            repetir=entradas(input());
        print ("Tu puntuación es de", correctas);
        return correctas
    def sumas(): #Este ciclo permite hacer tantas sumas como el usuario desee.
        print("Test de sumas");
        print("Escribe el resultado de las sumas siguientes");
        repetir="1";
        correctasS=0;
        incorrectasS=0;
        while repetir=="1":
            n1=random.randint(1,100);
            n2=random.randint(1,100);
            print(n1, "+", n2,"=");
            resultado=entradas(input());
            if int(resultado)==(n1+n2):
                print("Correcto");
                correctasS+=5;
            else:
                print("Incorreto, respuesta es:", (n1+n2));
            print("¿Quieres continuar? Escribe 1");
            repetir=entradas(input());
        print ("Tu puntuación es de", correctasS);
        return correctasS
    def restas(): #Este ciclo permite hacer tantas restas como el usuario desee.
        print("Test de restas");
        print("Escribe el resultado de las restas siguientes");
        repetir="1";
        correctasr=0;
        incorrectasr=0;
        while repetir=="1":
            n1=random.randint(1,100);
            n2=random.randint(1,100);
            print(n1, "-", n2,"=");
            resultado=entradas(input());
            if int(resultado)==(n1-n2):
                print("Correcto");
                correctasr+=5;
            else:
                print("Incorreto, respuesta es:", (n1-n2));
            print("¿Quieres continuar? Escribe 1");
            repetir=entradas(input());
        print ("Tu puntuación es de", correctasr);
        return correctasr
    def div(): #Este ciclo permite hacer tantas divisiones como el usuario desee.
        print("Test de Divisiones");
        print("Escribe el resultado de las siguientes divisiones en entero ");
        repetir="1";
        correctasd=0;
        incorrectasd=0;
        while repetir=="1":
            n1=random.randint(1,100);
            n2=random.randint(1,50);
            print(n1, "//", n2,"=");
            resultado=entradas(input());
            if int(resultado)==(n1//n2):
                print("Correcto");
                correctasd+=5;
            else:
                print("Incorreto, respuesta es:", (n1//n2));
            print("¿Quieres continuar? Escribe 1");
            repetir=entradas(input());
        print ("Tu puntuación es de", correctasd);
        return correctasd
    print("--------------------------------------------------------------MATH STAGE--------------------------------------------------------------------");
    print("¡Muy bien! Reforzaremos tus habilidades matemáticas.");
    print("Dime",nombre,"¿qué operación te gustaría practicar?");
    print("1.Multipicaciones")
    print("2.Sumas")
    print("3.Restas")
    print("4.División")
    OPCI=["1","2","3","4"]
    op=entradass(input(),OPCI)
    a=0
    if op=="1":
        a+=mult();
    elif op=="2":
        a+=sumas();
    elif op=="3":
        a+=restas();
    elif op=="4":
        a+=div();
    return a
def CIENCIAS(name): #Esta función engloba el modo de juego CIENCIAS.
    def print_time(x,t): #Esta función permite imprimir cada cierto intervalo.
        print(x)
        time.sleep(t)
    def print_matriz(A,C,E): #Esta función evalúa las respuestas de las preguntas y las coloca de forma aleatoria en la interfaz.
        z=[0,1,2,3]
        b=0
        for i in range(len(A[C])-1):
            a=random.choice(z)
            print(i+1,". ",A[C][E][a],"\n")
            if a==A[C][E][4]:
                b=i+1
            z.remove(a)
        return b
    def entradas(choose,R):#Esta función revisa si las entradas son válidas.
        while not(choose in R):
            print("Error de dedo. Por favor, escoge una de las ",len(R)," opciones")
            choose=input()
        return choose
    def repaso(A,C): #Esta función permite realizar repasos según el número de pregunta.
        print("REPASO".center(120, "="))
        print(A[C])
    #Esta matriz contiene las preguntas de cada nivel    
    preguntasfisica=[["¿Qué estudia la física?",
    "¿Qué es un vector en física?",
    "¿Qué es un escalar?",
    "¿Qué sistema de unidades se utiliza en México?" ,
    "¿Qué unidad se usa para medir la temperatura según el SI?"],
    ["¿Qué situación se presenta en un tiro parabólico?",
    "¿Cuál es la aceleración de un cuerpo a velocidad constante?",
    "¿Qué tipos de movimientos hay?",
    "¿Qué es el desplazamiento?",
    "¿Qué letras representan a los vectores unitarios de los ejes x,y,z?"],
    ["¿Cuántas son las Leyes de Newton?",
    "¿Qué dice la Primera Ley de Newton?",
    "¿Qué enuncia la Segunda Ley de Newton?",
    '¿Cuál de las Leyes de Newton establece que "a toda acción corresponde una reacción"?',
    "¿Cuántos cuerpos tienen que interactuar para que se cumplan las Leyes de Newton?"],
    ["¿Cómo es un movimiento de caída libre?",
    "¿Cómo se le llama a la altura en la caída libre en la que el cuerpo tiene una velocidad de 0?",
    "¿Qué significa caída libre?",
    "¿Cuál es la aceleración que afecta a un cuerpo en caída libre?",
    "¿Qué cae más rápido, una hoja de papel o un kilo de acero?"],
    ["¿Cuántas condiciones de equilibrio hay?",
    "¿Cuál es la condición de equilibrio para el equilibrio traslacional?",
    "¿Qué se necesita para que un cuerpo no gire?",
    "¿Cuál es la condición de equilibrio para el equilibrio rotacional?",
    "¿Qué leyes se relacionan con las condiciones de equilibrio?"],
    ["¿Quién estableció que a toda acción corresponde una reacción?",
    "¿Quién hizo la teoría de la relatividad?",
     "¿Quién descubrió el telescopio?",
    "¿Quién propuso las leyes orbitales?",
    "¿Quién es considerado el padre de la física cuántica?"]]
    #En esta matriz se almacenan las respuestas. EL NUMERO INDICA LA POSICION EN LA QUE ESTÁ LA RESPUESTA CORRECTA (0,3)
    respuestasfisica=[[["Propiedades de la energía y fenómenos naturales","Composición y propiedades de la materia","Seres vivos y sus procesos vitales","Superficie de la Tierra en su aspecto físico, actual y natural",0],
    ["Una cantidad que tiene magnitud, sentido y dirección","Fuerza que influye en el comportamiento de una persona","Constantes o complejos que sirven para describir un fenómeno físico con magnitud","Es cualquier agente que transporta y transmite un patógeno a otro organismo vivo",0],
    ["Una cantidad que tiene magnitud, pero no dirección","Un número cualquiera","Una escala de medición usada en la física","Una fuerza que se aplica en diferente sentido",0],
    ["Sistema Internacional de Unidades","Sistema Cegesimal de Unidades","Sistema Anglosajón de Unidades","Sistema Técnico de Unidades",0],
    ["Kelvin","Celcius","Fahrenheit","Rankine",0]],
    [["El vector velocidad en y es constante","El vector aceleración en x es constante","El vector aceleración tangencial es constante","No hay aceleración normal",0],
    ["No tiene aceleración","Mayor a la velocidad","Menor a la velocidad","Igual a la velocidad",0],
    ["MRU, MRUA y Movimiento Circular","Movimiento rápido","Movimiento angular y rotacional","Movimiento acelerado no constante",0],
    ["El desplazamiento es el cambio en las posiciones del movimiento de un cuerpo","La dirección en que se mueve un cuerpo","Un ángulo que crece respecto a un movimiento","Una distancia recorrida por una trayectoria",0],
    ["i,j,k","i,k,h","a,b,c","k,j,i",0]],
    [["3 leyes","7 leyes","2 leyes","8 leyes universales",0],
    ["La primera ley enuncia que un cuerpo permanece en reposo o a velocidad constante hasta que una fuerza externa intervenga su estado","Dice que la gravedad es proporcional a la masa de la Tierra","Indica que la suma de las fuerzas es igual a la aceleración","Establece que un cuerpo en movimiento no puede detenerse si no desacelera",0],
    ["Establece que la sumatoria de las fuerzas en un sistema es igual a la masa y la aceleración","Dice que a toda acción corresponde una reacción","Que la masa es proporcional a la torca de un objeto","Determina que un objeto en reposo no puede moverse sin una fuerza externa",0],
    ["Tercera Ley de Newton","Quinta Ley de Newton","Segunda Condición del Equilibrio","Segunda Ley de Newton",0],
    ["Mínimo 2 cuerpos","Solamente 1","Máximo 2 cuerpos","3 o más cuerpos",0]],
    [["Vertical","Horizontal","Parabólico","Diagonal",0],
    ["Altura máxima","Altura mínima","Punto de inflexión","Tangente",0],
    ["Que un objeto cae sin que ninguna fuerza externa lo intervenga","Que todos somos libres de caer","Que una caída siempre es libre","Que la velocidad es libre",0],
    ["La gravedad","La aceleración media","La aceleración instantánea","La fuerza de atracción del Sol",0],
    ["Un kilo de acero","Ambas caen al mismo tiempo","La hoja de papel","Es imposible decir",0]],
    [["2 Condiciones de Equilibrio","3 Condiciones de Equilibrio","4 Condiciones de Equilibrio","5 Condiciones de Equilibrio",0],
    ["La Primera Condición","La Segunda Condición","La Tercera Condición","Ninguna Condición",0],
    ["Que la suma de todas sus 'torcas' sean 0","Que las fuerzas sean muy grandes","Que esté en equilibrio","Que el cuerpo esté en reposo",0],
    ["La Segunda Condición","La Primera Condición","La Cuarta Condición","No hay",0],
    ["Leyes de Newton","Leyes de la Relatividad","Leyes de Migración","Leyes de la Gravitación Universal",0]],
    [["Sir Isaac Newton","Einstein","Hitler","Charles Darwin",0],
    ["Albert Einstein","Pasteur","Napoleón Bonaparte","Boyle",0],
    ["Galileo Galilei","Moctezuma","Cristóbal Colón","Hernán Cortés",0],
    ["Johannes Kepler","Darwin","Newton","James Kepler",0],
    ["Max Planck","Rutherford","Max Habsburgo","Marie Curie",0]]]
    #En esta matriz contiene los temas de cada nivel.
    temasfisica=["Conceptos básicos",
    "Cinemática",
    "Leyes de Newton",
    "Caída libre",
    "Condiciones de Equilibrio",
    "Personajes de la Física"]
    #Esta matriz contiene los repasos de cada tema.
    repasofisica=["""Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.fisicalab.com/tema/intro-magnitudes#contenidos""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.fisicalab.com/tema/movimiento-fisica#contenidos""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.fisicalab.com/tema/intro-leyes-newton#contenidos""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.fisicalab.com/apartado/caida-libre#contenidos""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://fisica.laguia2000.com/general/condiciones-de-equilibrio""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://ncncgrc.wordpress.com/fisica/fisica-primer-periodo/personajes-importantes-de-la-fisica/"""] 
    #Estas matrices contiene lo mismo que las anteriores, pero de otros temas.
    preguntasquimica=[["¿Qué estudia la Química?",
    "¿Qué es la materia?",
    "¿Cómo se clasifican las sustancias?",
    "¿Cómo se clasifican las mezclas?",
    "¿Cuál es la herramienta que clasifica a los elementos de acuerdo a sus características?"],
    ["¿A que nos referimos con H?",
    "¿Cuál de los siguientes no s un grupo de la tabla periódica?",
    "¿Cuántos periodos tiene la tabla periódica?",
    "¿Cuántos grupos tiene la tabla periódica?",
    "¿Cuál de los siguientes no es un grupo de la tabla periódica?"],
    ["¿Quién estableció el modelo atómico conocido como 'budín de pasas'?",
    "¿Quién describió el átomo por primera vez en la historia?",
    "¿Cuál es el modelo atómico usado en la actualidad?",
    "¿Quién describió el primer modelo con un núcleo atómico y capas externas de electrones?",
    "¿Quién describió el primer modelo atómico con bases científicas?"],
    ["¿Cuál es el enlace que es de tipo metal-no metal?",
    "¿Cuál es el enlace de tipo metal-metal?",
    "¿Cuál es el enlace de tipo no metal-no metal?",
    "¿Cuál de estos NO es un enlace intermolecular?",
    "¿Cuál de estas fuerzas intermoleculares es más fuerte?"],
    ["¿Cuántos estado de la materia hay?",
    "A la transformación de líquido a sólido se le llama:",
    "A la transformación de sólido a líquido se le llama:",
    "A la transformación de líquido a gaseoso se le llama:",
    "A la transformación de gaseoso a líquido se le llama:"],
    ["¿Cuál es una propiedad general de la materia?",
    "¿Cuál es NO una propiedad intensiva de la materia?",
    "¿Cuál es una propiedad específica física de la materia?",
    "¿Cuál de las siguientes propiedades depende de la masa y volumen?",
    "¿Cuál de las siguientes es una propiedad extensiva de la materia?"]]
    respuestasquimica=[[["Estudia a la materia y sus transformaciones","La vida y las ciencias naturales","Los diferentes tipos de números","La historia de los elementos",0],["Corresponde a toda la materia presente en el Universo","Un curso del colegio","Toda la masa","Algo que se puede tocar",0],["Puras y mezclas","Homogéneas y heterogéneas","Sólidas y líquidas","Cristalinas, gaseosas y puras ",0],["Homogéneas y heterogéneas","Puras y mezclas","Calientes y frías","Metálicas y ácidas",0],["La Tabla Periódica","Número de Avogadro","La Química","El método AUFBAU",0]],
    [["Hidrógeno","Helio","Hassio","Uranio",0],["Alcalinos","Gases noble","Gases fuertes","Otros no metales",0],["7","8","9","10",0],["18","23","17","10",0],["Ácidos","No metales","Metaloides","Hálogenos",0]],
    [["Thomson","Bohr","Rutherford","Einstein",0],["Demócrito","Dalton","Heisenberg","Tesla",0],["Modelo Cuántico","Modelo del átomo invisible","Modelo del budín de pasas","Modelo planetario",0],["Rutherford","Dalton","Lewis","Schrödiger",0],["Dalton","Rutherford","Thomson","Demócrito",0]],
    [["Iónico","Metálico","Covalente","Covalente Polar",0],["Metálico","Dipolo-dipolo","Covalente","Iónico",0],["Covalente","De London","Metálico","Puentes de Hidrógeno",0],["Covalente no polar","De London","Iónico","Metálico",0],["Ión-ión","Covalente","Metálico","Dipolo",0]],
    [["3","4","2","6",0],["Solidificación","Vaporización","Condensación","Sublimación",0],["Fusión","Vaporización","Solidificación","Sublimación",0],["Vaporización","Solidificación","Condensación","Fusión",0],["Condensación","Fusión","Vaporización","Sublimación",0]],
    [["Masa","Densidad","Flexibilidad","Solubilidad",0],["Volumen","Dureza","Color","Olor",0],["Punto de congelación","Acidez","Combustibilidad","Reactividad",0],["Volumen","Punto de ebullición","Peso","Porosidad",0],["Peso","Conductividad","Maleabilidad","Densidad",0]]]
    temasquimica=["Conceptos básicos",
    "Tabla periódica",
    "Modelos atómicos",
    "Estados de la materia",
    "Propiedades de la materia",
    "Enlaces químicos"]
    repasoquimica=["""Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://es-puraquimica.weebly.com/conceptos-basicos.html""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.ptable.com/?lang=es""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.todamateria.com/modelos-atomicos/""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: http://concurso.cnice.mec.es/cnice2005/93_iniciacion_interactiva_materia/curso/materiales/estados/cambios.htm""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://www.todamateria.com/propiedades-de-la-materia/""",
    """Para conocer la respuesta correcta y aprender más acerca del tema, visita el siguiente sitio: https://es.khanacademy.org/science/biology/chemistry--of-life/chemical-bonds-and-reactions/a/chemical-bonds-article"""]
    score=0
    print_time("--------------------------------------------------------------SCIENCE GAME--------------------------------------------------------------------",1)
    print_time("¡Excelente elección, la ciencia nos permite conocer cómo funcionan las cosas y para entender los fenómenos del universo!",3)
    print("Dime, ",name, " ¿qué rama de la ciencia prefieres conocer?")
    print_time("¿Te gustaría conocer más de la Física o de la Química?",5)
    print_time("Escribe 1 para Física.",1)
    print_time("Escribe 2 para Química.",1)
    eleccion1=input()
    lista=["1","2"]
    eleccion1=entradas(eleccion1,lista)
    while eleccion1!="0":
        if eleccion1=="1": #Aquí se abre la primera sección de preguntas
            print_time("¿Así que quieres conocer las leyes que rigen a la naturaleza y al universo? Muy bien.",2)
            print_time("""Tendrás la oportunidad de contestar 6 preguntas,la pregunta no. 6 te da puntos extra. 
Y si te quedas con la duda, puedes revisar los temas antes de continuar.
¡Mucho éxito!""",7)
            for i in range(6): #Mientras que aquí se repite el ciclo por 11 veces, ya que son 11 preguntas por sección.
                p=i
                print("--------------------------------------------------------------PORTAL ",i+1,"--------------------------------------------------------------------")
                print(str(temasfisica[i]).center(120, "/"))
                Z=random.randint(0,4)
                print_time((preguntasfisica[i][Z]),3)
                M=print_matriz(respuestasfisica,p,Z)
                print_time("Ingresa el número de la respuesta",3)
                respuesta=input()
                k=["1","2","3","4"]
                respuesta=entradas(respuesta,k)
                if respuesta==str(M):#Si la respuesta es correcta, se suman 5 puntos a la puntuación.
                    print_time("¡Felicidades, respuesta correcta!",1)
                    score+=5
                    print("La puntuación actual de ",name," es de: ",score," puntos")
                    continue
                else: #Si no el usuario tiene la opción de continuar o repasar el tema.
                    print_time("Lo siento. Respuesta incorrecta",1)
                    print_time("¿Deseas continuar o prefieres repasar el tema?",1)
                    print_time("Escribe 0 para repasar el tema",1)
                    print_time("Escribe 1 para continuar",1)
                    lista=["0","1"]
                    decision=input()
                    decision=entradas(decision,lista)
                    if decision=="1":
                        continue
                    else: #Aquí se le da la opción al usuario de realizar la siguiente pregunta o salir del juego.
                        repaso(repasofisica,p)
                        lista=["1","5"]
                        print_time("Para continuar. Escribe 1", 1)
                        print_time("Para salir del juego. Escribe 5", 1)
                        decision=input()
                        decision=entradas(decision,lista)
                        if decision=="1":
                            continue
                        if decision=="5":
                            print("Tu puntuación es de ", score, " puntos")
                            exit()
            print_time("¡Excelente, has completado la dimensión de  la Física!",1)
            print("Tu puntación es de ",score,".")
            print_time("Si deseas conocer la dimensión de la Química. Escribe M",1)
            print_time("Si quieres salir de SCIENCE GAME. Escribe E",1)
            cad=["M","E"]
            cambio=input()#Si el usuario quiere cambiar de sección puede elegir o cambiar de Historia a Matemáticas.
            cambio=entradas(cambio,cad)
            if cambio=="M":
                eleccion1="2"
                continue
            if cambio=="E":
                eleccion1="0"
                continue
        elif eleccion1=="2": #Esta sección es idéntica a la anterior en estructura, solo que con distinto contenido.
            print_time("¿Eres de los que les gusta conocer la composición de las moléculas y las reacciones químicas? Excelente.",2)
            print_time(""" Tendrás la oportunidad de contestar 6 preguntas, la pregunta no. 6 te da puntos extra. 
Y si te quedas con la duda, puedes revisar los temas antes de continuar. 
¡Mucho éxito!""",7)
            for p in range(6):
                print("--------------------------------------------------------------PORTAL ",i+1,"--------------------------------------------------------------------")
                print(str(temasquimica[p]).center(120, "/"))
                Y=random.randint(0,4)
                print_time((preguntasquimica[p][Y]),5)
                MA=print_matriz(respuestasquimica,p,Y)
                print_time("Ingresa el número de la respuesta.",3)
                respuesta=input()
                ka=["1","2","3","4"]
                respuesta=entradas(respuesta,ka)
                if respuesta==str(MA):
                    print_time("¡Felicidades, respuesta correcta!",1)
                    score+=5
                    print("La puntuación actual de ",name," es de: ",score," puntos.")
                    continue
                else:
                    print_time("Lo siento. Respuesta incorrecta.",1)
                    print_time("¿Deseas continuar o prefieres repasar el tema?",1)
                    print_time("Escribe 0 para repasar el tema.",1)
                    print_time("Escribe 1 para continuar.",1)
                    lista=["0","1"]
                    decision=input()
                    decision=entradas(decision,lista)
                    if decision=="1":
                        continue
                    else:
                        repaso(repasoquimica,p)
                        lista=["1","5"]
                        print_time("Para continuar. Escribe 1.", 1)
                        print_time("Para salir del programa. Escribe 5.", 1)
                        decision=input()
                        decision=entradas(decision,lista)
                        if decision=="1":
                            continue
                        if decision=="5":
                            print("Tu puntuación es de ", score, " puntos.")
                            exit()
            print_time("¡Excelente, has completado la dimensión de la Química!",1)
            print("Tu puntación es de ",score,".")
            print_time("Si deseas conocer la dimensión de la Física. Escribe M.",1)
            print_time("Si quieres salir de SCIENCE GAME. Escribe E.",1)
            cad=["M","E"]
            cambio=input()
            cambio=entradas(cambio,cad)
            if cambio=="M":
                eleccion1="1"
                continue
            if cambio=="E":
                eleccion1="0"
                continue
        elif eleccion1=="0":
            print_time("Guardando puntajes. Saliendo SCIENCE GAME...",2)
            break
    return score
def gamemode(name,sco): #FUNCIÓN QUE ESCOGE EL MODO DE JUEGO
    def entradas(choose,R): #ESTA FUNCIÓN VALIDA LAS ENTRADAS, SI NO SON LAS ESPERADAS, EL CICLO SE REPITE.
        while not(choose in R): 
            print("Error de dedo. Por favor, escoge una de las",len(R),"opciones.")
            choose=input()
        return choose
    g=input()
    op=["5","10", "0","T"]
    g=entradas(g,op)
    turn=0
    if g=="5": #Si el usuario escribe 5 se llama a la función de CIENCIAS
        sco+=CIENCIAS(name)
        turn+=1
    elif g=="10":
        sco+=mate(name) #Si el usuario escribe 10 se llama a la función de matemáticas
        turn+=1
    elif g=="0": #Con esta función el usuario sale del juego
        print(("FIN DEL JUEGO").center(150,"¬"))
        time.sleep(2)
        exit()
    elif g=="T":
        print("TABLERO DE PUNTUACIONES")
        T=open("tablero.txt","r")
        tab=T.read()
        print(tab)
        exit()
    if turn>0: #Cuando el usuario haya regresado al menú principal después de una partida, puede cambiar de modo de juego
        print("¿Deseas cambiar el modo de juego?")
        print("Si eliges Ciencias, escribe 5.")
        print("Si escoges Matemáticas, escribe 10.")
        print("Si deseas salir del juego escribe 0.")
        g=input()
        g=entradas(g,op)
        if g=="5":
            sco+=CIENCIAS(name)
            turn+=1
        elif g=="10":
            sco+=mate(name)
            turn+=1
        elif g=="0": 
            print("Tu puntuación final es de", sco,".")
            print(("FIN DEL JUEGO").center(150,"¬"))
            time.sleep(2)
            f=open ("tablero.txt","w")
            f.write("\n"+ name+" " +str(sco))
            f.close()
            exit()
#CUERPO PRINCIPAL DEL PROGRAMA
print(("KNOWLAND").center(150,"¬")) 
print("¡Bienvenido, valiente! ¿Cuál es tu nombre?") #Solicita nombre del usuario
nombre=input()
print("¿Deseas aprender un poco de ciencias o practicar tus habilidades matemáticas?")
print("Tus aciertos se irán acumulando conforme vayas avanzando, no hay penalización por respuesta incorrecta.")
time.sleep(3)
print("Si eliges Ciencias, escribe 5") #El usuario escoge el modo de juego
print("Si escoges Matemáticas, escribe 10")
print("Si deseas salir del juego escribe 0")
print("Si deseas consultar puntuaciones, escribe T")
puntuacion=0 
gamemode(nombre,puntuacion) #Llamada de función del modo de juego