# Process Image Library

A `process_img` é uma biblioteca Python para processamento de imagens, permitindo a segmentação e análise de contornos com base em limites de cor definidos.

## Instalação

### 1. Instale o Python
Certifique-se de que você tem o Python 3.6 ou superior instalado. Caso não tenha, siga os passos abaixo:

1️⃣ Baixe o instalador do Python no site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/).  
2️⃣ Siga as instruções de instalação para o seu sistema operacional.  
3️⃣ Após instalar, verifique se o Python está funcionando corretamente executando o comando no terminal:

```bash
python --version
```

### 2. Baixe o arquivo `.whl`
Obtenha o arquivo `.whl` da biblioteca fornecido pelo desenvolvedor.

### 3. Instale a biblioteca
Instale a biblioteca usando o comando:

```bash
pip install process_img-1.0.1-py3-none-any.whl
```

## Como usar

### 1. Importando a biblioteca
Você pode importar a função principal da biblioteca no seu código:

```python
from process_img.process_img_interface import process_image_with_boundaries
```

### 2. Exemplo de uso
Aqui está um exemplo completo de como usar a biblioteca para processar uma imagem:

```python
import cv2
from process_img.process_img_interface import process_image_with_boundaries

if __name__ == "__main__":
    # Caminho para a imagem que será processada
    image_path = "/caminho/para/sua/imagem.jpg"

    # Defina os limites de cor para segmentação
    limiteInferiorPositivo = (34, 20, 34)
    limiteSuperiorPositivo = (100, 100, 100)
    limiteInferiorNegativo = (0, 0, 0)
    limiteSuperiorNegativo = (150, 151, 158)

    # Processar a imagem
    results = process_image_with_boundaries(
        image_path,
        limiteInferiorPositivo,
        limiteSuperiorPositivo,
        limiteInferiorNegativo,
        limiteSuperiorNegativo,
    )

    # Exibir os resultados
    print("Resultados:")
    print(f"Positive Contours Counting: {results['positive_contours_counting']}")
    print(f"Negative Contours Counting: {results['negative_contours_counting']}")
    print(f"Total Cells: {results['total_cells']}")
    print(f"Positive Percentage: {results['positive_percentage']}%")
    print(f"Negative Percentage: {results['negative_percentage']}%")

    # Exibir as imagens processadas
    cv2.imshow("Processed Image - Positive", results["processed_image_positive"])
    cv2.imshow("Processed Image - Negative", results["processed_image_negative"])
    cv2.imshow("Merged Image", results["merged_image"])

    # Aguardar até que uma tecla seja pressionada para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### 3. Estrutura dos resultados
A função `process_image_with_boundaries` retorna um dicionário com os seguintes dados:

- **positive_contours_counting**: Número de contornos positivos identificados.
- **negative_contours_counting**: Número de contornos negativos identificados.
- **total_cells**: Total de células identificadas.
- **positive_percentage**: Porcentagem de células positivas.
- **negative_percentage**: Porcentagem de células negativas.
- **processed_image_positive**: Imagem processada com contornos positivos.
- **processed_image_negative**: Imagem processada com contornos negativos.
- **merged_image**: Imagem combinada com todos os contornos.

### 4. Executar o Script
1️⃣ Abra o terminal no diretório do script `main_from_lib.py`.  

2️⃣ Execute:
```
python main_from_lib.py
```