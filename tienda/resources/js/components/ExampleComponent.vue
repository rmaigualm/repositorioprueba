<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Example Component</div>

                    <!-- <input type="text"> -->
                    <input type="text" v-model="articulo" @keyup.enter="agregar()">

                    <div class="card-body">
                        {{ count }}
                    </div>

                    <button @click="agregar()">agregar</button>
                    <h1 v-text="nombre"></h1>
                    <ul v-for="fruta in frutas">
                        <li v-text="fruta"></li>

                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return{
                count: 0,
                nombre: '',
                articulo: '',
                frutas: ['banano','fresa','mora']
            }
        },

        methods: {
            agregar(){
                this.frutas.push(this.articulo)
            },
            lista(){
                let me = this;
                axios.get('/producto')
                .then(function(response){
                    console.log(response.data);
                    // me.nombre = response.data.nombre
                })
                .catch(function(error){
                    console.log(error)
                })
        },

        

        mounted() {
            console.log('Component mounted.')
            this.lista()
        }
    }

}    
</script>
