
# 📖 README - Guia Rápido para Uso da Biblioteca `process_img`

## 📦 Instalação

1️⃣ Baixe o arquivo `.whl` da biblioteca `process_img`.  

2️⃣ No terminal, instale o pacote com:
```
pip install path/to/process_img-1.0.0-py3-none-any.whl
```
📌 Substitua `path/to/` pelo caminho onde o `.whl` está localizado.

---

## 🚀 Preparar o Script
Crie um arquivo Python, por exemplo `main.py`, com o seguinte conteúdo:
```python
from process_img.process_img_interface import process_image_with_boundaries
import cv2

if __name__ == "__main__":
    image_path = "CAMINHO/DA/IMAGEM.JPG"  # Substitua pelo caminho da imagem

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

    cv2.imshow("Processed Image - Positive", results["processed_image_positive"])
    cv2.imshow("Processed Image - Negative", results["processed_image_negative"])
    cv2.imshow("Merged Image", results["merged_image"])

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
📌 Substitua `CAMINHO/DA/IMAGEM.JPG` pelo caminho completo da imagem que deseja processar.

---

## 🖥 Executar o Script
1️⃣ Abra o terminal no diretório do script `main.py`.  

2️⃣ Execute:
```
python main.py
```

---

## 🛠 Dicas Avançadas
✅ Reinstalar o pacote se necessário (por exemplo, após uma nova versão):
```
pip install --force-reinstall path/to/process_img-1.0.0-py3-none-any.whl
```

✅ Resolver conflitos de dependências, como `numpy`, criando um ambiente virtual isolado:
```
python -m venv venv
.env\Scriptsctivate
pip install path/to/process_img-1.0.0-py3-none-any.whl
pip install opencv-python numpy scikit-learn Pillow
```

---

### 📢 Pronto para rodar sua biblioteca com sucesso!
