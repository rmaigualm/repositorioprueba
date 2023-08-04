<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class ProductosRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, mixed>
     */
    public function rules()
    {
        return [
            //estas reglas se traen desde ProductoController
            'nombre'=> 'require|min:1|max:20|unique:productos',
            'cantidad'=> 'require|numeric|min:1|max:1000',
        ];
    }

    public function messages(){
        return [
            'required' => "El campo :attribute es obligatori",
            'max' => "El campo : attribute es mayor a : max",
            'min' => "El campo : attribute es menor a : min",
            'nimeric' => "El campo : attribute debe ser de tipo Numero",
            'unique' => "El campo : attribute ya existe"
        ];

    }




}
