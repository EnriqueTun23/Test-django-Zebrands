# Prueba Tecnica

Necesitamos construir un sistema de catálogo básico para administrar productos. Un producto debe tener información básica como sku, nombre, precio y marca.

En este sistema, necesitamos tener al menos dos tipos de usuarios: (i) administradores para crear/actualizar/borrar productos y para crear/actualizar/borrar otros administradores; y (ii) usuarios anónimos que solo pueden recuperar información de productos pero no pueden realizar cambios.

Como requisito especial, cada vez que un usuario administrador realiza un cambio en un producto (por ejemplo, si se ajusta el precio), debemos notificar a todos los demás administradores sobre el cambio, ya sea por correo electrónico u otro mecanismo.

También debemos realizar un seguimiento de la cantidad de veces que un usuario anónimo consulta cada producto, para que podamos crear algunos informes en el futuro.

Su tarea es construir este sistema implementando una API REST o GraphQL utilizando la pila de su preferencia.


## Instalacion

Se usa docker para levantar el proyecto

```bash
  docker-compose up -d 
```
## Se levanta en el puerto local

**Client:** http://localhost:8000/


## Uso

Entrando ala url http://localhost:8000/doc/ se puede saber que existe una url para crear un usuario nuevo

- Crear usuario
- Obtener el token 
