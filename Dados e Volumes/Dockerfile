# Usa a imagem base do PHP com Apache
FROM php:8-apache

# Define o diretório de trabalho
WORKDIR /var/www/html

# Copia o conteúdo da aplicação para o contêiner
COPY . /var/www/html

# Ajusta as permissões para o usuário do Apache
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

# Habilita o módulo rewrite do Apache para URLs amigáveis
RUN a2enmod rewrite

# Garante que as permissões estejam configuradas corretamente no Apache
RUN echo "<Directory /var/www/html>\n\
    Options Indexes FollowSymLinks\n\
    AllowOverride All\n\
    Require all granted\n\
</Directory>" > /etc/apache2/conf-available/app.conf && \
    a2enconf app

# Expõe a porta 80 para o Apache
EXPOSE 80

# Comando padrão para iniciar o Apache
CMD ["apache2-foreground"]
