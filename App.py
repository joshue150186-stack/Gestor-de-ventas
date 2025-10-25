importar React, { useState } de 'react';
importar { Botón } desde "@/componentes/ui/button";
importar { Tarjeta, ContenidoDeTarjeta } desde "@/componentes/ui/tarjeta";
importar { Input } desde "@/components/ui/input";
importar { Tabla, Cuerpo de tabla, Celda de tabla, Encabezado de tabla, Encabezado de tabla, Fila de tabla } desde "@/componentes/ui/table";
importar { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } de "@/components/ui/dialog";
importar { Descargar, Impresora, Plus } de 'lucide-react';

// Formulario de Envío (fuera del componente principal)
function EnvíoForm({ puntos, onRegistrar }) {
  const [punto, setPunto] = useState('');
  const [monto, setMonto] = useState('');
  const [hora, setHora] = useState('');
  const [quienEnvia, setQuienEnvia] = useState('');
  const [quienRecibe, setQuienRecibe] = useState('');

  constante handleSubmit = () => {
    if (punto && monto && hora && quienEnvia && quienRecibe) {
      onRegistrar(punto, parseFloat(monto), hora, quienEnvia, quienRecibe);
      setPunto('');
      setMonto('');
      establecerHora('');
      setQuienEnvia('');
      setQuienRecibe('');
    }
  };

  devolver (
    <div className="espacio-y-3">
      <select className="w-borde completo redondeado p-2" valor={punto} onChange={e => setPunto(e.target.value)}>
        <option value="">Selecciona un punto</option>
        {puntos.map((p, i) => <option key={i}>{p.nombre}</option>)}
      </seleccionar>
      <Input placeholder="Monto" type="number" value={monto} onChange={e => setMonto(e.target.value)} />
      <Input placeholder="Hora" type="time" value={hora} onChange={e => setHora(e.target.value)} />
      <Input placeholder="Quien envia" value={quienEnvia} onChange={e => setQuienEnvia(e.target.value)} />
      <Input placeholder="Quién recibe" value={quienRecibe} onChange={e => setQuienRecibe(e.target.value)} />
      <Button className="w-full" onClick={handleSubmit}>Registrador</Button>
    </div>
  );
}

exportar función predeterminada GestorVentas() {
  const [puntos, setPuntos] = useState([]);
  const [vendedores, setVendedores] = useState([]);
  const [transacciones, setTransacciones] = useState([]);

  const [nuevoPunto, setNuevoPunto] = useState('');
  const [nuevoVendedor, setNuevoVendedor] = useState('');

  const agregarPunto = () => {
    si (nuevoPunto.trim()) {
      setPuntos([...puntos, { nombre: nuevoPunto, ventas: [], envíos: [] }]);
      setNuevoPunto('');
    }
  };

  const agregarVendedor = () => {
    si (nuevoVendedor.trim()) {
      setVendedores([...vendedores, { nombre: nuevoVendedor, entregado: 0, vendido: 0 }]);
      setNuevoVendedor('');
    }
  };

  const registrarEntrega = (vendedor, cantidad) => {
    setVendedores(vendedores.map(v => v.nombre === vendedor ? { ...v, entregado: v.entregado + cantidad } : v));
  };

  const registrarVenta = (vendedor, cantidad) => {
    setVendedores(vendedores.map(v => v.nombre === vendedor ? { ...v, vendido: v.vendido + cantidad } : v));
  };

  const registrarEnvio = (punto, monto, hora, quienEnvia, quienRecibe) => {
    const envío = { punto, monto, hora, quienEnvia, quienRecibe };
    setTransacciones([...transacciones, envío]);
  };

  const generarReporte = () => {
    constante contenido = [
      'REPORTE DE VENTAS Y ENVIOS',
      '\n\nVENDEDORES:',
      ...vendedores.map(v => `${v.nombre} | Entregado: ${v.entregado} | Vendido: ${v.vendido}`),
      '\nPUNTOS DE VENTA:',
      ...puntos.map(p => p.nombre),
      '\nENVIOS:',
      ...transacciones.map(t => `${t.punto}: $${t.monto} enviado por ${t.quienEnvia} a ${t.quienRecibe} a las ${t.hora}`)
    ].join('\n');

    const blob = new Blob([contenido], { tipo: 'texto/plano;conjunto de caracteres=utf-8' });
    constante link = document.createElement('a');
    enlace.href = URL.createObjectURL(blob);
    link.download = 'reporte_ventas.txt';
    enlace.click();
  };

  const imprimirReporte = () => {
    constante html = `
      <html>
      <cabeza>
        <title>Reporte de Ventas</title>
        <estilo>
          cuerpo { familia de fuentes: Arial; relleno: 20px; }
          h1 { alineación del texto: centro; }
          tabla { ancho: 100%; colapso del borde: colapsar; margen superior: 20px; }
          th, td { borde: 1px sólido #ccc; relleno: 8px; alineación del texto: izquierda; }
          th { fondo: #f0f0f0; }
        </estilo>
      </cabeza>
      <cuerpo>
        <h1>Reporte de Ventas y Envíos</h1>
        <h2>Vendedores</h2>
        <tabla>
          <tr><th>Nombre</th><th>Entregado</th><th>Vendido</th></tr>
          ${vendedores.map(v => `<tr><td>${v.nombre}</td><td>${v.entregado}</td><td>${v.vendido}</td></tr>`).join('')}
        </tabla>
        Puntos de venta
        <ul>${puntos.map(p => `<li>${p.nombre}</li>`).join('')}</ul>
        Envíos
        <tabla>
          <tr><th>Punto</th><th>Monto</th><th>Hora</th><th>Envia</th><th>Recibe</th></tr>
          ${transacciones.map(t => `<tr><td>${t.punto}</td><td>$${t.monto}</td><td>${t.hora}</td><td>${t.quienEnvia}</td><td>${t.quienRecibe}</td></tr>`).join('')}
        </tabla>
        <script>ventana.print();</script>
      </cuerpo>
      </html>
    `;
    const ventana = ventana.open('', '_blank');
    ventana.documento.write(html);
    ventana.documento.close();
  };

  devolver (
    <div className="p-6 espacio-y-6">
      <h1 className="text-2xl font-bold">Gestor de Ventas Interactivo</h1>
      <div className="cuadrícula md:cuadrícula-cols-2 espacio-6">
        <Tarjeta>
          <CardContent className="espacio-y-3">
            <h2 className="font-semibold">Puntos de Venta</h2>
            <div className="flex gap-2">
              <Input placeholder="Nombre del punto" value={nuevoPunto} onChange={e => setNuevoPunto(e.target.value)} />
              <Button onClick={agregarPunto}><Plus /> Agregar</Button>
            </div>
            <ul className="lista-disco ml-6">
              {puntos.map((p,i) => <li key={i}>{p.nombre}</li>)}
            </ul>
          </Contenido de la tarjeta>
        </Tarjeta>
        <Tarjeta>
          <CardContent className="espacio-y-3">
            <h2 className="font-semibold">Vendedores</h2>
            <div className="flex gap-2">
              <Input placeholder="Nombre del vendedor" value={nuevoVendedor} onChange={e => setNuevoVendedor(e.target.value)} />
              <Button onClick={agregarVendedor}><Plus /> Agregar</Button>
            </div>
            <Tabla>
              <Encabezado de tabla>
                <Fila de tabla>
                  <TableHead>Nombre</TableHead>
                  <TableHead>Entregado</TableHead>
                  <TableHead>Vendido</TableHead>
                </FilaDeTabla>
              </Encabezado de tabla>
              <Cuerpo de la tabla>
                {vendedores.map((v, i) => (
                  <Clave de fila de tabla={i}>
                    <TableCell>{v.nombre}</TableCell>
                    <TableCell>{v.entregado}</TableCell>
                    <TableCell>{v.vendido}</TableCell>
                  </FilaDeTabla>
                ))}
              </CuerpoDeTabla>
            </Tabla>
          </Contenido de la tarjeta>
        </Tarjeta>
      </div>

      {/* Diálogo para envío del registrador */}
      <Diálogo>
        <DialogTrigger como hijo>
          <Button variant="outline">Registrar Envío</Button>
        </Disparador de diálogo>
        <Contenido del diálogo>
          <Encabezado de diálogo>
            <DialogTitle>Registrador Envío de Dinero</DialogTitle>
          </Encabezado de diálogo>
          <EnvioForm puntos={puntos} onRegistrar={registrarEnvio} />
        </Contenido de diálogo>
      </Diálogo>

      <div className="flex justify-end gap-3">
        <Button onClick={generarReporte}><Descargar className="mr-2" /> Descargar TXT</Button>
        <Button variant="secondary" onClick={imprimirReporte}><Printer className="mr-2" /> Imprimir / PDF</Button>
      </div>
    </div>
  );
}
