def x_mod_y(e):
  num1 = Element("num1")
  num2 = Element("num2")
  pyscript.write("output", "{} % {} = {}".format(num1.value, num2.value, int(num1.value) % int(num2.value)))
