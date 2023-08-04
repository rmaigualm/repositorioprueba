/**
 * funcion qeu recibe el id del producto a eliminar
 * abre un MOdal y verifica si la personas desea eliminar el producto.
 * si dice que si,llamauna url llamada
 * /eliminar/idProducto
 * @param {*} idProducto
 */

function abrirModalEliminar(idProducto){
    Swal.fire({
        title:'Eliminar producto',
        text:'¿esta seguro de eliminar?',
        icon:'warning',
        showCancelButton:true,
        confirmButtonColor:'#3085d6',
        cancelButtonColor:'#d33',
        cancelButtonText:'NO',
        confirmButtonText:'SI'
    }).then((result)=>{
        if(result.isConfirmed){
            location.href="/eliminarProducto/"+idProducto+"/"
        }
    })
}