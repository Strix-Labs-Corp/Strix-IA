from ultralytics import YOLO
import cv2

# Carregar o modelo treinado
model = YOLO("best.pt")  # Ou outro caminho para seu modelo

# Abrir a webcam (0 é a webcam padrão)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz predição no frame atual
    results = model(frame)

    # Plotar os resultados diretamente
    annotated_frame = results[0].plot()

    # Mostrar o resultado
    cv2.imshow("Detecção ao vivo", annotated_frame)

    # Sair com a tecla ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
