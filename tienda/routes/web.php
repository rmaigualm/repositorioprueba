<?php
namespace App\Http\Controllers\saludo;
use App\Http\Controllers\ProductoController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
Route::get('/',function () {
    return view('index');
});

Route::get('/home', function () {
    
    return view('welcome');
})->name('index');


Route::get('/productos',function(){
    return view('productos');
});


//Route::get('/index/{nombre}', [saludo::class,'saludar']);


// Route::get('/producto',[ProductoController::class,'index']);
// Route::post('/producto',[ProductoController::class,'store']);
// Route::put('/producto/{producto}',[ProductoController::class,'update']);
// Route::delete('/producto/{producto}',[ProductoController::class,'destroy']);


Route::resource('/producto',ProductoController::class)->only('index','store','update','destroy'); //manera mas efectiva de crear las rutas

