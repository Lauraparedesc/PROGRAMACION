import matplotlib.pyplot as plt

ciudades = ['Medellín', 'Cali', 'Ibagué', 'Cartagena']
personas = [80923, 53454, 134554, 321212]
plt.bar(ciudades,personas)
plt.title('Ciudades vs Pablación')
plt.xlabel('Ciudades Colombianas')
plt.ylabel('Población')
plt.savefig('GraficoCiudades.png')
plt.show()
