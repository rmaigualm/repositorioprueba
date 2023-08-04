<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class CantidadMin
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure(\Illuminate\Http\Request): (\Illuminate\Http\Response|\Illuminate\Http\RedirectResponse)  $next
     * @return \Illuminate\Http\Response|\Illuminate\Http\RedirectResponse
     */
    public function handle(Request $request, Closure $next)
    {
        //para hacer validacion en las rutas se escribe esto y se redirije a donde usted quiera
        if($request->cantidad <=50){
            return redirect('/home');
        }
        return $next($request);
    }
}
