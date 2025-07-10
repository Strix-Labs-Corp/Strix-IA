from ultralytics import YOLO
import cv2

def start_camera_detection(model_path: str = "./AI/models/best.pt", camera_index: int = 0):
    """
    Inicia a detecção ao vivo de pássaros usando o modelo YOLO.

    Args:
        model_path (str): Caminho para o arquivo .pt do modelo treinado.
        camera_index (int): Índice da câmera a ser usada (default = 0).
    """
    # Carregar modelo
    model = YOLO(model_path)

    # Inicializar câmera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise RuntimeError(f"Não foi possível acessar a câmera {camera_index}")

    print("Pressione ESC para sair da detecção ao vivo...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Predição
        results = model(frame)
        annotated_frame = results[0].plot()

        # Exibir
        cv2.imshow("Detecção ao vivo", annotated_frame)

        # Sair no ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
