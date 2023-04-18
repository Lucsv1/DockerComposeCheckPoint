#imagem
FROM node:alpine

#Definindo Usuario
RUN adduser -D -g 'admdimdim' apiuser
USER apiuser

#Definindo o diretorio de trabalho na imagem
WORKDIR /app

#Copiando os arquivos de packe.json
COPY package*.json ./

#INstalando dependencias da aplicação
RUN npm install

#Copiando codigo fonte da aplicação para imagem
COPY . .

#expondo a porta 
EXPOSE 3000

#comando de incialização
CMD ["npm", "start "]