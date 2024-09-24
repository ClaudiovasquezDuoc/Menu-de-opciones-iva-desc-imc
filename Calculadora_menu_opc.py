import math 
sw = 1

while sw == 1:
  print("Ejercicio sobre funciones")
  print("-----------","Calculadora","------------")
  print("1)Calculadora de IVA")
  print("2)Calculadora de descuentos")
  print("3)Calculadora de IMC")
  print("4)Salir de la aplicacion")
  def iva():
    prod1=int(input("Favor ingresar el valor de el producto:"))
    calc_iva=(prod1/100*19)+prod1
    print("El valor final de el producto es:", {calc_iva})
    print("El valor de el iva del producto es:", {(prod1/100)*19})
    
  def descuentos():
    prod1=int(input("Favor ingresar el valor del producto:"))
    desc=20
    valor_desc=(prod1/100)*20
    valor_fin=prod1+valor_desc
    print("El valor de el producto + descuento seria:", {valor_fin})
    print("El valor de el descuento es:",desc ,"%")

  def imc():
    ("\t","Calcular IMC")
    peso=int(input("Favor ingresar su peso:"))
    estatura=float(input("Favor ingresar su estatura en metros:"))
    calc_imc=peso/(estatura**2)  
    print("Su imc seria de:", calc_imc)  
    if calc_imc <= 18.5:
      print("Su peso se encuentra bajo")
    elif 18.6 <= calc_imc <= 24.9:
      print("Su peso se encuentra adecuado")
    elif 25 <= calc_imc <= 29.9:
      print("Su peso se encuentra en el sobrepeso")
    elif 30 <= calc_imc <= 34.9:
      print("Su peso se encuentra en Obesidad Nivel 1")
    elif 35 <= calc_imc <= 39.9:
      print("Su peso se encuentra en Obesidad Nivel 2")
    elif calc_imc >= 40:
      print("Su peso se encuentra en OBESIDAD NIVEL 3")

  op=int(input("Favor ingresar la opcion:"))
  try:
    if (op > 0 and op < 5):
      if op == 1:
        print(f"Calculador de IVA")
        iva()
        continu=int(input("Desea salir 1=si o 2=no"))
        if continu == 1:
          print("Cerrando aplicacion")
          sw=0
      if op == 2:
        print("Calculadora de descuentos")
        descuentos()
        continu=int(input("Desea salir 1=si o 2=no"))
        if continu == 1:
          print("Cerrando aplicacion")
          sw=0              
      if op == 3:
        print("Calculadora de IMC")
        imc()
        continu=int(input("Desea salir 1=si o 2=no"))
        if continu == 1:
          print("Cerrando aplicacion")
          sw=0
      if op == 4:
        print("Salir de la aplicacion")  
        sw=0 
  except:
    print("Ingreso de opcion erroneo")