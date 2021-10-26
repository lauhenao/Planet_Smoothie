create table Clientes(
	id integer primary key,
	nombre text,
	apellidos text,
	direccion text,
	telefono text,
	email text,
	contrasena text,
	cumpleanos text,
);

create table FormaDePago(
	id integer primary key,
	nombre text
);
create table Pedido(
	id integer primary key,
	fecha text,
        id_cliente integer references Clientes(id),
        id_forma_pago integer references FormaDePago(id)
);
create table Producto(
	id integer primary key,
	codigo text,
	nombre text,
	cantidad integer,
	precio real,
);
create table DetallePedido(
	sec integer primary key,
        cantidad integer,
        precio real,
        id_pedido integer references Pedido(id),
        id_producto integer references Producto(id)
);
