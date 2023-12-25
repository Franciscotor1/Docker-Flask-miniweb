from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # Configuración para ejecutar la aplicación en modo de desarrollo (debug=True)
    app.run(debug=True, host='0.0.0.0')

# Configuración para ejecutar la aplicación en modo de producción (debug=False)
# Asegúrate de comentar o eliminar la línea anterior (app.run(debug=True, host='0.0.0.0')) al cambiar a producción.

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
