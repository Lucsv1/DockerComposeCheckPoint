# Utilizar uma imagem base do Node.js
FROM node:14-alpine

# Definir diretório de trabalho na imagem
WORKDIR /app

# Copiar os arquivos do serviço de API para a imagem
COPY package.json package-lock.json /app/
COPY src /app/src

# Instalar as dependências do serviço de API
RUN npm ci --production

# Expor a porta utilizada pelo serviço de API
EXPOSE 3000

# Iniciar o serviço de API
CMD ["node", "src/app.js"]
