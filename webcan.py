import cv2 as cv

#Carregar o pré treinoda face(opencv)
trained_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#inicia captura pela webcan default
webcam = cv.VideoCapture(0)

#capturar os frames
while True:
    #ler o frame atual
    isTrue, frame = webcam.read()
    
    #converter para graycale(tons de cinza)
    grayscale_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Detectar a face
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    #desenghar o retângulo em torna da face detectada
    for (x, y, w, h) in face_coordinates:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 10)

    #exibir a imagem capturada
    cv.imshow('Face Detector', frame)
    key = cv.waitKey(1)

    #aguardar o pressionamento da tecla 'Q' para sair do programa
    # if (key==81 or key==113): #qQ
    #     break
    if cv.waitKey(1) & (key==81 or key==113):
        break


#liberar a webcam
webcam.release()
cv.destroyAllWindows()




    
