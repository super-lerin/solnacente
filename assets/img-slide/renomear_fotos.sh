#!/bin/bash

# Diretório alvo baseado na imagem fornecida
TARGET_DIR="/var/www/html/thiago/lumen/assets/img-slide"

# Verifica se o diretório existe, caso contrário usa o diretório atual de execução
if [ -d "$TARGET_DIR" ]; then
    cd "$TARGET_DIR" || exit
    echo "Entrando no diretório: $TARGET_DIR"
else
    echo "Diretório $TARGET_DIR não encontrado. Executando no diretório atual."
fi

# Contador para o novo padrão de nomenclatura (foto1, foto2...)
count=1

# Loop indexado para garantir a ordem numérica correta de 1 a 15
for i in {1..15}; do
    # Verifica se o arquivo existe com extensão .jpeg ou .jpg
    if [ -f "slide-${i}.jpeg" ]; then
        echo "Renomeando slide-${i}.jpeg para foto${count}.jpg"
        mv "slide-${i}.jpeg" "foto${count}.jpg"
        ((count++))
    elif [ -f "slide-${i}.jpg" ]; then
        echo "Renomeando slide-${i}.jpg para foto${count}.jpg"
        mv "slide-${i}.jpg" "foto${count}.jpg"
        ((count++))
    else
        echo "Arquivo slide-${i} (.jpg/.jpeg) não encontrado, pulando..."
    fi
done

echo "Processo de renomeação concluído! Total de fotos processadas: $((count-1))"

