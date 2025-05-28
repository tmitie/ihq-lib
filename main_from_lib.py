import sys
import os

import cv2

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from process_img.process_img_interface import process_image_with_boundaries

if __name__ == "__main__":
    image_path = "/Users/thaynaramitie/Documents/Images/Amostras/Amostras/IMG_5431 2.jpeg"

    limiteInferiorPositivo = (34, 20, 34)
    limiteSuperiorPositivo = None
    limiteInferiorNegativo = None
    limiteSuperiorNegativo = (150, 151, 158)

    results = process_image_with_boundaries(
        image_path,
        limiteInferiorPositivo,
        limiteSuperiorPositivo,
        limiteInferiorNegativo,
        limiteSuperiorNegativo,
    )

    print("Resultados:")
    print(f"Positive Contours Counting: {results['positive_contours_counting']}")
    print(f"Negative Contours Counting: {results['negative_contours_counting']}")
    print(f"Total Cells: {results['total_cells']}")
    print(f"Positive Percentage: {results['positive_percentage']}%")
    print(f"Negative Percentage: {results['negative_percentage']}%")

    # Exibir as imagens na tela
    cv2.imshow("Processed Image - Positive", results["processed_image_positive"])
    cv2.imshow("Processed Image - Negative", results["processed_image_negative"])
    cv2.imshow("Merged Image", results["merged_image"])

    # Aguardar até que uma tecla seja pressionada para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()