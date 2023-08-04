<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Producto extends Model
{
    use HasFactory;


    protected $fillable = [
        'name',
        'cantidad',
        'estado'
    ];

    protected $hidden = [
        'created_at',
        'updated_at'
    ];

    //las dos lineas de abajo son para cuando se necesite cambiar los nombres de los campos de la bases de datos
    // protected $table = "alimentos";
    // protected $primaryKey = "id_alimentos";
}
