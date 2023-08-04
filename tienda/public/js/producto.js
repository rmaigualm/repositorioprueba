const { forEach } = require("lodash");

var id = 0;
function create() {
    axios.post('/producto', {
        nombre: txtNombre.value,
        cantidad: txtCantidad.value,
    })
        .then(function (response) {
            console.log(response);
            read();
        })
        .catch(function (error) {
            console.log(error.response.data.errors);
            let errors = "";
            Object.values(error.response.data.errors).forEach((element)=>{
                error += `<li>${element}</li>`;
            })
            errores.innerHTML = errors;
        })
}

function read(url = "/producto") {
    let data = ""
    axios.get(url)
        .then(function (response) {
            console.log(response.data);
            let data = "";
            let paginacion = "";
            response.data.forEach((p, index) => {
                data += `<tr>
                            <th scope="row">${index+1}</th>
                            <td>${p.nombre}</td>
                            <td>${p.cantidad}</td>
                            <td>${p.estado}</td>
                            <td>
                                <input type="radio" name="checkOpcion" id="checkOpcion" onclick='load(${JSON.stringify(p)})'>
                                <a href="" onclick='deleted(${p.id})' class="btn btn-danger">Eliminar</a>
                            </td>
                        </tr>`
            })
            response.data.links.forEach((element) => {
                paginacion += `<td><a class='links' onclick="read('${element.url}')">${element.label}</a>
                </td>`

            });
            pages.innerHTML = paginacion
            table.innerHTML = data;
        })
        .catch(function (error) {
            console.log(error);
        })
}

function load(element) {
    console.log(element);
    this.id = element.id;
    txtNombre.value = element.nombre;
    txtCantidad.value = element.cantidad;
}

function update() {
    axios.put(`producto/${this.id}`,{
        id: this.id,
        nombre:txtNombre.value,
        cantidad:txtCantidad.value,
    })
    .then(function(response){
        console.log(response);
        read()
    })
    .catch(function(error){
        console.log(error);
    })
}


function deletes(){
    let rest = confirm("Seguro de eliminar el Producto? ")
    if (rest){
        axios.delete(`producto/${this.id}`)
        .then(function(response){
            console.log(response);
            read()
        })
        .catch(function(error){
            console.log(error);
        })
    }
}

function deleted(idD){
    let rest = confirm("Seguro de eliminar el Producto? ")
    if (rest){
        axios.delete(`producto/${idD}`)
        .then(function(response){
            console.log(response);
            read()
        })
        .catch(function(error){
            console.log(error);
        })
    }
}
read()