#Imagem
FROM postgres:alpine

#definindo variaveis de ambiente
ENV ORACLE_USER = RM95177
ENV ORACLE_PASSWORD = 210104

#copiando script sql
COPY scripts/* /opt/oracle/scripts/setup/

# Executar os scripts de inicialização do banco de dados
RUN chmod +x /opt/oracle/scripts/setup/*.sh && \
    /opt/oracle/scripts/setup/install.sh