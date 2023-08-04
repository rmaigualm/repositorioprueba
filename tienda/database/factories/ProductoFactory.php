<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Producto>
 */
class ProductoFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            //el fake es una libreria para agregar datos ficticios
            'nombre' =>fake()->text($maxNbChars = 10),
            'cantidad' =>fake()->numberBetween($min = 51, $max = 100),
            'estado' => 'A',
        ];
    }
}
