# Use a imagem oficial do Node.js como base
FROM alpine:3.14

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos do aplicativo para o diretório de trabalho
COPY package.json .
COPY index.js ./

# Instale as dependências do aplicativo
RUN npm install

# Exponha a porta do aplicativo
EXPOSE 8080

# Inicie o aplicativo
CMD ["node", "index.js"]
