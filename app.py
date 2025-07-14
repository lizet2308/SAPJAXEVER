from flask import Flask, render_template, request, redirect, url_for, flash, Response, session

app = Flask(__name__, template_folder='Templates')  # Parametro

# Creamos Ruta Principal
@app.route("/")
def Index():
    return render_template('suma.html')

@app.route("/sumar", methods=["GET", "POST"])
def OperSuma():
    if request.method == "POST":
        a = int(request.form["t1"])
        b = int(request.form["t2"])
        c = a + b
        return render_template('suma.html', sm=c, pv=a, sv=b)
    else:
        return render_template('suma.html', sm=None)
    
@app.route("/imc", methods=["GET", "POST"])
def OperIMC():
    if request.method == "POST":
        p = float(request.form["t1"])
        alt = float(request.form["t2"])
        i = p/(alt*alt)
        
        if i < 18.5:
         estado = "Bajo peso"
        elif i < 25:
         estado = "Normal"
        elif i < 30:
         estado = "Sobrepeso"
        elif i < 35:
         estado = "Obesidad tipo 1"
        elif i < 40:
         estado = "Obesidad tipo 2"
        else:
         estado = "Obesidad tipo 3" 
        
        return render_template('imc.html', IM=i, pe=p, al=alt, es=estado)
    else:
        return render_template('imc.html', IM=None)
    
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
