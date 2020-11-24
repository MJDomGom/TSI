# Descripción del Proyecto

El objetivo a conseguir con este software es gestionar las ventas de productos realizados a partir de madera, así como su envío y devolución. Todo esto
acompañado de una gestión del stock de producto, materiales para su fabricación y compra de materiales a partir de nuestros proveedores. 

 Utilizaremos Odoo por ser un ERP de código abierto y porque dispone de una interfaz web.🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local._


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
-Tener Odoo instalado en tu maquina
-Si no tienes Odoo, seguir las instrucciones en las EPDs 1 y 2 de la asignatura de Tecnologias de Sistemas de Informacion
```

### Instalación 🔧

Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener el modulo operativo.(Las siguientes instrucciones son para ejecutarlas en una maquina Ubuntu)

```
-Copia la carpeta del modulo en /home/usuario/odoo/addons
-Ejecute el comando python3 odoo-bin --addons-path=addons -r usuario -w usuario --db_host=localhost --db_port=5432 -d usuario -i base --dev=all
-Inserte en su navegador localhost:8069 para entrar en odoo
-Una vez en odoo, busque la app UPOWOOD e instale el modulo
```

_El modulo contiene una series de datos de prueba para su funcionamiento, pero no se han insertado fotos para no aumentar el tamaño del modulo_

Nota: Realizando los datos de prueba nos hemos encontrado con una serie de fallos que el equipo del proyecto no ha sabido solucionar para la entrega del día 24/11/2020, por lo que se consultara a un equipo de experto. Los problemas son:

1. Los datos de Personas nos da un error y no hemos encontrado cual
2. Las relaciones entre Material y Proveedor falla debido a que Odoo no esta cerrando bien la instrucción xml. Para mas información, mirar el fallo que da Odoo quitando los comentarios en esa parte del código.



## Autores ✒️

* **Aurelio López Fernández** - *Director Asignatura* - [alopfer](alopfer@upo.es)
* **Manuel Jesús Domínguez Gómez** - *Grupo 4* - [MJDomGom](https://github.com/MJDomGom)
* **Federico González Acosta** - *Grupo 4* - [fedevale46](https://github.com/fedevale46)
* **Patricia Vázquez del Cerro** - *Grupo 4* - [pativxx](https://github.com/pativxx)
* **Arturo López-Damas Oliveres** - *Grupo 4* - [artuloda](https://github.com/artuloda)

## Licencia 📄

Este proyecto está bajo la licencia aplicada por la asignatura de Tecnologías de Sistemas de Información del Grado en Ingeniería Informática en Sistemas de Información

## Expresiones de Gratitud 🎁

* Dar las gracias a Aurelio por todas las tutorías, que se sabe el proyecto de memoria 📢

---
⌨️ con ❤️ por [Grupo UPOWOOD TSI](https://github.com/MJDomGom/TSI) 😊
