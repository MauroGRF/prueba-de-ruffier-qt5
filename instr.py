from PyQt5.QtCore import QTime

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = '¡Bienvenido al programa de detección del estado de salud!'
txt_next = 'Comenzar'
txt_instruction = ('Esta aplicación le permite utilizar el test de Rufier para realizar un diagnóstico inicial de su salud.\n'
                    'El test de Rufier es un conjunto de ejercicios físicos diseñados para evaluar su rendimiento cardíaco durante el esfuerzo físico.\n'
                    'El sujeto se acuesta en posición supina durante 5 minutos y se mide su pulso durante 15 segundos; \n'
                    'luego, en un lapso de 45 segundos, el sujeto realiza 30 sentadillas.\n'
                    'Cuando termina el ejercicio, el sujeto se acuesta y se mide su pulso nuevamente durante los primeros 15 segundos\n'
                    'y luego durante los últimos 15 segundos del primer minuto del período de recuperación.\n'
                    '¡Importante! Si se siente mal durante la prueba (mareos,\n'
                    'tinnitus, falta de aire, etc.), detenga la prueba y consulte a un médico.' )
txt_title = 'Salud'
txt_name = 'Ingrese su nombre completo:'
txt_hintname = "Nombre completo"
txt_hintage = "0"
txt_test1 = 'Acuéstese de espaldas y tómese el pulso durante 15 segundos. Haga clic en el botón "Iniciar primera prueba" para comenzar el temporizador.\nAnote el resultado en el campo correspondiente.'
txt_test2 = 'Realice 30 sentadillas en 45 segundos. Para hacer esto, haga clic en el botón "Comenzar a hacer sentadillas"\npara iniciar el contador de sentadillas.'
txt_test3 = 'Acuéstese de espaldas y tómese el pulso durante los primeros 15 segundos del minuto, luego durante los últimos 15 segundos del minuto.\nPresione el botón "Iniciar prueba final" para comenzar el temporizador.\nLos segundos que deben medirse se indican en verde y los que no deben medirse se indican en negro. Anote los resultados en los campos correspondientes.'
txt_sendresults = 'Enviar los resultados'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Iniciar la primera prueba'
txt_starttest2 = 'Comenzar a hacer sentadillas'
txt_starttest3 = 'Iniciar la prueba final'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Años cumplidos:'
txt_finalwin = 'Resultados'
txt_index = 'Índice de Rufier: '
txt_workheart = 'Rendimiento cardíaco: '
txt_res1 = "bajo. ¡Consulte a su médico de inmediato!"
txt_res2 = "satisfactorio. ¡Consulte a su médico!"
txt_res3 = "promedio. Podría valer la pena consultar a su médico para un chequeo."
txt_res4 = "por encima del promedio"
txt_res5 = "alto"