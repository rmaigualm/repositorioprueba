<?php

namespace App\Http\Controllers;

use App\Http\Requests\ProductosRequest;
use App\Models\Producto;
// use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Symfony\Component\Mime\Message;

class ProductoController extends Controller

{


    public function __construct()
    {

        $this->middleware('cant',['only' => ['store']]);
        //
    }
    /**
     * Display a listing of the resource. CONSULTAR
     */
    public function index()
    {
        return Producto::paginate(5);
    }

   

    /**
     * Store a newly created resource in storage. REGISTRAR
     */
    public function store(ProductosRequest $request)
    //esto es para manejar las validaciones
    {   

        // Producto::created($request->all());
        Producto::created($request->all());
    }


    
    
    /**
     * Update the specified resource in storage. MODIFICAR
     */
    public function update(Request $request, Producto $producto)
    {
        Producto::findOrFail($request->id)->updated($request->all());
    }

    /**
     * Remove the specified resource from storage. ELIMINAR
     */
    public function destroy(Producto $producto)
    {
        Producto::findOrFail($producto->id)->delete();
    }
}